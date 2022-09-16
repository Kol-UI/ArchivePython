def barreNaif(prixVente,longueur):
    if longueur==0:
        return 0
    else:
        maxi = 0
        for i in range(longueur):
            val=prixVente[i]+barreNaif(prixVente,longueur-(i+1))
            if maxi<val:
                maxi=val      
        return maxi


longueur=5
prixVente=[3,5,10,12,14]

#print(barreNaif(prixVente,longueur))
    
    

#########################################


def barreTopDownRec(prixVente,longueur,track):
    print(track)
    if longueur==0:
        return 0
    elif track[longueur-1]>0:
        return track[longueur-1]
    else:
        for i in range(longueur):
            val=prixVente[i]+barreTopDownRec(prixVente,longueur-(i+1),track)
            if track[longueur-1]<val:
                track[longueur-1]= val
        
        return track[longueur-1]

def barreTopDown(prixVente,longueur):
    track=[0]*longueur
    return barreTopDownRec(prixVente,longueur,track)

longueur=5
prixVente=[3,5,10,12,14]
print(barreTopDown(prixVente,longueur))
