from Grille import *
class Joueur:

    def __init__(self,pseudo):
        self.__pseudo = pseudo
        self.__grille = Grille(10,10)

    def getGrille(self):
        return self.__grille
