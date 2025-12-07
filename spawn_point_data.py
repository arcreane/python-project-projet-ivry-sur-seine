
from PySide6.QtCore import QPointF



class SpawnPoint:
    #Représente un point d'entrée pour les avions sur la carte

    def __init__(self, name, x_pixel, y_pixel, initial_heading):
        """
        :param name: Nom du point (ex: 'NORD_OUEST').
        :param x_pixel: Coordonnée X sur l'image de la carte (int).
        :param y_pixel: Coordonnée Y sur l'image de la carte (int).
        :param initial_heading: Cap initial en degrés (0=Nord) pour l'avion spawné.
        """
        self.name = name
        self.x = x_pixel
        self.y = y_pixel
        self.heading = initial_heading
        self.pos = QPointF(x_pixel, y_pixel)



SPAWN_POINTS = [
    # Nord-Est (pour les avions venant d'Allemagne/Benelux)
    SpawnPoint("NE_ENTRY", x_pixel=1307, y_pixel=15, initial_heading=210),

    # Nord-Ouest (pour les avions venant du Royaume-Uni)
    SpawnPoint("NW_ENTRY", x_pixel=284, y_pixel=10, initial_heading=140),

    # Sud-Ouest (pour les avions allant vers Bordeaux/Atlantique)
    SpawnPoint("SW_ENTRY", x_pixel=459, y_pixel=747, initial_heading=45),

    # Sud-Est (pour les avions allant vers la Méditerranée/Suisse)
    SpawnPoint("SE_ENTRY", x_pixel=1177, y_pixel=740, initial_heading=315),
]