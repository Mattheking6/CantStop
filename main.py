from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import time

import css_ui as ui
from util import *


class Jeu(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Afficher le menu contextuel windows
        self.icone_windows()

        # desactiver bouton
        self.Continue.setEnabled(False)
        self.Stop.setEnabled(False)

        # On lance un nouveau jeu
        partie = Partie()

        # Les actions des boutons du jeu
        self.Continue.clicked.connect(self.nouveau_lance)
        self.Stop.clicked.connect(lambda: self.nouveau_tour(partie))
        self.Choix_1.clicked.connect(self.activer_choix)
        self.Choix_2.clicked.connect(self.activer_choix)
        self.Choix_3.clicked.connect(self.activer_choix)
        # self.actionQuitter.triggered(self.close)

        self.execution(partie)

    def icone_windows(self):
        systray_icon = QIcon("ressources\De5.png")
        systray = QSystemTrayIcon(systray_icon, self)
        menu = QMenu()
        restore = QAction("Restaurer", self)
        close = QAction("Fermer", self)
        menu.addActions([restore, close])
        systray.setContextMenu(menu)
        systray.show()
        close.triggered.connect(self.close)

    def execution(self, partie):
        self.nouveau_tour(partie)

    def nouveau_tour(self, partie):
        # Afficher la couleur du joueur
        partie.tourSuivant()
        self.JoueurCourant.setPixmap(QPixmap(":/interface/Pion{}.png".format(
            partie.joueurs[partie.j_actuel])))
        self.nouveau_lance()

    def nouveau_lance(self):
        # On desactive les boutons
        self.desactiver_choix()
        # On lance les dés
        des, possibilite = lancer_de()
        # Affichier les dés
        self.DeA.setPixmap(QPixmap(":/interface/De{}.png".format(des[0])))
        self.DeB.setPixmap(QPixmap(":/interface/De{}.png".format(des[1])))
        self.DeC.setPixmap(QPixmap(":/interface/De{}.png".format(des[2])))
        self.DeD.setPixmap(QPixmap(":/interface/De{}.png".format(des[3])))
        # Afficher les possibilites
        self.Choix_1.setText(str(possibilite[1]))
        self.Choix_2.setText(str(possibilite[2]))
        self.Choix_3.setText(str(possibilite[3]))

    def desactiver_choix(self):
        self.Continue.setEnabled(False)
        self.Stop.setEnabled(False)
        self.Choix_1.setChecked(False)
        self.Choix_2.setChecked(False)
        self.Choix_3.setChecked(False)

    def activer_choix(self):
        self.Continue.setEnabled(True)
        self.Stop.setEnabled(True)

class Partie:
    def __init__(self):
        self.nombre_joueurs = 2
        self.joueurs = {1: "Bleu", 2: "Jaune"}
        self.infojoueur = {}
        for index, couleur in self.joueurs.items():
            self.infojoueur[index] = Joueur(index, couleur)
        self.j_actuel = 0

    def tourSuivant(self):
        self.j_actuel = 1 if self.j_actuel == self.nombre_joueurs else self.j_actuel + 1


class Joueur:
    def __init__(self, numero, couleur):
        self.couleur = couleur
        self.termine = 0
        self.position = {x: 0 for x in range(2, 13)}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jeu = Jeu()

    splash_image = QPixmap(r"ressources\De.png")
    splash = QSplashScreen()

    for x in range(1, 7):
        splash_image = QPixmap(r"ressources\De{}.png".format(x))
        splash = QSplashScreen(splash_image)
        splash.show()
        time.sleep(0.1)

    jeu.show()
    app.exec_()

    splash.finish(jeu)
