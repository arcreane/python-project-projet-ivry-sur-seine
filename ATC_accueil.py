# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ATC_accueil.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ATC_accueil(object):
    def setupUi(self, ATC_accueil):
        if not ATC_accueil.objectName():
            ATC_accueil.setObjectName(u"ATC_accueil")
        ATC_accueil.resize(858, 603)
        ATC_accueil.setAcceptDrops(False)
        ATC_accueil.setStyleSheet(u"")
        ATC_accueil.setIconSize(QSize(30, 24))
        ATC_accueil.setAnimated(False)
        self.centralwidget = QWidget(ATC_accueil)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_carte = QFrame(self.centralwidget)
        self.frame_carte.setObjectName(u"frame_carte")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_carte.sizePolicy().hasHeightForWidth())
        self.frame_carte.setSizePolicy(sizePolicy)
        self.frame_carte.setMinimumSize(QSize(561, 531))
        self.frame_carte.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_carte.setFrameShadow(QFrame.Shadow.Raised)
        self.carte_france = QLabel(self.frame_carte)
        self.carte_france.setObjectName(u"carte_france")
        self.carte_france.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.carte_france.setAlignment(Qt.AlignCenter)

        #self.carte_france.setGeometry(QRect(22, 20, 521, 491))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.carte_france.sizePolicy().hasHeightForWidth())
        self.carte_france.setSizePolicy(sizePolicy1)
        self.carte_france.setPixmap(QPixmap(u"image/MAP_france.png"))
        self.carte_france.setScaledContents(True)
        self.carte_france.setWordWrap(False)
        self.ATC_brestlfrr = QPushButton(self.frame_carte)
        self.ATC_brestlfrr.setObjectName(u"ATC_brestlfrr")
        self.ATC_brestlfrr.setGeometry(QRect(32, 60, 161, 171))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.ATC_brestlfrr.setFont(font)
        self.ATC_brestlfrr.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 204, 0, 0.4);  /* Normal */\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 200, 0, 40); /* Survol */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 205, 0, 180); /* Clic */\n"
"}\n"
"QPushButton{\n"
"color: black;\n"
"}")
        self.ATC_parislfff = QPushButton(self.frame_carte)
        self.ATC_parislfff.setObjectName(u"ATC_parislfff")
        self.ATC_parislfff.setGeometry(QRect(192, 20, 181, 211))
        self.ATC_parislfff.setMinimumSize(QSize(181, 211))
        self.ATC_parislfff.setFont(font)
        self.ATC_parislfff.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 225, 0.4);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 0, 200, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 200, 180); /* Clic */\n"
"}\n"
"QPushButton{\n"
"color: black;\n"
"}")
        self.ATC_reimslfee = QPushButton(self.frame_carte)
        self.ATC_reimslfee.setObjectName(u"ATC_reimslfee")
        self.ATC_reimslfee.setGeometry(QRect(372, 100, 111, 131))
        self.ATC_reimslfee.setFont(font)
        self.ATC_reimslfee.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(204, 0, 204, 0.4);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(200, 0, 200, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(200, 0, 200, 180); /* Clic */\n"
"}\n"
"QPushButton{\n"
"color: black;\n"
"}")
        self.ATC_marseillelfmm = QPushButton(self.frame_carte)
        self.ATC_marseillelfmm.setObjectName(u"ATC_marseillelfmm")
        self.ATC_marseillelfmm.setGeometry(QRect(300, 230, 171, 281))
        self.ATC_marseillelfmm.setFont(font)
        self.ATC_marseillelfmm.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 0, 0.4);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(252, 252, 0, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 252, 0, 180); /* Clic */\n"
