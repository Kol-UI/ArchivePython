def tp2016Glouton(liste,ind,y):
    if ind==len(liste)-1:
        return liste[ind][y]
    else:
        if liste[ind+1][y]>liste[ind+1][y+1]:
            return liste[ind][y]+tp2016Glouton(liste,ind+1,y)
        else:
            return liste[ind][y]+tp2016Glouton(liste,ind+1,y+1)
        

liste=[[3],[5,4],[4,6,1],[2,5,3,8]]
print(tp2016Glouton(liste,0,0))
