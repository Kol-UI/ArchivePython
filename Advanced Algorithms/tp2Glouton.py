def tp2Glouton(x,y,pyram):

    print("x: ",x," y: ",y," valeur: " , pyram[x][y])
    if x==0 and y ==0:
        return pyram[x][y]
    elif x-1<0:
        return pyram[x][y]+tp2Glouton(x,y-1,pyram)
    elif y-1<0:       
        return pyram[x][y]+tp2Glouton(x-1,y,pyram)
    else:
        if pyram[x-1][y]<pyram[x][y-1]:
            return pyram[x][y]+tp2Glouton(x-1,y,pyram)
        else:
            return pyram[x][y]+tp2Glouton(x,y-1,pyram)
            

pyram=[[2,3,1,1,6],[1,4,4,1,4],[7,1,2,2,5],[2,1,3,8,3],[2,4,3,2,1]]
print(tp2Glouton(len(pyram)-1,len(pyram)-1,pyram))
