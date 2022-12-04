from Case import *
class Bateau:
    """class bateau"""
    def __init__(self,grille,taille,estVertical,initiale,position):
        self.__taille=taille
        self.__estVertical=estVertical
        self.__initiale=initiale
        self.__position=position
        self.__cases = []
        if estVertical:
            #Bateau vertical
            for i in range(taille):
                #On ajoute la case suivante du bateau dans self.__cases
                positionSuivante = (position[0],position[1]+i)
                self.__cases.append(grille.getCase(positionSuivante))
        else:
            #bateau Horizontal
            for i in range(taille):
                #On ajoute la case suivante du bateau dans self.__cases
                positionSuivante = (position[0]+i,position[1])
                self.__cases.append(grille.getCase(positionSuivante))
        self.placerBateau()




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


    def placerBateau(self):
        for case in self.__cases:
            case.placerBateau()

