import sys
import time

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import css_ui as ui
import A_Propos_ui
import Regle_ui
import joueur
import util as u


class Regle(QDialog, Regle_ui.Ui_Regles):
    def __init__(self):
        QDialog.__init__(self, flags=Qt.WindowFlags())
        self.setupUi(self)


class APropos(QDialog, A_Propos_ui.Ui_Propos):
    def __init__(self):
        QDialog.__init__(self, flags=Qt.WindowFlags())
        self.setupUi(self)


class Jeu(QMainWindow, ui.Ui_MainWindow):
    """Classe pour gérer le plateau de jeu et les actions des joueurs"""
    def __init__(self):
        QMainWindow.__init__(self, flags=Qt.WindowFlags())
        self.setupUi(self)

        # Afficher le menu contextuel windows
        self.icone_windows()

        # Action des menus
        self.actionQuitter.triggered.connect(self.close)
        self.action2_joueurs.triggered.connect(lambda: self.nouvelle_partie(2))
        self.action3_joueurs.triggered.connect(lambda: self.nouvelle_partie(3))
        self.action4_joueurs.triggered.connect(lambda: self.nouvelle_partie(4))
        self.actionRegles.triggered.connect(self.afficher_regle)
        self.actionA_propos.triggered.connect(self.afficher_propos)

        # Apparence
        self.actionAppSoft.setChecked(True)
        self.actionAppSoft.triggered.connect(lambda: self.design("soft"))
        self.actionAppBois.triggered.connect(lambda: self.design("bois"))
        self.actionAppCouleur.triggered.connect(lambda: self.design("couleur"))

        # Barre de statut
        self.statusBar().showMessage('Commencez une nouvelle partie.')

        # Tableau des boutons
        self.tableau_boutons = [[self.Choix_1_0, self.Choix_1_1, self.Choix_1_2],
                                [self.Choix_2_0, self.Choix_2_1, self.Choix_2_2],
                                [self.Choix_3_0, self.Choix_3_1, self.Choix_3_2]]
        self.tableau_echelles = {2: self.Echelle_2, 3: self.Echelle_3, 4: self.Echelle_4, 5: self.Echelle_5,
                                 6: self.Echelle_6, 7: self.Echelle_7, 8: self.Echelle_8, 9: self.Echelle_9,
                                 10: self.Echelle_10, 11: self.Echelle_11, 12: self.Echelle_12}

        # action sur les boutons
        self.initier_boutons()

        # Echelles invisibles
        self.desactiver_echelles()

        # En atttente de commencer une partie
        self.desactiver_bouton()

        # les objets hors interface
        self.partie = None

        # necessaire pour manager le jeu
        self.choix = []
        self.liste_choix = []

    def initier_boutons(self):
        """
        A faire une fois pour initialiser l'interface
        :return:
        """
        # Les actions des boutons stop et continuer
        self.Continue.clicked.connect(self.continuer)
        self.Stop.clicked.connect(self.stopper)
        self.Echec.clicked.connect(self.echec)
        # Les actions des boutons de choix
        for choix in range(3):
            for option in range(3):
                self.tableau_boutons[choix][option].clicked.connect(self.f_activer_choix(choix, option))
        # cacher gagné
        self.Gagne.setVisible(False)

    @staticmethod
    def afficher_regle():
        """
        Afficher la fenêtre des règles
        :return:
        """
        dialog_regle = Regle()
        dialog_regle.exec_()

    @staticmethod
    def afficher_propos():
        """Afficher la fenêtre de l'à propos"""
        dialog_propos = APropos()
        dialog_propos.exec_()

    def f_activer_choix(self, val1: int, val2: int):
        """
        Fonction relais pour activer les choix de dés
        :param val1: choix de la ligne (combinaison de dés)
        :param val2: choix de la colonne (combinaison 1, 2 ou les 2)
        :return: la vrai fonction
        """
        return lambda: self.decoder_choix(val1, val2)

    def desactiver_bouton(self):
        """ Désactiver tous les boutons de choix"""
        # desactiver bouton
        self.Continue.setEnabled(False)
        self.Stop.setEnabled(False)
        self.Echec.setVisible(False)
        for choix in range(3):
            for option in range(3):
                self.tableau_boutons[choix][option].setDisabled(True)

    def desactiver_echelles(self):
        """ Rendre les échelles terminées invisible """
        for index in range(2, 13):
            self.tableau_echelles[index].setVisible(False)

    def icone_windows(self):
        """Menu contextuel de windows"""
        systray_icon = QIcon(r"ressources\De5.png")
        systray = QSystemTrayIcon(systray_icon, self)
        menu = QMenu()
        close = QAction("Fermer", self)
        menu.addActions([close])
        systray.setContextMenu(menu)
        systray.show()
        close.triggered.connect(qApp.quit)

    def nouvelle_partie(self, nb_joueurs: int):
        """Remet le jeu en place pour une nouvelle partie"""
        # repositionner les pions
        pions.nouvelle_partie()
        # Effacer gagné
        self.Gagne.setVisible(False)
        self.desactiver_echelles()
        # On lance un nouveau jeu
        self.partie = Partie(nb_joueurs)
        # si on joue contre l'ordinateur
        if bot:
            ordi.append(joueur.Bot(2, aggressivite))
        self.Choix_1_0.setVisible(True)
        self.Choix_2_0.setVisible(True)
        self.Choix_3_0.setVisible(True)
        self.nouveau_tour()

    def continuer(self):
        """Le joueur choisi de continuer """
        print(f"==> Continuer avec le choix : {self.choix}")
        # Rendre effectif le choix
        self.partie.bouger_n(self.choix)
        poursuite = self.nouveau_lance()
        self.verification(poursuite)

    def stopper(self):
        """Le joueur chois de stopper"""
        print(f"==> Stopper avec le choix : {self.choix}")
        # Faire le dernier mouvement
        self.partie.bouger_n(self.choix)
        # Regarder ou en sont les noirs et les remplacer
        self.partie.ajouter_pion_c()
        # Fin de partie ?
        if self.partie.joueur[self.partie.j_actuel].termine >= 3:
            # Afficher Gagner
            self.desactiver_bouton()
            u.ranger_neutre(pions.liste_pions_neutres)
            self.Gagne.setVisible(True)
            self.statusBar().showMessage(f'Victoire du joueur {self.partie.couleur_actuelle}. Bravo !!!')
        else:
            self.nouveau_tour()

    def nouveau_tour(self):
        """Changement de joueur dans la partie """
        # Afficher la couleur du joueur
        self.partie.tour_suivant()
        self.JoueurCourant.setPixmap(u.image_pion(self.partie.couleurs_joueurs[self.partie.j_actuel]))
        poursuite = self.nouveau_lance()
        self.statusBar().showMessage(f'Tour du joueur {self.partie.couleur_actuelle}.')
        self.verification(poursuite)

    def nouveau_lance(self):
        """
        Nouveau lancé de dé
        :return: False si aucun choix n'est possible, True si on peux continuer à jouer
        """
        # On desactive les boutons
        self.desactiver_bouton()
        # On lance les dés
        possibilite = u.lancer_de(self.DeA, self.DeB, self.DeC, self.DeD)
        # retrouver les infos du plateau
        neutres_restants, possible_neutres, possible_autres = self.partie.trouver_position_jouable()

        zip_boutons = zip(possibilite, self.tableau_boutons)
        blocage = 0
        self.liste_choix.clear()

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

            if all([pos[0], pos[1], cout <= neutres_restants]):
                # On peut bouger les 2 pions
                print(f" {choix} ==> On peut bouger les 2 pions")
                bouton[0].setEnabled(True)
                self.liste_choix.append(choix)
            elif not any([pos[0], pos[1]]):
                # On ne peut rien faire
                print(f" {choix} ==> Aucun choix possible")
                blocage += 1
            else:
                # On ne peut choisir qu'une possibilité
                if pos[0]:
                    print(f" {choix} ==> Bouton 1")
                    bouton[1].setEnabled(True)
                    self.liste_choix.append(choix[0])
                if pos[1]:
                    print(f" {choix} ==> Bouton 2")
                    bouton[2].setEnabled(True)
                    self.liste_choix.append(choix[1])
        self.repaint()

        if bot and self.partie.j_actuel == 2 and blocage != 3:
            self.bot_joue()

        return False if blocage == 3 else True

    def bot_joue(self):
        """Faire jouer un bot"""
        self.desactiver_bouton()
        jeu.repaint()
        time.sleep(0.1)
        bot_choix, bot_continue = ordi[0].jouer(self.partie.joueur, self.liste_choix, self.partie.liste_neutre)
        self.activer_choix(bot_choix)
        jeu.repaint()
        time.sleep(0.5)
        if bot_continue:
            self.continuer()
        else:
            self.stopper()

    def decoder_choix(self, choix: int, option: int):
        """Décoder le choix lorsqu'il ne s'agit pas d'un bot"""
        self.Continue.setEnabled(True)
        self.Stop.setEnabled(True)
        # le choix actuel
        if option == 0:
            # noinspection PyUnresolvedReferences
            texte1, texte2 = str(self.tableau_boutons[choix][option].text()).split(" et ")
            choix_res = [int(texte1), int(texte2)]
        else:
            # noinspection PyUnresolvedReferences
            choix_res = [int(self.tableau_boutons[choix][option].text())]
        self.activer_choix(choix_res)

    def activer_choix(self, choix: list):
        """Un joueur a fait un choix de déplacement, le prendre en compte"""
        # le choix actuel
        if len(choix) == 2:
            self.choix = [choix[0], choix[1]]
        else:
            self.choix = choix
        # Afficher les noirs
        print(f"Nouveau choix: {self.choix}")
        lst_neutre = self.partie.liste_neutre.copy()
        self.replacer_neutre()
        for echelle in self.choix:
            hauteur, numero = self.partie.nouvelle_position_noir(echelle, lst_neutre)
            u.pion_bouger(pions.liste_pions_neutres[numero], 0, echelle, hauteur)
            # bouger le pion aussi dans la liste temporaire
            lst_neutre[numero] = (echelle, hauteur)

    def replacer_neutre(self):
        """Remettre les pions neutre à leur place"""
        numero = 0
        print(f"**** neutres : {self.partie.liste_neutre} ****")
        for neutre in self.partie.liste_neutre:
            # tester qu'il ne s'agit pas d'un neutre à remettre à sa place
            if neutre[0] == 0:
                u.pion_neutre_repositionner(pions.liste_pions_neutres[numero], numero)
            else:
                u.pion_bouger(pions.liste_pions_neutres[numero], 0, neutre[0], neutre[1])
            numero += 1

    def verification(self, poursuite: bool):
        """En cas d'échec faire subir la perte de progression"""
        if not poursuite:
            print("** Plus rien n'est jouable !!! **")
            self.statusBar().showMessage(f'Aucun positionnement possible.'
                                         f' Perte de la progression, tour du joueur suivant.')
            self.Echec.setVisible(True)

    def echec(self):
        """En cas d'échec d'un joueur: faire passer le tour par le bouton """
        self.nouveau_tour()

    def design(self, param: str):
        """Changer le design du plateau"""
        self.actionAppSoft.setChecked(False)
        self.actionAppCouleur.setChecked(False)
        self.actionAppBois.setChecked(False)
        design_choix = self.sender()
        design_choix.setChecked(True)
        self.Plateau.setPixmap(QPixmap(f":/interface/plateau_{param}.jpg"))


