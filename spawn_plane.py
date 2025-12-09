
#_____________________________________les_imports_________________________________

# Imports PySide6.QtWidgets
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene,QGraphicsRectItem, QToolTip, QApplication,QGraphicsPolygonItem
from PySide6.QtWidgets import QGraphicsEllipseItem,QGraphicsLineItem, QGraphicsTextItem
from PySide6.QtWidgets import QLabel, QWidget, QToolTip # QLabel et QWidget peuvent être supprimés si non utilisés

# Imports PySide6.QtGui (Contient QPainter, QPixmap, QColor, QPen, QBrush, etc.)
from PySide6.QtGui import QPainter, QPixmap, QColor, QTransform, QPen, QBrush, QFont,QResizeEvent

# Imports PySide6.QtCore
from PySide6.QtCore import Qt, QPointF, QRectF, QSize, Signal

import math

#________________________________________________________________________________

# Taille du carré central (à ajuster)
SQUARE_SIZE = 14
# Longueur du vecteur de direction (à ajuster)
VECTOR_LENGTH = 23

REMOVAL_THRESHOLD_PIXELS = 10

class AircraftItem(QGraphicsRectItem):

    def __init__(self, callsign, data: dict,size=SQUARE_SIZE, vector_len=VECTOR_LENGTH):

        position = data['pos']
        heading = data['heading']

        # 1. Dessiner le carré central (corps de l'avion)
        # Le rectangle est dessiné autour de l'origine (0,0) pour faciliter la rotation
        super().__init__(-size / 2, -size / 2, size, size)


        self.callsign = callsign
        self.data = data
        self.size = size

        # 2. Dessiner le vecteur de direction (la petite droite)
        # La ligne va de (0, 0) au haut (-Y)
        self.vector = QGraphicsLineItem(0, 0, 0, -vector_len, self)  # 'self' rend la ligne enfant du carré
        self.vector.setPen(QPen(QColor(250, 255, 250), 2))  # Ligne Verte (standard ATC)

        # 3. Couleurs et Rotation
        self.default_brush = QBrush(Qt.GlobalColor.transparent)  # Rouge
        self.hover_brush = QBrush(QColor(255, 128, 0))  # Orange

        self.setBrush(Qt.BrushStyle.NoBrush)
        self.setPen(QPen(QColor(250, 250, 250), 1))

        # définir le centre de rotation au centre du carré (très important !)
        self.setTransformOriginPoint(0, 0)

        # Placer l'icône à la position initiale
        self.setPos(position)
        self.setRotation(heading)

        self.setAcceptHoverEvents(True)
        self.tooltip_text = self.create_tooltip_text()

        # 4. Assurer que le ToolTip fonctionne sur la bonne référence
        self.setToolTip(self.tooltip_text)


        """
        # Définition des couleurs pour l'effet de survol
        self.default_brush = QBrush(QColor(255, 0, 0))  # Rouge par défaut
        self.hover_brush = QBrush(QColor(255, 128, 0))  # Orange plus clair pour survol
        self.setBrush(self.default_brush)
        self.setPen(QPen(QColor(0, 0, 0), 1))

        # Configuration de la rotation (Centre du cercle)
        self.setTransformOriginPoint(size / 2, size / 2)
        self.setRotation(data['heading'])

        self.setAcceptHoverEvents(True)
        self.tooltip_text = self.create_tooltip_text()


        self.setRotation(heading) # Démarrage de la rotation
        self.setBrush(QBrush(QColor(255, 0, 0))) # Rouge
        self.setPen(QPen(QColor(0, 0, 0), 1))
        # Important : définit le centre de rotation au centre de l'item
        self.setTransformOriginPoint(size/2, size/2)
        # Stocke les données pour l'interaction
        self.data = {'position': position, 'heading': heading} # Stockage temporaire des données"""

    def set_landing_target(self, callsign, target_pos: QPointF, threshold: int):
        """
        Définit la destination d'atterrissage et affiche le cercle de proximité (geofence).
        """

        # 1. Retirer l'ancien cercle si l'avion en avait un
        if callsign in self.landing_targets:
            self.scene.removeItem(self.landing_targets[callsign]['circle_item'])

        # 2. Créer le cercle de proximité (creux et jaune par exemple)
        radius = threshold
        circle = QGraphicsEllipseItem(target_pos.x() - radius,
                                      target_pos.y() - radius,
                                      2 * radius, 2 * radius)

        # Couleur du cercle (Geofence)
        circle.setPen(QPen(QColor(255, 255, 0), 2))  # Jaune
        circle.setBrush(Qt.BrushStyle.NoBrush)  # Creux

        self.scene.addItem(circle)

        # 3. Stocker la cible et le cercle
        self.landing_targets[callsign] = {
            'target_pos': target_pos,
            'threshold': threshold,
            'circle_item': circle
        }

    def create_tooltip_text(self):
        #Construit le texte du ToolTip à partir des données de l'avion
        return (
            f"Vol : {self.callsign}\n"
            f"Cap : {self.data.get('heading', '?')}°\n"
            f"Alt : {self.data.get('altitude', '?')} ft\n"
            f"Vitesse : {self.data.get('speed', '?')} kts"
        )

    def hoverEnterEvent(self, event):
        """Change la couleur et AFFICHE LE TOOLTIP MANUELLEMENT."""

        # Mettre à jour le texte du ToolTip juste avant l'affichage (car les données changent)
        self.tooltip_text = self.create_tooltip_text()

        self.setBrush(self.hover_brush)

        # Affichage forcé du ToolTip
        QToolTip.showText(
            event.screenPos(),
            self.tooltip_text,
            self.scene().views()[0]
        )
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        """Remet la couleur par défaut et MASQUE LE TOOLTIP."""

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


    def set_map_image(self, pixmap_path):     #defini limage détude comme etant limage en fond

        self.scene.clear()        #nous devons d'abord retirer l'ancienne image si elle existe
        self.map_pixmap =QPixmap(pixmap_path)

        self.scene.setSceneRect(self.map_pixmap.rect())         # definir la taille de la scène à la taille de l'image
        self.scene.addPixmap(self.map_pixmap)                   #ajouter l'image de fond à la scène

        self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def resizeEvent(self, event: QResizeEvent):
        """
        Surcharge la méthode de redimensionnement pour garantir que la carte
        s'adapte à la taille de la QGraphicsView.
        """
        # Appel de la méthode parent
        super().resizeEvent(event)

        # Vérifie si la carte a été chargée (si self.sceneRect() est défini)
        if self.map_pixmap and not self.map_pixmap.isNull():
            # 1. Applique fitInView à chaque fois que le widget est redimensionné
            # Cela force la scène à s'adapter à la nouvelle taille du QGraphicsView.
            self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def remove_aircraft(self, callsign):    #pour enlever un avion en fonction de son callsign
        #Supprime un avion de la carte
        if callsign in self.aircraft_data:
            item = self.aircraft_data[callsign]['item']
            self.scene.removeItem(item)
            del self.aircraft_data[callsign]

    def mousePressEvent(self, event):
        """Détecte le clic en utilisant la QGraphicsScene."""

        # 1. Obtenir la position du clic dans les coordonnées de la VUE
        pos_view = event.pos()

        # 2. Demander à la VUE quel item se trouve à cette position
        item = self.itemAt(pos_view)

        if item and isinstance(item, AircraftItem):
            # 3. Avion détecté : Émettre le signal avec le callsign
            self.aircraft_clicked.emit(item.callsign)

        super().mousePressEvent(event)

    def show_aircraft_tooltip(self, callsign, global_pos: QPointF):
        #Construit et affiche la bulle d'aide pour l'avion

        data = self.aircraft_data.get(callsign)
        if not data:
            return

        # CONSTRUCTION DU TEXTE (À personnaliser)
        info_text = (
            f"**Vol : {callsign}**<hr>"
            f"Cap : {data['heading']:.0f}°<br>"
            f"Pos X : {data['position'].x():.1f}<br>"
            f"Pos Y : {data['position'].y():.1f}"

            # Ajoutez ici toutes les autres caractéristiques de l'avion (altitude, vitesse, etc.)
        )

        # Affiche la bulle d'aide à la position globale du curseur
        QToolTip.showText(global_pos.toPoint(), info_text, self)  #

    def add_aircraft(self, callsign, data: dict):  #ajout de speed
        """Ajoute ou met à jour un avion sur la carte.
        :param position: QPointF(x, y) - position en pixels sur la carte.
        :param heading: Angle en degrés (0=Nord, 90=Est).
        """
        heading = data['heading']
        speed = data['speed']

        aircraft_item = AircraftItem(callsign, data)
        aircraft_item.setPos(data['pos'])
        self.scene.addItem(aircraft_item)

        self.aircraft_data[callsign] = {
            'item': aircraft_item,
            'heading': heading,
            'speed': speed
        }#stocke la vitesse et met à jour le dictionnaire

    def set_landing_target(self, callsign, target_pos: QPointF, threshold: int):

        #Définit la destination d'atterrissage et affiche le cercle de proximité (geofence).


        # 1. Retirer l'ancien cercle si l'avion en avait un
        if callsign in self.landing_targets:
            # self.scene est directement accessible ici
            self.scene.removeItem(self.landing_targets[callsign]['circle_item'])

            # 2. Créer le cercle de proximité (creux et jaune)
        radius = threshold
        # Assurez-vous que QGraphicsEllipseItem est bien importé en haut du fichier
        circle = QGraphicsEllipseItem(target_pos.x() - radius,
                                      target_pos.y() - radius,
                                      2 * radius, 2 * radius)

        # Couleur du cercle (Geofence)
        circle.setPen(QPen(QColor(255, 255, 0), 2))
        circle.setBrush(Qt.BrushStyle.NoBrush)

        self.scene.addItem(circle)

        # 3. Stocker la cible et le cercle dans l'attribut de la MAP
        self.landing_targets[callsign] = {
            'target_pos': target_pos,
            'threshold': threshold,
            'circle_item': circle
        }

    def move_aircrafts(self, delta_time):
        #Déplace les objets QGraphicsItem sur la scène

        landed_callsigns = []

        for callsign, data in self.aircraft_data.items():
            item = data['item']  # L'objet graphique à déplacer
            landed_callsigns = []  # Pour stocker les avions à supprimer
            # Récupérer les données de la simulation (vitesse/cap)
            heading = self.all_aircraft_details[callsign]['heading']
            speed = self.all_aircraft_details[callsign]['speed']

            # --- CALCUL DES DÉPLACEMENTS (RÉUTILISÉ) ---
            heading_rad = math.radians(heading)
            dx = speed * delta_time * math.sin(heading_rad)
            dy = speed * delta_time * -math.cos(heading_rad)

            # 🟢 DÉPLACEMENT D'OBJET (Simple et efficace)
            # Item.pos() retourne la position actuelle (QPointF)
            new_pos = item.pos() + QPointF(dx, dy)
            item.setPos(new_pos)  # Met à jour la position de l'objet graphique

            if callsign in self.landing_targets:
                target = self.landing_targets[callsign]['target_pos']

                # Calcul de la distance au carré
                dist_sq = (new_pos.x() - target.x()) ** 2 + (new_pos.y() - target.y()) ** 2

                # 🟢 La condition est uniquement que la distance soit inférieure au seuil (cercle)
                if dist_sq < REMOVAL_THRESHOLD_PIXELS ** 2:
                    landed_callsigns.append(callsign)

                # 4. Déplacement et Mise à jour des données (pour le prochain cycle)
            item.setPos(new_pos)
            if self.all_aircraft_details:
                self.all_aircraft_details[callsign]['pos'] = new_pos

            # 🟢 CORRECTION 4 : Nettoyage des avions atterris (à la fin de la méthode)
        for callsign in landed_callsigns:
            # Retirer le cercle de la scène
            if callsign in self.landing_targets:
                self.scene.removeItem(self.landing_targets[callsign]['circle_item'])
                del self.landing_targets[callsign]

            # Retirer l'avion de la carte (item) et de aircraft_data
            self.remove_aircraft(callsign)
            # 🟢 MISE À JOUR DES DONNÉES DANS LE DICTIONNAIRE PRINCIPAL
            if self.all_aircraft_details:
                self.all_aircraft_details[callsign]['pos'] = new_pos

    def update_aircraft(self, callsign, new_heading):

        #met à jour le cap d'un avion existant.

        if callsign in self.aircraft_data:
            item = self.aircraft_data[callsign]['item']
            item.setRotation(new_heading)
            # mettre à jour le cap dans l'objet de l'avion
            self.aircraft_data[callsign]['heading'] = new_heading

        else:
            print(f"Erreur: Avion {callsign} non trouvé pour la mise à jour.")

    def display_airport_geofence(self, iata_code: str, target_pos: QPointF, threshold: int):
        """Affiche un cercle de proximité permanent autour d'un aéroport."""

        radius = threshold
        circle = QGraphicsEllipseItem(target_pos.x() - radius,
                                      target_pos.y() - radius,
                                      2 * radius, 2 * radius)

        # Configuration du style du cercle (Jaune creux)
        circle.setPen(QPen(QColor(255, 255, 0), 2))
        circle.setBrush(Qt.BrushStyle.NoBrush)

        self.scene.addItem(circle)

        # Stocker l'objet pour référence future
        self.airport_geofences[iata_code] = {
            'target_pos': target_pos,
            'threshold': threshold,
            'circle_item': circle
        }