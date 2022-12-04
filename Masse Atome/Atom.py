class Atom:
    constante = 1.67*pow(10,-27)
    
    def __init__(self,nom,symbol,nombre,masse):
        self.__nom = nom
        self.__symbol = symbol
        self.__nombre = nombre
        self.__masse = masse
    def display(self):
        print("Caracteristique de l'atome : {} {} {} {}".format(self.__nom, self.__symbol, self.__nombre, self.__masse))
    def getNom(self):
        return self.__nom
    def getSymbol(self):
        return self.__symbol
    def getNombre (self):
        return self.__nombre
    def getMasse (self):
        return self.__masse
    def setNom (self,n):
        self.__nom = n
    def setSymbol (self,s):
        self.__symbol = s
    def setNombre (self,nb):
        self.__nombre = nb
    def setMasse (self,m):
        self.__masse = m
    def weight (self):
        return self.__masse * Atom.constante
