# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ATC_marseille.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QPointF, QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout,
                               QLabel, QMainWindow, QMenuBar, QPushButton,
                               QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
                               QWidget, QGridLayout)

from spawn_plane import AircraftMapWidget


# ___________________________________________________________________________________________________________


class Ui_ATC_marseille(object):
    def setupUi(self, ATC_marseille):
        if not ATC_marseille.objectName():
            ATC_marseille.setObjectName(u"ATC_marseille")

        ATC_marseille.resize(900, 648)
        ATC_marseille.setMinimumSize(QSize(900, 620))

        self.centralwidget = QWidget(ATC_marseille)  # ligne de création
        self.centralwidget.setObjectName(u"centralwidget")

        self.main_grid_layout = QGridLayout(self.centralwidget)
        self.main_grid_layout.setObjectName(u"main_grid_layout")
        self.main_grid_layout.setContentsMargins(5, 5, 5, 5)
        self.main_grid_layout.setColumnStretch(0, 8)

        sizePolicy_expanding = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy_strip = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.frame_carte = QFrame(self.centralwidget)
        self.frame_carte.setObjectName(u"frame_carte")

        self.frame_carte.setSizePolicy(sizePolicy_expanding)
        self.carte_inner_layout = QVBoxLayout(self.frame_carte)
        self.carte_inner_layout.setContentsMargins(0, 0, 0, 0)

        self.frame_carte.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_carte.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = AircraftMapWidget(self.frame_carte)
        self.label_5.setObjectName(u"label_5")

        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setSizePolicy(sizePolicy_expanding)
        self.carte_inner_layout.addWidget(self.label_5)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setContentsMargins(0, 0, 0, 0)
        self.main_grid_layout.addWidget(self.frame_carte, 0, 0, 1, 1)

        self.label_5.set_map_image(u"image/MAP_marseille.png")
        """ 
        self.frame_strip = QFrame(self.centralwidget)
        self.frame_strip.setObjectName(u"frame_strip")

        self.frame_strip.setSizePolicy(sizePolicy_strip)

        self.frame_strip.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_strip.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_strip.setStyleSheet(u"font-size: 11pt;")
        self.frame_strip.setMinimumHeight(180)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_strip)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_strip)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.frame)
        '''self.main_grid_layout.addWidget(self.frame_strip, 1, 0, 1, 1)'''
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
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
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
        self.label_4.setFont(font)
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
        self.label_10.setFont(font)
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
        self.label_12.setFont(font)
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
        self.label_14.setFont(font)
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
        self.label_16.setFont(font)
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
        self.label_18.setFont(font)
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
        self.label_20.setFont(font)
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
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_22.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_22)

        self.horizontalLayout_2.addWidget(self.frame_8)
        """
        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy_panel = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.frame_11.setSizePolicy(sizePolicy_panel)
        self.main_grid_layout.setColumnStretch(1, 2)
        self.frame_11.setMinimumWidth(300)
        self.main_grid_layout.addWidget(self.frame_11, 0, 1, 2, 1)

        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_titre = QFrame(self.frame_11)
        self.frame_titre.setObjectName(u"frame_titre")
        self.frame_titre.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_titre.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_titre)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txt_titre = QLabel(self.frame_titre)
        self.txt_titre.setObjectName(u"txt_titre")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setUnderline(False)
        self.txt_titre.setFont(font1)
        self.txt_titre.setStyleSheet(u"")
        self.txt_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.txt_titre)

        self.verticalLayout_11.addWidget(self.frame_titre)

        # 🟢 DÉBUT DU BLOC DE REMPLACEMENT (Commence à self.frame_stat)

        self.frame_stat = QFrame(self.frame_11)  # Le parent est frame_11
        self.frame_stat.setObjectName(u"frame_stat")

        # Policy Verticale Expand pour que ce bloc remplisse la majorité de frame_11
        sizePolicy_stat = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.frame_stat.setSizePolicy(sizePolicy_stat)
        self.frame_stat.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_stat.setFrameShadow(QFrame.Shadow.Raised)

        # 🟢 LAYOUT PRINCIPAL DE LA SECTION STATS (Empilement vertical)
        self.stat_main_layout = QVBoxLayout(self.frame_stat)
        self.stat_main_layout.setObjectName(u"stat_main_layout")
        self.stat_main_layout.setContentsMargins(10, 10, 10, 10)
        self.stat_main_layout.setSpacing(15)  # Espacement entre les blocs

        # ----------------------------------------------------
        # BLOC 1 : HEADING ET INPUT
        # ----------------------------------------------------
        self.txt_heading = QLabel(self.frame_stat)
        self.txt_heading.setObjectName(u"txt_heading")
        self.txt_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stat_main_layout.addWidget(self.txt_heading)

        self.heading_input_layout = QHBoxLayout()  # Layout Horizontal pour le champ + unité
        self.heading_input_layout.setObjectName(u"heading_input_layout")

        self.txt_heading_valeur = QTextEdit(self.frame_stat)
        self.txt_heading_valeur.setObjectName(u"txt_heading_valeur")
        self.txt_heading_valeur.setMinimumHeight(31)
        self.txt_heading_valeur.setMaximumHeight(31)

        self.unit_heading = QLabel(self.frame_stat)
        self.unit_heading.setObjectName(u"unit_heading")
        self.unit_heading.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.unit_heading.setMaximumWidth(25)  # Largeur fixe pour l'unité

        # Ajout au layout horizontal, centré horizontalement
        self.heading_input_layout.addStretch(1)  # Pousse à droite
        self.heading_input_layout.addWidget(self.txt_heading_valeur, alignment=Qt.AlignmentFlag.AlignCenter)
        self.heading_input_layout.addWidget(self.unit_heading)
        self.heading_input_layout.addStretch(1)  # Pousse à gauche

        self.stat_main_layout.addLayout(self.heading_input_layout)

        # ----------------------------------------------------
        # BLOC 2 : ROSE DES VENTS / COMPAS
        # ----------------------------------------------------
        self.frame_compas = QFrame(self.frame_stat)
        self.frame_compas.setObjectName(u"frame_compas")
        self.frame_compas.setMinimumSize(QSize(100, 100))  # Taille minimale pour le compas

        # 🟢 LAYOUT EN GRILLE POUR LE COMPAS (N, S, E, O, Avion)
        self.compas_grid = QGridLayout(self.frame_compas)
        self.compas_grid.setContentsMargins(0, 0, 0, 0)

        # Le Cercle et l'Icône de l'avion (au centre de la grille)
        self.img_cercle = QLabel(self.frame_compas)
        self.img_cercle.setObjectName(u"img_cercle")
        self.img_cercle.setPixmap(QPixmap(u"image/cercle.png"))
        self.img_cercle.setScaledContents(True)  # Le cercle peut s'étirer

        self.img_icon_avion = QLabel(self.frame_compas)
        self.img_icon_avion.setObjectName(u"img_icon_avion")
        self.img_icon_avion.setPixmap(QPixmap(u"image/avion_icon.png"))
        self.img_icon_avion.setScaledContents(True)
        self.img_icon_avion.setFixedSize(60, 60)  # Taille fixe pour l'avion

        # Positionnement dans la grille (Ligne, Colonne, RowSpan, ColSpan)
        self.compas_grid.addWidget(self.img_cercle, 1, 1, 3, 3)  # Cercle (étend sur L1-3, C1-3)
        self.compas_grid.addWidget(self.img_icon_avion, 2, 2, 1, 1, Qt.AlignmentFlag.AlignCenter)  # Avion (au centre)

        # Les points cardinaux (labels N, S, E, O)
        # Note : Les variables txt_nord, txt_est, txt_sud, txt_ouest doivent être déclarées et configurées (objetName) avant ces lignes.
        # Nous supposons qu'elles sont créées par le reste du code généré et sont réutilisées ici.
        self.txt_nord = QLabel(self.frame_compas)
        self.txt_nord.setObjectName(u"txt_nord")
        self.compas_grid.addWidget(self.txt_nord, 0, 2, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.txt_est = QLabel(self.frame_compas)
        self.txt_est.setObjectName(u"txt_est")
        self.compas_grid.addWidget(self.txt_est, 2, 4, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.txt_sud = QLabel(self.frame_compas)
        self.txt_sud.setObjectName(u"txt_sud")
        self.compas_grid.addWidget(self.txt_sud, 4, 2, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.txt_ouest = QLabel(self.frame_compas)
        self.txt_ouest.setObjectName(u"txt_ouest")
        self.compas_grid.addWidget(self.txt_ouest, 2, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)

        self.stat_main_layout.addWidget(self.frame_compas,
                                        stretch=2)  # Ajout du bloc Compas (stretch 2 pour prendre plus de place)
        # ----------------------------------------------------
        # BLOC 3 : ALTITUDE, VITESSE, VITESSE VERTICALE
        # ----------------------------------------------------

        # ALTITUDE
        self.txt_altitude = QLabel(self.frame_stat)
        self.txt_altitude.setObjectName(u"txt_altitude")
        self.txt_altitude.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_altitude_valeur = QTextEdit(self.frame_stat)
        self.txt_altitude_valeur.setObjectName(u"txt_altitude_valeur")
        self.txt_altitude_valeur.setMaximumHeight(31)
        self.unit_altitude = QLabel(self.frame_stat)
        self.unit_altitude.setObjectName(u"unit_altitude")
        self.unit_altitude.setMaximumWidth(25)

        altitude_h_layout = QHBoxLayout()
        altitude_h_layout.addStretch(1)
        altitude_h_layout.addWidget(self.txt_altitude_valeur, alignment=Qt.AlignmentFlag.AlignCenter)
        altitude_h_layout.addWidget(self.unit_altitude)
        altitude_h_layout.addStretch(1)

        self.stat_main_layout.addWidget(self.txt_altitude)
        self.stat_main_layout.addLayout(altitude_h_layout)

        # VITESSE
        self.txt_vitesse = QLabel(self.frame_stat)
        self.txt_vitesse.setObjectName(u"txt_vitesse")
        self.txt_vitesse.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_vitesse_valeur = QTextEdit(self.frame_stat)
        self.txt_vitesse_valeur.setObjectName(u"txt_vitesse_valeur")
        self.txt_vitesse_valeur.setMaximumHeight(31)
        self.unit_vitesse = QLabel(self.frame_stat)
        self.unit_vitesse.setObjectName(u"unit_vitesse")
        self.unit_vitesse.setMaximumWidth(25)

        vitesse_h_layout = QHBoxLayout()
        vitesse_h_layout.addStretch(1)
        vitesse_h_layout.addWidget(self.txt_vitesse_valeur, alignment=Qt.AlignmentFlag.AlignCenter)
        vitesse_h_layout.addWidget(self.unit_vitesse)
        vitesse_h_layout.addStretch(1)

        self.stat_main_layout.addWidget(self.txt_vitesse)
        self.stat_main_layout.addLayout(vitesse_h_layout)

        # VITESSE VERTICALE
        self.txt_vitesse_verticale = QLabel(self.frame_stat)
        self.txt_vitesse_verticale.setObjectName(u"txt_vitesse_verticale")
        self.txt_vitesse_verticale.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_vitesse_verticale_valeur = QTextEdit(self.frame_stat)
        self.txt_vitesse_verticale_valeur.setObjectName(u"txt_vitesse_verticale_valeur")
        self.txt_vitesse_verticale_valeur.setMaximumHeight(31)
        self.unit_vitesse_verticale = QLabel(self.frame_stat)
        self.unit_vitesse_verticale.setObjectName(u"unit_vitesse_verticale")
        self.unit_vitesse_verticale.setMaximumWidth(40)

        vitesse_vert_h_layout = QHBoxLayout()
        vitesse_vert_h_layout.addStretch(1)
        vitesse_vert_h_layout.addWidget(self.txt_vitesse_verticale_valeur, alignment=Qt.AlignmentFlag.AlignCenter)
        vitesse_vert_h_layout.addWidget(self.unit_vitesse_verticale)
        vitesse_vert_h_layout.addStretch(1)

        self.stat_main_layout.addWidget(self.txt_vitesse_verticale)
        self.stat_main_layout.addLayout(vitesse_vert_h_layout)

        # ----------------------------------------------------
        # BLOC 4 : BOUTON APPLY
        # ----------------------------------------------------

        # bouton apply
        self.btn_apply = QPushButton(self.frame_stat)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setFixedSize(91, 31)  # Taille fixe pour le bouton

        apply_h_layout = QHBoxLayout()
        apply_h_layout.addStretch(1)  # Pousse le bouton au centre
        apply_h_layout.addWidget(self.btn_apply)
        apply_h_layout.addStretch(1)

        self.stat_main_layout.addLayout(apply_h_layout)

        # bouton land
        self.btn_land = QPushButton(self.frame_stat)
        self.btn_land.setObjectName(u"btn_land")
        self.btn_land.setText(u"Land")
        self.btn_land.setFixedSize(91, 31)  # Utilise la même taille que Apply

        # Layout Horizontal pour centrer le bouton Land
        land_h_layout = QHBoxLayout()
        land_h_layout.addStretch(1)  # Pousse le bouton au centre
        land_h_layout.addWidget(self.btn_land)
        land_h_layout.addStretch(1)

        self.stat_main_layout.addLayout(land_h_layout)

        self.stat_main_layout.addStretch(1)  # Pousse tous les éléments vers le haut de la frame_stat

        # 🟢 FIN DU BLOC DE REMPLACEMENT
        self.verticalLayout_11.addWidget(self.frame_stat)

        self.verticalLayout_11.addWidget(self.frame_stat)

        self.frame_boutons = QFrame(self.frame_11)
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
        """
        self.btn_parametres = QPushButton(self.frame_boutons)
        self.btn_parametres.setObjectName(u"btn_parametres")
        icon1 = QIcon()
        icon1.addFile(u"image/parametres.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_parametres.setIcon(icon1)
        self.btn_parametres.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_parametres)"""

        self.btn_sortie = QPushButton(self.frame_boutons)
        self.btn_sortie.setObjectName(u"btn_sortie")
        icon2 = QIcon()
        icon2.addFile(u"image/sortie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sortie.setIcon(icon2)
        self.btn_sortie.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_sortie)

        self.verticalLayout_11.addWidget(self.frame_boutons)

        ATC_marseille.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ATC_marseille)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 33))
        ATC_marseille.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ATC_marseille)
        self.statusbar.setObjectName(u"statusbar")
        ATC_marseille.setStatusBar(self.statusbar)

        if not self.label_5.map_pixmap.isNull():
            map_width = self.label_5.map_pixmap.width()
            map_height = self.label_5.map_pixmap.height()

            # Ajoute un deuxième avion un peu décalé avec un cap différent
            # self.label_5.add_aircraft("BAW456", QPointF(map_width / 3, map_height / 4), 180)

        self.retranslateUi(ATC_marseille)

        QMetaObject.connectSlotsByName(ATC_marseille)

    # setupUi

    def retranslateUi(self, ATC_marseille):
        ATC_marseille.setWindowTitle(QCoreApplication.translate("ATC_marseille", u"MainWindow", None))
        """self.label_5.setText("")"""
        '''
        self.label.setText(QCoreApplication.translate("ATC_marseille", u"Callsign", None))
        self.label_2.setText(QCoreApplication.translate("ATC_marseille", u"AFR 002 Heavy", None))
        self.label_3.setText(QCoreApplication.translate("ATC_marseille", u"From", None))
        self.label_4.setText(QCoreApplication.translate("ATC_marseille", u"D\u00e9part", None))
        self.label_9.setText(QCoreApplication.translate("ATC_marseille", u"To", None))
        self.label_10.setText(QCoreApplication.translate("ATC_marseille", u"Arriv\u00e9", None))
        self.label_11.setText(QCoreApplication.translate("ATC_marseille", u"Type", None))
        self.label_12.setText(QCoreApplication.translate("ATC_marseille", u"B777", None))
        self.label_13.setText(QCoreApplication.translate("ATC_marseille", u"Immat", None))
        self.label_14.setText(QCoreApplication.translate("ATC_marseille", u"F-GSPZ", None))
        self.label_15.setText(QCoreApplication.translate("ATC_marseille", u"Turb", None))
        self.label_16.setText(QCoreApplication.translate("ATC_marseille", u"Beaucoup", None))
        self.label_17.setText(QCoreApplication.translate("ATC_marseille", u"Pax", None))
        self.label_18.setText(QCoreApplication.translate("ATC_marseille", u"312", None))
        self.label_19.setText(QCoreApplication.translate("ATC_marseille", u"Level", None))
        self.label_20.setText(QCoreApplication.translate("ATC_marseille", u"360", None))
        self.label_21.setText(QCoreApplication.translate("ATC_marseille", u"Sqwk", None))
        self.label_22.setText(QCoreApplication.translate("ATC_marseille", u"1000", None))
        '''
        self.txt_titre.setText(QCoreApplication.translate("ATC_marseille", u"Marseille LFMM", None))
        self.txt_heading.setText(QCoreApplication.translate("ATC_marseille", u"Heading :", None))
        self.img_cercle.setText("")
        self.txt_nord.setText(QCoreApplication.translate("ATC_marseille", u"0", None))
        self.txt_est.setText(QCoreApplication.translate("ATC_marseille", u"90", None))
        self.txt_sud.setText(QCoreApplication.translate("ATC_marseille", u"180", None))
        self.txt_ouest.setText(QCoreApplication.translate("ATC_marseille", u"270", None))
        self.txt_altitude.setText(QCoreApplication.translate("ATC_marseille", u"Altitude :", None))
        self.unit_altitude.setText(QCoreApplication.translate("ATC_marseille", u" ft", None))
        self.txt_vitesse.setText(QCoreApplication.translate("ATC_marseille", u"Vitesse :", None))
        self.txt_vitesse_verticale.setText(QCoreApplication.translate("ATC_marseille", u"Vitesse Verticale :", None))
        self.unit_vitesse.setText(QCoreApplication.translate("ATC_marseille", u"kts", None))
        self.unit_vitesse_verticale.setText(QCoreApplication.translate("ATC_marseille", u" ft/min", None))
        self.img_icon_avion.setText("")
        self.unit_heading.setText(QCoreApplication.translate("ATC_marseille", u"\u00b0", None))
        self.btn_apply.setText(QCoreApplication.translate("ATC_marseille", u"Apply", None))
        self.btn_accueil.setText("")
        '''self.btn_parametres.setText("")'''
        self.btn_sortie.setText("")
    # retranslateUi

