import util as u
import pytest


@pytest.fixture()
def liste_neutre():
    return [(0, 0), (2, 1), (7, 10)]


def test_pion_present(liste_neutre):
    numero, hauteur = u.pion_neutre_present(liste_neutre, 2)
    assert numero == 1 and hauteur == 1


def test_pion_absent(liste_neutre):
    numero, hauteur = u.pion_neutre_present(liste_neutre, 5)
    print(numero, hauteur)
    assert numero is None and hauteur == 0
