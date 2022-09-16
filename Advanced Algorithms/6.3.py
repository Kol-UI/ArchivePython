# Récurrence naïve

def maximum(s):
    N,M=len(s),len(s[0])
    maxi=0
    for i in range(N):
        for j in range(M):
            if s[i][j]>maxi:
                maxi=s[i][j]
    return maxi
    

def recSubSquare(matrix,i,j):
    if (i==0) or (j==0):
        return matrix[i][j]
    elif matrix[i][j]==0:
        return 0
    else:
        return 1+min(recSubSquare(matrix,i,j-1),recSubSquare(matrix,i-1,j),recSubSquare(matrix,i-1,j-1))

def naiveSubSquare(matrix):
    N,M=len(matrix),len(matrix[0])
    s=[[0]*M for i in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(M-1,-1,-1):
            s[i][j]=recSubSquare(matrix,i,j)
    return maximum(s)
        
# DP Top Down

def recDPTDSubSquare(matrix,i,j,s):
    if s[i][j]>0:
        return s[i][j]
    if (i==0) or (j==0):
        s[i][j]=matrix[i][j]
        return s[i][j]
    elif matrix[i][j]==0:
        return 0
    else:
        s[i][j]=1+min(recDPTDSubSquare(matrix,i,j-1,s),recDPTDSubSquare(matrix,i-1,j,s),recDPTDSubSquare(matrix,i-1,j-1,s))
        return s[i][j]

def DPTDSubSquare(matrix):
    N,M=len(matrix),len(matrix[0])
    s=[[0]*M for i in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(M-1,-1,-1):
            s[i][j]=recDPTDSubSquare(matrix,i,j,s)
    return maximum(s)

# DP Bottom Up

def DPBUSubSquare1(matrix):
    N,M=len(matrix),len(matrix[0])
    s=[[0]*M for i in range(N)]
    for i in range(N):
        s[i][0]=matrix[i][0]
    for j in range(M):
        s[0][j]=matrix[0][j]
    for i in range(N):
        for j in range(M):
            if matrix[i][j]==0:
                s[i][j]=0
            else:
                s[i][j]=min(s[i-1][j],s[i][j-1],s[i-1][j-1])+1
    return maximum(s)

def maximum2(s):
    N,M=len(s),len(s[0])
    maxi,k,l=0,1,1
    for i in range(N):
        for j in range(M):
            if s[i][j]>maxi:
                maxi=s[i][j]
                k,l=i+1,j+1
    return maxi,k,l

def DPBUSubSquare2(matrix):
    N,M=len(matrix),len(matrix[0])
    s=[[0]*M for i in range(N)]
    for i in range(N):
        s[i][0]=matrix[i][0]
    for j in range(M):
        s[0][j]=matrix[0][j]
    for i in range(N):
        for j in range(M):
            if matrix[i][j]==0:
                s[i][j]=0
            else:
                s[i][j]=min(s[i-1][j],s[i][j-1],s[i-1][j-1])+1
    return maximum2(s)

mat=[[0,1,0,0,0,1],[1,0,1,1,1,1],[0,1,1,1,1,1],[0,0,1,1,1,0],[0,1,1,1,1,1]]
print(naiveSubSquare(mat))
print(DPTDSubSquare(mat))
print(DPBUSubSquare1(mat))
print(DPBUSubSquare2(mat))

    
