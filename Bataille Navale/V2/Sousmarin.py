from Bateau import *


class Sousmarin(Bateau):
    def __init__(self,grille,position,estVertical):
        super().__init__(grille,3,estVertical,"S",position)
