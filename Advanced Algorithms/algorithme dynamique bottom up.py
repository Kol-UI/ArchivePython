def DPBUChange(S,X):
    track = [0]*(X+1)
    for x in range(1,X+1):
        mini = X
        for i in range(len(S)):
            if (S[i]<=x) and (1+track[x-S[i]]<mini):
                mini = 1+track[x-S[i]]
        track[x] = mini
    return track[X]
