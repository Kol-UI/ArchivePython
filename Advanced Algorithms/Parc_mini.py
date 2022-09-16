import math
INF = float("inf")
matrix = [[2,3,1,1,6],[1,4,4,1,4],[7,1,2,2,5],[2,1,3,8,3],[2,4,3,2,1]]

def naive(matrix, x, y, mini):
    szY = len(matrix) - 1
    szX = len(matrix[0]) - 1
    mini += matrix[y][x]
    if x == szX and y == szY:
        return mini
    elif x == szX:
        return naive(matrix, x, y + 1, mini)
    elif y == szY:
        return naive(matrix, x + 1, y, mini)
    else:
        return min(naive(matrix, x, y + 1, mini), naive(matrix, x + 1, y, mini))

def topDown(matrix, x, y, mini, track):
    mini += matrix[y][x]
    szY = len(matrix) - 1
    szX = len(matrix[0]) - 1
    global lastValue
    lastValue = track[szY][szX]
    if track[y][x] != INF and mini > track[y][x]:
        return track[y][x]
    
    track[y][x] = mini
    
    if x == szX and y == szY:
        return track[y][x]
    elif x == szX:
        return topDown(matrix, x, y + 1, mini, track)
    elif y == szY:
        return topDown(matrix, x + 1, y, mini, track)
    else:
        return min(topDown(matrix, x, y + 1, mini, track), topDown(matrix, x + 1, y, mini, track))

def topDownCreate(matrix):
    szmY = len(matrix)
    szmX = len(matrix[0])
    track = [[INF for i in range(szmY)] for j in range(szmX)]
    topDown(matrix, 0, 0, 0, track)
    print("Total Top Down :", lastValue)

def bottomUp(matrix, track, keep): 
    sztY = len(track) - 1
    sztX = len(track[0]) - 1
    for i in range(sztY + 1):
        for j in range(sztX + 1):
            if i < sztY:
                testi = track[i][j] + matrix[i+1][j]
                if testi < track[i+1][j]:
                    track[i+1][j] = testi
                    keep[i+1][j] = [i,j]
            if j < sztX:
                testj = track[i][j] + matrix[i][j+1]
                if testj < track[i][j+1]:
                    track[i][j+1] = testj
                    keep[i][j+1] = [i,j]
                        
    print("Total Bottom Up :", track[sztY][sztX])
    displayKeep(keep, sztX, sztY)

def displayKeep(keep, x, y):
    if x == 0 and y == 0:
        return
    else:
        x2 = (keep[x][y])[0]
        y2 = (keep[x][y])[1]
        print("x :", x2, "et y :", y2)
        displayKeep(keep, x2, y2)
        
def bottomUpCreate(matrix):
    szmY = len(matrix)
    szmX = len(matrix[0])
    track = [[INF for i in range(szmY)] for j in range(szmX)]
    keep = [[[0,0] for i in range(szmY)] for j in range(szmX)]
    track[0][0] = matrix[0][0]
    bottomUp(matrix, track, keep)

def createMatrix(file):
    myFile = open(file,'r')
    L=[]
    for line in myFile:
        line = line.replace(',',' ') #Oust les virgules !
        line = line.split()
        line = [int(x) for x in line]
        L.append(line)
    return L

def greedy(matrix, x, y):
    mini = matrix[y][x]
    szY = len(matrix) - 1
    szX = len(matrix[0]) - 1
    if x == szX and y == szY:
        return mini
    elif x == szX:
        return mini + greedy(matrix, x, y + 1)
    elif y == szY:
        return mini + greedy(matrix, x + 1, y)
    else:
        if matrix[y+1][x] < matrix[y][x+1]:
            return mini + greedy(matrix, x, y + 1)
        else:
            return mini + greedy(matrix, x + 1, y)

          
print("Total Naif :", naive(matrix, 0, 0, 0))
print("\n")
topDownCreate(matrix)
print("\n")
bottomUpCreate(matrix)
print("\n")
print("---- Txt : ----")
matrix2 = createMatrix("2ADS-TP-Sujet2.txt")
#topDownCreate(matrix2)
print("\n")
print("Total Glouton :", greedy(matrix, 0, 0))
