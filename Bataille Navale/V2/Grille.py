from Case import *
from Bateau import *
import pygame
from pygame.locals import *

class Grille :
    """classe grille"""
    largeur = 0
    longueur = 0

    def __init__(self, largeur, longueur, surface):
        Grille.largeur = largeur
        Grille.longueur = longueur
        self.__plateau = [[Case((i,j)) for i in range (largeur)] for j in range (longueur)]
        self.__bateaux = []
        self.__surface = surface
        self.__offset = 50
        self.__taillecase = 40
        self.__offsetJoueur = (2 * self.__offset + self.__taillecase*Grille.largeur)

    def afficher(self,indexJoueur):
        for j, ligne in enumerate(self.__plateau) :
            for i, case in enumerate(ligne) :
                pygame.draw.rect(self.__surface, (0,0,0), (self.__offset + i*self.__taillecase  + indexJoueur*self.__offsetJoueur, self.__offset + j * self.__taillecase, self.__taillecase,self.__taillecase), 1)
                if case.possedeBateau():
                    font = pygame.font.SysFont("arial", 25, "bold")
                    text = font.render(case.getBateau().getInitiale(), 1, (0,0,0))
                    if case.estTouche():
                        pygame.draw.rect(self.__surface, (255,50,50), (self.__offset+1 + i*self.__taillecase + indexJoueur*self.__offsetJoueur, self.__offset+1 + j * self.__taillecase, self.__taillecase-2, self.__taillecase-2))
                    else:
                        pygame.draw.rect(self.__surface, (110,110,250), (self.__offset+1 + i*self.__taillecase + indexJoueur*self.__offsetJoueur, self.__offset+1 + j * self.__taillecase, self.__taillecase-2, self.__taillecase-2))
                    self.__surface.blit(text, (self.__offset+10 + i*self.__taillecase + indexJoueur*self.__offsetJoueur, self.__offset + 5 + j*self.__taillecase))
                else:
                    if case.estTouche():
                        pygame.draw.rect(self.__surface, (0,0,255), (self.__offset+1 + i*self.__taillecase + indexJoueur*self.__offsetJoueur, self.__offset+1 + j * self.__taillecase, self.__taillecase-2, self.__taillecase-2))
                    else:
                        pygame.draw.rect(self.__surface, (255,255,255), (self.__offset+1 + i*self.__taillecase + indexJoueur*self.__offsetJoueur, self.__offset+1 + j * self.__taillecase, self.__taillecase-2, self.__taillecase-2))
        pygame.display.update()
        pygame.event.clear()

    def afficherGrilleTir(self,indexJoueur):
        for j, ligne in enumerate(self.__plateau) :
            for i, case in enumerate(ligne) :
                pygame.draw.rect(self.__surface, (0,0,0), (self.__offset + i*self.__taillecase  + indexJoueur*self.__offsetJoueur, self.__offset + j * self.__taillecase + self.__offsetJoueur, self.__taillecase,self.__taillecase), 1)
                if case.estTouche():
                    if case.possedeBateau():
                        pygame.draw.rect(self.__surface, (255,0,0), (self.__offset+1 + i*self.__taillecase + indexJoueur*self.__offsetJoueur, self.__offset+1 + j * self.__taillecase + self.__offsetJoueur, self.__taillecase-2, self.__taillecase-2))
                    else:
                        pygame.draw.rect(self.__surface, (0,0,255), (self.__offset+1 + i*self.__taillecase + indexJoueur*self.__offsetJoueur, self.__offset+1 + j * self.__taillecase + self.__offsetJoueur, self.__taillecase-2, self.__taillecase-2))
                else:
                    pygame.draw.rect(self.__surface, (255,255,255), (self.__offset+1 + i*self.__taillecase + indexJoueur*self.__offsetJoueur, self.__offset+1 + j * self.__taillecase + self.__offsetJoueur, self.__taillecase-2, self.__taillecase-2))
        pygame.display.update()
        pygame.event.clear()

    def getCase(self,position):
        if (position[0]+1) > Grille.longueur or (position[1]+1) > Grille.largeur :
            return False
        return self.__plateau[position[1]][position[0]]

    def getBateaux(self):
        return self.__bateaux

    def getOffset(self):
        return self.__offset

    def getTailleCase(self):
        return self.__taillecase

    def getOffsetJoueur(self):
        return self.__offsetJoueur

    def placerBateau(self,bateau):
        bateau.placerBateauSurLaGrille()

    #Méthode qui permet de savoir si on peut placer un bateau à la position donnée
    def peutPlacerBateau(self,bateau):
        if bateau.estVertical():
            #Bateau vertical
            for i in range(bateau.getTaille()):
                positionSuivante = (bateau.getPosition()[0],(bateau.getPosition()[1])+i)
                if not isinstance(self.getCase(positionSuivante),Case) or self.getCase(positionSuivante).possedeBateau():
                    return False
        else:
            #bateau Horizontal
            for i in range(bateau.getTaille()):
                positionSuivante = ((bateau.getPosition()[0])+i,bateau.getPosition()[1])
                if not isinstance(self.getCase(positionSuivante),Case) or self.getCase(positionSuivante).possedeBateau():
                    return False
        return True



    def ajouterBateau(self,bateau):
        bateau.placerBateauSurLaGrille()
        self.__bateaux.append(bateau)
