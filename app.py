

#___________________________________les_imports________________________________________
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsTextItem # Mis à jour
from PySide6.QtGui import QColor, QFont # Mis à jour
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer, QPointF
import math
#__________________________________les_imports_de_fichiers_________________________________________
from ATC_paris import Ui_ATC_paris  # import de la window paris
from ATC_reims import Ui_ATC_reims# import de la window reims
from ATC_brest import Ui_ATC_brest# import de la window brest
from ATC_bordeaux import Ui_ATC_bordeaux# import de la window bordeaux
from ATC_marseille import Ui_ATC_marseille# import de la window marseille

from ATC_accueil import Ui_ATC_accueil  #import de la main window
from airport import AIRPORTS_DATA #on importe la liste des aeroport depuis le fichier pévu a cet effet
from airport_dots import AirportDot  #on importe ce qui permet de dessiner les aeroports
from utilities import json_data, json_avion, import_json_data
from gestion_avion import init_avion, gestion_avion, landing


#___________________________________________________________________________

LANDING_DISTANCE_THRESHOLD = 80
LANDING_THRESHOLD_PIXELS = 80
REMOVAL_THRESHOLD_PIXELS = 10 # Seuil de retrait (doit être atteint

#__________________________class_accueil________________________________

class ATC_accueil(QMainWindow, Ui_ATC_accueil):          #def de la page accueil
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATC Simulator - Accueil") #titre de la page
        #_____________________________paris
        self.ATC_parislfff.clicked.connect(self.ouvrir_paris) #déclenchement du bouton et ouvre paris
        self.fenetre_paris = None
        #_____________________________reims
        self.ATC_reimslfee.clicked.connect(self.ouvrir_reims)  # déclenchement du bouton et ouvre reims
        self.fenetre_reims = None
        #_____________________________marseille
        self.ATC_marseillelfmm.clicked.connect(self.ouvrir_marseille)  # déclenchement du bouton et ouvre marseille
        self.fenetre_marseille = None
        #_____________________________bordeaux
        self.ATC_bordeauxlfbb.clicked.connect(self.ouvrir_bordeaux)  # déclenchement du bouton et ouvre bordeaux
        self.fenetre_bordeaux = None
        #_____________________________brest
        self.ATC_brestlfrr.clicked.connect(self.ouvrir_brest)  # déclenchement du bouton et ouvre brest
        self.fenetre_brest = None
        #______________________________btn_sorti
        self.btn_sortie.clicked.connect(QApplication.quit)

    def ouvrir_paris(self):           #fonction qui ouvre paris
        self.fenetre_paris = ATC_parislfff()
        self.fenetre_paris.showMaximized() #permet douvrir la fenetre en pleine ecran
        json_data('paris')
        json_avion('paris')
        self.close()

    def ouvrir_reims(self):           #fonction qui ouvre reims
        self.fenetre_reims = ATC_reimslfee()
        self.fenetre_reims.showMaximized() #permet douvrir la fenetre en pleine ecran
        json_data('reims')
        json_avion('reims')
        self.close()

    def ouvrir_marseille(self):           #fonction qui ouvre marseille
        self.fenetre_marseille = ATC_marseillelfmm()
        self.fenetre_marseille.showMaximized() #permet douvrir la fenetre en pleine ecran
        json_data('merseille')
        json_avion('marseille')
        self.close()

    def ouvrir_bordeaux(self):           #fonction qui ouvre bordeaux
        self.fenetre_bordeaux = ATC_bordeauxlfbb()
        self.fenetre_bordeaux.showMaximized() #permet douvrir la fenetre en pleine ecran
        json_data('bordeaux')
        json_avion('bordeaux')
        self.close()

    def ouvrir_brest(self):           #fonction qui ouvre brest
        self.fenetre_brest = ATC_brestlfrr()
        self.fenetre_brest.showMaximized() #permet douvrir la fenetre en pleine ecran
        json_data('brest')
        json_avion('brest')
        self.close()

