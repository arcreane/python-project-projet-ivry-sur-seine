


from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem
from PySide6.QtGui import QColor, QPen, QBrush, QFont
from PySide6.QtCore import Qt


class AirportDot(QGraphicsEllipseItem):
    """Représente le point d'aéroport sur la carte avec un effet de survol (hover)."""

    def __init__(self, airport_obj, dot_size=10):
        # Initialiser le cercle (point)
        super().__init__(
            airport_obj.x - dot_size / 2,
            airport_obj.y - dot_size / 2,
            dot_size, dot_size
        )

        self.airport_data = airport_obj
        self.dot_size = dot_size

        # Apparence (Jaune)
        self.setPen(QPen(QColor(0, 0, 0), 1))
        self.default_brush = QBrush(QColor(255, 255, 0))  # Jaune
        self.hover_brush = QBrush(QColor(255, 165, 0))  # Orange
        self.setBrush(self.default_brush)

        self.setAcceptHoverEvents(True)

        # Définir le ToolTip pour afficher les données au survol
        self.setToolTip(f"Aéroport : {self.airport_data.name} (Code IATA : {self.airport_data.iata})")

    def hoverEnterEvent(self, event):
        """Action lorsque le curseur entre (Hover Enter)."""
        self.setBrush(self.hover_brush)
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        """Action lorsque le curseur quitte (Hover Leave)."""
        self.setBrush(self.default_brush)
        super().hoverLeaveEvent(event)