from Case import *
from Bateau import *

class Grille :
    """classe grille"""

    def __init__(self, largeur, longueur):
        self.__plateau = [[Case((i,j)) for i in range (largeur)] for j in range (longueur)]
        self.__bateaux = [Bateau(self,4,True,"A",(3,4))]

    def afficher(self):
        for ligne in self.__plateau :
            for case in ligne :
                print("- ", end="")
            print("")

    def getCase(self,position):
        return self.__plateau[position[1]][position[0]]




