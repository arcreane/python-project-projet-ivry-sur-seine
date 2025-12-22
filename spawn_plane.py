
#_____________________________________les_imports_________________________________

# Imports PySide6.QtWidgets
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene,QGraphicsRectItem, QToolTip, QApplication,QGraphicsPolygonItem
from PySide6.QtWidgets import QGraphicsEllipseItem,QGraphicsLineItem, QGraphicsItem
from PySide6.QtWidgets import QLabel, QWidget, QToolTip # QLabel et QWidget peuvent être supprimés si non utilisés

# Imports PySide6.QtGui (Contient QPainter, QPixmap, QColor, QPen, QBrush, etc.)
from PySide6.QtGui import QPainter, QPixmap, QColor, QTransform, QPen, QBrush, QFont,QResizeEvent

# Imports PySide6.QtCore
from PySide6.QtCore import Qt, QPointF, QRectF, QSize, Signal

from gestion_avion import gestion_avion, check_avion
from time import sleep

#________________________________________________________________________________

# Taille du carré central (à ajuster)
SQUARE_SIZE = 14
# Longueur du vecteur de direction (à ajuster)
VECTOR_LENGTH = 23

REMOVAL_THRESHOLD_PIXELS = 10

class AircraftItem(QGraphicsRectItem):

    def __init__(self, callsign, data: dict,size=SQUARE_SIZE, vector_len=VECTOR_LENGTH):

        position = data.pos
        heading = data.heading

        #dessiner le carré central (corps de l'avion)
        #le rectangle est dessiné autour de l'origine (0,0) pour faciliter la rotation
        super().__init__(-size / 2, -size / 2, size, size)


        self.callsign = callsign
        self.data = data
        self.size = size

        #dessiner le vecteur de direction (la petite droite)
        #la ligne va de (0, 0) au haut (-Y)
        self.vector = QGraphicsLineItem(0, 0, 0, -vector_len, self)  # self rend la ligne enfant du carré
        self.vector.setPen(QPen(QColor(250, 255, 250), 2))  #ligne Verte (standard ATC)

        #couleurs et Rotation
        self.default_brush = QBrush(Qt.GlobalColor.transparent)  #rouge
        self.hover_brush = QBrush(QColor(255, 128, 0))  #orange
        self.setBrush(Qt.BrushStyle.NoBrush)
        self.setPen(QPen(QColor(250, 250, 250), 1))

        #définir le centre de rotation au centre du carré (très important !)
        self.setTransformOriginPoint(0, 0)

        #placer l'icône à la position initiale
        self.setPos(position[0], position[1])
        self.setRotation(heading)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.LeftButton)
        self.tooltip_text = self.create_tooltip_text()

        #assurer que le ToolTip fonctionne sur la bonne référence
        self.setToolTip(self.tooltip_text)


    def set_landing_target(self, callsign, target_pos: QPointF, threshold: int):

        #définit la destination d'atterrissage et affiche le cercle de proximité (geofence).

        #retirer l'ancien cercle si l'avion en avait un
        if callsign in self.landing_targets:
            self.scene.removeItem(self.landing_targets[callsign]['circle_item'])

        #créer le cercle de proximité (creux et jaune par exemple)
        radius = threshold
        circle = QGraphicsEllipseItem(target_pos.x() - radius,
                                      target_pos.y() - radius,
                                      2 * radius, 2 * radius)

        #couleur du cercle
        circle.setPen(QPen(QColor(255, 255, 0), 2))  #jaune
        circle.setBrush(Qt.BrushStyle.NoBrush)  #centre creux

        self.scene.addItem(circle)

        #stocker la cible et le cercle
        self.landing_targets[callsign] = {
            'target_pos': target_pos,
            'threshold': threshold,
            'circle_item': circle
        }

    def create_tooltip_text(self):
        #Construit le texte du ToolTip à partir des données de l'avion
        return (
            f"Vol : {self.callsign}\n"
            f"Cap : {self.data.heading}°\n"
            f"Alt : {self.data.alt} ft\n"
            f"Vitesse : {self.data.speed} kts\n"
            f"Vers : {self.data.aprt_code}"
        )

    def hoverEnterEvent(self, event):
        #change la couleur et AFFICHE LE TOOLTIP

        #met à jour le texte du ToolTip juste avant l'affichage (les données changent)
        self.tooltip_text = self.create_tooltip_text()

        self.setBrush(self.hover_brush)

        #affichage forcé du ToolTip
        QToolTip.showText(
            event.screenPos(),
            self.tooltip_text,
            self.scene().views()[0]
        )
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        #Remet la couleur par défaut et MASQUE LE TOOLTIP

        self.setBrush(self.default_brush)
        QToolTip.hideText()

        super().hoverLeaveEvent(event)



