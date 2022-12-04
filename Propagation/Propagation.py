import copy
import random

class Arbre:
    def __init__(self, état = 0):
        self.__état = état


    #Affiche état arbre    
    def symboleAffichage(self):
            # . si pas arbre
            if self.__état == 0:
                print(".", end = ' ')
            # A si arbre
            elif self.__état == 1:
                print("A", end = ' ')
            # F si en feu
            elif self.__état == 2:
                print("F", end = ' ')
            # C si en cendre
            elif self.__état == 3:
                print("C", end = ' ')


    #Défini le prochain état
    def prochainEtat(self, enFeu = False):
        self._enFeu = enFeu
        #Pas d'arbre reste pas d'arbre
        if self.__état == 0 :
             self.__état = 0
        #Si arbre et autour en feu, devient en feu
        elif self.__état == 1 and self._enFeu == True:
            self.__état = 2
        #Si arbre et pas de feu autour, reste normal
        elif self.__état == 1 and self._enFeu == False:
            self.__état = 1
        #Si en feu, devient cendre
        elif self.__état == 2:
            self.__état = 3
        #Si en cendre, reste en cendre
        else:
            self.__état = 3


    #Transforme en arbre    
    def setEtat1(self):
        self.__état = 1


    #Met le feu
    def onFire(self):
        self.__état = 2


    #Récupère l'état
    def getEtat(self):
        return self.__état

            
class Foret:
    def __init__(self, m, n, p):
        self.__m = m
        self.__n = n
        self.__p = p

        self._plateau = [[Arbre() for l in range(self.__m)] for k in range(self.__n)]


    #Choisi un nombre parmi 100, si il est inférieur à la proportion, met un arbre
    def setter(self):
        for i in self._plateau:
            for j in i:
                aleatoire = random.randint(0,99)
                if aleatoire <= ((self.__p * 100) - 1):
                    j.setEtat1()
                else:
                    continue


    #Choisi une ligne et une colonne et met le feu si il y a un arbre
    def allumezLeFeu(self):
        print('\n\n')
        while 1:
            self.__feuM = random.randint(0, self.__m -1)
            self.__feuN = random.randint(0, self.__n -1)
            
            if self._plateau[self.__feuM][self.__feuN].getEtat() == 1:
                self._plateau[self.__feuM][self.__feuN].onFire()
                break
            else:
                continue


    #Affiche les symboles du plateau
    def affichage(self):
        for i in self._plateau:
            for j in i:
                j.symboleAffichage()
            print('\n')


    #Cherche si un voisin est en feu
    def voisin(self, x, y):

        if self._plateau[x][y].getEtat() == 1:
            if (x != 0) and self._plateau[x-1][y].getEtat() == 2:
                return True
            elif (x != self.__m -1) and self._plateau[x+1][y].getEtat() == 2:
                return True
            elif (y != 0) and self._plateau[x][y-1].getEtat() == 2:
                return True            
            elif (y != self.__n -1) and self._plateau[x][y+1].getEtat() == 2:
                return True            
            else:
                return False
           
        else:
            return False


    #Copie le plateau, place dans la copie les états du plateau suivant            
    def __duplication(self):
        nextPlateau = copy.deepcopy(self._plateau)
        print("\n-------------------------------------------------------")        
        for x in range (self.__m):
            for y in range (self.__n):
                
                enFeu = self.voisin(x,y)
                nextPlateau[x][y].prochainEtat(enFeu)
                
        #Rebascule la copie sur le principal
        self._plateau = nextPlateau

        
    #Appelle la métode privée
    def générationSuivante(self):
        self.__duplication()


    #Calcule la proportion : arbres/total cases
    def nombreArbres(self):
        arbresRestants = 0
        total = self.__m * self.__n
        
        for i in self._plateau:
            for j in i:
                if j.getEtat() == 1 or j.getEtat() == 2:
                    arbresRestants += 1
                else:
                    continue

        return (arbresRestants / total) * 100
                    

    #Compare 2 plateaux
    def __lt__(self, other):
        return self.nombreArbres() < other.nombreArbres()
    


class ForetTorique(Foret):
    def __init__(self, Fn, Fm, Fp):
        Foret.__init__(self, Fn, Fm, Fp)
        self.__m = Fm
        self.__n = Fn
        

    #Cherche si un voisin est en feu, de manière torique    
    def voisin(self, x, y):
        if self._plateau[x][y].getEtat() == 1:
            if (x != 0) and self._plateau[x-1][y].getEtat() == 2:
                return True
            elif (x != self.__m -1) and self._plateau[x+1][y].getEtat() == 2:
                return True
            elif (y != 0) and self._plateau[x][y-1].getEtat() == 2:
                return True            
            elif (y != self.__n -1) and self._plateau[x][y+1].getEtat() == 2:
                return True
            elif (x == 0) and self._plateau[self.__m - 1][y].getEtat() == 2:
                return True
            elif (y == 0) and self._plateau[x][self.__n - 1].getEtat() == 2:
                return True
            elif (x == self.__m - 1) and self._plateau[0][y].getEtat() == 2:
                return True
            elif (y == self.__n - 1) and self._plateau[x][0].getEtat() == 2:
                return True
                
            else:
                return False
           
        else:
            return False
            
#Choix type, taille et proportion
choix = int(input("Forêt normale (1) ou torique (2) ? "))
tailleCL = int(input("Nombre de lignes et de colonnes : "))
propArbres = float(input("Proportion d'arbres - environ (0.5 pour 50%) : "))

if choix == 1:
    toto = Foret(tailleCL, tailleCL, propArbres)                 
else:
    toto = ForetTorique(tailleCL, tailleCL, propArbres)
    
toto.setter()
print("\nTout se passait bien dans la jolie forêt...")
toto.affichage()
toto.allumezLeFeu()
w = input()
print("******************\nQuand soudain...\n\nGénération 1 :\n")
toto.affichage()
print("Proportion d'arbres :", toto.nombreArbres(),"%.\n")
count = 1

#Boucle pour répéter le jeu
while 1:
    w = input()
    toto.générationSuivante()
    count = count +1
    print("Génération", count, ":\n")
    toto.affichage()
    print("Proportion d'arbres", toto.nombreArbres(),"%.\n")













