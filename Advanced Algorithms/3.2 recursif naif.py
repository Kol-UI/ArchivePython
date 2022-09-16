S = [6,5,2,7,3,5]
sommeMaxJoueur1 = [0]

def recurrence(S,n,sommeMaxJoueur1):
	while mini != 0:
		mini = n-1
		for i in range(len(S)):
			for j in range(len(S)):
				if S[i] & S[j]<= n:
                                        sommeMaxJoueur1.append(S[i][j])
                                        scoreJoueur1 = sum(sommeMaxJoueur1)
					nb = 1 + recurrence(S,mini-S[i][j])
					if nb < mini:
						mini = nb
	if mini == 0:
            print("Score max: ", scoreJoueur1)
	    return 0

recurrence(S,n,sommeMaxJoueur1)


// Calcul de complexité: 5 + 3*3*(3+4+2)
