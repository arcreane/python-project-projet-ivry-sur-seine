


from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem,QToolTip
from PySide6.QtGui import QColor, QPen, QBrush, QFont
from PySide6.QtCore import Qt, QPointF, QPoint


class AirportDot(QGraphicsEllipseItem):
    #Représente le point d'aéroport sur la carte avec un effet de survol (hover)

    def __init__(self, airport_obj, dot_size=10):
        #initialiser le cercle (point)
        super().__init__(
            airport_obj.x - dot_size / 2,
            airport_obj.y - dot_size / 2,
            dot_size, dot_size
        )

        self.airport_data = airport_obj
        self.dot_size = dot_size

        #apparence en jaune
        self.setPen(QPen(QColor(0, 0, 0), 1))
        self.default_brush = QBrush(QColor(255, 255, 0))  #jaune
        self.hover_brush = QBrush(QColor(255, 165, 0))  #orange
        self.setBrush(self.default_brush)

        self.setAcceptHoverEvents(True)
        #definir le ToolTip pour afficher les données au survol
        self.tooltip_text = f"Aéroport : {self.airport_data.name}\nCode IATA : {self.airport_data.iata}"#definir les couleurs pour l'effet visuel (changé pour l'ellipse)
        self.default_brush = QBrush(QColor(255, 255, 0))  #jaune
        self.hover_brush = QBrush(QColor(255, 165, 0))  #orange
        self.setBrush(self.default_brush)


    def hoverEnterEvent(self, event):
        self.setBrush(self.hover_brush)
        QToolTip.showText(
            event.screenPos(),  #la position du curseur sur l'écran
            self.tooltip_text,  #le texte à afficher
            self.scene().views()[0]  #le widget parent (la QGraphicsView)
        )
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):

        self.setBrush(self.default_brush)
        QToolTip.hideText()
        super().hoverLeaveEvent(event)
