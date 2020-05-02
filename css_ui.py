# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppliCantStop.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(817, 706)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(817, 706))
        MainWindow.setMaximumSize(QtCore.QSize(817, 706))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/interface/De5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Plateau = QtWidgets.QLabel(self.centralwidget)
        self.Plateau.setEnabled(True)
        self.Plateau.setGeometry(QtCore.QRect(0, 0, 821, 661))
        self.Plateau.setText("")
        self.Plateau.setPixmap(QtGui.QPixmap(":/interface/montagne-matt.jpg"))
        self.Plateau.setObjectName("Plateau")
        self.DeA = QtWidgets.QLabel(self.centralwidget)
        self.DeA.setGeometry(QtCore.QRect(50, 50, 40, 40))
        self.DeA.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DeA.setText("")
        self.DeA.setPixmap(QtGui.QPixmap(":/interface/De.png"))
        self.DeA.setScaledContents(True)
        self.DeA.setObjectName("DeA")
        self.DeB = QtWidgets.QLabel(self.centralwidget)
        self.DeB.setGeometry(QtCore.QRect(50, 110, 40, 40))
        self.DeB.setText("")
        self.DeB.setPixmap(QtGui.QPixmap(":/interface/De.png"))
        self.DeB.setScaledContents(True)
        self.DeB.setObjectName("DeB")
        self.DeC = QtWidgets.QLabel(self.centralwidget)
        self.DeC.setGeometry(QtCore.QRect(110, 50, 40, 40))
        self.DeC.setText("")
        self.DeC.setPixmap(QtGui.QPixmap(":/interface/De.png"))
        self.DeC.setScaledContents(True)
        self.DeC.setObjectName("DeC")
        self.DeD = QtWidgets.QLabel(self.centralwidget)
        self.DeD.setGeometry(QtCore.QRect(110, 110, 40, 40))
        self.DeD.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DeD.setText("")
        self.DeD.setPixmap(QtGui.QPixmap(":/interface/De.png"))
        self.DeD.setScaledContents(True)
        self.DeD.setObjectName("DeD")
        self.Continue = QtWidgets.QPushButton(self.centralwidget)
        self.Continue.setGeometry(QtCore.QRect(640, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Continue.setFont(font)
        self.Continue.setObjectName("Continue")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(640, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Stop.setFont(font)
        self.Stop.setObjectName("Stop")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(190, 50, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.JoueurCourant = QtWidgets.QLabel(self.groupBox)
        self.JoueurCourant.setGeometry(QtCore.QRect(40, 30, 41, 41))
        self.JoueurCourant.setText("")
        self.JoueurCourant.setPixmap(QtGui.QPixmap(":/interface/PionBlanc.png"))
        self.JoueurCourant.setScaledContents(True)
        self.JoueurCourant.setObjectName("JoueurCourant")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(600, 110, 191, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.Choix_1_0 = QtWidgets.QPushButton(self.frame)
        self.Choix_1_0.setGeometry(QtCore.QRect(70, 10, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Choix_1_0.setFont(font)
        self.Choix_1_0.setText("")
        self.Choix_1_0.setCheckable(False)
        self.Choix_1_0.setChecked(False)
        self.Choix_1_0.setObjectName("Choix_1_0")
        self.Choix_2_0 = QtWidgets.QPushButton(self.frame)
        self.Choix_2_0.setGeometry(QtCore.QRect(70, 45, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Choix_2_0.setFont(font)
        self.Choix_2_0.setText("")
        self.Choix_2_0.setCheckable(False)
        self.Choix_2_0.setChecked(False)
        self.Choix_2_0.setObjectName("Choix_2_0")
        self.Choix_3_0 = QtWidgets.QPushButton(self.frame)
        self.Choix_3_0.setGeometry(QtCore.QRect(70, 80, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Choix_3_0.setFont(font)
        self.Choix_3_0.setText("")
        self.Choix_3_0.setCheckable(False)
        self.Choix_3_0.setChecked(False)
        self.Choix_3_0.setObjectName("Choix_3_0")
        self.Choix_2_1 = QtWidgets.QPushButton(self.frame)
        self.Choix_2_1.setGeometry(QtCore.QRect(10, 45, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Choix_2_1.setFont(font)
        self.Choix_2_1.setText("")
        self.Choix_2_1.setCheckable(False)
        self.Choix_2_1.setChecked(False)
        self.Choix_2_1.setObjectName("Choix_2_1")
        self.Choix_3_1 = QtWidgets.QPushButton(self.frame)
        self.Choix_3_1.setGeometry(QtCore.QRect(10, 80, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Choix_3_1.setFont(font)
        self.Choix_3_1.setText("")
        self.Choix_3_1.setCheckable(False)
        self.Choix_3_1.setChecked(False)
        self.Choix_3_1.setObjectName("Choix_3_1")
        self.Choix_1_1 = QtWidgets.QPushButton(self.frame)
        self.Choix_1_1.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Choix_1_1.setFont(font)
        self.Choix_1_1.setText("")
        self.Choix_1_1.setCheckable(False)
        self.Choix_1_1.setChecked(False)
        self.Choix_1_1.setObjectName("Choix_1_1")
        self.Choix_2_2 = QtWidgets.QPushButton(self.frame)
        self.Choix_2_2.setGeometry(QtCore.QRect(130, 45, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Choix_2_2.setFont(font)
        self.Choix_2_2.setText("")
        self.Choix_2_2.setCheckable(False)
        self.Choix_2_2.setChecked(False)
        self.Choix_2_2.setObjectName("Choix_2_2")
        self.Choix_1_2 = QtWidgets.QPushButton(self.frame)
        self.Choix_1_2.setGeometry(QtCore.QRect(130, 10, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Choix_1_2.setFont(font)
        self.Choix_1_2.setText("")
        self.Choix_1_2.setCheckable(False)
        self.Choix_1_2.setChecked(False)
        self.Choix_1_2.setObjectName("Choix_1_2")
        self.Choix_3_2 = QtWidgets.QPushButton(self.frame)
        self.Choix_3_2.setGeometry(QtCore.QRect(130, 80, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Choix_3_2.setFont(font)
        self.Choix_3_2.setText("")
        self.Choix_3_2.setCheckable(False)
        self.Choix_3_2.setChecked(False)
        self.Choix_3_2.setObjectName("Choix_3_2")
        self.Echec = QtWidgets.QPushButton(self.frame)
        self.Echec.setGeometry(QtCore.QRect(20, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Echec.setFont(font)
        self.Echec.setObjectName("Echec")
        self.Gagne = QtWidgets.QLabel(self.centralwidget)
        self.Gagne.setEnabled(True)
        self.Gagne.setGeometry(QtCore.QRect(130, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Gagne.setFont(font)
        self.Gagne.setTextFormat(QtCore.Qt.RichText)
        self.Gagne.setObjectName("Gagne")
        self.Echelle_2 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_2.setGeometry(QtCore.QRect(100, 540, 41, 91))
        self.Echelle_2.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_2.setLineWidth(18)
        self.Echelle_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_2.setObjectName("Echelle_2")
        self.Echelle_3 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_3.setGeometry(QtCore.QRect(160, 460, 41, 171))
        self.Echelle_3.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_3.setLineWidth(18)
        self.Echelle_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_3.setObjectName("Echelle_3")
        self.Echelle_4 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_4.setGeometry(QtCore.QRect(220, 370, 41, 261))
        self.Echelle_4.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_4.setLineWidth(18)
        self.Echelle_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_4.setObjectName("Echelle_4")
        self.Echelle_5 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_5.setGeometry(QtCore.QRect(280, 280, 41, 351))
        self.Echelle_5.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_5.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_5.setLineWidth(18)
        self.Echelle_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_5.setObjectName("Echelle_5")
        self.Echelle_6 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_6.setGeometry(QtCore.QRect(339, 190, 41, 441))
        self.Echelle_6.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_6.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_6.setLineWidth(18)
        self.Echelle_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_6.setObjectName("Echelle_6")
        self.Echelle_7 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_7.setGeometry(QtCore.QRect(398, 100, 41, 531))
        self.Echelle_7.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_7.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_7.setLineWidth(18)
        self.Echelle_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_7.setObjectName("Echelle_7")
        self.Echelle_8 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_8.setGeometry(QtCore.QRect(458, 190, 41, 441))
        self.Echelle_8.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_8.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_8.setLineWidth(18)
        self.Echelle_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_8.setObjectName("Echelle_8")
        self.Echelle_9 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_9.setGeometry(QtCore.QRect(517, 280, 41, 351))
        self.Echelle_9.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_9.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_9.setLineWidth(18)
        self.Echelle_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_9.setObjectName("Echelle_9")
        self.Echelle_10 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_10.setGeometry(QtCore.QRect(577, 370, 41, 261))
        self.Echelle_10.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_10.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_10.setLineWidth(18)
        self.Echelle_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_10.setObjectName("Echelle_10")
        self.Echelle_11 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_11.setGeometry(QtCore.QRect(635, 460, 41, 171))
        self.Echelle_11.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_11.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_11.setLineWidth(18)
        self.Echelle_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_11.setObjectName("Echelle_11")
        self.Echelle_12 = QtWidgets.QFrame(self.centralwidget)
        self.Echelle_12.setGeometry(QtCore.QRect(695, 540, 41, 91))
        self.Echelle_12.setMinimumSize(QtCore.QSize(0, 0))
        self.Echelle_12.setSizeIncrement(QtCore.QSize(0, 0))
        self.Echelle_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Echelle_12.setLineWidth(18)
        self.Echelle_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.Echelle_12.setObjectName("Echelle_12")
        self.Plateau.raise_()
        self.DeA.raise_()
        self.DeB.raise_()
        self.DeC.raise_()
        self.DeD.raise_()
        self.Continue.raise_()
        self.Stop.raise_()
        self.groupBox.raise_()
        self.frame.raise_()
        self.Gagne.raise_()
        self.Echelle_2.raise_()
        self.Echelle_3.raise_()
        self.Echelle_4.raise_()
        self.Echelle_5.raise_()
        self.Echelle_6.raise_()
        self.Echelle_8.raise_()
        self.Echelle_9.raise_()
        self.Echelle_10.raise_()
        self.Echelle_11.raise_()
        self.Echelle_12.raise_()
        self.Echelle_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 21))
        self.menubar.setObjectName("menubar")
        self.menuPartie = QtWidgets.QMenu(self.menubar)
        self.menuPartie.setObjectName("menuPartie")
        self.menuNouvelle_partie = QtWidgets.QMenu(self.menuPartie)
        self.menuNouvelle_partie.setObjectName("menuNouvelle_partie")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setSizeIncrement(QtCore.QSize(0, 0))
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionSauvegarder = QtWidgets.QAction(MainWindow)
        self.actionSauvegarder.setEnabled(False)
        self.actionSauvegarder.setObjectName("actionSauvegarder")
        self.actionCharger = QtWidgets.QAction(MainWindow)
        self.actionCharger.setEnabled(False)
        self.actionCharger.setObjectName("actionCharger")
        self.actionRegles = QtWidgets.QAction(MainWindow)
        self.actionRegles.setEnabled(False)
        self.actionRegles.setObjectName("actionRegles")
        self.actionA_propos = QtWidgets.QAction(MainWindow)
        self.actionA_propos.setEnabled(False)
        self.actionA_propos.setObjectName("actionA_propos")
        self.action2_joueurs = QtWidgets.QAction(MainWindow)
        self.action2_joueurs.setObjectName("action2_joueurs")
        self.action3_joueurs = QtWidgets.QAction(MainWindow)
        self.action3_joueurs.setObjectName("action3_joueurs")
        self.action4_joueurs = QtWidgets.QAction(MainWindow)
        self.action4_joueurs.setObjectName("action4_joueurs")
        self.menuNouvelle_partie.addSeparator()
        self.menuNouvelle_partie.addAction(self.action2_joueurs)
        self.menuNouvelle_partie.addAction(self.action3_joueurs)
        self.menuNouvelle_partie.addAction(self.action4_joueurs)
        self.menuPartie.addAction(self.menuNouvelle_partie.menuAction())
        self.menuPartie.addAction(self.actionSauvegarder)
        self.menuPartie.addAction(self.actionCharger)
        self.menuPartie.addSeparator()
        self.menuPartie.addAction(self.actionQuitter)
        self.menuAide.addAction(self.actionRegles)
        self.menuAide.addAction(self.actionA_propos)
        self.menubar.addAction(self.menuPartie.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Can\'t Stop"))
        self.Continue.setText(_translate("MainWindow", "Continue ..."))
        self.Stop.setText(_translate("MainWindow", "STOP !!!"))
        self.groupBox.setTitle(_translate("MainWindow", "Tour du joueur"))
        self.Echec.setText(_translate("MainWindow", "Choix impossible"))
        self.Gagne.setText(_translate("MainWindow", "C\'est gagné !"))
        self.menuPartie.setTitle(_translate("MainWindow", "Partie"))
        self.menuNouvelle_partie.setTitle(_translate("MainWindow", "Nouvelle partie"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionSauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.actionSauvegarder.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCharger.setText(_translate("MainWindow", "Charger"))
        self.actionCharger.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionRegles.setText(_translate("MainWindow", "Règles"))
        self.actionA_propos.setText(_translate("MainWindow", "A propos..."))
        self.action2_joueurs.setText(_translate("MainWindow", "2 joueurs"))
        self.action2_joueurs.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.action3_joueurs.setText(_translate("MainWindow", "3 joueurs"))
        self.action3_joueurs.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.action4_joueurs.setText(_translate("MainWindow", "4 joueurs"))
        self.action4_joueurs.setShortcut(_translate("MainWindow", "Ctrl+4"))
import images_rc