"}\n"
"QPushButton{\n"
"color: black;\n"
"}")
        self.ATC_bordeauxlfbb = QPushButton(self.frame_carte)
        self.ATC_bordeauxlfbb.setObjectName(u"ATC_bordeauxlfbb")
        self.ATC_bordeauxlfbb.setGeometry(QRect(110, 230, 191, 231))
        self.ATC_bordeauxlfbb.setFont(font)
        self.ATC_bordeauxlfbb.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 128, 0, 0.4);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(252, 125, 0, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(252, 125, 0, 180); /* Clic */\n"
"}\n"
"QPushButton{\n"
"color: black;\n"
"}")

        self.horizontalLayout_3.addWidget(self.frame_carte)

        self.frame_else = QFrame(self.centralwidget)
        self.frame_else.setObjectName(u"frame_else")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_else.sizePolicy().hasHeightForWidth())
        self.frame_else.setSizePolicy(sizePolicy2)
        self.frame_else.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_else.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_else)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame_else)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_titre = QFrame(self.frame_2)
        self.frame_titre.setObjectName(u"frame_titre")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_titre.sizePolicy().hasHeightForWidth())
        self.frame_titre.setSizePolicy(sizePolicy3)
        self.frame_titre.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_titre.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_titre)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_titre = QLabel(self.frame_titre)
        self.txt_titre.setObjectName(u"txt_titre")
        sizePolicy3.setHeightForWidth(self.txt_titre.sizePolicy().hasHeightForWidth())
        self.txt_titre.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setUnderline(False)
        self.txt_titre.setFont(font1)
        self.txt_titre.setStyleSheet(u"")
        self.txt_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.txt_titre)


        self.verticalLayout_2.addWidget(self.frame_titre)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_intro = QLabel(self.frame)
        self.txt_intro.setObjectName(u"txt_intro")
        font2 = QFont()
        font2.setPointSize(11)
        self.txt_intro.setFont(font2)
        self.txt_intro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_intro.setWordWrap(True)
        self.txt_intro.setOpenExternalLinks(False)

        self.horizontalLayout_2.addWidget(self.txt_intro)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.btn_aide = QPushButton(self.frame_else)
        self.btn_aide.setObjectName(u"btn_aide")
        icon = QIcon()
        icon.addFile(u"image/livre-ouvert.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_aide.setIcon(icon)
        self.btn_aide.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.btn_aide)

        self.btn_parametre = QPushButton(self.frame_else)
        self.btn_parametre.setObjectName(u"btn_parametre")
        icon1 = QIcon()
        icon1.addFile(u"image/parametres.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_parametre.setIcon(icon1)
        self.btn_parametre.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.btn_parametre)

        self.btn_sortie = QPushButton(self.frame_else)
        self.btn_sortie.setObjectName(u"btn_sortie")
        icon2 = QIcon()
        icon2.addFile(u"image/sortie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sortie.setIcon(icon2)
        self.btn_sortie.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.btn_sortie)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addWidget(self.frame_else)

        ATC_accueil.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ATC_accueil)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 858, 33))
        ATC_accueil.setMenuBar(self.menubar)

        self.retranslateUi(ATC_accueil)

        QMetaObject.connectSlotsByName(ATC_accueil)
    # setupUi

    def retranslateUi(self, ATC_accueil):
        ATC_accueil.setWindowTitle(QCoreApplication.translate("ATC_accueil", u"MainWindow", None))
        self.carte_france.setText("")
        self.ATC_brestlfrr.setText(QCoreApplication.translate("ATC_accueil", u"Brest LFRR", None))
        self.ATC_parislfff.setText(QCoreApplication.translate("ATC_accueil", u"Paris LFFF", None))
        self.ATC_reimslfee.setText(QCoreApplication.translate("ATC_accueil", u"Reims LFEE", None))
        self.ATC_marseillelfmm.setText(QCoreApplication.translate("ATC_accueil", u"Marseille LFMM", None))
        self.ATC_bordeauxlfbb.setText(QCoreApplication.translate("ATC_accueil", u"Bordeaux LFBB", None))
        self.txt_titre.setText(QCoreApplication.translate("ATC_accueil", u"ATC SIMULATOR", None))
        self.txt_intro.setText(QCoreApplication.translate("ATC_accueil", u"Bienvenue dans ATC Simulator. Ce logiciel imite un software typique de la DGAC (Dir\u00e9ction G\u00e9n\u00e9ral de l'Aviation Civile) ou bien des tours de contr\u00f4les d'a\u00e9roports. Pour commencer, s\u00e9lectionnez une zone de la France.", None))
        self.btn_aide.setText("")
        self.btn_parametre.setText("")
        self.btn_sortie.setText("")
    # retranslateUi

if __name__ == "__main__":   # test pour ouvrir la fenetre
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_ATC_accueil()  # instancie ton interface
    ui.setupUi(MainWindow)  # applique-la à ta QMainWindow
    MainWindow.show()  # affiche la fenêtre
    sys.exit(app.exec_())
