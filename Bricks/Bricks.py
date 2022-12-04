class Gameboard:
    """Board of the game"""
    
    def __init__(self, height = 5, width = 6):
        if height%2 == 0 or width%2 != 0:
            self.__height = 5
            self.__width = 6
        else:
            self.__height = height
            self.__width = width
            
        self.__gameboard = [[0 for i in range(self.__width)]
                            for j in range(self.__height)]
        
        self.__gameboard[int((self.__height)/2)][int((self.__width-2)/2)] = 1
        self.__gameboard[int((self.__height)/2)][int((self.__width)/2)] = 2


    def display(self):
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__gameboard[i][j] == 0:
                    print(".", end="")
                elif self.__gameboard[i][j] == 1:
                    print("X", end="")
                elif self.__gameboard[i][j] == 2:
                    print("O", end="")
                elif self.__gameboard[i][j] == 3:
                    print("B", end="")
                    
            print("", end="\n")
        print()


    def isFree(self, row, column):
        if self.__gameboard[row][column] == 0:
            return True
        
        return False


    def getHeight(self):
        return self.__height


    def setHeight(self, x):
        self.__height = x


    def getWidth(self):
        return self.__width


    def setWidth(self, x):
        self.__width = x


    def getSquare(self, row, column):
        return self.__gameboard[row][column]


    def setSquare(self, row, column, x):
        self.__gameboard[row][column] = x



class Pawn:
    """Pawn of the players"""

    def __init__(self, row, column):
        self.__row = row
        self.__column = column


    def getRow(self):
        return int(self.__row)


    def setRow(self, x):
        self.__row = x


    def getColumn(self):
        return int(self.__column)


    def setColumn(self, x):
        self.__column = x



class Player():
    """Players in game"""

    def __init__(self, name, playerNumber, board):
        self.__name = name
        self.__number = playerNumber
        if self.__number == 1:
            self.__pawn = Pawn(int(board.getHeight())/2, int((board.getWidth())-2)/2)
        elif self.__number == 2:
            self.__pawn = Pawn(int(board.getHeight())/2, int(board.getWidth())/2)


    def getName(self):
        return self.__name

    
    def canMove(self, board):
        for i in range(-1,2):
            for j in range(-1,2):
                if (i == 0 and j == 0) or (self.__pawn.getRow()+ i < 0) or (self.__pawn.getColumn()+ j < 0):
                    pass
                else:
                    try:
                        if board.getSquare(self.__pawn.getRow()+ i, self.__pawn.getColumn()+ j) == 0:
                            return True
                    except:
                        continue
                    
        return False

    
    def move(self, board):
        row = -1
        column = -1
        while True:
            while True:
                row = int(input("Row : "))
                if self.__pawn.getRow() -1 <= row <= self.__pawn.getRow() +1:
                    break

            while True:
                column = int(input("Column : "))
                if self.__pawn.getColumn() -1 <= column <= self.__pawn.getColumn() +1:
                    break

            if row < 0 or row > board.getWidth() or column < 0 or column > board.getHeight():
                print("Out of range !")
                
            elif board.getSquare(row, column) != 0:
                print("You can't move here !")

            else:
                board.setSquare(self.__pawn.getRow(), self.__pawn.getColumn(), 0)
                self.__pawn.setRow(row)
                self.__pawn.setColumn(column)
                board.setSquare(self.__pawn.getRow(), self.__pawn.getColumn(), self.__number)
                break


    def putBrick(self, board):
        row = -1
        column = -1
        while True:
            while True:
                row = int(input("Row : "))
                if self.__pawn.getRow() -1 <= row <= self.__pawn.getRow() +1:
                    break

            while True:
                column = int(input("Column : "))
                if self.__pawn.getColumn() -1 <= column <= self.__pawn.getColumn() +1:
                    break                
                
            if row < 0 or row > board.getWidth() or column < 0 or column > board.getHeight():
                print("Out of range !")
                
            elif board.getSquare(row, column) != 0:
                print("You can't put a brick here !")

            else:
                board.setSquare(row, column, 3)
                break



class Game:
    """Game manager"""

    def __init__(self):
        self.__playersList = []
        row = int(input("Rows of the gameboard : "))
        column = int(input("Columns of the gameboard : "))          
        self.__board = Gameboard(row, column)
        self.__board.display()
        name1 = input("Name of the player 1 : ")
        name2 = input("Name of the player 2 : ")
        player1 = Player(name1, 1, self.__board)
        player2 = Player(name2, 2, self.__board)
        self.__playersList.append(player1)
        self.__playersList.append(player2)


    def play(self):
        turn = 0
        while(True):
            if not self.__playersList[turn].canMove(self.__board):
                print(self.__playersList[turn-1].getName(), "wins !")
                break

            print(self.__playersList[turn].getName(), "moves")
            self.__playersList[turn].move(self.__board)
            self.__board.display()
            print(self.__playersList[turn].getName(), "puts a brick")
            self.__playersList[turn].putBrick(self.__board)
            self.__board.display()
            print("\n")
            
            if turn == 0:
                turn = 1
            else:
                turn = 0
        
            
        
game = Game()
game.play()
   
