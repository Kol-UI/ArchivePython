
S=(1,2,5)
X=6

def recursiveChange(S,X):
    #print(S)
    #print(X)
    if X==0:
        return 0
    else:
        mini = X+1
        for i in range(len(S)):
            if S[i]<=X:
                nb = 1 + recursiveChange(S,X-S[i])
                if nb<mini:
                    mini = nb
        return mini
    #print(mini)

recursiveChange(S,X)
