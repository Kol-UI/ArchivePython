from bases import*
from possibles import*
from merge import *

n = 5
proba = (0.05, 0.30, 0.6)
tableau = nouveaux_tableau(n, proba)
print()
print(tableau)
print()
while verif_coup_possible(n, tableau):
    affiche_tableau(tableau, n)
    print()
    i = int(input("ligne ="))
    j = int(input("colonne ="))
    print()
    position = (i, j)
    if adjacent_équivalent(n, tableau, i, j):
        Z = [position]
        Z = propagation(n, tableau, position, Z)
        tableau = modification(n, tableau, Z)
        print()
        affiche_tableau(tableau, n)
        print()
        tableau = gravity(n, tableau, proba)
    else:
        print("case selectionner aucun adjacent équivalent")