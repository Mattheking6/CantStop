import util as u
import pytest


@pytest.fixture()
def liste_neutre():
    """Exemple de positionnement des pions neutres"""
    return [(0, 0), (2, 1), (7, 10)]


def test_pion_present(liste_neutre):
    """Vérifier la présence d'un pion"""
    numero, hauteur = u.pion_neutre_present(liste_neutre, 2)
    assert numero == 1 and hauteur == 1


def test_pion_absent(liste_neutre):
    """Vérifier l'absence d'un pion"""
    numero, hauteur = u.pion_neutre_present(liste_neutre, 5)
    assert numero is None and hauteur == 0


@pytest.fixture()
def position_test():
    return {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}


def test_calcul_proba(position_test):
    """Vérifier que la probabilité n'est pas trop déconnate"""
    pourcentage = u.calcul_resussite(position_test)
    assert pourcentage == 1
