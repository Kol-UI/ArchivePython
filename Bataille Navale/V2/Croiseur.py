from Bateau import *


class Croiseur (Bateau):
    def __init__(self,grille,position,estVertical):
        super().__init__(grille,4,estVertical,"C",position)
