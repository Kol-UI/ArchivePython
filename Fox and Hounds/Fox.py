#class Fox
from gameBoard.py import *

class fox(self):
    def __init__(self, deplacementFox, win):
        self._deplacementFox = deplacementFox
        self.win = win
    def canMoveTo(self, plateauJeu):
        if self._plateauJeu.affichage() == 0: #Si la case est vide
            return deplacementFox == True    #Le Fox peut se déplacer vers la case en question
        #Ici nous allons pas tester si la case est occupée par un Fox (-1) étant donné qu'il n'y a qu'un seul Fox par partie
        elif self._plateauJeu.affichage() == 2: #Si la case est occupée par un Hound
            return deplacementFox == False           #Le Fox ne peux pas se déplacer vers la case
        elif self._plateauJeu.affichage() == NULL: #Si la case n'existe pas
            return deplacementFox == False           #Le Fox ne peux donc pas s'y déplacer
    def canMove(self, plateauJeu):
        #Cette méthode retourne True s’il existe au moins une case du plateau vers laquelle le pion peut se déplacer, False si non.
        if self.deplacementFox = True:
            return True
        else:
            return False        
    def move(self, plateauJeu):
        if canMove = True:  #Cette méthode demande à l’utilisateur de saisir les coordonnées d’une case, si la méthode d'au dessus a return True
            coordonnéesCase = input("Selectionnez les coordonnées d'une case: ")
    def win(self, plateauJeu):
        for pion in range self._plateauJeu[1;1][1;2][1;3][1;4]:
            #Si dans le plateau de jeu, une case de la ligne 1 possède la valeur -1, soit un Fox, win va return True
            if pion = -1
                return True
            else
                return False
