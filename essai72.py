import outils72
commandes = [45, 12, 230, 8, 99, 150]

print(list(outils72.filtrer_par(outils72.est_grosse,
                                commandes)))

print(outils72.moyenne_commandes(commandes))

print(outils72.total_commandes(commandes))
print(outils72.total_commandes([]))

print(outils72.total_commandes(
    list(outils72.filtrer_par(outils72.est_grosse, commandes))))
