from Bateau import *


class Torpilleur (Bateau):
    def __init__(self,grille,position,estVertical):
        super().__init__(grille,2,estVertical,"T",position)

