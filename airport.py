









class Airport:
    #Représente un aéroport fixe sur la carte ATC

    def __init__(self, name, iata_code, x_pixel, y_pixel):
        """
        Initialise un aéroport.
        :param name: Nom complet de l'aéroport (str).
        :param iata_code: Code IATA (e.g., 'CDG') (str).
        :param x_pixel: Coordonnée X sur l'image de la carte (int).
        :param y_pixel: Coordonnée Y sur l'image de la carte (int).
        """
        self.name = name
        self.iata = iata_code
        self.x = x_pixel
        self.y = y_pixel

# --- Liste des aéroports ---
# ATTENTION : Les coordonnées X_PIXEL et Y_PIXEL sont des exemples.
# Vous devez remplacer ces chiffres par les coordonnées que vous mesurez
# directement sur votre propre image de la France / région ATC.

AIRPORTS_DATA = [
    # ___________________________________________Région Parisienne
    Airport(name="Charles de Gaulle", iata_code="CDG", x_pixel=847, y_pixel=495),
    Airport(name="Orly", iata_code="ORY", x_pixel=824, y_pixel=585),

    # ____________________________________________Région Nord
    Airport(name="Lille-Lesquin", iata_code="LIL", x_pixel=894, y_pixel=115),
    #___________________________________________________________Est
    Airport(name="Strasbourg", iata_code="SXB", x_pixel=680, y_pixel=280),
    Airport(name="Bâle-Mulhouse", iata_code="BSL", x_pixel=700, y_pixel=350),  # Mulhouse est souvent référé par BSL/MLH
    Airport(name="Dole-Jura", iata_code="DLE", x_pixel=600, y_pixel=400),

    # ___________________________________________________Ouest / Bretagne
    Airport(name="Brest Bretagne", iata_code="BES", x_pixel=50, y_pixel=250),
    Airport(name="Rennes Bretagne", iata_code="RNS", x_pixel=200, y_pixel=300),

    # _______________________________________________________Sud-Ouest
    Airport(name="Bordeaux-Mérignac", iata_code="BOD", x_pixel=200, y_pixel=600),
    Airport(name="Toulouse-Blagnac", iata_code="TLS", x_pixel=300, y_pixel=750),

    # _________________________________________________________Sud-Est
    Airport(name="Montpellier-Méditerranée", iata_code="MPL", x_pixel=500, y_pixel=700),
    Airport(name="Marseille-Provence", iata_code="MRS", x_pixel=550, y_pixel=750),
    Airport(name="Nice Côte d'Azur", iata_code="NCE", x_pixel=700, y_pixel=700),

    # __________________________________________________________Région Rhône-Alpes
    Airport(name="Lyon Saint-Exupéry", iata_code="LYS", x_pixel=600, y_pixel=500)
]