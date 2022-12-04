class Player:

    def __init__(self, name, symbol):
        self.__name = name
        self.__symbol = symbol

    def __init__(self):
        self.__name = ''
        self.__name = ''

    def getname(self):
        return self.__name
    def getsymbol(self):
        return self.__symbol
    def askname(self):
        self.__name = input('Quel est ton nom ?')
