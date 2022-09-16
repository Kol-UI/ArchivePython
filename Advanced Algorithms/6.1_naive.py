def recCut1(p, n):
    if n == 0:
        return 0
    maxi = 0
    for i in range(n):
        v = p[i] + recCut1(p, n-i-1)
        if v > maxi:
            maxi = v
    return maxi


p = [3, 5, 10, 12, 14]
print(recCut1(p, len(p)))
