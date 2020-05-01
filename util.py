import random as rand
from pprint import pprint

from PyQt5.QtCore import QRect
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# constantes
COULEURS = ["Bleu", "Blanc", "Gris", "Jaune", "Orange", "Rouge", "Vert", "Violet"]
COULEUR_NEUTRE = "Noir"
ECHELLE = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13,
           12: 3, 11: 5, 10: 7, 9: 9, 8: 11}
POSITION_neutre = {1: QRect(50, 190, 41, 41),
                 2: QRect(50, 240, 41, 41),
                 3: QRect(50, 290, 41, 41)}


def lancer_de():
    """
    Effectue un lance de dés et expose le résultat
    :return: lancer_des : liste des 4 dés
             possibilite : liste des 3 possibilités
    """
    lancer_des = [rand.randrange(1, 7) for _ in range(4)]
    possibilite = [(lancer_des[0] + lancer_des[1], lancer_des[2] + lancer_des[3]),
                   (lancer_des[0] + lancer_des[2], lancer_des[1] + lancer_des[3]),
                   (lancer_des[0] + lancer_des[3], lancer_des[2] + lancer_des[1])
                   ]
    return lancer_des, possibilite


def image_pion(couleur: str):
    """
    Trouver l'image du pion
    :param couleur: valeur parmis COULEURS
    :return: image du pion
    """
    return QPixmap(":/interface/Pion{}.png".format(couleur))


def image_de(des: int):
    """
    Trouver l'image d'un dé, le dé 0 existe
    :param des: valeur du dé
    :return: image du dé
    """
    return QPixmap(":/interface/De{}.png".format(des))


def positionnement(joueur: int, colonne: int, position: int) -> tuple:
    """
    Positionne sur l'image pixelle le pion
    :param joueur: entier joueur , 0 correspond aux pions noirs
    :param colonne: entier colonne
    :param position: entier position sur l'échelle
    :return: position x, y de l'image
    """
    try:
        x = 92 + int((colonne - 2) * 595 / 10)
        y = 582 - int((position - 1) * (535 / 12))
        # supperposition joueur
        x += joueur * 4
        y += joueur * 4
        return x, y
    except Exception as e:
        print(f"Problème dans le passe des paramètres :"
              f"joueur = {joueur}"
              f"colonne = {colonne}"
              f"position = {position}"
              f"{str(e)}")
        return 1, 1


def creer_joueurs(nombre: int, couleurs: list = None) -> dict:
    """
    En début de partie créer les joueurs avec des couleurs aléatoires
    :param nombre: int nombre de joueurs
    :param couleurs: valeur des couleurs possibles par défaut COULEURS
    :return: {numéro du joueur : couleur}
    """
    table = {}
    if couleurs is None:
        couleurs = COULEURS.copy()
    for personne in range(nombre):
        couleur = rand.choice(couleurs)
        table[personne + 1] = couleur
        couleurs.remove(couleur)
    return table


def pion_initier(central_widget: QWidget, joueur: int, colonne: int) -> QLabel:
    """
    Initie une fois pour toutes tous les labels des pions pour les 4 joueurs
    :param central_widget: fenêtre principale
    :param joueur: numéro du joueur
    :param colonne: echelle
    :return:
    """
    position = 1

    pos_x, pos_y = positionnement(joueur, colonne, position)

    # partie graphique du pion
    pion = QLabel(central_widget)
    pion.setGeometry(QRect(pos_x, pos_y, 41, 41))
    pion.setText("")
    pion.setScaledContents(True)
    pion.setObjectName(f"Pion_{joueur}-{colonne}")
    return pion


def pion_neutre_initier(central_widget: QWidget, numero: int) -> QLabel:
    """
    Initie une fois pour toutes tous les labels des pions noirs
    :param central_widget: 
    :param numero: 
    :return: 
    """
    pion_neutre = QLabel(central_widget)
    pion_neutre_repositionner(pion_neutre, numero)
    pion_neutre.setText("")
    pion_neutre.setPixmap(QPixmap(f":/interface/Pion{COULEUR_NEUTRE}.png"))
    pion_neutre.setScaledContents(True)
    pion_neutre.setObjectName(f"Pion_neutre_{numero}")
    pion_neutre.show()
    return pion_neutre


def pion_neutre_repositionner(pion_neutre: QLabel, numero: int):
    """
    Déplacer un pion neutre
    :param pion_neutre: le label du pion
    :param numero: le numéro du pion
    """
    pion_neutre.setGeometry(POSITION_neutre[numero])


def pion_ajouter(pion: QLabel, joueur: int, colonne: int, position: int, couleur: str):
    """
    Mettre un 1er pion sur l'échelle
    :param pion: label du pion
    :param joueur: numéro du joueur
    :param colonne: échelle
    :param position: position sur l'échelle
    :param couleur: couleur du pion
    """
    pos_x, pos_y = positionnement(joueur, colonne, position)
    pion.setPixmap(image_pion(couleur))
    pion.setGeometry(QRect(pos_x, pos_y, 41, 41))
    pion.show()


def pion_bouger(pion: QLabel, joueur: int, colonne: int, position: int):
    pos_x, pos_y = positionnement(joueur, colonne, position)
    pion.setGeometry(QRect(pos_x, pos_y, 41, 41))


def raz(liste_couleur: dict, liste_neutre: list):
    for pion, pion_c in liste_couleur.items():
        pion_c.hide()
    numero = 0
    for pion_n in liste_neutre:
        numero += 1
        pion_neutre_repositionner(pion_n, numero)


def pion_neutre_present(list_neutre: list, test: int):
    count = 0
    pprint(list_neutre)
    for echelle, position in list_neutre:
        if echelle == test:
            print(count, position)
            return count, position
        count += 1
    return None, 0


def pion_neutre_dispo(list_neutre: list) -> int:
    numero = 0
    for emplacement in list_neutre:
        if emplacement == (0, 0):
            return numero
        else:
            numero += 1

