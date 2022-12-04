from Grille import *
from Porteavions import *
from Destroyer import *
from Croiseur import *
from Sousmarin import *
from Torpilleur import *
import pygame
from pygame.locals import *


class Joueur:

    def __init__(self,pseudo,Board):
        self.__pseudo = pseudo
        self.__grille = Grille(10,10,Board)

    def getGrille(self):
        return self.__grille

    def getPseudo(self):
        return self.__pseudo

    def aPerdu(self):
        for bateau in self.__grille.getBateaux():
            if not bateau.estCoule():
                return False
        return True

    def placerBateaux(self,index):
        listeBateaux = ["Porte Avions", "Croiseur", "Destroyer", "Sous-marin", "Torpilleur"]
        for i in listeBateaux:
            ok = False
            print(self.getPseudo(),", veuillez placer votre " + i + ".")
            while not ok:
                try:
                    click = False
                    while not click:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                return "QUIT"
                            elif event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    x, y = event.pos[0], event.pos[1]
                                    if (self.getGrille().getOffset() + index*self.getGrille().getOffsetJoueur())< x < (self.getGrille().getOffset() + self.getGrille().getTailleCase() * Grille.largeur + index*self.getGrille().getOffsetJoueur()):
                                        if self.getGrille().getOffset() < y < self.getGrille().getOffset() + self.getGrille().getTailleCase() * Grille.longueur:
                                            x -= self.getGrille().getOffset() + index*self.getGrille().getOffsetJoueur()
                                            x //= self.getGrille().getTailleCase()
                                            y -= self.getGrille().getOffset()
                                            y //= self.getGrille().getTailleCase()
                                            click = True
                    click = False
                    while not click:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                return "QUIT"
                            elif event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    x1, y1 = event.pos[0], event.pos[1]
                                    if (self.getGrille().getOffset() + index*self.getGrille().getOffsetJoueur())< x1 < (self.getGrille().getOffset() + self.getGrille().getTailleCase() * Grille.largeur + index*self.getGrille().getOffsetJoueur()):
                                        if self.getGrille().getOffset() < y1 < self.getGrille().getOffset() + self.getGrille().getTailleCase() * Grille.longueur:
                                            x1 -= self.getGrille().getOffset() + index*self.getGrille().getOffsetJoueur()
                                            x1 //= self.getGrille().getTailleCase()
                                            y1 -= self.getGrille().getOffset()
                                            y1 //= self.getGrille().getTailleCase()
                                            if x1 == (x+1) and y1 == y:
                                                isVertical = 0
                                                click = True
                                            elif x1 == x and y1 == (y+1):
                                                isVertical = 1
                                                click = True

                except:
                    continue
                print(x,y)
                if i == "Porte Avions":
                     bateauDuJoueur = Porteavions(self.__grille,(x,y),isVertical)
                elif i == "Destroyer":
                    bateauDuJoueur = Destroyer(self.__grille,(x,y),isVertical)
                elif i == "Croiseur":
                    bateauDuJoueur = Croiseur(self.__grille,(x,y),isVertical)
                elif i == "Sous-marin":
                    bateauDuJoueur = Sousmarin(self.__grille,(x,y),isVertical)
                elif i == "Torpilleur":
                    bateauDuJoueur = Torpilleur(self.__grille,(x,y),isVertical)

                if self.__grille.peutPlacerBateau(bateauDuJoueur):
                    self.__grille.ajouterBateau(bateauDuJoueur)
                    self.__grille.afficher(index)
                    ok = True
                else:
                    print("Réessayez")
        return
