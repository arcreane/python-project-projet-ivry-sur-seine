

#___________________________________les_imports________________________________________
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsTextItem # Mis à jour
from PySide6.QtGui import QColor, QFont # Mis à jour
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer, QPointF

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
from utilities import json_data, json_avion #import des fonctions du fichier utilities
from gestion_avion import init_avion
from avion import Avion
#___________________________________________________________________________



#__________________________class_accueil________________________________

class ATC_accueil(QMainWindow, Ui_ATC_accueil):          #def de la page accueil
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATC Simulator - Accueil") #titre de la page
        #_____________________________paris
        self.ATC_parislfff.clicked.connect(self.ouvrir_paris) #déclenchement du bouton et ouvre paris
        json_data('paris')
        json_avion('paris')
        self.fenetre_paris = None
        #_____________________________reims

        self.ATC_reimslfee.clicked.connect(self.ouvrir_reims)  # déclenchement du bouton et ouvre reims
        json_data('reims')
        json_avion('reims')
        self.fenetre_reims = None
        #_____________________________marseille
        self.ATC_marseillelfmm.clicked.connect(self.ouvrir_marseille)  # déclenchement du bouton et ouvre marseille
        json_data('marseille')
        json_avion('marseille')
        self.fenetre_marseille = None
        #_____________________________bordeaux
        self.ATC_bordeauxlfbb.clicked.connect(self.ouvrir_bordeaux)  # déclenchement du bouton et ouvre bordeaux
        json_data('bordeaux')
        json_avion('bordeaux')
        self.fenetre_bordeaux = None
        #_____________________________brest
        self.ATC_brestlfrr.clicked.connect(self.ouvrir_brest)  # déclenchement du bouton et ouvre brest
        json_data('brest')
        json_avion('brest')
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
        self.aircraft_details = init_avion({})
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
        if self.selected_callsign:
            self.display_aircraft_stats(self.selected_callsign)

    def _load_aircraft_on_map(self):
        """Charge les avions sur le widget carte."""
        for data in self.aircraft_details.values():
            print(data.callsign)
            self.label_5.add_aircraft(data.callsign, data)

    def _connect_signals(self):
        """Connecte le signal de clic de la carte à la méthode d'affichage des stats."""
        # 🟢 CONNEXION SIGNAL -> SLOT
        # self.label_5 est l'AircraftMapWidget
        self.label_5.aircraft_clicked.connect(self.display_aircraft_stats)
        self.btn_apply.clicked.connect(self.apply_new_command)

        # Connectez vos autres boutons ici (Apply, Land, etc.)
        # self.btn_apply.clicked.connect(self.apply_new_command)

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
