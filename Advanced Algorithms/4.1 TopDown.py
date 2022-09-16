S = [6,5,2,7,3,5]
sommeMaxJoueur1 = [0]

def topDown(S, n, sommeMaxJoueur1):
    if n == 0:
        return 0
    elif track[n]>0:
        return track[n]
    elif mini == 0:
        print("Score max: ", scoreJoueur1)
        return 0
    else:
        mini = n-1
        for i in range(len(S)):
            for j in range(len(S)):
                if S[i] & S[j] <= n:
                    sommeMaxJoueur1.append(S[i][j])
                    scoreJoueur1 = sum(sommeMaxJoueur1)
                    nb = 1 + topDown(S, mini-S[i][j])
                    if nb < mini:
                        mini = nb
                        track[n] = mini
            return mini

topDown(S,n,sommeMaxJoueur1)

