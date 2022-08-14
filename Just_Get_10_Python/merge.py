from bases import*
from possibles import*

def pos_adj_équi(n, tableau, Z):        #def qui permet de return un tuple qui contient des listes avec les coordonnées des cellules adjacentes aux premières coordonées de Z
    m = n-1
    i = Z[0]
    j = Z[1]
    liste_occurence = []
    liste_occurence.append((i, j))
    if i == 0:                              #3 grand if si i et au bord gauche , droit ou milieux du tableau
        if j == 0:                          #3 moyen if si j et au bord gauche , droit ou milieux du tableau dans chaque grand if
            if tableau[i][j] == tableau[i + 1][j]:      #de cette manière (longue certe) on sait où l'on se trouve dans le tableau et on teste les cases adjacentes qui existent forcément
                liste_occurence.append((i + 1, j))      #de cette manière on évite les bugs en voulant vérifier les cellules en dehors du plateau
            if tableau[i][j] == tableau[i][j + 1]:
                liste_occurence.append((i, j + 1))

        elif 0 < j < m:
            if tableau[i][j] == tableau[i + 1][j]:
                liste_occurence.append((i + 1, j))
            if tableau[i][j] == tableau[i][j - 1]:
                liste_occurence.append((i, j - 1))
            if tableau[i][j] == tableau[i][j + 1]:
                liste_occurence.append((i, j + 1))

        elif j == m:
            if tableau[i][j] == tableau[i + 1][j]:
                liste_occurence.append((i + 1, j))
            if tableau[i][j] == tableau[i][j - 1]:
                liste_occurence.append((i, j - 1))

    elif 0 < i < m:
        if j == 0:
            if tableau[i][j] == tableau[i - 1][j]:
                liste_occurence.append((i - 1, j))
            if tableau[i][j] == tableau[i + 1][j]:
                liste_occurence.append((i + 1, j))
            if tableau[i][j] == tableau[i][j + 1]:
                liste_occurence.append((i, j + 1))

        elif 0 < j < m:
            if tableau[i][j] == tableau[i - 1][j]:
                liste_occurence.append((i - 1, j))
            if tableau[i][j] == tableau[i + 1][j]:
                liste_occurence.append((i + 1, j))
            if tableau[i][j] == tableau[i][j + 1]:
                liste_occurence.append((i, j + 1))
            if tableau[i][j] == tableau[i][j - 1]:
                liste_occurence.append((i, j - 1))

        elif j == m:
            if tableau[i][j] == tableau[i - 1][j]:
                liste_occurence.append((i - 1, j))
            if tableau[i][j] == tableau[i + 1][j]:
                liste_occurence.append((i + 1, j))
            if tableau[i][j] == tableau[i][j - 1]:
                liste_occurence.append((i, j - 1))

    elif i == m:
        if j == 0:
            if tableau[i][j] == tableau[i - 1][j]:
                liste_occurence.append((i - 1, j))
            if tableau[i][j] == tableau[i][j + 1]:
                liste_occurence.append((i, j + 1))
        elif 0 < j < m:
            if tableau[i][j] == tableau[i - 1][j]:
                liste_occurence.append((i - 1, j))
            if tableau[i][j] == tableau[i][j - 1]:
                liste_occurence.append((i, j - 1))
            if tableau[i][j] == tableau[i][j + 1]:
                liste_occurence.append((i, j + 1))
        elif j == m:
            if tableau[i][j] == tableau[i - 1][j]:
                liste_occurence.append((i - 1, j))
            if tableau[i][j] == tableau[i][j - 1]:
                liste_occurence.append((i, j -1))
    else:
        print("quelque chose a buger ...")
    return liste_occurence

def propagation(n, tableau, position, Z): #z est un tuple qui contient la position + contiendra a la fin la position des cellules de meme valeur
        print(Z)
        if n >= Z[0][0] >= 0 and n >= Z[0][1] >= 0:
            print(position,'ici')
            if adjacent_équivalent(n, tableau, position):
                list_occurence1 = [position]
                i = 0
                while i < len(list_occurence1):
                    list_occurence2 = pos_adj_équi(n, tableau, list_occurence1[i])
                    for x in list_occurence2:
                        if x not in list_occurence1:
                            list_occurence1.append(x)
                    i += 1
                for x in list_occurence1:
                    if x not in Z:
                        Z.append(x)
                return Z
            else:
                print("pas d'adjacent équivalent a la case selectionée")
        else:
            print("donée de Z( donc de la position) incorrect")



def modification(n, tableau, Z,):           #def qui permet de "fusionner" les cellules aux coordonnées de la première liste contenue dans Z tout les autre coordonnée sont utiliser pour passé les valeur de celle ci a 0
    affiche_tableau(tableau,n)
    tableau[Z[0][0]][Z[0][1]] += 1
    i = 1
    for i in range(1, len(Z), 1):
        tableau[Z[i][0]][Z[i][1]] = 0
    return tableau

def gravity(n, tableau, proba):             #def qui est appelée après modification elle permet de faire descendre toutes les cases si un 0 est en dessous ou alors créer de nouvelles cases si les 0 sont en haut du plateau
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if tableau[i][j] == 0:
                if i != 0:
                    for k in range(i, 0, -1):
                        tableau[k][j] = tableau[k-1][j]
                        tableau[k-1][j] = 0
                else:
                    tableau[i][j] = valeurs(proba)
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if tableau[i][j] == 0:
                gravity(n, tableau, proba)
    return tableau
