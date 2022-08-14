import random

def valeurs(proba):             #def qui renvoi un int entre 1 et 4 par rapport au nombre aléatoire qui est apparrue
    i = random.random()
    if i < proba[0]:
        return 4
    elif i < proba[1]:
        return 3
    elif i < proba[2]:
        return 2
    else:
        return 1

def nouveaux_tableau(n,proba):      #def qui crée un tableau de n * n et qui le remplis de nombre retourner par la fonction valeur
    return [[valeurs(proba) for i in range(n)] for j in range(n)]

def affiche_tableau(tableau, taille_plateau):   #def qui permet d'afficher un tableau dans la console
    for i in range(taille_plateau):
        for j in range(taille_plateau):
            print(tableau[i][j], end=" ")
        print()


"""
n = 5
proba = (0.05, 0.30, 0.6);
tableau = nouveaux_tableau(n, proba)
affiche_tableau(tableau, n)
"""