class Case:
    """cases"""
    def __init__(self, position):
        self.__possedeBateau=False
        self.__estTouche=False
        self.__position=position

    def possedeBateau(self):
        return self.__possedeBateau

    def estTouche(self):
        return self.__estTouche

    def getPosition(self):
        return self.__position

    def recevoirTir(self):
        self.__estTouche=True

    def afficherPosition(self):
        print("x = ",self.__position[0], "y = ",self.__position[1])

    def placerBateau(self):
        self.possedeBateau = True