class AircraftMapWidget(QGraphicsView):

    aircraft_clicked = Signal(str) #declaration du signal

    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.aircraft_data = {}  # stock les avions : {'callsign': {'position': QPointF, 'heading': float}}, liste de liste
        self.setMinimumSize(QSize(1, 1)) # important pour les QLabels dans les layouts
        self.setMouseTracking(True)  #active le suivi de la souris pour leffet "hover"
        self.hovered_aircraft = None #par defaut mis a none
        self.all_aircraft_details = None
        self.landing_targets = {}  # {'callsign': {'target_pos': QPointF, 'threshold': 80, 'circle_item': QGraphicsEllipseItem}}
        self.airport_geofences = {}
        self.aircraft_items = {}

    def set_map_image(self, pixmap_path):     #defini limage détude comme etant limage en fond

        self.scene.clear()        #nous devons d'abord retirer l'ancienne image si elle existe
        self.map_pixmap =QPixmap(pixmap_path)

        self.scene.setSceneRect(self.map_pixmap.rect())         # definir la taille de la scène à la taille de l'image
        self.scene.addPixmap(self.map_pixmap)                   #ajouter l'image de fond à la scène

        self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def resizeEvent(self, event: QResizeEvent):

        #Surcharge la méthode de redimensionnement pour garantir que la carte s'adapte à la taille de la QGraphicsView.

        #appel de la méthode parent
        super().resizeEvent(event)

        #verifie si la carte a été chargée (si self.sceneRect() est défini)
        if self.map_pixmap and not self.map_pixmap.isNull():
            self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)    #applique fitInView à chaque fois que le widget est redimensionné cela force la scène à s'adapter à la nouvelle taille du QGraphicsView.

    def remove_aircraft(self, callsign):    #pour enlever un avion en fonction de son callsign
        #Supprime un avion de la carte
        if callsign in self.aircraft_items:
            item = self.aircraft_items[callsign]
            self.scene.removeItem(item)
            del self.aircraft_items[callsign]
            del self.aircraft_data[callsign]

    def mousePressEvent(self, event):
        pos_view = event.pos()
        item = self.itemAt(pos_view)

        while item and not isinstance(item, AircraftItem):
            item = item.parentItem()

        # Si on a trouvé un AircraftItem
        if isinstance(item, AircraftItem):
            callsign = item.callsign
            self.aircraft_clicked.emit(callsign)

        super().mousePressEvent(event)

    def show_aircraft_tooltip(self, callsign, global_pos: QPointF):
        #Construit et affiche la bulle d'aide pour l'avion

        data = self.aircraft_data.get(callsign)
        if not data:
            return

        # construction du txt
        info_text = (
            f"**Vol : {callsign}**<hr>"
            f"Cap : {data['heading']:.0f}°<br>"
            f"Pos X : {data['position'].x():.1f}<br>"
            f"Pos Y : {data['position'].y():.1f}"
            f"To : {data.aprt_code:.f}<br>"
        )

        #affiche la bulle d'aide à la position globale du curseur
        QToolTip.showText(global_pos.toPoint(), info_text, self)

    def add_aircraft(self, callsign, data: dict):
        #Ajoute ou met à jour un avion sur la carte.

        aircraft_item = AircraftItem(callsign, data)
        aircraft_item.setPos(data.pos[0], data.pos[1])
        self.scene.addItem(aircraft_item)

        self.aircraft_data[callsign] = data
        self.aircraft_items[callsign] = aircraft_item

    def set_landing_target(self, callsign, target_pos: QPointF, threshold: int):

        #définit la destination d'atterrissage et affiche le cercle de proximité (geofence).


        if callsign in self.landing_targets:        #retirer l'ancien cercle si l'avion en avait un

            self.scene.removeItem(self.landing_targets[callsign]['circle_item'])            #self.scene est directement accessible ici

        #créer le cercle de proximité (cercle jaune)
        radius = threshold
        circle = QGraphicsEllipseItem(target_pos.x() - radius,
                                      target_pos.y() - radius,
                                      2 * radius, 2 * radius)

        circle.setPen(QPen(QColor(255, 255, 0), 2))#couleur du cercle
        circle.setBrush(Qt.BrushStyle.NoBrush)
        self.scene.addItem(circle)

        #stocker la cible et le cercle dans l'attribut de la map
        self.landing_targets[callsign] = {
            'target_pos': target_pos,
            'threshold': threshold,
            'circle_item': circle
        }

    def move_aircrafts(self):
        #déplace les objets QGraphicsItem sur la scène
        self.aircraft_data = gestion_avion()
        remove = []
        for data in self.aircraft_data.values():
            callsign = data.callsign
            if callsign not in self.aircraft_items.keys():
                self.add_aircraft(callsign, self.aircraft_data[callsign])
            if data.etat['land ?'] == True:
                remove.append(callsign)
            item = self.aircraft_items[callsign]
            item.setRotation(data.heading)
            item.setPos(data.pos[0], data.pos[1])
        for callsign in remove:
            self.remove_aircraft(callsign)
        self.aircraft_data = check_avion()
        sleep(1)


    def display_airport_geofence(self, iata_code: str, target_pos: QPointF, threshold: int):
        #Affiche un cercle de proximité permanent autour d'un aéroport

        radius = threshold
        circle = QGraphicsEllipseItem(target_pos.x() - radius,
                                      target_pos.y() - radius,
                                      2 * radius, 2 * radius)

        #configuration du style du cercle (Jaune creux)
        circle.setPen(QPen(QColor(255, 255, 0), 1))
        circle.setBrush(Qt.BrushStyle.NoBrush)

        self.scene.addItem(circle)

        #stocker l'objet pour référence future
        self.airport_geofences[iata_code] = {
            'target_pos': target_pos,
            'threshold': threshold,
            'circle_item': circle
        }