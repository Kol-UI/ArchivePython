import random

#Classe dé à 6 faces
class De:
    
    nbDeFaces = 6
    
    def __init__(self):
        #Choisi aléatoirement une face de 1 à 6
        self.__faceVisible = random.randint(1,De.nbDeFaces)


    def lancer(self):
        #Retourne la face
        return self.__faceVisible


    def __str__(self):
        #Affiche le numéro de la face
        return str(De.lancer(self))



#Classe Joueur qui contient le nom et le score du joueur
class Joueur:

    #Définition du nom et du score
    def __init__(self, pseudo = "NULL", points = 0):
        self.__nom = pseudo
        self.__score = points


    #Retourne le nom
    def getNom(self):
        return self.__nom


    #Retourne le score   
    def getScore(self):
        return self.__score


    #Modifie le score
    def setScore(self, value):
        self.__score = self.__score + value
        


#Classe de l'environnement de jeu
class Jeu:
    
    #Définition du nombre de dés, du score pour gagner, de la liste des joueurs, de la liste des dés
    def __init__(self, nbDes = 3, scoreMini = 500):
        self.__nombreDeDes = nbDes
        self._listeJoueurs = []
        self._listeDes = []
        self.__scorePourGagner = scoreMini

        #Entrée du nom de chaque joueur
        nomJoueur1 = str(input("Nom du premier joueur : "))
        nomJoueur2 = str(input("Nom du deuxième joueur : "))
        print("\n\n")

        #Objet Joueur instancié dans la liste avec le nom donné
        self._listeJoueurs = [Joueur(nomJoueur1), Joueur(nomJoueur2)]

        #Attribut pour additionner les valeurs des dés et listes pour repérer si les dés sont identiques
        self.__total = 0
        self.__compare = []
        self.__compare2 = []


    #Objet Dé instancié dans la liste en fonction du nombre de dés 
    def lancer(self):
        self._listeDes = [De() for i in range(self.__nombreDeDes)]


    #Affiche chaque dé de la liste
    def affichageLancer(self):
        n = 1
        for i in self._listeDes:
            print("Dé", n, ":", i)
            n += 1


    #Additionne chaque valeur pour chaqué dé à un total et le retourne
    def scoreDuLancer(self):
        self.__total = 0
        for i in self._listeDes:
            self.__total = self.__total + i.lancer()
            
        return self.__total


    #Crée une liste composée de la valeur du 1er dé répétée pour chaque dé, va comparer avec une autre
    #liste contenant les vraies valeurs pour les autres dés. Si les listes sont identiques c'est que les
    #valeurs pour tous les dés sont identiques entre elles
    def desIdentiques(self):
        self.__compare = [self._listeDes[0].lancer() for i in range(self.__nombreDeDes)]
        self.__compare2 = [self._listeDes[i].lancer() for i in range(self.__nombreDeDes)]
        
        if self.__compare == self.__compare2:
            return True
        else:
            return False


    #Fonction générale de jeu : va appeler la fonction tourDeJeu() tant que l'un des 2 joueurs n'aura pas gagné
    def partie(self):
        while 1:
            jouer.tourDeJeu()
            input()

            if self._listeJoueurs[0].getScore() >= self.__scorePourGagner:
                print(self._listeJoueurs[0].getNom(), "a gagné !")
                break

            elif self._listeJoueurs[1].getScore() >= self.__scorePourGagner:
                print(self._listeJoueurs[1].getNom(), "a gagné !")
                break
    


#Classe pour le jeu Zanzibar
class Zanzibar(Jeu):

    #3 dés, score pour gagner de 500, score au tour fixé à 0, appelle la classe Jeu, jeton de tour pour savoir à qui le tour    
    def __init__(self):
        self.__des = 3
        self.__score = 500
        self.__total = 0

        Jeu.__init__(self, self.__des, self.__score)

        self.__aQui = 0


    #Va additionner le score pour chaque dé : + 100 si 1, + 60 si 6 sinon + la valeur de la face du dé
    def scoreDuLancer(self):
        self.__total = 0
        for i in self._listeDes:
            if i.lancer() == 1:
                self.__total = self.__total + 100
            elif i.lancer() == 6:
                self.__total = self.__total + 60
            else:
                self.__total = self.__total + i.lancer()
                
        return self.__total


    #Affiche et appelle les méthodes, modifie le score du joueur en additionnant avec celui du tour
    def tourDeJeu(self):
        print("A", self._listeJoueurs[self.__aQui].getNom(), "de jouer !")
        jouer.lancer()
        jouer.affichageLancer()
        print("Score du lancer :", jouer.scoreDuLancer())
        self._listeJoueurs[self.__aQui].setScore(jouer.scoreDuLancer())
        print("Score total :", self._listeJoueurs[self.__aQui].getScore())

        #Si le joueur 1 joue, c'est au tour du joueur 2 ; Si le joueur 2 joue, c'est au tour du joueur 1
        if self.__aQui == 0:
            self.__aQui = 1
        else:
            self.__aQui = 0



#Classe pour le jeu Sept
class Sept(Jeu):

    #2 dés, score pour gagner de 200, score provisoire au tour fixé à 0, indice multiplicateur du score selon si un double a été effectué avant,
    #appelle la classe Jeu, jeton de tour pour savoir à qui le tour
    def __init__(self):
        self.__des = 2
        self.__score = 200
        self.__pointAuTour = 0
        self.__doubleOuPas = 1

        Jeu.__init__(self, self.__des, self.__score)

        self.__aQui = 0


    #Affiche et appelle les méthodes
    def tourDeJeu(self):
        self.__pointAuTour = 0
        print("A", self._listeJoueurs[self.__aQui].getNom(), "de jouer !")
        
        while 1:
            jouer.lancer()
            jouer.affichageLancer()
            print("Score du lancer :", jouer.scoreDuLancer())
            
            #Si le joueur fait un total de 7, passe le tour et supprime son score au tour
            if jouer.scoreDuLancer() == 7:
                self.__pointAuTour = 0
                break

            #Sinon additionne au score du tour les points effectués avec ou non un coefficient multiplicateur selon si un double a été effectué
            #au tour précédent
            else:
                self.__pointAuTour = self.__pointAuTour + (jouer.scoreDuLancer() * self.__doubleOuPas)
                #Coefficient remis à 1
                self.__doubleOuPas = 1
                print("Total provisoire du tour :", self.__pointAuTour)
                #Choix de continuer si oui fixe le coefficient à 2 si les dés sont identiques, sinon le laisse à 1 ; sinon passe la main
                suivant = int(input("Saisir 0 pour arrêter ou 1 pour continuer : "))
                if suivant == 1:
                    if jouer.desIdentiques() == True:
                        self.__doubleOuPas = 2
                    continue
                else:
                    break

        #Additionne les points du tour au score du joueur    
        self._listeJoueurs[self.__aQui].setScore(self.__pointAuTour)
        print("Total du tour :", self.__pointAuTour)
        print("Score total :", self._listeJoueurs[self.__aQui].getScore())

        #Si le joueur 1 joue, c'est au tour du joueur 2 ; Si le joueur 2 joue, c'est au tour du joueur 1
        if self.__aQui == 0:
            self.__aQui = 1
        else:
            self.__aQui = 0


#Choix du jeu et initialisation
lequel = int(input("Saisir 0 pour le 'Zanzibar' ou 1 pour le 'Sept' : "))

if lequel == 0:
    jouer = Zanzibar()
else:  
    jouer = Sept()
    
jouer.partie()
    

