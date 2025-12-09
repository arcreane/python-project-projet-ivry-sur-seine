
from PySide6.QtCore import QPointF


class SpawnPoint:
    #Représente un point d'entrée pour les avions sur la carte

    def __init__(self, name, x_pixel, y_pixel, initial_heading):

        self.name = name           #nom
        self.x = x_pixel        #coord x sur limage de la carte
        self.y = y_pixel        #coord y sur limage de la carte
        self.heading = initial_heading          #cap des avions qui spawnent
        self.pos = QPointF(x_pixel, y_pixel)



SPAWN_POINTS = [
    #nord-est (pour les avions venant d'Allemagne/Benelux)
    SpawnPoint("NE_ENTRY", x_pixel=1307, y_pixel=15, initial_heading=210),

    #nord-ouest (pour les avions venant du Royaume-Uni)
    SpawnPoint("NW_ENTRY", x_pixel=284, y_pixel=10, initial_heading=140),

    #sud-ouest (pour les avions allant vers Bordeaux/Atlantique)
    SpawnPoint("SW_ENTRY", x_pixel=459, y_pixel=747, initial_heading=45),

    #sud-est (pour les avions allant vers la Méditerranée/Suisse)
    SpawnPoint("SE_ENTRY", x_pixel=1177, y_pixel=740, initial_heading=315),
]