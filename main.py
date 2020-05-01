from pprint import pprint

from PyQt5.QtGui import *
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

        self.desactiver_bouton()

        # Nouvelles parties
        self.action2_joueurs.triggered.connect(lambda: self.nouvelle_partie(2))
        self.action3_joueurs.triggered.connect(lambda: self.nouvelle_partie(3))
        self.action4_joueurs.triggered.connect(lambda: self.nouvelle_partie(4))

        # necessaire pour manager le plateau
        self.choix = {}  # cle = numero de choix tuples possible , cle 0 = choix definitif

        # les objets hors interface
        self.partie = None

    def desactiver_bouton(self):
        # desactiver bouton
        self.Continue.setEnabled(False)
        self.Stop.setEnabled(False)
        self.Choix_1_0.setVisible(False)
        self.Choix_2_0.setVisible(False)
        self.Choix_3_0.setVisible(False)

    def initier_boutons(self):
        # Les actions des boutons du jeu
        self.Continue.clicked.connect(self.continuer)
        self.Stop.clicked.connect(self.stopper)
        self.Choix_1_0.clicked.connect(lambda: self.activer_choix(1))
        self.Choix_2_0.clicked.connect(lambda: self.activer_choix(2))
        self.Choix_3_0.clicked.connect(lambda: self.activer_choix(3))

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

    def nouvelle_partie(self, nb_joueurs):
        # repositionner les pions
        pions.nouvelle_partie()
        # On lance un nouveau jeu
        self.partie = Partie(nb_joueurs)
        self.Choix_1_0.setVisible(True)
        self.Choix_2_0.setVisible(True)
        self.Choix_3_0.setVisible(True)
        self.nouveau_tour()
        self.initier_boutons()

    def continuer(self):
        print("continuer")
        valeur1, valeur2 = self.choix[0]
        # todo verifier qu'on peut mettre les pions
        self.partie.bouger_n(valeur1, valeur2)
        self.nouveau_lance()

    def stopper(self):
        print("stopper")
        valeur1, valeur2 = self.choix[0]
        # todo fix : trouver la position des pions
        position = 1
        # todo verifier qu'on peut mettre les pions
        self.partie.ajouter_pion_c(valeur1, position)
        self.partie.ajouter_pion_c(valeur2, position)
        self.nouveau_tour()

    def nouveau_tour(self):
        # Afficher la couleur du joueur
        self.partie.tour_suivant()
        self.JoueurCourant.setPixmap(u.image_pion(self.partie.joueurs[self.partie.j_actuel]))
        self.nouveau_lance()

    def nouveau_lance(self):
        # On desactive les boutons
        self.desactiver_choix()
        # On lance les dés
        des, possibilite = u.lancer_de()
        # Afficher les possibilites
        self.Choix_1_0.setText(str(possibilite[1]))
        self.Choix_2_0.setText(str(possibilite[2]))
        self.Choix_3_0.setText(str(possibilite[3]))
        # Lister les possibilités
        self.choix = possibilite

    def desactiver_choix(self):
        self.Continue.setEnabled(False)
        self.Stop.setEnabled(False)
        self.Choix_1_0.setChecked(False)
        self.Choix_2_0.setChecked(False)
        self.Choix_3_0.setChecked(False)

    def activer_choix(self, choix):
        self.Continue.setEnabled(True)
        self.Stop.setEnabled(True)
        # le choix actuel
        self.choix[0] = self.choix[choix]

    # def ajouter_pion(self, joueur, couleur, colonne):
    #
    #     self.listePions[joueur] = Pion(joueur, couleur, colonne)
    def init_application(self):
        # remettre les boutons a 0
        self.desactiver_bouton()


class Partie:
    def __init__(self, nombre_joueurs):
        print(f"==> Nouvelle partie de {nombre_joueurs} joueurs")
        self._nombre_joueurs = nombre_joueurs
        self.joueurs = u.creer_joueurs(nombre_joueurs)
        self.j_actuel = 0
        self.liste_pions = {}  # key : (joueur, colonne), valeur : Pion instance
        self.dic_neutre = {1: (0, 0), 2: (0, 0), 3: (0, 0)}

    def tour_suivant(self):
        if self.j_actuel == self._nombre_joueurs:
            self.j_actuel = 1
        else:
            self.j_actuel += 1
        print(f"==> Tour du joueur {self.j_actuel}")
        return self.j_actuel

    def couleur_actuelle(self):
        couleur = self.joueurs[self.j_actuel]
        return couleur

    def bouger_n(self, *colonnes):
        for colonne in colonnes:
            numero, emplacement = u.pion_neutre_present(self.dic_neutre, colonne)
            emplacement += 1
            if numero is None:
                numero = u.pion_neutre_dispo(self.dic_neutre)
                if numero is None:
                    print("Il n'y a plus de point noir dispo")
                else:
                    u.pion_bouger(pions.liste_pions_neutres[numero], 0, colonne, emplacement)
            else:
                u.pion_bouger(pions.liste_pions_neutres[numero], 0, colonne, emplacement)

    def ajouter_pion_c(self, colonne, position):
        u.pion_ajouter(pions.liste_pions[self.j_actuel, colonne], self.j_actuel, colonne, position,
                       self.couleur_actuelle())


class Joueur:
    def __init__(self, numero, couleur):
        self.couleur = couleur
        self.numero = numero
        self.termine = 0
        self.position = {x: 0 for x in range(2, 13)}


class Pions:

    def __init__(self):
        # creer les pions noirs
        self.liste_pions_neutres = [u.pion_neutre_initier(jeu.centralwidget, _) for _ in range(1, 4)]

        # creer un pion par joueur et par colonne
        self.liste_pions = {(joueur, colonne): u.pion_initier(jeu.centralwidget, joueur, colonne)
                            for joueur in range(1, 4)
                            for colonne in range(2, 13)}

    def nouvelle_partie(self):
        # cacher les pions
        u.raz(self.liste_pions, self.liste_pions_neutres)
        # mettre les scores a 0


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        jeu = Jeu()
        pions = Pions()

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

    except ValueError as e:
        str(e)
