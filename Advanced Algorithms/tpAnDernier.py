def tp1(long):
    if long==0:
        return 1
    else:
        total=0
        for i in range(4):
            if long>=(i+1):
                total+=tp1(long-(i+1))
        return total


#print(tp1(5))



def tpTopDownRec(long,track):
    if long==0:
        return 1
    elif track[long-1]>0:
        return track[long-1]
    else:
        total=0
        for i in range(4):
            if long>=(i+1):
                total+=tpTopDownRec(long-(i+1),track)              
                track[long-1]=total

        
        print(track)        
        return track[long-1]

def tpTopDown(long):
    track=[0]*long
    return tpTopDownRec(long,track)



#print(tpTopDown(5))



def tpButtonUp(long):
    track=[0]*(long+1)
    track[0]=1
    for i in range(1,long+1):
        total=0
        for j in range(1,5):
            if i>=j:
                total+=track[i-j]
        track[i]=total
        print(track)
    return track[long]
                
    
print(tpButtonUp(5))

