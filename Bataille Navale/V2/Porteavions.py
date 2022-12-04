from Bateau import *


class Porteavions (Bateau):
    def __init__(self,grille,position,estVertical):
        super().__init__(grille,5,estVertical,"P",position)
