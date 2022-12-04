#class hound
from gameBoard.py import *

class hound(self,):
    def __init__(self, nbLigne, nbColonne, deplacementHounds):
        self.__nbLigne = nbLigne
        self.__nbColonne = nbColonne
        self._deplacementHounds = deplacementHounds
    def canMoveTo(self, plateauJeu):
        if self._plateauJeu.affichage() == 0: #Si la case est vide
            return deplacementHounds == True    #Le hound peut se déplacer vers la case en question
        elif self._plateauJeu.affichage() == -1:    #Si la case est occupée par un Fox
            return deplacementHounds == False   #Le hound ne peut pas se déplacer vers la case
        elif self._plateauJeu.affichage() == 2: #Si la case est occupée par un autre Hound
            return deplacementHounds == False            #Le hound ne peux pas se déplacer vers la case
        elif self._plateauJeu.affichage() == NULL: #Si la case n'existe pas
            return deplacementHounds == False            #Le hound ne peux s'y déplacer
    def canMove(self, plateauJeu):
        #Cette méthode retourne True s’il existe au moins une case du plateau vers laquelle le pion peut se déplacer, False si non.
        if self.deplacementHound = True:
            return True
        else:
            return False        
    def move(self, plateauJeu):
        if canMove = True:  #Cette méthode demande à l’utilisateur de saisir les coordonnées d’une case, si la méthode d'au dessus a return True
            coordonnéesCase = input("Selectionnez les coordonnées d'une case: ")
