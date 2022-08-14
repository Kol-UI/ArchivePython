# Créé par herves, le 28/09/2017 en Python 3.2
name=input("Monsieur, comment dois-je vous appeler ?")
print("Bonjour" ,name, "et bienvenue en finale du Juste Prix ! Dans notre vitrine aujourd'hui, un voyage paradisiaque, une voiture de luxe et une cuisine toute équipée !")
from random import *
nombre1=randrange(10000,50000)
essai=int(input("Voici votre nombre d'essais :"))
k=1
nombre2=int(input("Entrez un nombre quelconque entre 10000 et 50000"))
while (nombre2 != nombre1) and k<essai:
    if nombre2 < nombre1 :
        print("C'est plus.")
    if nombre2 > nombre1 :
        print("C'est moins.")
    k=k+1
    nombre2=int(input("Entrez un nombre quelconque entre 10000 et 50000"))
if k==essai and nombre2 != nombre1 :
    print("C'est perdu, dommage vous restez au RSA" ,name, "! Il fallait deviner le prix de",nombre1,"euros... Vous nous devez désormais un million de dollars :D")
else :
    print("C'est gagné ! Oui oui oui oui",name,", vous avez la vitrine qui était en effet de ",nombre1,"euros ! Le voyage en Lituanie en colonie de vacances -2 étoiles, la Fiat Multipla et la cuisine qui en réalité n'est qu'une casserole !")

print("Vous avez atteint les ",k,"essais. Vous aviez en tout",essai,"essais.")