class ATC_parislfff(QMainWindow, Ui_ATC_paris):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # --- avions (OBJETS persistants)
        self.aircrafts = init_avion()
        self.label_5.all_aircraft_details = self.aircrafts

        self.selected_callsign = None

        # --- affichage initial
        for cs, avion in self.aircrafts.items():
            self.label_5.add_aircraft(cs, avion)

        # --- affichage des aéroports
        self._load_airports_on_map()

        # --- signaux
        self.label_5.aircraft_clicked.connect(self.display_aircraft)
        self.btn_apply.clicked.connect(self.apply_command)
        self.btn_accueil.clicked.connect(self.back_home)
        self.btn_sortie.clicked.connect(QApplication.quit)
        self.btn_land.clicked.connect(self.apply_landing)

        # --- timer simulation (1 tick = 1 update)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.simulation_step)
        self.timer.start(1000)  # 1 seconde


    # ============================
    #  SIMULATION
    # ============================

    def simulation_step(self):
        # met à jour l'affichage
        self.label_5.move_aircrafts()

        # met à jour panneau si avion sélectionné
        if self.selected_callsign:
            self.display_aircraft(self.selected_callsign, refresh_only=True)


    # ============================
    #  UI / COMMANDES
    # ============================

    def display_aircraft(self, callsign, refresh_only=False):
        if callsign not in self.aircrafts:
            return

        self.selected_callsign = callsign
        avion = self.aircrafts[callsign]

        self.txt_titre.setText(f"Contrôle – {callsign}")

        if not refresh_only:
            self.txt_heading_valeur.setText(str(int(avion.heading)))
            self.txt_altitude_valeur.setText(str(int(avion.alt)))
            self.txt_vitesse_valeur.setText(str(int(avion.speed)))
            self.txt_vitesse_verticale_valeur.setText(str(int(avion.vs)))


    def apply_command(self):
        if not self.selected_callsign:
            return

        avion = self.aircrafts[self.selected_callsign]

        try:
            avion.consigne_change({
                'heading': int(self.txt_heading_valeur.toPlainText()),
                'alt': int(self.txt_altitude_valeur.toPlainText()),
                'speed': int(self.txt_vitesse_valeur.toPlainText()),
                'vs': int(self.txt_vitesse_verticale_valeur.toPlainText())
            })
            self.statusBar().showMessage(
                f"Commande appliquée à {avion.callsign}", 3000
            )

        except ValueError:
            self.statusBar().showMessage("Saisie invalide", 3000)

    def apply_landing(self):
        if not self.selected_callsign:
            self.statusBar().showMessage(
                "Aucun avion sélectionné", 3000
            )
            return

        avion = self.aircrafts[self.selected_callsign]

        # Vérification optionnelle : autorisation d'atterrir
        if not avion.etat.get("can_land", False):
            self.statusBar().showMessage(
                f"{avion.callsign} n'est pas en zone d'approche", 3000
            )
            return

        # Mise à jour de la consigne d'atterrissage
        avion.consigne_change({
            'landing': True
        })

        self.statusBar().showMessage(
            f"Atterrissage autorisé pour {avion.callsign}", 4000
        )

    def _load_airports_on_map(self):
        data = import_json_data() # Paris
        CODES = ['LFPG', 'LFPO', 'LFQQ']

        font = QFont("Arial", 13)
        text_color = QColor(255, 255, 0)

        for airport in CODES:

            # Point aéroport
            airport_dot_item = AirportDot(data[airport])
            self.label_5.scene.addItem(airport_dot_item)

            # Label IATA
            label = QGraphicsTextItem(airport)
            label.setFont(font)
            label.setDefaultTextColor(text_color)
            label.setPos(data[airport]['pos_x'] + 7, data[airport]['pos_y'] - 15)
            self.label_5.scene.addItem(label)

            # Cercle de zone d'atterrissage
            target_pos = QPointF(data[airport]['pos_x'], data[airport]['pos_y'])
            self.label_5.display_airport_geofence(
                airport,
                target_pos,
                LANDING_THRESHOLD_PIXELS
            )

    def back_home(self):
        self.home = ATC_accueil()
        self.home.showMaximized()
        self.close()


