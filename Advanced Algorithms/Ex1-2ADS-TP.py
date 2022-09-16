def RecursifNaif(x, y, n):
    Liste=[[5, 10, 4, 4], [9, 2, 8, 7], [4, 3, 1, 4], [9, 2, 8, 10], [10, 5, 4, 1]]
    n += 1
    for i in range(Liste):
        for j in range(Liste):
            if i==0 or j==0:
                return i, j
            else:
                if i+1 and j < i and j-1:       #test si le nombre de droite est plus petit que le nombre en bas
                    return RecursifNaif(x+1, y, n)
                if i and j-1 < i+1 and j:       #test si le nombre en bas est plus petit que le nombre de droite
                    return RecursifNaif(x, y-1, n)
                if i+1 and j < i+1 and j-1:     #test si le nombre de droite est plus petit que le nombre en diagonale
                    return RecursifNaif(x+1, y, n)
                if i+1 and j-1 < i+1 and j:     #test si le nombre en diagonale est plus petit que le nombre de droite
                    return RecursifNaif(x+1, y-1, n)
                if i+1 and j-1 < i and j-1:     #test si le nombre en diagonale est plus petit que le nombre en bas
                    return RecursifNaif(x+1, y-1, n)
                if i and j-1 < i+1 and j-1:     #test si le nombre en bas est plus petit que le nombre en diagonale
                    return RecursifNaif(x, y-1, n)
                else:
                    print("Erreur")
                    RecursifNaif(x, y, n)
    return n



def TopDown(x, y, n, cache, compteur):      #algorithme top down avec mise en mémoire cache
    Liste = [[5, 10, 4, 4], [9, 2, 8, 7], [4, 3, 1, 4], [9, 2, 8, 10], [10, 5, 4, 1]]
    compteur+=Liste[x][y]
    cache[x][y] = Liste[x][y]
    if cache[len(Liste)-1-x][len(Liste)-1-y] and compteur > cache[len(Liste)-1-x][len(tableau)-1-y]:
        return cache[len(Liste)-1-x][len(Liste)-1-y]
    cache[len(Liste)-1-x][len(Liste)-1-y] = compteur
    if x==0 and y==0:
        return cache[x][y]
    elif x-1>0:
        return TopDown(x, y-1, n, cache, compteur)
    elif y-1>0
        return TopDown(x-1, y, n, cache, compteur)
    else:
        return TopDown(x, y-1, n, cache, compteur), TopDown(x-1, y, n, cache, compteur)

def appelTopDown(x, y, n, cache, compteur):     #fonction permettant le premier appel
    cache = [[0 for i in range(len(Liste))]for j in range(len(Liste))] 
    return TopDown(x, y, n, cache, compteur)



def BottomUp(x, y, n):      # fonction du bottom up
    Liste = [[5, 10, 4, 4], [9, 2, 8, 7], [4, 3, 1, 4], [9, 2, 8, 10], [10, 5, 4, 1]]
    listeKeep = [0]*(x+1)
    cacheX = [0]*(x-1)
    cacheY = [0]*(y-1) 
    for x in range(1,x+1):
        for y in range(1,y-1):
            for i in range(len(Liste)):
                for j in range(len(Liste)):
                    if (Liste[i][j] <= x) and (Liste[i][j] <= y):
                        n = i
            listeKeep[x] = n
            while x>0:
                Liste.append(Liste[listeKeep[x]])
                x -= Liste[listeKeep[x]]
            while y>0:
                Liste.append(Liste[listeKeep[y]])
                y -= Liste[listeKeep[y]]
            return cacheX[x], cacheY[y], Liste
