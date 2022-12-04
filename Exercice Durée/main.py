from Cercle import *
from Duree import *

#moncercle = cercle(3,4,5)
#print(moncercle.perimetre())
#moncercle.afficherCoordonnees()

#moncercle.homothetie(0.5)
#moncercle.afficherCoordonnees()

maduree = duree(1, 20 , 20)
print(60 // 3600)
maduree.afficher_duree()

#print("durée en seconde de 1h30 = ",maduree.getSeconde(1,30,0),"s")


maduree.addSeconde(60)
maduree.afficher_duree()