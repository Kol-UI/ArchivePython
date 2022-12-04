import random

plateau = [0, 1, 2, 3, 4, 5, 6, 7, 8]
chooseMode = True

def display():
    print (plateau[0],' ',plateau[1],' ',plateau[2])
    print (plateau[3],' ',plateau[4],' ',plateau[5])
    print (plateau[6],' ',plateau[7],' ',plateau[8])

def checkLine(char, a, b, c):
    if plateau[a] == char and plateau[b] == char and plateau[c] == char:
           return True

def checkAll(char):
    if checkLine(char, 0, 1, 2):
           return True
    if checkLine(char, 3, 4, 5):
           return True
    if checkLine(char, 6, 7, 8):
           return True
    if checkLine(char, 0, 3, 6):
           return True
    if checkLine(char, 1, 4, 7):
           return True
    if checkLine(char, 2, 5, 8):
           return True
    if checkLine(char, 0, 4, 8):
           return True
    if checkLine(char, 2, 4, 6):
           return True

class Player:
    def __init__(self, name):
        self.name = name
    def chooseSquare(self):
        print(self.name, ', select a spot ')

while chooseMode == True:
    mode = int(input("Choose the game mode: 1)player vs bot 2)player vs player "))
    if mode == 1:
        chooseMode = False
        while True:
            spot = int(input("Select a spot: "))
            if plateau[spot] != 'x' and plateau[spot] != 'o':
                plateau[spot] = 'x'
                if checkAll('x') == True:
                    print("x wins")
                    break
                while True:
                    random.seed()
                    bot = random.randint(0,8)
                    if plateau[bot] != 'o' and plateau[bot] != 'x':
                        plateau[bot] = 'o'
                        if checkAll('o') == True:
                            print("o wins")
                            break
                        break
            else:
                print('You cant do that.')
            display()
    if mode == 2:
        chooseMode = False
        namePlayer1 = input("What is the name of the first player ? ")
        Player1 = Player(namePlayer1)
        namePlayer2 = input("What is the name of the second player ? ")
        Player2 = Player(namePlayer2)
        display()
        while True:
            Player1.chooseSquare()
            spot = int(input())
            print("The player choose square ", spot, "...")
            if plateau[spot] != 'x' and plateau[spot] != 'o':
                plateau[spot] = 'x'
                display()
                if checkAll('x') == True:
                    print(namePlayer1, " wins !!!")
                    break;
                while True:
                    Player2.chooseSquare()
                    spot = int(input())
                    print("The player choose square ", spot, "...")
                    if plateau[spot] != 'o' and plateau[spot] != 'x':
                        plateau[spot] = 'o'
                        display()
                        if checkAll('o') == True:
                            print(namePlayer2, " wins !!!")
                            break
                        break
            else:
                print('You cant do that.')
                
    else:
        print('You cant do that.')
        chooseMode = True
           
