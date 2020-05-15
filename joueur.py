import random

# constantes
COULEURS = ["Bleu", "Blanc", "Gris", "Jaune", "Orange", "Rouge", "Vert", "Violet"]
COULEUR_NEUTRE = "Noir"
ECHELLE = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13,
           12: 3, 11: 5, 10: 7, 9: 9, 8: 11}

# Pour les calculs de probabilité
DES_POSSIBLE = [(a, b, c, d) for a in range(1, 7)
                for b in range(1, 7)
                for c in range(1, 7)
                for d in range(1, 7)]


def trouver_termine(mes_positions: dict) -> int:
    """
    Compte le nombre de lignes terminées
    :param mes_positions: position tenant compte des neutres
    :return: int : colonne finies
    """
    count = 0
    # assembler les echelles
    for value in range(2, 13):
        if mes_positions[value] == ECHELLE[value]:
            count += 1
    return count


def retourne_possibilite(des: tuple):
    """
    Calcule les possibilités
    :return: possibilite : liste des 3 doubles possibilités au mieux
    """
    de_a, de_b, de_c, de_d = des
    possibilite = [de_a + de_b, de_c + de_d,
                   de_a + de_c, de_b + de_d,
                   de_a + de_d, de_c + de_b
                   ]

    return list(set(possibilite))


def test_probabilite(combinaisons, choix: set):
    """
    Calcule le pourcentage de réalisation d'un set
    :return: pourcentage de reussite
    """
    resultat_match = [_ for _ in combinaisons
                      if set(_) & choix]
    print(resultat_match)
    reussite = len(resultat_match) / 1296
    return reussite


def calcul_resussite(a_tester: set) -> float:
    """
    Retourne le pourcentage de réussite de sortir au moins un de ces numéros
    :param a_tester: {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} ou l'un de ses sous ensemble
    :return: le taux de réussite: 1 = 100%
    """
    combinaisons = list(map(retourne_possibilite, DES_POSSIBLE))
    calcul_reussite = test_probabilite(combinaisons, a_tester)
    return calcul_reussite


class Bot:
    """Classe generique de Bot"""

    def __init__(self, mon_numero: int, aggressivite: int):
        print("Ajout d'un bot")
        self.aggressivite = aggressivite
        self.mon_numero = mon_numero
        encore = [True for _ in range(self.aggressivite)]
        stop = [False for _ in range(100 - self.aggressivite)]
        self.stop_encore = stop + encore

    def jouer(self, joueurs: dict, options: list, neutres: list) -> (list, bool):
        """
        Demander au jouer de jouer, fonction obligatoire
        :param joueurs: les joueurs avec leurs caractéristiques
        :param options: fonction de son lancé de dé
        :param neutres: l'emplacement des pions neutres
        :return:
        """
        print("Je réfléchis...")

        # print(f"J'analyse la situation :\n{repr(joueurs)}")

        mes_positions = self.trouver_mes_positions(joueurs, neutres)
        print(f"Mes positions de jeu : {mes_positions}")

        mon_choix = random.choice(options)
        if type(mon_choix) is int:
            mon_choix = [mon_choix]

        continuer = random.choice(self.stop_encore)

        neutres_echelle = [echelle for echelle, _ in neutres
                           if echelle != 0]

        # Si j'arrive en haut de l'échelle je décide de m'arrêter
        for valeur in mon_choix:
            # simuler l'avancée
            mes_positions[valeur] += 1
            if valeur not in neutres_echelle:
                neutres_echelle.append(valeur)
            if ECHELLE[valeur] == mes_positions[valeur]:
                # je suis en haut
                continuer = False
                break

        # Si j'ai encore des pions noir, je décide de continuer
        if len(neutres_echelle) != 3:
            continuer = True

        # Si j'ai 3 pions arrivés, j'arrête
        if trouver_termine(mes_positions) == 3:
            continuer = False

        return mon_choix, continuer

    def trouver_mes_positions(self, joueurs: dict, neutres: list) -> dict:
        """
        Utilitaire pour trouver ma position sur le plateau
        :param joueurs: les joueurs avec leurs caractéristiques
        :param neutres: l'emplacement des pions neutres
        :return: la hauteur de mes pions sur les échelles
        """
        mes_echelles = joueurs[self.mon_numero].position
        # si un neutre est présent on remet la bonne hauteur
        for echelle, hauteur in neutres:
            if echelle != 0:
                mes_echelles[echelle] = hauteur
        return mes_echelles
