def recDistance(word1,word2,m,n):
    if m==0:
        return n
    elif n==0:
        return m
    elif word1[m-1]==word2[n-1]:
        return recDistance(word1,word2,m-1,n-1)
    else:
        return 1+min(recDistance(word1,word2,m,n-1),recDistance(word1,word2,m-1,n),
                     recDistance(word1,word2,m-1,n-1))

def naiveDistance(word1,word2):
    return recDistance(word1,word2,len(word1),len(word2))


def DPTDdistanceRec(word1,word2,m,n,track):
    if track[m][n]>0:
        return track[m][n]
    if m==0:
        track[m][n]=n
        return n
    elif n==0:
        track[m][n]=m
        return m
    elif word1[m-1]==word2[n-1]:
        track[m][n]= DPTDdistanceRec(word1,word2,m-1,n-1,track)
        return track[m][n]
    else:
        track[m][n] = 1+min(DPTDdistanceRec(word1,word2,m,n-1,track),DPTDdistanceRec(word1,word2,m-1,n,track),
                     DPTDdistanceRec(word1,word2,m-1,n-1,track))
        return track[m][n]

def DPTDdistance(word1,word2):
    track = [[0]*(len(word2)+1) for x in range(len(word1)+1)]
    return DPTDdistanceRec(word1,word2,len(word1),len(word2),track)
    


def DPBUdistance1(word1,word2):
    m,n=len(word1),len(word2)
    track = [[0]*(n+1) for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                track[i][j] = j    
            elif j == 0:
                track[i][j] = i    
            elif word1[i-1]==word2[j-1]:
                track[i][j] = track[i-1][j-1]
            else:
                track[i][j] = 1 + min(track[i][j-1],track[i-1][j],track[i-1][j-1])
    return track[m][n]
    


def DPBUdistance2(word1,word2):
    m,n=len(word1),len(word2)
    track = [[0]*(n+1) for x in range(m+1)]
    keep = [['.']*(n+1) for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                track[i][j] = j
                keep[i][j] = 'm'
            elif j == 0:
                track[i][j] = i
                keep[i][j] = 'm'
            elif word1[i-1]==word2[j-1]:
                track[i][j] = track[i-1][j-1]
                keep[i][j] = 'n'
            else:
                if track[i][j-1]<min(track[i-1][j],track[i-1][j-1]):
                    track[i][j] = 1 + track[i][j-1]
                    keep[i][j] = 'i'
                elif track[i-1][j]<min(track[i][j-1],track[i-1][j-1]):
                    track[i][j] = 1 + track[i-1][j]
                    keep[i][j] = 's'
                else:
                    track[i][j] = 1 + track[i-1][j-1]
                    keep[i][j] = 'm'
    mm,nn=m,n
    L=[]
    for k in range(max(m,n)):
        L.append(keep[mm][nn])
        if (keep[mm][nn]=='m') or (keep[mm][nn]=='n'):
            mm,nn=mm-1,nn-1
        elif keep[mm][nn]=='i':
            nn-=1
        else:
            mm-=1            
    return track[m][n],L

print(naiveDistance("durite","carie"))
print(DPTDdistance("durite","carie"))
print(DPBUdistance1("durite","carie"))
print(DPBUdistance2("carie","durite"))

