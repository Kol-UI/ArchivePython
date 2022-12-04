from Joueur import *
from Grille import *

class Jeu:
    def __init__(self, Board):
        self.__joueur1 = Joueur("Toto",Board)
        self.__joueur2 = Joueur("Titi",Board)
        self.__isOver = False
        self.__listeJoueurs = [self.__joueur1, self.__joueur2]
        self.__indexJoueur = 0

    #Méthode pour initaliser les bateaux puis lancer la boucle du jeu
    def start(self):
        for index, joueur in enumerate(self.__listeJoueurs):
            joueur.getGrille().afficher(index)
            joueur.getGrille().afficherGrilleTir(index)
        for index, joueur in enumerate(self.__listeJoueurs):
            if joueur.placerBateaux(index) == "QUIT":
                return

        #Boucle du jeu
        while not self.__isOver:
            if self.tourSuivant(self.__indexJoueur) == "QUIT":
                return
            self.__indexJoueur = not self.__indexJoueur #Permet de changer de joueur qui joue
            if self.__listeJoueurs[self.__indexJoueur].aPerdu():
                self.__isOver = True
                print("Joueur", self.__listeJoueurs[not self.__indexJoueur].getPseudo(), "a gagné !")

    def tourSuivant(self, index):
        ok = False
        print(self.__listeJoueurs[self.__indexJoueur].getPseudo(), ", insérez les coordonées de tir")
        while not ok:
            try:
                click = False
                while not click:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            return "QUIT"
                        elif event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                x, y = event.pos[0], event.pos[1]
                                if (self.__listeJoueurs[self.__indexJoueur].getGrille().getOffset() + index*self.__listeJoueurs[self.__indexJoueur].getGrille().getOffsetJoueur())< x < (self.__listeJoueurs[self.__indexJoueur].getGrille().getOffset() + self.__listeJoueurs[self.__indexJoueur].getGrille().getTailleCase() * Grille.largeur + index*self.__listeJoueurs[self.__indexJoueur].getGrille().getOffsetJoueur()):
                                    if (self.__listeJoueurs[self.__indexJoueur].getGrille().getOffset() + self.__listeJoueurs[self.__indexJoueur].getGrille().getOffsetJoueur()) < y < (self.__listeJoueurs[self.__indexJoueur].getGrille().getOffset() + self.__listeJoueurs[self.__indexJoueur].getGrille().getTailleCase() * Grille.longueur + self.__listeJoueurs[self.__indexJoueur].getGrille().getOffsetJoueur()):
                                        x -= self.__listeJoueurs[self.__indexJoueur].getGrille().getOffset() + index*self.__listeJoueurs[self.__indexJoueur].getGrille().getOffsetJoueur()
                                        x //= self.__listeJoueurs[self.__indexJoueur].getGrille().getTailleCase()
                                        y -= self.__listeJoueurs[self.__indexJoueur].getGrille().getOffset() + self.__listeJoueurs[self.__indexJoueur].getGrille().getOffsetJoueur()
                                        y //= self.__listeJoueurs[self.__indexJoueur].getGrille().getTailleCase()
                                        print(x,y)
                                        click = True
                #x = int(input())-1
                #y = int(input())-1
                if x > Grille.largeur or x < 0:
                    continue
                if y > Grille.largeur or y < 0:
                    continue

            except: continue

            if isinstance(self.__listeJoueurs[not self.__indexJoueur].getGrille().getCase((x,y)),Case):
                if not self.__listeJoueurs[not self.__indexJoueur].getGrille().getCase((x,y)).estTouche():
                    self.__listeJoueurs[not self.__indexJoueur].getGrille().getCase((x,y)).recevoirTir()
                    ok = True
            else:
                print("Réessayez, les coordonnées ne sont pas correctes !")
        self.__listeJoueurs[not self.__indexJoueur].getGrille().afficher(not self.__indexJoueur) #Affiche en mode normal
        self.__listeJoueurs[not self.__indexJoueur].getGrille().afficherGrilleTir(self.__indexJoueur) #Affiche en mode bateaux cachés
