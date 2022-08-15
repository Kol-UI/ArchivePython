# -*- coding: utf-8 -*-
 
import pygame, math, random
 
pygame.init() # initialisation du module "pygame"
 
fenetre = pygame.display.set_mode( (600,600) ) # Création d'une fenêtre graphique de taille 600x600 pixels
pygame.display.set_caption("Color Switch") # Définit le titre de la fenêtre
 
 
# On définit les variables qui contiendront les positions des différents éléments (vaisseau, alien, projectile)
# Chaque position est un couple de valeur '(x,y)'
positionDepart = (300,525)
projectile = (300,400)
CoordonneArc=(300,350)
vitesse=1
 
 
 
#On va créé les coordonné pour le triangle
zz=-100*(math.sqrt(3)-4)
Coor1=(200,400)
Coor2=(400,400)
Coor3=(300,zz)
r=336
a=300
b=400 - 100*math.sqrt(3)
tour=1
 
#on créé des variables pour les couleurs
 
red=(255,0,0)
jaune=(255, 228, 54)
bleu=(43, 250, 250)
violet=(121, 28, 248)
 
#On créé une liste où on ajoutera les couleurs
seq=[]
seq.append(red)
seq.append(jaune)
seq.append(red)
seq.append(bleu)
 
#On créé deux rectangle qui vont nous servir à détecter si les obstacles sont passés ou pas
rectObstacle=pygame.Rect(300,350,5,2)
rectObstacle2=pygame.Rect(300,50,5,5)
Couleur1=0
#On assigne au hasard une couleur au projectile
couleurProjectile = random.choice(seq)
couleurProjecilte = Couleur1
t=math.pi/40000
def triangle():
    global fenetre, projectile,red,bleu,jaune,violet,couleurProjectile,Coor1,Coor2,Coor3,r,a,b,t
    for a in range(0,100):
         pygame.draw.line(fenetre,red,Coor1,Coor2,5)
         pygame.draw.line(fenetre,jaune,Coor1,Coor3,5)
         pygame.draw.line(fenetre,bleu,Coor3,Coor2,5)
         Coor3 = [a + r*(math.cos(t)),b + r*(math.sin(t))]
         Coor2 = [a + r*(math.cos(2*math.pi/3 + t )),b + r*(math.sin(2*math.pi/3 + t))]
         Coor1 = [a + r*(math.cos(-2*math.pi/3 + t)),b + r*(math.sin(-2*math.pi/3 + t))]
         t = t - math.pi/40000000
# Fonction en charge de dessiner tous les éléments sur notre fenêtre graphique.
# Cette fonction sera appelée depuis notre boucle infinie
def dessiner():
    global fenetre, projectile, angle0, angle, angle1, angle2,angle3,angle4,angle5,red,bleu,jaune,violet,couleurProjectile,arc1,arc2,arc3,arc4,rect,couleurProjectile,Couleur1,rect,Coor1,Coor2,Coor3,r,a,b,tour
    # On remplit complètement notre fenêtre avec la couleur noire: (0,0,0)
    # Ceci permet de 'nettoyer' notre fenêtre avant de la dessiner
    fenetre.fill( (0,0,0) )
    if projectile != (-1, -1):
        pygame.draw.circle(fenetre, couleurProjectile , projectile, 5) # On dessine le projectile (un simple petit cercle)
       #On créé le 1er obstacle : Le cercle, pour cela on doit créé un rectangle
    rect=pygame.Rect(150,50,300,300)
    #Ensuite, on dessine les cercles à une certaines couleur, et on fait évoluer les angles dans la boucle
    triangle()
    pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières opérations de dessin
 
 
 
# Fonction en charge de gérer les évènements clavier (ou souris)
# Cette fonction sera appelée depuis notre boucle infinie
def gererClavierEtSouris():
    global continuer, positionDepart, projectile, vitesse,rect
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            continuer = 0
    # Gestion du clavier ainsi que du déplacement du projectile
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_SPACE] == True:
        projectile = (projectile[0], projectile[1] - 4)
        vitesse = 1
    else :
        projectile = (projectile[0], projectile[1] + vitesse)
        vitesse = vitesse  + int(0.9999999)
 
# On crée une nouvelle horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()
 
# La boucle infinie de pygame:
# On va continuellement dessiner sur l a fenêtre, gérer les évènements et calculer certains déplacements
continuer = 1
while continuer==1:
    # pygame permet de fixer la vitesse de notre:
    # ici on déclare 50 tours par secondes soit une animation à 50 images par secondes
    clock.tick(30)
    dessiner()
    gererClavierEtSouris()
 
 
   # On gère la fin de la partie, la détection du passage de l'obstacle et le changement de couleur
    if projectile[1] > 600:
        continuer=0
 
 
 
# A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()
