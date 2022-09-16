def tp2(x,y,tableau,total):
    total+=tableau[x][y]
    if x==0 and y==0:
        return total
    elif x-1<0:
        return tp2(x,y-1,tableau,total)
    elif y-1<0:       
        return tp2(x-1,y,tableau,total)
    else:
        return min(tp2(x-1,y,tableau,total),tp2(x,y-1,tableau,total))
        


#tableau=[[2,3,1,1,6],[1,4,4,1,4],[7,1,2,2,5],[2,1,3,8,3],[2,4,3,2,1]]
#print(tp2(len(tableau)-1,len(tableau)-1,tableau,0))




def tp2TopDownRec(x,y,tableau,total,track):
    print(track)
    total+=tableau[x][y]
    if track[len(tableau)-1-x][len(tableau)-1-y]!=0 and total>track[len(tableau)-1-x][len(tableau)-1-y]:
        return track[len(tableau)-1-x][len(tableau)-1-y]
    track[len(tableau)-1-x][len(tableau)-1-y]=total
    if x==0 and y==0:
        return track[x][y]
    elif x-1<0:
        return tp2TopDownRec(x,y-1,tableau,total,track)
    elif y-1<0:       
        return tp2TopDownRec(x-1,y,tableau,total,track)
    else:
        return min(tp2TopDownRec(x-1,y,tableau,total,track),tp2TopDownRec(x,y-1,tableau,total,track))


def tp2TopDown(x,y,tableau,total):
    track=[ [0  for j in range (len(tableau))] for i in range(len(tableau))] 
    return tp2TopDownRec(x,y,tableau,total,track)


tableau=[[2,3,1,1,6],[1,4,4,1,4],[7,1,2,2,5],[2,1,3,8,3],[2,4,3,2,1]]
print(tp2TopDown(len(tableau)-1,len(tableau)-1,tableau,0))
