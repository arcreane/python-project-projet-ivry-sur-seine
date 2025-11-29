
from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtGui import QPainter, QPixmap, QColor, QTransform, QPen
from PySide6.QtCore import Qt, QPointF, QRectF, QSize, Signal
from PySide6.QtWidgets import QToolTip, QApplication
import math

class AircraftMapWidget(QLabel):

    aircraft_clicked = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScaledContents(True) # La carte elle-même sera mise à l'échelle
        self.setAlignment(Qt.AlignmentFlag.AlignCenter) # Centre la carte
        self.aircraft_data = {}  # Stocke les avions : {'callsign': {'position': QPointF, 'heading': float}}
        self.setMinimumSize(QSize(1, 1)) # Important pour les QLabels dans les layouts
        self.setMouseTracking(True)  #active le suivi de la souris
        self.hovered_aircraft = None
        self.aircraft_items = {}

    def set_map_image(self, pixmap_path):
        #Définit l'image de fond de la carte
        self.map_pixmap = QPixmap(pixmap_path)
        self.setPixmap(self.map_pixmap)
        self.update()

    def add_aircraft(self, callsign, position: QPointF, heading: float):
        """Ajoute ou met à jour un avion sur la carte.
        :param position: QPointF(x, y) - position en pixels sur la carte.
        :param heading: Angle en degrés (0=Nord, 90=Est).
        """
        self.aircraft_data[callsign] = {'position': position, 'heading': heading}
        self.update() # Déclenche un redessinage pour afficher le nouvel avion

    def remove_aircraft(self, callsign):
        """Supprime un avion de la carte."""
        if callsign in self.aircraft_data:
            del self.aircraft_data[callsign]
            self.update()

    def paintEvent(self, event):
        """Surcharge la méthode de dessin pour inclure les avions."""
        super().paintEvent(event) # Dessine d'abord la carte de fond

        if not self.map_pixmap.isNull():
            painter = QPainter(self)

            # Ajuster le peintre pour dessiner sur l'image à l'échelle
            # Ceci est crucial pour que les coordonnées de l'avion correspondent à l'image affichée
            current_pixmap = self.pixmap()
            if not current_pixmap.isNull():
                scale_x = current_pixmap.width() / self.map_pixmap.width()
                scale_y = current_pixmap.height() / self.map_pixmap.height()

                offset_x = (self.width() - current_pixmap.width()) / 2
                offset_y = (self.height() - current_pixmap.height()) / 2

                # Déplacer l'origine du peintre pour correspondre au coin supérieur gauche de la pixmap
                painter.translate(offset_x, offset_y)

                # Appliquer la mise à l'échelle
                painter.scale(scale_x, scale_y)

            # Dessiner chaque avion
            for callsign, data in self.aircraft_data.items():
                pos = data['position']
                heading = data['heading']

                # Dessiner le carré de l'avion
                square_size = 8 # Taille du carré en pixels de l'image originale
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

                painter.setPen(QPen(QColor(0, 255, 0), 2)) # Ligne verte
                painter.drawLine(QPointF(0, 0), QPointF(0, -line_length)) # Dessine la ligne vers le haut (Nord)

                painter.restore() # Restaure l'état du peintre (supprime la translation et la rotation)

            painter.end()

    def mouseMoveEvent(self, event):
        """Détecte si le curseur de la souris survole un avion."""

        current_pixmap = self.pixmap()
        if current_pixmap.isNull():
            return

        # Calcul de l'échelle et du décalage (code réutilisé de paintEvent)
        map_pixmap_size = self.map_pixmap.size()
        scale_x = current_pixmap.width() / map_pixmap_size.width()
        scale_y = current_pixmap.height() / map_pixmap_size.height()

        offset_x = (self.width() - current_pixmap.width()) / 2
        offset_y = (self.height() - current_pixmap.height()) / 2

        # Position du curseur dans les coordonnées de l'image originale
        pos_widget = event.position()
        pos_map_x = (pos_widget.x() - offset_x) / scale_x
        pos_map_y = (pos_widget.y() - offset_y) / scale_y

        # Rayon de détection (en pixels de l'image originale)
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

        # Affichage/Masquage du ToolTip
        if newly_hovered:
            if newly_hovered != self.hovered_aircraft:
                self.show_aircraft_tooltip(newly_hovered, event.globalPosition())
                self.hovered_aircraft = newly_hovered
        elif self.hovered_aircraft:
            QToolTip.hideText()
            self.hovered_aircraft = None

        super().mouseMoveEvent(event)

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
                    # 🟢 AVION DÉTECTÉ : Émettre le signal avec le callsign
                    self.aircraft_clicked.emit(callsign)
                    break

    def show_aircraft_tooltip(self, callsign, global_pos: QPointF):
        """Construit et affiche la bulle d'aide pour l'avion."""

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

    def update_aircraft(self, callsign, new_heading):
        """
        Met à jour le cap d'un avion existant.
        """
        if callsign in self.aircraft_items:
            # mettre à jour le cap dans l'objet de l'avion
            self.aircraft_items[callsign]['heading'] = new_heading
            # demander à Qt de repeindre le widget pour appliquer la rotation
            self.update()
        else:
            print(f"Erreur: Avion {callsign} non trouvé pour la mise à jour.")