

#___________________________________les_imports________________________________________
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ATC_accueil import Ui_ATC_accueil  #import de la main window
#___________________________________________________________________________
from ATC_paris import Ui_ATC_paris  # import de la window paris
from ATC_reims import Ui_ATC_reims# import de la window reims
from ATC_brest import Ui_ATC_brest# import de la window brest
from ATC_bordeaux import Ui_ATC_bordeaux# import de la window bordeaux
from ATC_marseille import Ui_ATC_marseille# import de la window marseille
#___________________________________________________________________________
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import (QPointF)


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
        self.aircraft_details = {
            "AFR123": {"heading": 45, "altitude": 32000, "speed": 450, "vertical_speed": 0, "pos": QPointF(250, 200)},
            "BAW456": {"heading": 180, "altitude": 28000, "speed": 480, "vertical_speed": 1000,
                       "pos": QPointF(500, 400)},
        }
        self.selected_callsign = None

        self._load_aircraft_on_map()
        self._connect_signals()

    def _load_aircraft_on_map(self):
        """Charge les avions sur le widget carte."""
        for callsign, data in self.aircraft_details.items():
            # Utilise l'objet label_5 (qui est maintenant AircraftMapWidget)
            self.label_5.add_aircraft(callsign, data['pos'], data['heading'])

    def _connect_signals(self):
        """Connecte le signal de clic de la carte à la méthode d'affichage des stats."""
        # 🟢 CONNEXION SIGNAL -> SLOT
        # self.label_5 est l'AircraftMapWidget
        self.label_5.aircraft_clicked.connect(self.display_aircraft_stats)

        # Connectez vos autres boutons ici (Apply, Land, etc.)
        # self.btn_apply.clicked.connect(self.apply_new_command)

    # 2. 🟢 MÉTHODE (SLOT) POUR METTRE À JOUR LE PANNEAU
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

    def retour_accueil(self):  #fonction btn_accueil
        from app import ATC_accueil
        self.accueil = ATC_accueil()
        self.accueil.showMaximized()      #permet douvrir la fenetre en pleine ecran
        self.close()       # permet de refermer la fenetre

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
