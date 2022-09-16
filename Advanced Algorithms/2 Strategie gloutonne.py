Liste = [6,5,2,7,3,5]
NbJoueur1 = [0]
NbJoueur2 = [0]

def glouton(Liste,NbJoueur1,NbJoueur2):
    for i in range(len(Liste[:2])):
        NbJoueur1.append(Liste[i])
    for i in range(len(Liste[3:])):
        NbJoueur2.append(Liste[i])
    Score1 = sum(NbJoueur1)
    Score2 = sum(NbJoueur2)
    print("Score joueur 1:", Score1)
    print("Score joueur 2:", Score2)
    if Score1 < Score2:
        print("Le joueur 2 possede le plus grand nombre, il a donc gagné.")
    else:
        print("Le joueur 1 possede le plus grand nombre, il a donc gagné.")

glouton(Liste,NbJoueur1,NbJoueur2)
