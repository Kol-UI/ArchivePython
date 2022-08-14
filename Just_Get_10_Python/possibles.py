from bases import*

"""
def adjacent_équivalent(n, tableau,i,j):
    if i == 0:
        if j == 0:
            if tableau[i][j] == tableau[i + 1][j]:
                return True
            elif tableau[i][j] == tableau[i][j + 1]:
                return True

        elif 0 < j < n:
            if tableau[i][j] == tableau[i + 1][j]:
                return True
            elif tableau[i][j] == tableau[i][j - 1]:
                return True
            elif tableau[i][j] == tableau[i][j + 1]:
                return True

        elif j == n:
            if tableau[i][j] == tableau[i + 1][j]:
                return True
            elif tableau[i][j] == tableau[i][j - 1]:
                return True

    elif 0 < i < n :
        if j == 0:
            if tableau[i][j] == tableau[i - 1][j]:
                return True
            elif tableau[i][j] == tableau[i + 1][j]:
                return True
            elif tableau[i][j] == tableau[i][j + 1]:
                return True

        elif 0 < j < n:
            if tableau[i][j] == tableau[i - 1][j]:
                return True
            elif tableau[i][j] == tableau[i + 1][j]:
                return True
            elif tableau[i][j] == tableau[i][j + 1]:
                return True
            elif tableau[i][j] == tableau[i][j - 1]:
                return True

        elif j == n:
            if tableau[i][j] == tableau[i - 1][j]:
                return True
            elif tableau[i][j] == tableau[i + 1][j]:
                return True
            elif tableau[i][j] == tableau[i][j - 1]:
                return True

    elif i == n:                #attention ici on compare a n et ( tableau est de 5  genre tu compare a 5 pas a 4 qui est normalment la dernière ligne)
        if j == 0:
            if tableau[i][j] == tableau[i - 1][j]:
                return True
            elif tableau[i][j] == tableau[i][j + 1]:
                return True
        elif 0 < j < n:
            if tableau[i][j] == tableau[i - 1][j]:
                return True
            elif tableau[i][j] == tableau[i][j - 1]:
                return True
            elif tableau[i][j] == tableau[i][j + 1]:
                return True
        elif j == n:
            if tableau[i][j] == tableau[i - 1][j]:
                return True
            elif tableau[i][j] == tableau[i][j - 1]:
                return True
    else:
        return False
"""

def adjacent_équivalent(n, tableau, position):                      #fonction plus court que celle en commentaire au dessu qui effectue simplement un return si une cellule adjacent et équivalent a la valeur de la cellue selectionner
    print("check adjacent équivalent/ position =", position)
    i = position[0]
    j = position[1]
    if i-1 >= 0:
        if tableau[i][j] == tableau[i-1][j]:
            return True
    if i+1 < n:
        if tableau[i][j] == tableau[i+1][j]:
            return True
    if j-1 >= 0:
        if tableau[i][j] == tableau[i][j-1]:
            return True
    if j+1 < n:
        if tableau[i][j] == tableau[i][j+1]:
            return True
    return False


def verif_coup_possible(n, tableau):            #fonction qui parcours le plateau et return True au premier coup possible jouable dans le plateau False ci aucun coup ne peut être joué
    for i in range(0, n):
        for j in range(0, n):
            position = []
            position.append(i)
            position.append(j)
            if adjacent_équivalent(n, tableau, position):
                print("coup possible en [",i, ",", j, "] ")
                print()
                return True
    return False

def valeur_max(n, tableau):                     #fonction qui permet de connaître la valeur la plus élevée du tableau(donc le score du joueur)
    x = 0
    for i in range(0, n):
        for j in range(0, n):
            if tableau[i][j] > x:
                x = tableau[i][j]
    return x
