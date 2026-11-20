import outils72
commandes = [45, 12, 230, 8, 99, 150]


def test_filtrer_par():
    assert (list(outils72.filtrer_par(outils72.est_grosse,
                                      commandes))) == [230, 150]


def test_moyenne_commandes():
    assert outils72.moyenne_commandes(commandes) == 90.67


def test_total_commandes_liste_vide():
    assert outils72.total_commandes([]) == 0