class Partie:
    """
    Classe pour gérer la partie en cours
    """
    def __init__(self, nombre_joueurs: int):
        print(f"==> Nouvelle partie de {nombre_joueurs} joueurs")
        self._nombre_joueurs = nombre_joueurs
        self.couleurs_joueurs = u.creer_joueurs(nombre_joueurs)
        self.j_actuel = 0
        self.liste_neutre = [(0, 0), (0, 0), (0, 0)]
        self.echelle_clos = []
        # Creer les joueurs
        self.joueur = {numero: Joueur(numero, self.couleurs_joueurs[numero]) for numero in range(1, nombre_joueurs + 1)}
        self.etat_joueur_actuel = {}

    def tour_suivant(self):
        """
        Faire passer le tour au prochain joueur
        :return: le numéro du joueur actuel
        """
        # increment boucle
        if self.j_actuel == self._nombre_joueurs:
            self.j_actuel = 1
        else:
            self.j_actuel += 1

        # Ranger les neutres
        self.liste_neutre = [(0, 0), (0, 0), (0, 0)]
        pions.nouveau_tour()

        # Affecter la position du joueur
        self.etat_joueur_actuel = self.joueur[self.j_actuel].position.copy()

        return self.j_actuel

    @property
    def couleur_actuelle(self):
        """
        Retrouver la couleur du joueur qui joue actuellement
        :return: str: la couleur
        """
        couleur = self.couleurs_joueurs[self.j_actuel]
        return couleur

    @property
    def neutres_poses(self) -> list:
        """
        filtre la liste des neutres (echelle, position) avec ceux sur les échelles
        :return: list : les pions neutres
        """
        neutres = list(filter(lambda l: l[0] != 0, self.liste_neutre))
        return neutres

    def trouver_position_jouable(self) -> (int, list, list):
        """
        trouver les actions possible à l'utilisateur pour son tirage de dés fonction du plateau
        :return: le nombre de neutre restant, les neutres posés, les échelles encores disponibles
        """
        # Les pions neutres poses
        neutres = self.neutres_poses
        neutres_restants = 3 - len(neutres)
        possible_neutres = [_[0] for _ in neutres]

        # traiter les echelons ou ils n'y a pas de neutres
        if neutres_restants == 0:
            possible_autres = []  # pas d'autres possibilité
        else:
            # trouver les échellons encore jouables
            possible_autres = [numero for numero in range(2, 13)
                               if numero not in self.echelle_clos
                               if numero not in possible_neutres]

        # verifier qu'on n'est pas déjà en haut
        if len(neutres):
            for test in neutres:
                if test[1] == u.ECHELLE[test[0]]:
                    # si c'est le cas on ne garde pas la colonne
                    possible_neutres.remove(test[0])
        return neutres_restants, possible_neutres, possible_autres

    def bouger_n(self, colonnes: list):
        """Faire le déplacement des pions neutres"""
        # invalider les derniers choix temporaires
        jeu.replacer_neutre()
        for colonne in colonnes:
            # Trouver le déplacement du pion noir
            emplacement, numero = self.nouvelle_position_noir(colonne, self.liste_neutre)
            # Faire le déplacement
            u.pion_bouger(pions.liste_pions_neutres[numero], 0, colonne, emplacement)
            # bouger le pion aussi dans la liste
            self.liste_neutre[numero] = (colonne, emplacement)

    def nouvelle_position_noir(self, colonne: int, lst_neutre: list):
        """
        Pour trouver la position la liste est passée en paramètre car il peut s'agir d'une liste temporaire
        :param colonne: echelle
        :param lst_neutre: formalisme de liste_neutre
        :return:
        """
        numero, emplacement = u.pion_neutre_present(lst_neutre, colonne)
        if numero is None:
            numero = u.pion_neutre_dispo(lst_neutre)
            # Trouver l'avancement du joueur
            emplacement = self.joueur[self.j_actuel].position[colonne]
            if numero is None:
                raise ValueError("Il n'y a plus de pions noir dispo")

        # Déplacement du pion noir si pas déjà arrivé
        if u.ECHELLE[colonne] != emplacement:
            emplacement += 1
        return emplacement, numero

    def ajouter_pion_c(self):
        """Ajouter les pions de couleur en remplacement des neutres"""
        for neutre in self.neutres_poses:
            echelle = neutre[0]
            niveau = neutre[1]
            # partie graphique
            u.pion_ajouter(pions.liste_pions[self.j_actuel, echelle], self.j_actuel, echelle, niveau,
                           self.couleur_actuelle)
            # partie logique
            self.joueur[self.j_actuel].position[echelle] = niveau
            # Le pion est arrivé au bout ?
            if u.ECHELLE[echelle] == niveau:
                self.echelle_clos.append(echelle)
                print(self.echelle_clos)
                self.joueur[self.j_actuel].termine += 1
                jeu.tableau_echelles[echelle].setVisible(True)
                # Supprimer les pions qui étaient dans l'échelle
                self.supprimer_perdant(echelle)

    def supprimer_perdant(self, colonne):
        """Lorsqu'une échelle est terminée, supprimer les pions des autres joueurs"""
        for j in range(1, 5):
            if j != self.j_actuel:
                pions.liste_pions[j, colonne].hide()


