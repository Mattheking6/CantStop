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


        # Nouvelles parties
        self.action2_joueurs.triggered.connect(lambda: self.nouvelle_partie(2))
        self.action3_joueurs.triggered.connect(lambda: self.nouvelle_partie(3))
        self.action4_joueurs.triggered.connect(lambda: self.nouvelle_partie(4))

        # necessaire pour manager le plateau
        self.choix = []  # cle = numero de choix tuples possible , cle 0 = choix definitif


        # Tableau des boutons
        self.tableau_boutons = [[self.Choix_1_0, self.Choix_1_1, self.Choix_1_2],
                               [self.Choix_2_0, self.Choix_2_1, self.Choix_2_2],
                               [self.Choix_3_0, self.Choix_3_1, self.Choix_3_2]]

        # action sur les boutons
        self.initier_boutons()

        # En atttente de commencer une partie
        self.desactiver_bouton()

        # les objets hors interface
        self.partie = None


    def initier_boutons(self):
        # Les actions des boutons stop et continuer
        self.Continue.clicked.connect(self.continuer)
        self.Stop.clicked.connect(self.stopper)
        # Les actions des boutons de choix
        for choix in range(3):
            for option in range(3):
                self.tableau_boutons[choix][option].clicked.connect(self.test(choix, option))
        # self.tableau_boutons[0][0].clicked.connect(lambda: self.activer_choix(0, 0))
        # self.tableau_boutons[0][1].clicked.connect(lambda: self.activer_choix(0, 1))
        # self.tableau_boutons[0][2].clicked.connect(lambda: self.activer_choix(0, 2))
        # self.tableau_boutons[1][0].clicked.connect(lambda: self.activer_choix(1, 0))
        # self.tableau_boutons[1][1].clicked.connect(lambda: self.activer_choix(1, 1))
        # self.tableau_boutons[1][2].clicked.connect(lambda: self.activer_choix(1, 2))
        # self.tableau_boutons[2][0].clicked.connect(lambda: self.activer_choix(2, 0))
        # self.tableau_boutons[2][1].clicked.connect(lambda: self.activer_choix(2, 1))
        # self.tableau_boutons[2][2].clicked.connect(lambda: self.activer_choix(2, 2))

    def test(self, val1, val2):
        return lambda: self.activer_choix(val1, val2)

    def desactiver_bouton(self):
        # desactiver bouton
        self.Continue.setEnabled(False)
        self.Stop.setEnabled(False)
        for choix in range(3):
            for option in range(3):
                self.tableau_boutons[choix][option].setDisabled(True)

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

    def continuer(self):
        print("continuer")
        print(self.choix)
        # Rendre effectif le choix
        self.partie.bouger_n(self.choix)
        self.nouveau_lance()

    def stopper(self):
        print("stopper")
        print(self.choix)
        # todo fix : trouver la position des pions
        position = 1
        # todo verifier qu'on peut mettre les pions
        self.partie.ajouter_pion_c(self.choix[0], position)
        self.nouveau_tour()

    def nouveau_tour(self):
        # Afficher la couleur du joueur
        self.partie.tour_suivant()
        self.JoueurCourant.setPixmap(u.image_pion(self.partie.couleurs_joueurs[self.partie.j_actuel]))
        self.nouveau_lance()

    def nouveau_lance(self):
        # On desactive les boutons
        self.desactiver_choix()
        # On lance les dés
        des, possibilite = u.lancer_de()
        # retrouver les infos du plateau
        neutres_restants, possible_neutres, possible_autres = self.partie.trouver_position_jouable()

        zip_boutons = zip(possibilite, self.tableau_boutons)
        # Afficher les possibilites
        for choix, bouton in zip_boutons:
            # Afficher les possibilités
            bouton[0].setText("{} et {}".format(*choix))
            bouton[1].setText("{}".format(choix[0]))
            bouton[2].setText("{}".format(choix[1]))

            # Activer uniquement ce qui est possible
            cout = 0
            pos = 2 * [False]
            if choix[0] in possible_neutres:
                pos[0] = True
            elif choix[0] in possible_autres:
                pos[0] = True
                cout += 1
            if choix[1] in possible_neutres:
                pos[1] = True
            elif choix[1] in possible_autres:
                pos[1] = True
                cout += 1

            if pos[0] and pos[1] and cout <= neutres_restants:
                # On peut bouger les 2 pions
                bouton[0].setEnabled(True)
            elif pos[0] or pos[1]:
                # On ne peut rien faire
                print("Aucun choix possible")
            else:
                # On ne peut choisir qu'une possibilité
                if pos[0]:
                    bouton[1].setEnabled(True)
                if pos[1]:
                    bouton[2].setEnabled()

    def desactiver_choix(self):
        self.Continue.setEnabled(False)
        self.Stop.setEnabled(False)
        self.Choix_1_0.setChecked(False)
        self.Choix_2_0.setChecked(False)
        self.Choix_3_0.setChecked(False)

    def activer_choix(self, choix, option):
        self.Continue.setEnabled(True)
        self.Stop.setEnabled(True)
        print(f"Bouton de choix: {choix}, option: {option}")
        # le choix actuel
        if option == 0:
            texte1, texte2 = str(self.tableau_boutons[choix][option].text()).split(" et ")
            self.choix = [int(texte1), int(texte2)]
        else:
            self.choix = [int(self.tableau_boutons[choix][option].text())]
        # Afficher les noirs
        # Todo modifier l'affichage
        print(f"Nouveau choix: {self.choix}")


    def init_application(self):
        # remettre les boutons a 0
        self.desactiver_bouton()