class ATC_reimslfee(QMainWindow, Ui_ATC_reims):       #def de la page paris
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATC_reimsLFEE") #titre de la page
        self.btn_accueil.clicked.connect(self.retour_accueil)   #declenchement du bouton et ouvre la page daccueil
        self.btn_sortie.clicked.connect(QApplication.quit)

    def retour_accueil(self):        #fonction btn_accueil
        from app import ATC_accueil
        self.accueil = ATC_accueil()
        self.accueil.showMaximized()      #permet douvrir la fenetre en pleine ecran
        self.close()       # permet de refermer la fenetre

class ATC_brestlfrr(QMainWindow, Ui_ATC_brest):       #def de la page paris
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATC_brestLFRR") #titre de la page
        self.btn_accueil.clicked.connect(self.retour_accueil)   #declenchement du bouton et ouvre la page daccueil
        self.btn_sortie.clicked.connect(QApplication.quit)

        self.aircraft_details = self._create_initial_aircrafts()
        self.label_5.all_aircraft_details = self.aircraft_details #on assigne le dico au widget map
        self.selected_callsign = None
        self._load_aircraft_on_map()
        self._load_airports_on_map()
        self._connect_signals()

        #on introduit la notion de temps pour faire bouger les avions
        self.simulation_timer = QTimer(self)
        self.simulation_timer.timeout.connect(self.run_simulation_step)
        self.simulation_timer.start(1000)  # Rafraîchit toutes les 1000 ms (delta_time = 1s)


    def run_simulation_step(self):
        #déclenche la mise à jour des positions de tous les avions
        delta_time = 0.1  # 100 ms / 1000 ms = 0.1 seconde

        #le widget carte gère le déplacement de tous les avions
        self.label_5.move_aircrafts(delta_time)

        is_input_active = (
                self.txt_heading_valeur.hasFocus() or
                self.txt_altitude_valeur.hasFocus() or
                self.txt_vitesse_valeur.hasFocus() or
                self.txt_vitesse_verticale_valeur.hasFocus()
        )

        if is_input_active:
            #si l'utilisateur est en train de saisir dans un champ, on ne met pas à jour l'affichage
            return
        #si le champ de Cap (ou un autre) a le focus, NE PAS écraser la saisie.
        if self.txt_heading_valeur.hasFocus() or self.txt_vitesse_valeur.hasFocus():
            #si l'utilisateur est en train de saisir, on sort sans appeler display_aircraft_stats
            return
        if self.selected_callsign:
            self.display_aircraft_stats(self.selected_callsign)

    def _load_aircraft_on_map(self):
        #charge les avions sur le widget carte
        for callsign, data in self.aircraft_details.items():
            self.label_5.add_aircraft(callsign, data)

    def _connect_signals(self):
        #connecte le signal de clic de la carte à la méthode d'affichage des stats

        self.label_5.aircraft_clicked.connect(self.display_aircraft_stats)
        self.btn_apply.clicked.connect(self.apply_new_command)
        self.btn_land.clicked.connect(self.initiate_landing_sequence)

    def initiate_landing_sequence(self):
        #lance la sequence datterissage uniquement si lavion est dans le cercle
        callsign = self.selected_callsign

        if not callsign or callsign not in self.aircraft_details:
            self.statusBar().showMessage("Veuillez sélectionner un avion d'abord.", 3000)
            return

        aircraft_pos = self.aircraft_details[callsign]['pos']

        target_airport = None
        min_dist_sq = LANDING_THRESHOLD_PIXELS ** 2

        #recherche de l'aéroport le plus proche DANS la zone de seuil

        for airport in AIRPORTS_DATA:

            dx = aircraft_pos.x() - airport.x
            dy = aircraft_pos.y() - airport.y
            dist_sq = dx ** 2 + dy ** 2

            #nous cherchons le plus proche, MAIS qui doit être DANS le seuil
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                target_airport = airport  #l'aéroport le plus proche DANS la zone

        # ----------------------------------------------------
        # 2. Exécution de la commande
        # ----------------------------------------------------
        if target_airport:
            #l'avion est dans la zone : lancer la séquence d'atterrissage

            #création du QPointF cible
            target_pos_qpointf = QPointF(target_airport.x, target_airport.y)

            #calculer le nouveau cap vers l'aéroport
            new_heading = self.calculate_heading_to_target(aircraft_pos, target_pos_qpointf)

            #mise à jour des données (Cap et Vitesse réduite)
            self.aircraft_details[callsign]['heading'] = new_heading
            self.aircraft_details[callsign]['speed'] = 20
            self.aircraft_details[callsign]['vertical_speed'] = 0  #pas de descente si atterrissage distance seule

            #mettre à jour l'affichage de l'avion sur la carte et afficher le cercle
            self.label_5.update_aircraft(callsign, new_heading)
            self.label_5.set_landing_target(callsign, target_pos_qpointf, LANDING_THRESHOLD_PIXELS)
            self.display_aircraft_stats(callsign)  #mettre à jour le panneau de droite

            self.statusBar().showMessage(f"LAND: {callsign} guidé vers {target_airport.iata}", 5000)

        else:
            #l'avion n'est pas dans le cercle de seuil d'un aéroport autorisé
            self.statusBar().showMessage(
                f"L'avion n'est pas en zone d'approche finale autorisée ({LANDING_THRESHOLD_PIXELS}px).", 3000)

    def calculate_heading_to_target(self, current_pos: QPointF, target_pos: QPointF) -> float:
        #Calcule le cap (en degrés, 0=Nord) pour aller de la position actuelle à la cible

        #différences en pixels
        dx = target_pos.x() - current_pos.x()
        dy = target_pos.y() - current_pos.y()

        #calcul de l'angle en radians (-180 à 180)
        angle_rad = math.atan2(dx, -dy)  # -dy car l'axe Y des pixels est inversé (positif vers le bas)

        #conversion en degrés (0 à 360)
        heading_deg = math.degrees(angle_rad)

        #normalisation du cap (0 à 360)
        return (heading_deg + 360) % 360

    def display_aircraft_stats(self, callsign):

        #Reçoit le callsign de l'avion cliqué et remplit les champs de texte du panneau.

        if callsign not in self.aircraft_details:
            return

        self.selected_callsign = callsign
        data = self.aircraft_details[callsign]

        #mise à jour du titre
        self.txt_titre.setText(f"Contrôle - {callsign}")

        #mise à jour du CAP/HEADING (Requis)
        #self.txt_heading_valeur est un QTextEdit
        self.txt_heading_valeur.setText(str(data["heading"]))

        #mise à jour des autres champs pour la complétude
        self.txt_altitude_valeur.setText(str(data["altitude"]))
        self.txt_vitesse_valeur.setText(str(data["speed"]))
        self.txt_vitesse_verticale_valeur.setText(str(data["vertical_speed"]))

    def apply_new_command(self):

        callsign = self.selected_callsign

        if not callsign or callsign not in self.aircraft_details:
            print("Erreur: Aucun avion sélectionné.")
            return

        try:
            new_heading = int(self.txt_heading_valeur.toPlainText())
            new_altitude = int(self.txt_altitude_valeur.toPlainText())
            new_speed = int(self.txt_vitesse_valeur.toPlainText())
            new_vertical_speed = int(self.txt_vitesse_verticale_valeur.toPlainText())

            consigne = {
                "heading": new_heading,
                "alt": new_altitude,
                "speed": new_speed,
                "vs": new_vertical_speed,
                "landing": False
            }

            # On applique la consigne à l'objet avion
            self.aircraft_details[callsign].consigne_change(consigne)

            self.statusBar().showMessage(
                f"Commande appliquée à {callsign}: Cap {new_heading}°"
            )

        except ValueError:
            print("Erreur: saisie invalide.")

    def retour_accueil(self):  #fonction btn_accueil
        from app import ATC_accueil
        self.accueil = ATC_accueil()
        self.accueil.showMaximized()      #permet douvrir la fenetre en pleine ecran
        self.close()       # permet de refermer la fenetre

    def _load_airports_on_map(self):
        CODES_AUTORISES = ["BES", "RNS"]

        font = QFont("Arial", 13)
        text_color = QColor(255, 255, 0)
        #boucle : charger uniquement les AÉROPORTS
        for airport in AIRPORTS_DATA:

            if airport.iata in CODES_AUTORISES:
                #dessin aeroport (point jaune)
                airport_dot_item = AirportDot(airport)
                self.label_5.scene.addItem(airport_dot_item)

                #dessin de letiquette iata
                label = QGraphicsTextItem(airport.iata)
                label.setFont(font)
                label.setDefaultTextColor(text_color)

                #positionnement
                label.setPos(airport.x + 10 / 2 + 2, airport.y - 10)
                self.label_5.scene.addItem(label)

        for airport in AIRPORTS_DATA:
            if airport.iata in CODES_AUTORISES:
                #dessin aeroport et etiquette
                airport_dot_item = AirportDot(airport)
                self.label_5.scene.addItem(airport_dot_item)


                #affichage permanent du cercle
                target_pos = QPointF(airport.x, airport.y)

                #appel une nouvelle méthode sur le widget carte pour dessiner le cercle
                self.label_5.display_airport_geofence(airport.iata, target_pos, LANDING_THRESHOLD_PIXELS)

    def _create_initial_aircrafts(self):

        #Crée un ensemble d'avions initiaux en utilisant les points de spawn.

        initial_aircrafts = {}
        callsign_counter = 100

        for sp in SPAWN_POINTS:
            callsign = f"AFR{callsign_counter}"

            #on assigne les caractéristiques du SpawnPoint
            initial_aircrafts[callsign] = {
                "heading": sp.heading,
                "altitude": 30000,  #altitude de croisière par défaut
                "speed": 60,  #vitesse de croisière
                "vertical_speed": 0,
                "pos": sp.pos  # position QPointF du SpawnPoint
            }
            callsign_counter += 1

        return initial_aircrafts

