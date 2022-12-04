from Bateau import *

class Destroyer(Bateau):

    def __init__(self,grille,position,estVertical):
        super().__init__(grille,3,estVertical,"D",position)
