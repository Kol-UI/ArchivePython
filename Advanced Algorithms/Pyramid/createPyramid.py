def createPyramid(file):
    myFile = open(file,'r')
    L=[]
    for line in myFile:
        line = line.split()
        line = [int(x) for x in line]
        L.append(line)
    return L

pyramid = createPyramid("pyramid.txt")

