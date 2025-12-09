

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
from spawn_point_data import SPAWN_POINTS #on import les points de spawn des avions


#___________________________________________________________________________

LANDING_DISTANCE_THRESHOLD = 80
LANDING_THRESHOLD_PIXELS = 80
REMOVAL_THRESHOLD_PIXELS = 10 # Seuil de retrait (doit être atteint)




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
        self.close()

    def ouvrir_reims(self):           #fonction qui ouvre reims
        self.fenetre_reims = ATC_reimslfee()
        self.fenetre_reims.showMaximized() #permet douvrir la fenetre en pleine ecran
        self.close()

    def ouvrir_marseille(self):           #fonction qui ouvre marseille
        self.fenetre_marseille = ATC_marseillelfmm()
        self.fenetre_marseille.showMaximized() #permet douvrir la fenetre en pleine ecran
        self.close()

    def ouvrir_bordeaux(self):           #fonction qui ouvre bordeaux
        self.fenetre_bordeaux = ATC_bordeauxlfbb()
        self.fenetre_bordeaux.showMaximized() #permet douvrir la fenetre en pleine ecran
        self.close()

    def ouvrir_brest(self):           #fonction qui ouvre brest
        self.fenetre_brest = ATC_brestlfrr()
        self.fenetre_brest.showMaximized() #permet douvrir la fenetre en pleine ecran
        self.close()

#_____________________BOUTONS____________________________________

