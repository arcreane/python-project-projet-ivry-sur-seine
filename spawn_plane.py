
#_____________________________________les_imports_________________________________

# Imports PySide6.QtWidgets
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QToolTip, QApplication,QGraphicsPolygonItem
from PySide6.QtWidgets import QGraphicsEllipseItem,QGraphicsLineItem, QGraphicsTextItem
from PySide6.QtWidgets import QLabel, QWidget, QToolTip # QLabel et QWidget peuvent être supprimés si non utilisés

# Imports PySide6.QtGui (Contient QPainter, QPixmap, QColor, QPen, QBrush, etc.)
from PySide6.QtGui import QPainter, QPixmap, QColor, QTransform, QPen, QBrush, QFont,QResizeEvent

# Imports PySide6.QtCore
from PySide6.QtCore import Qt, QPointF, QRectF, QSize, Signal

from gestion_avion import gestion_avion

#________________________________________________________________________________

# Taille du carré central (à ajuster)
SQUARE_SIZE = 8
# Longueur du vecteur de direction (à ajuster)
VECTOR_LENGTH = 15

class AircraftItem(QGraphicsEllipseItem):
    def __init__(self, callsign, data: dict,size=SQUARE_SIZE, vector_len=VECTOR_LENGTH):

        position = data.pos
        heading = data.heading

        # 1. Dessiner le carré central (corps de l'avion)
        # Le rectangle est dessiné autour de l'origine (0,0) pour faciliter la rotation
        super().__init__(-size / 2, -size / 2, size, size)


        self.callsign = callsign
        self.data = data
        self.size = size

        # 2. Dessiner le vecteur de direction (la petite droite)
        # La ligne va de (0, 0) au haut (-Y)
        self.vector = QGraphicsLineItem(0, 0, 0, -vector_len, self)  # 'self' rend la ligne enfant du carré
        self.vector.setPen(QPen(QColor(0, 255, 0), 2))  # Ligne Verte (standard ATC)

        # 3. Couleurs et Rotation
        self.default_brush = QBrush(QColor(255, 0, 0))  # Rouge
        self.hover_brush = QBrush(QColor(255, 128, 0))  # Orange

        self.setBrush(self.default_brush)
        self.setPen(QPen(QColor(0, 0, 0), 1))

        # définir le centre de rotation au centre du carré (très important !)
        self.setTransformOriginPoint(0, 0)

        # Placer l'icône à la position initiale
        self.setPos(position[0], position[1])
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

    def create_tooltip_text(self):
        #Construit le texte du ToolTip à partir des données de l'avion
        return (
            f"Vol : {self.callsign}\n"
            f"Cap : {self.data.heading} ° \n"
            f"Alt : {self.data.alt} ft\n"
            f"Vitesse : {self.data.speed} kts"
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


    '''
    def paintEvent(self, event):               #methode pour dessiner les icones davion

        #surcharge la méthode de dessin pour inclure les avions
        super().paintEvent(event) #dessine d'abord la carte de fond et apres les avions

        if not self.map_pixmap.isNull():

            painter = QPainter(self)         # permet de dessiner les icones d'avions

            #permet de dessiner a lechelle par dessus la carte
            # important pour faire coincider limage et les coorodnnes
            current_pixmap = self.pixmap()
            if not current_pixmap.isNull():
                scale_x=current_pixmap.width()/self.map_pixmap.width()
                scale_y=current_pixmap.height()/self.map_pixmap.height()

                offset_x=(self.width()-current_pixmap.width())/2
                offset_y=(self.height()-current_pixmap.height())/2

                #déplacer l'origine du peintre pour correspondre au coin supérieur gauche de la map
                painter.translate(offset_x,offset_y)

                #appliquer la mise à l'échelle
                painter.scale(scale_x, scale_y)

            # Dessiner chaque avion
            for callsign, data in self.aircraft_data.items():
                pos = data['position']
                heading = data['heading']

                # Dessiner le carré de l'avion
                square_size = 8 # taille du carré en pixels de l'image originale
                square_rect = QRectF(pos.x() - square_size /2, pos.y() - square_size /2, square_size, square_size)
                painter.fillRect(square_rect, QColor(255, 0, 0)) # Rouge

                # Dessiner la ligne de direction
                line_length = 20 # Longueur de la ligne de direction en pixels

                # Calcul de la fin de la ligne en fonction du heading
                # Convertir le heading en radians et ajuster l'origine (0° = Nord = -Y)
                # Correction pour que 0° soit le haut de l'image (Nord)
                # Qt math.cos et math.sin utilisent des radians, et 0 rad est l'axe +X
                # Pour 0° (Nord) être le haut (-Y), nous devons ajuster l'angle.
                # Heading 0 (Nord) -> angle -90 degrés par rapport à +X
                # Heading 90 (Est) -> angle 0 degrés par rapport à +X
                # heading_rad = math.radians(heading - 90) # Ajuste pour 0=Nord

                # Approche plus intuitive : si 0° est le haut de l'image, pas besoin d'ajuster l'angle si l'image
                # a son nord vers le haut. Les fonctions sin/cos de math sont par rapport à l'axe X positif.
                # Pour 0° Nord (haut, -Y) et 90° Est (+X):
                angle_rad = math.radians(90 - heading) # 0° N -> 90°, 90° E -> 0°, 180° S -> -90°, 270° O -> -180°
                # OU si heading est 0=Nord, 90=Est
                # angle_rad = math.radians(-heading) # Si 0 est Y+

                # Utilisons une transformation pour la ligne pour simplifier le calcul
                painter.save() # Sauvegarde l'état actuel du peintre
                painter.translate(pos) # Déplace l'origine au centre de l'avion

                # Ajustement : 0° en aéronautique est le Nord. Pour Qt QPainter, 0° est l'axe X positif,
                # et la rotation est dans le sens horaire. Pour que 0° (Nord) pointe vers le haut (-Y)
                # et 90° (Est) pointe vers la droite (+X) :
                # On doit faire pivoter le système de coordonnées de -90 degrés (anti-horaire) pour que le 'Nord' du peintre soit 'Haut'.
                # Ensuite, on applique la rotation du heading directement.
                painter.rotate(heading) # Applique la rotation de l'avion (0 = vers le haut)

                painter.setPen(QPen(QColor(0, 255, 0), 2))              #ligne verte
                painter.drawLine(QPointF(0, 0), QPointF(0, -line_length))        # Dessine la ligne vers le haut (Nord)

                painter.restore() # Restaure l'état du peintre (supprime la translation et la rotation)

            painter.end()             #fin du dessin

    '''


    '''
    def mouseMoveEvent(self, event):
        #detecte si le curseur de la souris survole un avion

        current_pixmap = self.pixmap()
        if current_pixmap.isNull():
            return

        #calcul de l'échelle et du décalage (code réutilisé de paintEvent)
        map_pixmap_size = self.map_pixmap.size()
        scale_x=current_pixmap.width()/map_pixmap_size.width()
        scale_y=current_pixmap.height()/map_pixmap_size.height()

        offset_x=(self.width()-current_pixmap.width()) /2
        offset_y=(self.height()-current_pixmap.height()) /2

        #positions du curseur dans le coordonnées de l'image originale
        pos_widget = event.position()
        pos_map_x = (pos_widget.x() - offset_x) / scale_x
        pos_map_y = (pos_widget.y() - offset_y) / scale_y

        #rayon de détection (en pixels de l'image originale)
        hit_radius = 15

        newly_hovered = None

        for callsign, data in self.aircraft_data.items():
            pos_avion = data['position']

            # Calcul de la distance euclidienne entre le curseur et l'avion
            dx = pos_map_x - pos_avion.x()
            dy = pos_map_y - pos_avion.y()
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < hit_radius:
                newly_hovered = callsign
                break

        #affichage/Masquage du ToolTip
        if newly_hovered:
            if newly_hovered != self.hovered_aircraft:
                self.show_aircraft_tooltip(newly_hovered, event.globalPosition())
                self.hovered_aircraft = newly_hovered
        elif self.hovered_aircraft:
            QToolTip.hideText()
            self.hovered_aircraft = None

        super().mouseMoveEvent(event)

    '''


    '''
    def mousePressEvent(self, event):
        #Détecte le clic et vérifie si un avion a été cliqué

        if event.button() == Qt.MouseButton.LeftButton:
            # Code de détection de position (similaire à mouseMoveEvent)
            current_pixmap = self.pixmap()
            if current_pixmap.isNull():
                return

            map_pixmap_size = self.map_pixmap.size()
            scale_x = current_pixmap.width() / map_pixmap_size.width()
            scale_y = current_pixmap.height() / map_pixmap_size.height()

            offset_x = (self.width() - current_pixmap.width()) / 2
            offset_y = (self.height() - current_pixmap.height()) / 2

            pos_widget = event.position()
            pos_map_x = (pos_widget.x() - offset_x) / scale_x
            pos_map_y = (pos_widget.y() - offset_y) / scale_y

            hit_radius = 15  # Rayon de clic

            for callsign, data in self.aircraft_data.items():
                pos_avion = data['position']
                dx = pos_map_x - pos_avion.x()
                dy = pos_map_y - pos_avion.y()
                distance = math.sqrt(dx ** 2 + dy ** 2)

                if distance < hit_radius:
                    #  AVION DÉTECTÉ : Émettre le signal avec le callsign
                    self.aircraft_clicked.emit(callsign)
                    break
    '''


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
        heading = data.heading
        speed = data.speed

        aircraft_item = AircraftItem(callsign, data)
        aircraft_item.setPos(data.pos[0], data.pos[1])
        self.scene.addItem(aircraft_item)

        self.aircraft_data[callsign] = {
            'item': aircraft_item,
            'heading': heading,
            'speed': speed
        }#stocke la vitesse et met à jour le dictionnaire



    '''
    def move_aircrafts(self, delta_time):

        #Déplace les objets QGraphicsItem sur la scène

        for callsign, data in self.aircraft_data.items():
            pos = data['position']
            heading = data['heading']
            speed = self.all_aircraft_details[callsign]['speed']

            # --- CALCUL DE LA NOUVELLE POSITION ---

            # 1. Convertir le cap en radians (ajustement pour 0°=Nord, 90°=Est)
            # En maths, 0 est l'axe X positif. Pour Qt/ATC (0=Nord, 90=Est), on utilise un angle ajusté.
            # L'axe X est lié au sinus du cap, et l'axe Y au cosinus du cap.
            heading_rad = math.radians(heading)

            # 2. Calcul des déplacements (dx, dy)
            # Déplacement X : lié au sinus (cap 90°/Est donne sin(90)=1)
            dx = speed * delta_time * math.sin(heading_rad)
            # Déplacement Y : lié au cosinus (cap 0°/Nord donne cos(0)=1, et on va vers le haut, donc négatif)
            dy = speed * delta_time * -math.cos(
                heading_rad)  # Y est inversé dans les coordonnées écran (Y+ est le bas)


            #mise à jour de la position dans le dictionnaire de la carte
            data['position'] = QPointF(pos.x() + dx, pos.y() + dy)
            if self.all_aircraft_details:
                self.all_aircraft_details[callsign]['pos'] = data['position']

            # 3. Mise à jour de la position
            new_x = pos.x() + dx
            new_y = pos.y() + dy

            # 4. Enregistrer la nouvelle position
            data['position'] = QPointF(new_x, new_y)

        # 5. Demander un redessinage global
        self.update()

    '''


    def move_aircrafts(self):
       self.aircraft_data = gestion_avion()


    def update_aircraft(self):

        #met à jour le cap d'un avion existant.

        for callsign in self.aircraft_items:
            item = self.aircraft_data[callsign]['item']
            item.setRotation(self.aircraft_data[callsign].heading)
            # demander à Qt de repeindre le widget pour appliquer la rotation
            self.update()