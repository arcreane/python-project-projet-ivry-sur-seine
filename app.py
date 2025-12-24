#___________________________________les_imports________________________________________
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsTextItem # Mis à jour
from PySide6.QtGui import QColor, QFont # Mis à jour
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer, QPointF
import math
#__________________________________les_imports_de_fichiers_________________________________________
from ATC import Ui_ATC

from ATC_accueil import Ui_ATC_accueil  #import de la main window
from airport_dots import AirportDot  #on importe ce qui permet de dessiner les aeroports
from utilities import json_data, json_avion, import_json_data, change_FIR, get_FIR
from gestion_avion import init_avion, clear_dict_avion


#___________________________________________________________________________

LANDING_DISTANCE_THRESHOLD = 80
LANDING_THRESHOLD_PIXELS = 80
REMOVAL_THRESHOLD_PIXELS = 10 # Seuil de retrait (doit être atteint)
zone = ''

def get_zone():
    global zone
    return zone

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

    def ouvrir_paris(self): #fonction qui ouvre paris
        clear_dict_avion()
        json_data('paris')
        json_avion('paris')
        change_FIR('paris')
        self.fenetre_paris = ATC()
        self.fenetre_paris.showMaximized() #permet douvrir la fenetre en pleine ecran
        self.close()

    def ouvrir_reims(self):           #fonction qui ouvre reims
        clear_dict_avion()
        json_data('reims')
        json_avion('reims')
        change_FIR('reims')
        self.fenetre_reims = ATC()
        self.fenetre_reims.showMaximized() #permet douvrir la fenetre en pleine ecran
        self.close()

    def ouvrir_marseille(self):           #fonction qui ouvre marseille
        clear_dict_avion()
        json_data('marseille')
        json_avion('marseille')
        change_FIR('marseille')
        self.fenetre_marseille = ATC()
        self.fenetre_marseille.showMaximized() #permet douvrir la fenetre en pleine ecran
        self.close()

    def ouvrir_bordeaux(self):           #fonction qui ouvre bordeaux
        clear_dict_avion()
        json_data('bordeaux')
        json_avion('bordeaux')
        change_FIR('bordeaux')
        self.fenetre_bordeaux = ATC()
        self.fenetre_bordeaux.showMaximized() #permet douvrir la fenetre en pleine ecran
        self.close()

    def ouvrir_brest(self):           #fonction qui ouvre brest
        clear_dict_avion()
        json_data('brest')
        json_avion('brest')
        change_FIR('brest')
        self.fenetre_brest = ATC()
        self.fenetre_brest.showMaximized() #permet douvrir la fenetre en pleine ecran
        self.close()

class ATC(QMainWindow, Ui_ATC):       #def de la page paris
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.FIR = get_FIR()

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
        self.label_2.setText(f'{callsign}\n{avion.phonetic}')
        self.label_4.setText(f'{avion.from_}')
        self.label_10.setText(f'{avion.aprt_code}')
        self.label_12.setText(f'{avion.type_}')
        self.label_14.setText(f'{avion.immat}')
        self.label_16.setText(f'{avion.turb}')
        self.label_18.setText(f'{avion.pax}')
        self.label_20.setText(f'{avion.final_level}')
        self.label_22.setText(f'{avion.sqwk}\n{avion.emergency}')

        if not refresh_only:
            self.txt_heading_valeur.setText(str(int(avion.consigne['heading'])))
            self.txt_altitude_valeur.setText(str(int(avion.consigne['alt'])))
            self.txt_vitesse_valeur.setText(str(int(avion.consigne['speed'])))
            self.txt_vitesse_verticale_valeur.setText(str(int(avion.consigne['vs'])))

    def apply_command(self):
        if not self.selected_callsign:
            return

        avion = self.aircrafts[self.selected_callsign]
        hdg = int(self.txt_heading_valeur.toPlainText())
        alt = int(self.txt_altitude_valeur.toPlainText())
        speed = int(self.txt_vitesse_valeur.toPlainText())
        vs = int(self.txt_vitesse_verticale_valeur.toPlainText())

        if alt > 42000:
            alt = 42000
        if alt < 3500:
            alt = 3500
        if abs(vs) > 6000:
            vs = 6000
        if speed < avion.landing_speed:
            speed = avion.landing_speed
        if speed > 400:
            speed = 400

        try:
            if avion.sqwk != 7600:
                avion.consigne_change({
                    'heading': hdg,
                    'alt': alt,
                    'speed': speed,
                    'vs': vs
                })
                self.statusBar().showMessage(
                    f"Commande appliquée à {avion.callsign}", 3000
                )
            else:
                self.statusBar().showMessage(
                    f"{avion.callsign} => radio failure", 3000
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
        if self.FIR == 'paris':
            CODES = ['LFPG', 'LFPO', 'LFQQ']
        elif self.FIR == 'reims':
            CODES = ['LFST', 'LFSB', 'LFGJ']
        elif self.FIR == 'marseille':
            CODES = ['LFMN', 'LFML', 'LFLL']
        elif self.FIR == 'bordeaux':
            CODES = ['LFBD', 'LFBO', 'LFBZ']
        elif self.FIR == 'brest':
            CODES = ['LFRB', 'LFRN', 'LFRS']

        font = QFont("Arial", 13)
        text_color = QColor(0, 128, 255)

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
        clear_dict_avion()
        self.aircrafts = {}
        self.label_5.all_aircraft_details = self.aircrafts
        self.home = ATC_accueil()
        self.home.showMaximized()
        self.close()


if __name__ == "__main__":   # lance par defaut la fenetre accueil
    app = QApplication(sys.argv)
    window = ATC_accueil()
    window.showMaximized()
    sys.exit(app.exec())
