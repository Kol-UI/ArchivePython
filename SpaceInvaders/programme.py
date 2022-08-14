import pygame
from pygame.locals import *
import pygame.mixer
pygame.init()

# Reglages additionels de PyGame
pygame.key.set_repeat(1,5) # Repetion des touches de clavier pour aider au placement des bateaux
pygame.time.Clock().tick(120) # Limiter le nombre de boucles

# Ouverture d'une fenetre Pygame
taille = largeur, hauteur = 1024,768
pygame.display.set_caption("SPACE SHOOTER")
ecran = pygame.display.set_mode((taille),FULLSCREEN)

# Import des images et creation des "Rects" associes
fond = pygame.image.load("images/fond.png")
ennemi = pygame.image.load("images/ennemi.png")
ennemi_rect = ennemi.get_rect()
vaisseau = pygame.image.load("images/vaisseau.png")
vaisseau = pygame.transform.scale(vaisseau, (100, 100))
vaisseau_rect = vaisseau.get_rect()
alien = pygame.image.load("images/alien.png")
alien_rect = alien.get_rect()

# Initialisation des variables necessaires
continuer, left, up, right, down, shot = 1,0,0,0,0,0
vaisseau_rect = vaisseau_rect.move(462,600)
pos_tirs = []
aliens = [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
decalage, godroite, decalageY = 1,1,0

# Programme Pricipal
while continuer==1 :
    for event in pygame.event.get():
        if event.type==QUIT : # Si le Joueur ferme la fenetre
            continuer = 0
        if event.type==KEYDOWN : # Si le Joueur Appuie sur une Touche
            if event.key==K_ESCAPE :
                continuer = 0
            if event.key==K_LEFT :
                left = 1
            if event.key==K_UP :
                up = 1
            if event.key==K_RIGHT :
                right = 1
            if event.key==K_DOWN :
                down = 1
            if event.key==K_SPACE and shot==0 :
                if len(pos_tirs)<1 :
                    pos_tirs.append([vaisseau_rect.left+48,vaisseau_rect.top-25])
                    shot = 1
        if event.type==KEYUP : # Si le Joueur Relache sur une Touche
            if event.key==K_LEFT :
                left = 0
            if event.key==K_UP :
                up = 0
            if event.key==K_RIGHT :
                right = 0
            if event.key==K_DOWN :
                down = 0
            if event.key==K_SPACE :
                shot = 0
    if vaisseau_rect.left>0 :
        vaisseau_rect = vaisseau_rect.move(-10*left,0)
    if vaisseau_rect.top>0 :
        vaisseau_rect = vaisseau_rect.move(0,-10*up)
    if vaisseau_rect.right<1024 :
        vaisseau_rect = vaisseau_rect.move(10*right,0)
    if vaisseau_rect.bottom<768 :
        vaisseau_rect = vaisseau_rect.move(0,10*down)
    ecran.blit(fond,(0,0))
    ecran.blit(vaisseau,vaisseau_rect)
    if decalage==150 or decalage ==-150:
        godroite*=-1
        decalageY+=40
    decalage+=godroite
    gagne=1
    for i in range(3) :
        for j in range(8) :
            if aliens[i][j]==1 :
                gagne=0
                if (j*90+150+decalage)<vaisseau_rect.right and vaisseau_rect.left<(j*90+220+decalage) and (i*90+50+decalageY)<vaisseau_rect.bottom and vaisseau_rect.top<(i*90+120+decalageY) :
                    print("PERDU !")
                    continuer = 0
                for k in pos_tirs :
                    if (j*90+150+decalage)<k[0]<(j*90+220+decalage) and (i*90+50+decalageY)<k[1]<(i*90+120+decalageY) :
                        aliens[i][j]=0
                        pos_tirs.remove(k)
                ecran.blit(alien,((j*90)+150+decalage,(i*90)+50+decalageY))
    if gagne==1 :
        print("GAGNE !")
        continuer = 0
    for i in pos_tirs :
        i[1]-=10
        if i[1]<-20 :
            pos_tirs.remove(i)
        pygame.draw.circle(ecran,(255,0,0),i,10)
    pygame.display.flip()
pygame.quit()