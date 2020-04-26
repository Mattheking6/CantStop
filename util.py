import random as rand
from PyQt5.QtGui import *

# constantes
COULEURS = ["Bleu", "Blanc", "Gris", "Jaune", "Orange", "Rouge", "Vert", "Violet"]
COULEUR_NEUTRE = "Noir"


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
