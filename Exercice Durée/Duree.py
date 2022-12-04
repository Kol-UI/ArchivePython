class duree:
    """"""
    def __init__(self, h=1, m=0, s=0):
        self.__h = 0
        self.__m = 0
        self.__s = 0
        time = self.getSeconde(abs(h), abs(m), abs(s))
        self.addSeconde(time)

    #Ajoute un nombre de seconde à la durée
    def addSeconde(self,s):
        heure = s // 3600
        s -= heure * 3600
        minute = s // 60
        seconde = s%60
        self.__h += heure
        self.__m += minute
        self.__s += seconde



    #Converti une durée en nombre de secondes
    def getSeconde(self, h, m, s):
        time = h*3600+m*60+s
        return time


    #Affiche la durée
    def afficher_duree(self):
        print(self.__h, 'h', self.__m, 'm', self.__s, 's', sep='')







    # Setters et getters
    def setH(self,H):
        self.__h = H

    def setM(self,M):
        self.__m = M%60

    def setS(self,S):
        self.__s = S

    def getH(self):
        return self.__h

    def getM(self):
        return self.__m

    def getS(self):
        return self.__s
