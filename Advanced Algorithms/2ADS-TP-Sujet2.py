def createMatrix(file):
    myFile = open(file,'r')
    L=[]
    for line in myFile:
        line = line.replace(',',' ') #Oust les virgules !
        line = line.split()
        line = [int(x) for x in line]
        L.append(line)
    return L

matrix = createMatrix("2ADS-TP-Sujet2.txt")

