# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ATC_reims.ui'
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
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_ATC_reims(object):
    def setupUi(self, ATC_reims):
        if not ATC_reims.objectName():
            ATC_reims.setObjectName(u"ATC_reims")
        ATC_reims.resize(880, 686)
        self.centralwidget = QWidget(ATC_reims)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_carte = QFrame(self.centralwidget)
        self.frame_carte.setObjectName(u"frame_carte")
        self.frame_carte.setGeometry(QRect(0, 0, 621, 451))
        self.frame_carte.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_carte.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_carte)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setScaledContents(True)
        self.label_6.setGeometry(QRect(-250, 30, 900, 900))
        self.label_6.setPixmap(QPixmap(u"image/MAP_france_2.png"))
        self.frame_11 = QFrame(self.frame_carte)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(260, 100, 171, 261))
        self.frame_11.setStyleSheet(u"background-color: rgba(204,0,204, 10);\n"
"")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_12 = QFrame(self.centralwidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(620, 0, 261, 591))
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_titre = QFrame(self.frame_12)
        self.frame_titre.setObjectName(u"frame_titre")
        self.frame_titre.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_titre.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_titre)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txt_titre = QLabel(self.frame_titre)
        self.txt_titre.setObjectName(u"txt_titre")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.txt_titre.setFont(font)
        self.txt_titre.setStyleSheet(u"")
        self.txt_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.txt_titre)


        self.verticalLayout_11.addWidget(self.frame_titre)

        self.frame_stat = QFrame(self.frame_12)
        self.frame_stat.setObjectName(u"frame_stat")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_stat.sizePolicy().hasHeightForWidth())
        self.frame_stat.setSizePolicy(sizePolicy)
        self.frame_stat.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_stat.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_heading = QLabel(self.frame_stat)
        self.txt_heading.setObjectName(u"txt_heading")
        self.txt_heading.setGeometry(QRect(100, 10, 49, 16))
        self.txt_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.img_cercle = QLabel(self.frame_stat)
        self.img_cercle.setObjectName(u"img_cercle")
        self.img_cercle.setGeometry(QRect(80, 80, 91, 91))
        self.img_cercle.setPixmap(QPixmap(u"image/cercle.png"))
        self.img_cercle.setScaledContents(True)
        self.txt_nord = QLabel(self.frame_stat)
        self.txt_nord.setObjectName(u"txt_nord")
        self.txt_nord.setGeometry(QRect(100, 60, 49, 16))
        self.txt_nord.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_est = QLabel(self.frame_stat)
        self.txt_est.setObjectName(u"txt_est")
        self.txt_est.setGeometry(QRect(160, 120, 49, 16))
        self.txt_est.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_sud = QLabel(self.frame_stat)
        self.txt_sud.setObjectName(u"txt_sud")
        self.txt_sud.setGeometry(QRect(100, 170, 49, 16))
        self.txt_sud.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_ouest = QLabel(self.frame_stat)
        self.txt_ouest.setObjectName(u"txt_ouest")
        self.txt_ouest.setGeometry(QRect(40, 120, 49, 16))
        self.txt_ouest.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_altitude = QLabel(self.frame_stat)
        self.txt_altitude.setObjectName(u"txt_altitude")
        self.txt_altitude.setGeometry(QRect(100, 200, 49, 16))
        self.txt_altitude.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.unit_altitude = QLabel(self.frame_stat)
        self.unit_altitude.setObjectName(u"unit_altitude")
        self.unit_altitude.setGeometry(QRect(150, 230, 49, 16))
        self.unit_altitude.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_vitesse = QLabel(self.frame_stat)
        self.txt_vitesse.setObjectName(u"txt_vitesse")
        self.txt_vitesse.setGeometry(QRect(100, 260, 49, 16))
        self.txt_vitesse.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_vitesse_verticale = QLabel(self.frame_stat)
        self.txt_vitesse_verticale.setObjectName(u"txt_vitesse_verticale")
        self.txt_vitesse_verticale.setGeometry(QRect(80, 320, 101, 16))
        self.txt_vitesse_verticale.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.unit_vitesse = QLabel(self.frame_stat)
        self.unit_vitesse.setObjectName(u"unit_vitesse")
        self.unit_vitesse.setGeometry(QRect(160, 290, 49, 16))
        self.unit_vitesse.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.unit_vitesse_verticale = QLabel(self.frame_stat)
        self.unit_vitesse_verticale.setObjectName(u"unit_vitesse_verticale")
        self.unit_vitesse_verticale.setGeometry(QRect(150, 350, 81, 16))
        self.unit_vitesse_verticale.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_altitude_valeur = QTextEdit(self.frame_stat)
        self.txt_altitude_valeur.setObjectName(u"txt_altitude_valeur")
        self.txt_altitude_valeur.setGeometry(QRect(70, 220, 101, 31))
        self.txt_vitesse_valeur = QTextEdit(self.frame_stat)
        self.txt_vitesse_valeur.setObjectName(u"txt_vitesse_valeur")
        self.txt_vitesse_valeur.setGeometry(QRect(70, 280, 104, 31))
        self.txt_vitesse_verticale_valeur = QTextEdit(self.frame_stat)
        self.txt_vitesse_verticale_valeur.setObjectName(u"txt_vitesse_verticale_valeur")
        self.txt_vitesse_verticale_valeur.setGeometry(QRect(70, 340, 104, 31))
        self.txt_heading_valeur = QTextEdit(self.frame_stat)
        self.txt_heading_valeur.setObjectName(u"txt_heading_valeur")
        self.txt_heading_valeur.setGeometry(QRect(70, 30, 104, 31))
        self.img_icon_avion = QLabel(self.frame_stat)
        self.img_icon_avion.setObjectName(u"img_icon_avion")
        self.img_icon_avion.setGeometry(QRect(90, 90, 71, 61))
        self.img_icon_avion.setPixmap(QPixmap(u"image/avion_icon.png"))
        self.img_icon_avion.setScaledContents(True)
        self.unit_heading = QLabel(self.frame_stat)
        self.unit_heading.setObjectName(u"unit_heading")
        self.unit_heading.setGeometry(QRect(180, 30, 21, 16))
        self.btn_apply = QPushButton(self.frame_stat)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setGeometry(QRect(78, 393, 91, 31))

        self.verticalLayout_11.addWidget(self.frame_stat)

        self.frame_boutons = QFrame(self.frame_12)
        self.frame_boutons.setObjectName(u"frame_boutons")
        self.frame_boutons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_boutons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_boutons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_accueil = QPushButton(self.frame_boutons)
        self.btn_accueil.setObjectName(u"btn_accueil")
        icon = QIcon()
        icon.addFile(u"image/accueil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_accueil.setIcon(icon)
        self.btn_accueil.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_accueil)

        self.btn_parametres = QPushButton(self.frame_boutons)
        self.btn_parametres.setObjectName(u"btn_parametres")
        icon1 = QIcon()
        icon1.addFile(u"image/parametres.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_parametres.setIcon(icon1)
        self.btn_parametres.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_parametres)

        self.btn_sortie = QPushButton(self.frame_boutons)
        self.btn_sortie.setObjectName(u"btn_sortie")
        icon2 = QIcon()
        icon2.addFile(u"image/sortie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sortie.setIcon(icon2)
        self.btn_sortie.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_sortie)


        self.verticalLayout_11.addWidget(self.frame_boutons)

        self.frame_strip = QFrame(self.centralwidget)
        self.frame_strip.setObjectName(u"frame_strip")
        self.frame_strip.setGeometry(QRect(0, 450, 621, 141))
        self.frame_strip.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_strip.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_strip)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_strip)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_strip)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_strip)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9)

        self.line_7 = QFrame(self.frame_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_7)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_10)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_strip)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_11)

        self.line_8 = QFrame(self.frame_4)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_8)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_12)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_9 = QFrame(self.frame_strip)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)

        self.line_9 = QFrame(self.frame_9)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_9)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_14)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_strip)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_15)

        self.line_11 = QFrame(self.frame_5)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_11)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_16.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_16)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_strip)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_17)

        self.line_12 = QFrame(self.frame_6)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_12)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_18.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_18)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_strip)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_19)

        self.line_13 = QFrame(self.frame_7)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_13)

        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_20.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_20)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_strip)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_21 = QLabel(self.frame_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_21)

        self.line_14 = QFrame(self.frame_8)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_14)

        self.label_22 = QLabel(self.frame_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_22.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_22)


        self.horizontalLayout_2.addWidget(self.frame_8)

        ATC_reims.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ATC_reims)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 880, 33))
        ATC_reims.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ATC_reims)
        self.statusbar.setObjectName(u"statusbar")
        ATC_reims.setStatusBar(self.statusbar)

        self.retranslateUi(ATC_reims)

        QMetaObject.connectSlotsByName(ATC_reims)
    # setupUi

    def retranslateUi(self, ATC_reims):
        ATC_reims.setWindowTitle(QCoreApplication.translate("ATC_reims", u"ATC_reims", None))
        self.label_6.setText("")
        self.txt_titre.setText(QCoreApplication.translate("ATC_reims", u"Reims LFEE", None))
        self.txt_heading.setText(QCoreApplication.translate("ATC_reims", u"Heading :", None))
        self.img_cercle.setText("")
        self.txt_nord.setText(QCoreApplication.translate("ATC_reims", u"N", None))
        self.txt_est.setText(QCoreApplication.translate("ATC_reims", u"E", None))
        self.txt_sud.setText(QCoreApplication.translate("ATC_reims", u"S", None))
        self.txt_ouest.setText(QCoreApplication.translate("ATC_reims", u"O", None))
        self.txt_altitude.setText(QCoreApplication.translate("ATC_reims", u"Altitude :", None))
        self.unit_altitude.setText(QCoreApplication.translate("ATC_reims", u" ft", None))
        self.txt_vitesse.setText(QCoreApplication.translate("ATC_reims", u"Vitesse :", None))
        self.txt_vitesse_verticale.setText(QCoreApplication.translate("ATC_reims", u"Vitesse Verticale :", None))
        self.unit_vitesse.setText(QCoreApplication.translate("ATC_reims", u"kts", None))
        self.unit_vitesse_verticale.setText(QCoreApplication.translate("ATC_reims", u" ft/min", None))
        self.img_icon_avion.setText("")
        self.unit_heading.setText(QCoreApplication.translate("ATC_reims", u"\u00b0", None))
        self.btn_apply.setText(QCoreApplication.translate("ATC_reims", u"Apply", None))
        self.btn_accueil.setText("")
        self.btn_parametres.setText("")
        self.btn_sortie.setText("")
        self.label.setText(QCoreApplication.translate("ATC_reims", u"Callsign", None))
        self.label_2.setText(QCoreApplication.translate("ATC_reims", u"AFR 002 Heavy", None))
        self.label_3.setText(QCoreApplication.translate("ATC_reims", u"From", None))
        self.label_4.setText(QCoreApplication.translate("ATC_reims", u"D\u00e9part", None))
        self.label_9.setText(QCoreApplication.translate("ATC_reims", u"To", None))
        self.label_10.setText(QCoreApplication.translate("ATC_reims", u"Arriv\u00e9", None))
        self.label_11.setText(QCoreApplication.translate("ATC_reims", u"Type", None))
        self.label_12.setText(QCoreApplication.translate("ATC_reims", u"B777", None))
        self.label_13.setText(QCoreApplication.translate("ATC_reims", u"Immat", None))
        self.label_14.setText(QCoreApplication.translate("ATC_reims", u"F-GSPZ", None))
        self.label_15.setText(QCoreApplication.translate("ATC_reims", u"Turb", None))
        self.label_16.setText(QCoreApplication.translate("ATC_reims", u"Beaucoup", None))
        self.label_17.setText(QCoreApplication.translate("ATC_reims", u"Pax", None))
        self.label_18.setText(QCoreApplication.translate("ATC_reims", u"312", None))
        self.label_19.setText(QCoreApplication.translate("ATC_reims", u"Level", None))
        self.label_20.setText(QCoreApplication.translate("ATC_reims", u"360", None))
        self.label_21.setText(QCoreApplication.translate("ATC_reims", u"Sqwk", None))
        self.label_22.setText(QCoreApplication.translate("ATC_reims", u"1000", None))
    # retranslateUi

