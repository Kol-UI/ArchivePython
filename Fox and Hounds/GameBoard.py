#class game Board

class gameBoard:
    def __init__(self, nbPlateau, nbLigneColonne, plateauJeu, pion):
        self.__nbPlateau = nbPlateau
        self.__nbLigneColonne = nbLigneColonne
        self.__pion = pion
        self._plateauJeu = plateauJeu #liste bi-dimentionnelle d'entiers
        gameBoard.__init__(self, plateauJeu):
            if n == 4:
                self._plateauJeu = [[0, 1, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, -1, 0]]
            else:
                self._plateauJeu = [[0, 1, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, -1, 0]] * n
    def affichage(self):
        if self._plateauJeu == 0: #case vide
            self._pion == 0
            print("0", end = ' ')
        elif self._plateauJeu == -1: #case du pion fox
            pion == -1
            print("F", end = ' ')
        elif self._plateauJeu == 2: #case des pions hounds
            pion == 2
            print("2", end = ' ')
    def __getLigneColonne__(self, n):
        self.__nbLigneColonne == n
    def __setLignecolonne__(self, nbLigneColonne):
        return self.__nbLigneColonne

    
    
