import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ATC_accueil import Ui_ATC_accueil  #import de la main window
from ATC_paris import Ui_ATC_paris  # import de la window paris




class ATC_parislfff(QMainWindow, Ui_ATC_paris):       #def de la page paris
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Nouvelle Fenêtre")

        self.btn_accueil.clicked.connect(self.retour_accueil)

    def retour_accueil(self):
        from app import ATC_accueil
        self.accueil = ATC_accueil()
        self.accueil.show()
        self.close()




class ATC_accueil(QMainWindow, Ui_ATC_accueil):          #def de la page accueil
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATC Simulator - Accueil")


        self.ATC_parislfff.clicked.connect(self.ouvrir_autre_fenetre) #déclenchement du bouton et de la nouvelle page

        # on garde une référence pour éviter que la fenêtre se ferme aussitôt
        self.fenetre_paris = None

    def ouvrir_autre_fenetre(self):           #fonction qui ouvre paris
        self.fenetre_paris = ATC_parislfff()
        self.fenetre_paris.show()
        self.close()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ATC_accueil()
    window.show()
    sys.exit(app.exec())