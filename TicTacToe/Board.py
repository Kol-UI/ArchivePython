from Pawn import *

class Board:
    _pawns = []
    def __init__(self, size):
        self._size = size
        for i in range(self.size):
            temp = []
            for j in range(self._size):
                temp.append(Pawn())
