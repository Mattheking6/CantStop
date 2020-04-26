from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time

import css_ui as ui
import util as u


class Jeu(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Afficher le menu contextuel windows
        self.icone_windows()

        self.actionQuitter.triggered.connect(self.close)

        # desactiver bouton
        self.Continue.setEnabled(False)
        self.Stop.setEnabled(False)
        self.Choix_1.setVisible(False)
        self.Choix_2.setVisible(False)
        self.Choix_3.setVisible(False)

        self.action2_joueurs.triggered.connect(lambda: self.nouvelle_partie(2))
        self.action3_joueurs.triggered.connect(lambda: self.nouvelle_partie(3))
        self.action4_joueurs.triggered.connect(lambda: self.nouvelle_partie(4))

        # necessaire pour manager le plateau
        self.listePions = {}
        self.choix = {}  # cle = numero de choix 3 tuples possible , cle 0 = choix definitif

    def initier_boutons(self, partie):
        # Les actions des boutons du jeu
        self.Continue.clicked.connect(lambda: self.continuer(partie))
        self.Stop.clicked.connect(lambda: self.stopper(partie))
        self.Choix_1.clicked.connect(lambda: self.activer_choix(1))
        self.Choix_2.clicked.connect(lambda: self.activer_choix(2))
        self.Choix_3.clicked.connect(lambda: self.activer_choix(3))

    def icone_windows(self):
        systray_icon = QIcon("ressources\De5.png")
        systray = QSystemTrayIcon(systray_icon, self)
        menu = QMenu()
        restore = QAction("Restaurer", self)
        close = QAction("Fermer", self)
        menu.addActions([restore, close])
        systray.setContextMenu(menu)
        systray.show()
        close.triggered.connect(qApp.quit)

    def execution(self, partie):
        self.nouveau_tour(partie)

    def nouvelle_partie(self, nb_joueurs):
        # On lance un nouveau jeu
        partie = Partie(nb_joueurs)
        self.Choix_1.setVisible(True)
        self.Choix_2.setVisible(True)
        self.Choix_3.setVisible(True)
        self.nouveau_tour(partie)
        self.initier_boutons(partie)

    def continuer(self, partie):
        print("continuer")
        self.nouveau_lance()

    def stopper(self, partie):
        print("stopper")
        valeur1, valeur2 = self.choix[0]
        # todo verifier qu'on peut mettre les pions
        partie.ajouter_pion(valeur1)
        partie.ajouter_pion(valeur2)
        self.nouveau_tour(partie)

    def nouveau_tour(self, partie):
        # Afficher la couleur du joueur
        partie.tour_suivant()
        self.JoueurCourant.setPixmap(u.image_pion(partie._joueurs[partie.j_actuel]))
        self.nouveau_lance()

    def nouveau_lance(self):
        # On desactive les boutons
        self.desactiver_choix()
        # On lance les dés
        des, possibilite = u.lancer_de()
        # Affichier les dés
        self.DeA.setPixmap(u.image_de(des[0]))
        self.DeB.setPixmap(u.image_de(des[1]))
        self.DeC.setPixmap(u.image_de(des[2]))
        self.DeD.setPixmap(u.image_de(des[3]))
        # Afficher les possibilites
        self.Choix_1.setText(str(possibilite[1]))
        self.Choix_2.setText(str(possibilite[2]))
        self.Choix_3.setText(str(possibilite[3]))
        # Lister les possibilités
        self.choix = possibilite

    def desactiver_choix(self):
        self.Continue.setEnabled(False)
        self.Stop.setEnabled(False)
        self.Choix_1.setChecked(False)
        self.Choix_2.setChecked(False)
        self.Choix_3.setChecked(False)

    def activer_choix(self, choix):
        self.Continue.setEnabled(True)
        self.Stop.setEnabled(True)
        # le choix actuel
        self.choix[0] = self.choix[choix]

    # def ajouter_pion(self, joueur, couleur, colonne):
    #
    #     self.listePions[joueur] = Pion(joueur, couleur, colonne)


class Partie:
    def __init__(self, nombre_joueurs):
        print(f"==> Nouvelle partie de {nombre_joueurs} joueurs")
        self._nombre_joueurs = nombre_joueurs
        self._joueurs = u.creer_joueurs(nombre_joueurs)
        self.j_actuel = 0
        self.liste_pions = {}  # key : (joueur, colonne), valeur : Pion instance

    def tour_suivant(self):
        if self.j_actuel == self._nombre_joueurs:
            self.j_actuel = 1
        else:
            self.j_actuel += 1
        print(f"==> Tour du joueur {self.j_actuel}")
        return self.j_actuel

    def couleur_actuelle(self):
        couleur = self._joueurs[self.j_actuel]
        return couleur

    def ajouter_pion(self, colonne):
        self.liste_pions[(self.j_actuel, colonne)] = Pion(self.j_actuel, self.couleur_actuelle(), colonne)


class Joueur:
    def __init__(self, numero, couleur):
        self.couleur = couleur
        self.termine = 0
        self.position = {x: 0 for x in range(2, 13)}


class Pion:
    _num = 0

    @staticmethod
    def _numero_suivant():
        Pion._num += 1
        resultat = Pion._num
        return resultat

    def __init__(self, joueur, couleur, colonne):
        self._numero = Pion._numero_suivant()
        self._joueur = joueur
        self._couleur = couleur
        self._colonne = colonne
        self.position = 1

        x, y = u.positionnement(self._joueur, self._colonne, self.position)

        # partie graphique du pion
        self._pion = QLabel(jeu.centralwidget)
        self._pion.setGeometry(QRect(x, y, 41, 41))
        self._pion.setText("")
        self._pion.setPixmap(u.image_pion(self._couleur))
        self._pion.setScaledContents(True)
        self._pion.setObjectName(f"{self._numero}-{self._couleur}")
        self._pion.show()

    def bouger(self, position):
        # enlever l'affichage précédent
        # TODO
        # Mettre le nouvel affichage
        self.position = position
        self._pion.setGeometry(QRect(120, 450, 41, 41))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jeu = Jeu()

    splash_image = u.image_de("")
    splash = QSplashScreen()

    for x in range(1, 7):
        splash_image = u.image_de(x)
        splash = QSplashScreen(splash_image)
        splash.show()
        time.sleep(0.1)

    jeu.show()
    app.exec_()

    splash.finish(jeu)
