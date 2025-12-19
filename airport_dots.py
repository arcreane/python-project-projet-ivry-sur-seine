


from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem,QToolTip
from PySide6.QtGui import QColor, QPen, QBrush, QFont
from PySide6.QtCore import Qt, QPointF, QPoint


class AirportDot(QGraphicsEllipseItem):
    #Représente le point d'aéroport sur la carte avec un effet de survol (hover)

    def __init__(self, airport, dot_size=10):
        #initialiser le cercle (point)
        super().__init__(
            airport['pos_x'] - dot_size / 2,
            airport['pos_y'] - dot_size / 2,
            dot_size, dot_size
        )

        self.airport_data = airport
        self.dot_size = dot_size

        #apparence en jaune
        self.setPen(QPen(QColor(0, 0, 0), 1))
        self.default_brush = QBrush(QColor(255, 255, 0))  #jaune
        self.hover_brush = QBrush(QColor(255, 165, 0))  #orange
        self.setBrush(self.default_brush)

        #definir le ToolTip pour afficher les données au survol
        self.default_brush = QBrush(QColor(255, 255, 0))  #jaune
        self.hover_brush = QBrush(QColor(255, 165, 0))  #orange
        self.setBrush(self.default_brush)