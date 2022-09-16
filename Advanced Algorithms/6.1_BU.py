def DPBUCut1(p):
    n = len(p)
    track = [0]*(n+1)
    for l in range(1, n+1):
        maxi = 0
        for i in range(l):
            value = p[i] + track[l-i-1]
            if value > maxi:
                maxi = value
        track[l] = maxi
    return track[n]

def DPBUCut2(p):
    n = len(p)
    track = [0]*(n+1)
    keep = [0]*(n+1)
    for l in range(1, n+1):
        maxi = 0
        for i in range(l):
            value = p[i] + track[l-i-1]
            if value > maxi:
                maxi = value
                ind = i
        track[l] = maxi
        keep[l] = ind + 1
    i, L = n, []
    while i > 0:
        L.append(keep[i])
        i -= keep[i]
    return track[n], L            
    

p = [3, 5, 10, 12, 14]
#print(DPBUCut1(p))
print(DPBUCut2(p))
