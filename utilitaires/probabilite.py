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


if __name__ == '__main__':
    des_possible = [(a, b, c, d) for a in range(1, 7)
                    for b in range(1, 7)
                    for c in range(1, 7)
                    for d in range(1, 7)]

    combinaisons = list(map(retourne_possibilite, des_possible))

    # a_tester = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    a_tester = {2, 3, 10}
    calcul_reussite = test_probabilite(combinaisons, a_tester)
    print(calcul_reussite)
