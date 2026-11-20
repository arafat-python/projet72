def filtrer_par(fonction_test, liste):
    for nombre in liste:
        if fonction_test(nombre):
            yield nombre


def est_grosse(montant):
    return montant > 100


def arrondir(fonction):
    def enveloppe(valeur):
        resultat = fonction(valeur)
        return round(resultat, 2)
    return enveloppe


@arrondir
def moyenne_commandes(liste):
    return sum(liste) / len(liste)


def verifier_non_vide(fonction):
    def enveloppe(valeur):
        if valeur == []:
            print("aucune commande")
            return 0
        else:
            resultat = fonction(valeur)
            return resultat
    return enveloppe


@verifier_non_vide
def total_commandes(liste):
    return sum(liste)
