

#___________________________________________________________________________
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


#_________________________________________________________

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
        self.fenetre_paris.show()
        self.close()

    def ouvrir_reims(self):           #fonction qui ouvre reims
        self.fenetre_reims = ATC_reimslfee()
        self.fenetre_reims.show()
        self.close()

    def ouvrir_marseille(self):           #fonction qui ouvre marseille
        self.fenetre_marseille = ATC_marseillelfmm()
        self.fenetre_marseille.show()
        self.close()

    def ouvrir_bordeaux(self):           #fonction qui ouvre bordeaux
        self.fenetre_bordeaux = ATC_bordeauxlfbb()
        self.fenetre_bordeaux.show()
        self.close()

    def ouvrir_brest(self):           #fonction qui ouvre brest
        self.fenetre_brest = ATC_brestlfrr()
        self.fenetre_brest.show()
        self.close()

#_________________________________________________________

class ATC_parislfff(QMainWindow, Ui_ATC_paris):       #def de la page paris
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATC_parisfLFFF") #titre de la page
        self.btn_accueil.clicked.connect(self.retour_accueil)   #declenchement du bouton et ouvre la page daccueil
        self.btn_sortie.clicked.connect(QApplication.quit)

    def retour_accueil(self):        #fonction btn_accueil
        from app import ATC_accueil
        self.accueil = ATC_accueil()
        self.accueil.show()     #ouvre la fenetre
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
        self.accueil.show()     #ouvre la fenetre
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
        self.accueil.show()     #ouvre la fenetre
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
        self.accueil.show()     #ouvre la fenetre
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
        self.accueil.show()     #ouvre la fenetre
        self.close()       # permet de refermer la fenetre

#__________________________________________________________

if __name__ == "__main__":   # lance par defaut la fenetre accueil
    app = QApplication(sys.argv)
    window = ATC_accueil()
    window.show()
    sys.exit(app.exec())