class Joueur:
    """Classe pour gérer l'état de chaque joueur qu'il soit humain ou bot"""
    position: dict

    def __init__(self, numero: int, couleur: str):
        self.couleur = couleur
        self.numero = numero
        self.termine = 0
        self.position = {_: 0 for _ in range(2, 13)}

    def __repr__(self):
        return f"couleur : {self.couleur}\n" \
               f"numero : {self.numero}\n" \
               f"termine : {self.termine}\n" \
               f"position : {self.position}\n"


class Pions:
    """Classe pour gérer les pions sur le plateau"""
    def __init__(self):
        # creer un pion par joueur et par colonne
        self.liste_pions = {(num_joueur, num_colonne): u.pion_initier(jeu.centralwidget, num_joueur, num_colonne)
                            for num_joueur in range(1, 5)
                            for num_colonne in range(2, 13)}
        # creer les pions noirs
        self.liste_pions_neutres = [u.pion_neutre_initier(jeu.centralwidget, _) for _ in range(3)]

    def nouvelle_partie(self):
        """Repositionnement de tous les pions"""
        # cacher les pions
        u.raz(self.liste_pions, self.liste_pions_neutres)

    def nouveau_tour(self):
        """Ranger les neutres pour les rendre disponible"""
        # ranger les neutres
        u.ranger_neutre(self.liste_pions_neutres)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        jeu = Jeu()
        pions = Pions()
        bot = True
        aggressivite = 85
        ordi = []

        splash_image = u.image_de(1)
        splash = QSplashScreen()

        for x in range(1, 7):
            splash_image = u.image_de(x)
            splash = QSplashScreen(splash_image)
            splash.show()
            # time.sleep(0.1)

        jeu.show()
        splash.finish(jeu)
        sys.exit(app.exec_())

    except ValueError as e:
        str(e)
