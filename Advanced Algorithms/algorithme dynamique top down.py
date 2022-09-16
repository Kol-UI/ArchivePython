def DPTDChangeRec(S,X,trac):
    if X==0:
        return 0
    elif track[X]>0:
        return track[X]
    else:
        mini = X+1
        for i in range(len(S)):
            if S[i]<=X:
                nb=1+DPTDChangeRec(S,X-S[i],track)
                if nb<mini:
                    mini = nb
                    track[X] = mini
        return mini

def DPTDChange(S,X):
    track = [0]*(X+1)
    return DPTDChangeRec(S,X,track)

S=(1,2,5,10)
print(DPTDChange(S,11))