class Partie:
    def __init__(self, nombre_joueurs):
        print(f"==> Nouvelle partie de {nombre_joueurs} joueurs")
        self._nombre_joueurs = nombre_joueurs
        self.couleurs_joueurs = u.creer_joueurs(nombre_joueurs)
        self.j_actuel = 0
        self.liste_pions = {}  # key : (joueur, colonne), valeur : Pion instance
        self.liste_neutre = [(0, 0), (0, 0), (0, 0)]
        self.echelle_clos = []
        # Creer les joueurs
        self.joueur = {numero: Joueur(numero, self.couleurs_joueurs[numero]) for numero in range(1, nombre_joueurs + 1)}
        self.position_joueur = {}

    def tour_suivant(self):
        # increment boucle
        if self.j_actuel == self._nombre_joueurs:
            self.j_actuel = 1
        else:
            self.j_actuel += 1

        # Affecter la position du joueur
        self.position_joueur = self.joueur[self.j_actuel].position.copy()
        pprint(self.position_joueur)

        return self.j_actuel

    @property
    def couleur_actuelle(self):
        couleur = self.couleurs_joueurs[self.j_actuel]
        return couleur

    def trouver_position_jouable(self) -> (int, list, list):
        # Les pions neutres poses
        neutres = list(filter(lambda x: x[0] != 0, self.liste_neutre))
        neutres_restants = 3 - len(neutres)
        if len(neutres):
            # verifier qu'on n'est pas déjà en haut
            for test in neutres:
                if test[1] == u.ECHELLE[test[0]]:
                    # si c'est le cas on ne garde pas la colonne
                    neutres.remove(test)
        possible_neutres = [x[0] for x in neutres]
        if neutres_restants == 0:
            possible_autres = []  # pas d'autres possibilité
        else:
            # trouver les échellons encore jouables
            possible_autres = [numero for numero in range(2, 13)
                               if numero not in self.echelle_clos]

        return neutres_restants, possible_neutres, possible_autres

    def bouger_n(self, colonnes):
        for colonne in colonnes:
            print(f"colonne {colonne}")
            numero, emplacement = u.pion_neutre_present(self.liste_neutre, colonne)
            emplacement += 1
            if numero is None:
                numero = u.pion_neutre_dispo(self.liste_neutre)
                if numero is None:
                    raise ValueError("Il n'y a plus de point noir dispo")
                else:
                    u.pion_bouger(pions.liste_pions_neutres[numero], 0, colonne, emplacement)
            else:
                u.pion_bouger(pions.liste_pions_neutres[numero], 0, colonne, emplacement)
            # bouger le pion aussi dans la liste
            self.liste_neutre[numero] = (colonne, emplacement)


    def ajouter_pion_c(self, colonne, position):
        u.pion_ajouter(pions.liste_pions[self.j_actuel, colonne], self.j_actuel, colonne, position,
                       self.couleur_actuelle)


class Joueur:
    position: dict

    def __init__(self, numero: int, couleur: str):
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
