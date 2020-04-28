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
POSITION_NOIR = {1: QRect(50, 190, 41, 41),
                 2: QRect(50, 240, 41, 41),
                 3: QRect(50, 290, 41, 41)}


def lancer_de():
    lancer_des = [rand.randrange(1, 7) for x in range(4)]
    possibilite = {1: (lancer_des[0] + lancer_des[1], lancer_des[2] + lancer_des[3]),
                   2: (lancer_des[0] + lancer_des[2], lancer_des[1] + lancer_des[3]),
                   3: (lancer_des[0] + lancer_des[3], lancer_des[2] + lancer_des[1])
                   }
    return lancer_des, possibilite


def image_pion(couleur):
    return QPixmap(":/interface/Pion{}.png".format(couleur))


def image_de(des):
    return QPixmap(":/interface/De{}.png".format(des))


def positionnement(joueur, colonne, position):
    x = 92 + int((colonne - 2) * 595 / 10)
    y = 582 - int((position - 1) * (535 / 12))
    # supperposition joueur
    x += joueur * 4
    y += joueur * 4
    return x, y


def creer_joueurs(nombre, couleurs=None):
    table = {}
    if couleurs is None:
        couleurs = COULEURS
    for personne in range(nombre):
        couleur = rand.choice(couleurs)
        table[personne + 1] = couleur
        couleurs.remove(couleur)
    return table


def pion_initier(central_widget, joueur, colonne):
    couleur = "Noir"
    position = 1

    pos_x, pos_y = positionnement(joueur, colonne, position)

    # partie graphique du pion
    pion = QLabel(central_widget)
    pion.setGeometry(QRect(pos_x, pos_y, 41, 41))
    pion.setText("")
    pion.setScaledContents(True)
    pion.setObjectName(f"Pion_{joueur}-{colonne}")
    return pion


def pion_noir_initier(central_widget, numero):
    pion_noir = QLabel(central_widget)
    pion_noir_repositionner(pion_noir, numero)
    pion_noir.setText("")
    pion_noir.setPixmap(QPixmap(":/interface/PionNoir.png"))
    pion_noir.setScaledContents(True)
    pion_noir.setObjectName("Pion_noir_{numero}")
    pion_noir.show()
    return pion_noir


def pion_noir_repositionner(pion_noir, numero):
    pion_noir.setGeometry(POSITION_NOIR[numero])


def pion_ajouter(pion, joueur, colonne, couleur):
    pos_x, pos_y = positionnement(joueur, colonne, 1)
    pion.setPixmap(image_pion(couleur))
    pion.setGeometry(QRect(pos_x, pos_y, 41, 41))
    pion.show()


def pion_bouger(pion, joueur, colonne, position):
    pos_x, pos_y = positionnement(joueur, colonne, position)
    pion.setGeometry(QRect(pos_x, pos_y, 41, 41))


def raz(liste_couleur, liste_noir):
    for pion_c, pion in iter(liste_couleur):
        pion_c.hide()
    numero = 0
    for pion_n in liste_noir:
        numero += 1
        pion_noir_repositionner(pion_n, numero)


def pion_noir_present(dic_noir, test):
    pprint(dic_noir)
    for numero, emplacement in dic_noir:
        echelle, position = emplacement
        if echelle == test:
            return numero, emplacement
    return None, None


def pion_noir_dispo(dic_noir):
    for numero, emplacement in dic_noir:
        if emplacement == (0, 0):
            return numero
    return None

