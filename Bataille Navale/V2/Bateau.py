from Case import *
class Bateau:
    """class bateau"""
    def __init__(self,grille,taille,estVertical,initiale,position):
        self.__taille=taille
        self.__estVertical=estVertical
        self.__initiale=initiale
        self.__position=position
        self.__cases = []
        self.__grille = grille


    def getInitiale(self):
        return self.__initiale

    def getPosition(self):
        return self.__position

    def estVertical(self):
        return self.__estVertical

    def getTaille(self):
        return self.__taille

    def estCoule(self):
        for case in self.__cases:
            if not case.estTouche():
                return False
        return True

    #Permet de remplir le tableau self.__cases avec les cases de la grille ou se trouve le bateau
    def placerBateauSurLaGrille(self):
        if self.__estVertical:
            #Bateau vertical
            for i in range(self.__taille):
                #On ajoute la case suivante du bateau dans self.__cases
                positionSuivante = (self.__position[0],self.__position[1]+i)
                self.__cases.append(self.__grille.getCase(positionSuivante))
        else:
            #bateau Horizontal
            for i in range(self.__taille):
                #On ajoute la case suivante du bateau dans self.__cases
                positionSuivante = (self.__position[0]+i,self.__position[1])
                self.__cases.append(self.__grille.getCase(positionSuivante))
        for case in self.__cases:
            case.placerBateau(self)