class ATC_parislfff(QMainWindow, Ui_ATC_paris):       #def de la page paris
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATC_parisfLFFF") #titre de la page
        self.btn_accueil.clicked.connect(self.retour_accueil)   #declenchement du bouton et ouvre la page daccueil
        self.btn_sortie.clicked.connect(QApplication.quit)
        '''
        self.aircraft_details = {
            "AFR123": {"heading": 45, "altitude": 32000, "speed": 50, "vertical_speed": 0, "pos": QPointF(800, 200)},
            "BAW456": {"heading": 180, "altitude": 28000, "speed": 50, "vertical_speed": 1000,"pos": QPointF(200, 400)},
            "AFR789": {"heading": 60, "altitude": 32000, "speed": 50, "vertical_speed": 0, "pos": QPointF(400,100)},
            "BAW054": {"heading": 300, "altitude": 28000, "speed": 50, "vertical_speed": 1000, "pos": QPointF(100, 400)}
        }
        '''
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
            # Si l'utilisateur est en train de saisir dans un champ, on ne met pas à jour l'affichage
            return
        # Si le champ de Cap (ou un autre) a le focus, NE PAS écraser la saisie.
        if self.txt_heading_valeur.hasFocus() or self.txt_vitesse_valeur.hasFocus():
            # Si l'utilisateur est en train de saisir, on sort sans appeler display_aircraft_stats
            return
        if self.selected_callsign:
            self.display_aircraft_stats(self.selected_callsign)

    def _load_aircraft_on_map(self):
        """Charge les avions sur le widget carte."""
        for callsign, data in self.aircraft_details.items():
            self.label_5.add_aircraft(callsign, data)

    def _connect_signals(self):
        """Connecte le signal de clic de la carte à la méthode d'affichage des stats."""
        # 🟢 CONNEXION SIGNAL -> SLOT
        # self.label_5 est l'AircraftMapWidget
        self.label_5.aircraft_clicked.connect(self.display_aircraft_stats)
        self.btn_apply.clicked.connect(self.apply_new_command)

        self.btn_land.clicked.connect(self.initiate_landing_sequence)
        # Connectez vos autres boutons ici (Apply, Land, etc.)
        # self.btn_apply.clicked.connect(self.apply_new_command)
    '''
    def initiate_landing_sequence(self):

        #Lance la séquence d'atterrissage pour l'avion sélectionné trouve l'aéroport le plus proche et dirige l'avion vers lui.
        callsign = self.selected_callsign

        if not callsign or callsign not in self.aircraft_details:
            self.statusBar().showMessage("Veuillez sélectionner un avion d'abord.", 3000)
            return

        aircraft_pos = self.aircraft_details[callsign]['pos']
        nearest_airport = None
        min_dist_sq = LANDING_THRESHOLD_PIXELS ** 2
        # 1. Trouver l'aéroport le plus proche
        # Utilisation de la liste des aéroports autorisés pour cette zone

        for airport in AIRPORTS_DATA:
            # ⚠️ NOTE: Si vous ne voulez pas atterrir sur TOUS les aéroports_data,
            # vous devrez filtrer ici (ex: si airport.iata in CODES_AUTORISES).

            dx = aircraft_pos.x() - airport.x
            dy = aircraft_pos.y() - airport.y
            dist_sq = dx ** 2 + dy ** 2

            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                nearest_airport = airport

        if airport_in_range:
            # L'avion est dans la zone : lancer la séquence d'atterrissage
            target_pos_qpointf = QPointF(airport_in_range.x, airport_in_range.y)

            # 2. Continuer la séquence de suppression (Land)
            new_heading = self.calculate_heading_to_target(aircraft_pos, target_pos_qpointf)
            self.aircraft_details[callsign]['heading'] = new_heading
            self.aircraft_details[callsign]['speed'] = 20
            self.aircraft_details[callsign]['vertical_speed'] = 0

            self.label_5.update_aircraft(callsign, new_heading)
            self.label_5.set_landing_target(callsign, target_pos_qpointf, LANDING_THRESHOLD_PIXELS)
            self.display_aircraft_stats(callsign)

            self.statusBar().showMessage(f"LAND: {callsign} atterrit à {airport_in_range.iata}", 5000)

        else:
            # 🟢 L'avion n'est pas encore dans la zone d'approche définie (80 pixels)
            self.statusBar().showMessage("L'avion n'est pas en zone d'approche finale autorisée.", 3000)

        if nearest_airport:

            target_pos_qpointf = QPointF(nearest_airport.x, nearest_airport.y)   #Créer un QPointF pour la position cible à partir de x et y.

            self.label_5.set_landing_target(callsign, target_pos_qpointf, 80)

            # 2. Calculer le nouveau cap vers l'aéroport
            new_heading = self.calculate_heading_to_target(aircraft_pos, target_pos_qpointf)

            # 3. Mettre à jour les données (cap et vitesse réduite)
            self.aircraft_details[callsign]['heading'] = new_heading
            self.aircraft_details[callsign]['speed'] = 20  # Vitesse réduite pour l'approche
            self.aircraft_details[callsign]['vertical_speed'] = 0

            # 4. Mettre à jour l'affichage de l'avion sur la carte
            self.label_5.update_aircraft(callsign, new_heading)
            self.label_5.set_landing_target(callsign, nearest_airport.pos,LANDING_DISTANCE_THRESHOLD)  #  NOUVELLE MÉTHODE

            # 5. Mettre à jour les stats du panneau de droite (pour refléter le nouveau cap et vitesse)
            self.display_aircraft_stats(callsign)
            self.statusBar().showMessage(f"Guidage {callsign} vers {nearest_airport.iata} (Cap {new_heading:.0f}°)",
                                         5000)

        else:
            self.statusBar().showMessage("Aucun aéroport valide trouvé pour l'approche.", 3000)'''

    def initiate_landing_sequence(self):
        """
        Lance la séquence d'atterrissage pour l'avion sélectionné.
        L'avion est dirigé vers l'aéroport le plus proche, SEULEMENT s'il est
        déjà à l'intérieur du seuil de proximité (LANDING_THRESHOLD_PIXELS).
        """
        callsign = self.selected_callsign

        if not callsign or callsign not in self.aircraft_details:
            self.statusBar().showMessage("Veuillez sélectionner un avion d'abord.", 3000)
            return

        aircraft_pos = self.aircraft_details[callsign]['pos']

        # 🟢 VÉRIFIEZ QUE CODES_AUTORISES ET AIRPORTS_DATA sont accessibles ici
        # Si CODES_AUTORISES n'est pas global, définissez-le :
        # CODES_AUTORISES = ["CDG", "ORY", "LIL"]

        target_airport = None
        min_dist_sq = LANDING_THRESHOLD_PIXELS ** 2

        # 1. Recherche de l'aéroport le plus proche DANS la zone de seuil

        # NOTE: Pour la démo, nous utilisons tous les aéroports, mais vous pouvez filtrer
        for airport in AIRPORTS_DATA:
            # Optional: if airport.iata not in CODES_AUTORISES: continue

            dx = aircraft_pos.x() - airport.x
            dy = aircraft_pos.y() - airport.y
            dist_sq = dx ** 2 + dy ** 2

            # Nous cherchons le plus proche, MAIS qui doit être DANS le seuil
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                target_airport = airport  # L'aéroport le plus proche DANS la zone

        # ----------------------------------------------------
        # 2. Exécution de la commande
        # ----------------------------------------------------
        if target_airport:
            # L'avion est dans la zone : lancer la séquence d'atterrissage

            # création du QPointF cible
            target_pos_qpointf = QPointF(target_airport.x, target_airport.y)

            # calculer le nouveau cap vers l'aéroport
            new_heading = self.calculate_heading_to_target(aircraft_pos, target_pos_qpointf)

            # mise à jour des données (Cap et Vitesse réduite)
            self.aircraft_details[callsign]['heading'] = new_heading
            self.aircraft_details[callsign]['speed'] = 20
            self.aircraft_details[callsign]['vertical_speed'] = 0  # Pas de descente si atterrissage distance seule

            # mettre à jour l'affichage de l'avion sur la carte et afficher le cercle
            self.label_5.update_aircraft(callsign, new_heading)
            self.label_5.set_landing_target(callsign, target_pos_qpointf, LANDING_THRESHOLD_PIXELS)
            self.display_aircraft_stats(callsign)  # Mettre à jour le panneau de droite

            self.statusBar().showMessage(f"LAND: {callsign} guidé vers {target_airport.iata}", 5000)

        else:
            # L'avion n'est pas dans le cercle de seuil d'un aéroport autorisé
            self.statusBar().showMessage(
                f"L'avion n'est pas en zone d'approche finale autorisée ({LANDING_THRESHOLD_PIXELS}px).", 3000)


    def calculate_heading_to_target(self, current_pos: QPointF, target_pos: QPointF) -> float:
        """Calcule le cap (en degrés, 0=Nord) pour aller de la position actuelle à la cible."""

        # Différences en pixels
        dx = target_pos.x() - current_pos.x()
        dy = target_pos.y() - current_pos.y()

        # Calcul de l'angle en radians (-180 à 180)
        angle_rad = math.atan2(dx, -dy)  # -dy car l'axe Y des pixels est inversé (positif vers le bas)

        # Conversion en degrés (0 à 360)
        heading_deg = math.degrees(angle_rad)

        # Normalisation du cap (0 à 360)
        return (heading_deg + 360) % 360

    def display_aircraft_stats(self, callsign):
        """
        Reçoit le callsign de l'avion cliqué et remplit les champs de texte du panneau.
        """
        if callsign not in self.aircraft_details:
            return

        self.selected_callsign = callsign
        data = self.aircraft_details[callsign]

        # Mise à jour du titre
        self.txt_titre.setText(f"Contrôle - {callsign}")

        # 🎯 Mise à jour du CAP/HEADING (Requis)
        # self.txt_heading_valeur est un QTextEdit
        self.txt_heading_valeur.setText(str(data["heading"]))

        # Mise à jour des autres champs pour la complétude
        self.txt_altitude_valeur.setText(str(data["altitude"]))
        self.txt_vitesse_valeur.setText(str(data["speed"]))
        self.txt_vitesse_verticale_valeur.setText(str(data["vertical_speed"]))

    def apply_new_command(self):
        """
        Lit les valeurs des champs de texte de la colonne de droite,
        met à jour les données de l'avion sélectionné et met à jour l'affichage de l'avion.
        """
        # 1. Vérifier si un avion est sélectionné
        callsign = self.selected_callsign
        if not callsign or callsign not in self.aircraft_details:
            # Vous pouvez ajouter un message d'erreur/alerte ici pour l'utilisateur
            print("Erreur: Aucun avion sélectionné ou callsign inconnu.")
            return

        try:
            # 2. Lire les nouvelles valeurs des champs QTextEdit
            # .toPlainText() est nécessaire pour lire le contenu d'un QTextEdit
            new_heading = int(self.txt_heading_valeur.toPlainText())
            new_altitude = int(self.txt_altitude_valeur.toPlainText())
            new_speed = int(self.txt_vitesse_valeur.toPlainText())
            new_vertical_speed = int(self.txt_vitesse_verticale_valeur.toPlainText())

            # 3. Mettre à jour les données de l'avion dans le dictionnaire
            aircraft_data = self.aircraft_details[callsign]
            aircraft_data["heading"] = new_heading
            aircraft_data["altitude"] = new_altitude
            aircraft_data["speed"] = new_speed
            aircraft_data["vertical_speed"] = new_vertical_speed

            # 4. Demander au widget de carte de mettre à jour l'affichage de l'avion
            # 💡 NOTE : Cette ligne suppose que votre AircraftMapWidget (label_5)
            # a une méthode 'update_aircraft' qui prend un callsign et un cap.
            self.label_5.update_aircraft(callsign, new_heading)

            # Message de confirmation (optionnel)
            self.statusBar().showMessage(f"Commande appliquée à {callsign}: Cap {new_heading}°")

        except ValueError:
            # Gérer le cas où l'utilisateur entre du texte non numérique
            print("Erreur de saisie: Veuillez entrer des nombres entiers valides dans tous les champs.")

    def retour_accueil(self):  #fonction btn_accueil
        from app import ATC_accueil
        self.accueil = ATC_accueil()
        self.accueil.showMaximized()      #permet douvrir la fenetre en pleine ecran
        self.close()       # permet de refermer la fenetre

    def _load_airports_on_map(self):
        CODES_AUTORISES = ["CDG", "ORY", "LIL"]

        font = QFont("Arial", 13)
        text_color = QColor(255, 255, 0)
        # 2. Boucle : Charger uniquement les AÉROPORTS
        for airport in AIRPORTS_DATA:

            # cORRECTION LOGIQUE : Filtrer uniquement les aéroports pertinents
            if airport.iata in CODES_AUTORISES:
                # --- Dessin de l'Aéroport (Point Jaune Interactif) ---
                airport_dot_item = AirportDot(airport)
                self.label_5.scene.addItem(airport_dot_item)

                # --- Dessin de l'Étiquette IATA ---
                label = QGraphicsTextItem(airport.iata)
                label.setFont(font)
                label.setDefaultTextColor(text_color)

                # Positionnement (en supposant dot_size=10 pour AirportDot)
                label.setPos(airport.x + 10 / 2 + 2, airport.y - 10)
                self.label_5.scene.addItem(label)
        for airport in AIRPORTS_DATA:
            if airport.iata in CODES_AUTORISES:
                # --- 1. Dessin de l'Aéroport et de l'Étiquette (Votre code existant) ---
                airport_dot_item = AirportDot(airport)
                self.label_5.scene.addItem(airport_dot_item)

                # ... (code de positionnement et d'ajout du label) ...

                # --- 2. NOUVEAU : AFFICHAGE PERMANENT DU CERCLE ---
                target_pos = QPointF(airport.x, airport.y)

                # Nous appelons une nouvelle méthode sur le widget carte pour dessiner le cercle
                self.label_5.display_airport_geofence(airport.iata, target_pos, LANDING_THRESHOLD_PIXELS)

    def _create_initial_aircrafts(self):

        #Crée un ensemble d'avions initiaux en utilisant les points de spawn.

        initial_aircrafts = {}
        callsign_counter = 100

        for sp in SPAWN_POINTS:
            callsign = f"AFR{callsign_counter}"

            # 💡 On assigne les caractéristiques du SpawnPoint
            initial_aircrafts[callsign] = {
                "heading": sp.heading,
                "altitude": 30000,  # Altitude de croisière par défaut
                "speed": 60,  # Vitesse de croisière
                "vertical_speed": 0,
                "pos": sp.pos  # Position QPointF du SpawnPoint
            }
            callsign_counter += 1

        return initial_aircrafts



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

    def retour_accueil(self):        #fonction btn_accueil
        from app import ATC_accueil
        self.accueil = ATC_accueil()
        self.accueil.showMaximized()      #permet douvrir la fenetre en pleine ecran
        self.close()       # permet de refermer la fenetre

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