class ATC_bordeauxlfbb(QMainWindow, Ui_ATC_bordeaux):       #def de la page paris
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATC_bordeauxLFBB") #titre de la page
        self.btn_accueil.clicked.connect(self.retour_accueil)   #declenchement du bouton et ouvre la page daccueil
        self.btn_sortie.clicked.connect(QApplication.quit)

    def retour_accueil(self):        #fonction btn_accueil
        from app import ATC_accueil
        self.accueil = ATC_accueil()
        self.accueil.showMaximized()      #permet douvrir la fenetre en pleine ecran
        self.close()       # permet de refermer la fenetre

class ATC_marseillelfmm(QMainWindow, Ui_ATC_marseille):       #def de la page paris
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATC_marseilleLFmm") #titre de la page
        self.btn_accueil.clicked.connect(self.retour_accueil)   #declenchement du bouton et ouvre la page daccueil
        self.btn_sortie.clicked.connect(QApplication.quit)

    def retour_accueil(self):        #fonction btn_accueil
        from app import ATC_accueil
        self.accueil = ATC_accueil()
        self.accueil.showMaximized()      #permet douvrir la fenetre en pleine ecran
        self.close()       # permet de refermer la fenetre

#__________________________________________________________

if __name__ == "__main__":   # lance par defaut la fenetre accueil
    app = QApplication(sys.argv)
    window = ATC_accueil()
    window.showMaximized()
    sys.exit(app.exec())
