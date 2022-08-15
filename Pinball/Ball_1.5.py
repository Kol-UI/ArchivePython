from math import *
import pygame, sys, os
from pygame.locals import *
pygame.init()

NOIR = (0, 0, 0)
BLANC = (255,255,255)
taille = largeur, hauteur = 1280, 720
rayon_balle = 6
maSurface = pygame.display.set_mode(taille)
balle_vitesse  = [5, 5]
x,y=0,0

balle_x = 830
balle_y = 400
gravité = 0.05

largeur1 = [350,354,366,377,386,394,402,869,858,848,838,827,816,805,794,783,772,763,783,340,936,617,657,697,737,777,818,566,536,545,551,539,535,536,536,396,498,510,396,477,483,396,451,395,426,395,413,394,394,400,826,798,811,819,805,831,791,785,778,773,766,768,798,800,418,461,439,450,427,474,481,505,517,504,847,853,859,866,873,883,869,877,883,891,900,905,889,896,889,903,859,863,866,860,863,872,873,869,349,359,369,380,530,540,550,560,570,580,590,600,852,870,880,894,906,925,914,920,930,535,385,439,411,405,418,521,425,502,432,482,439,444,386,389,392,394,396,399,402]
largeur2 = [6,10,6,6,6,6,4,10,10,10,10,10,10,10,10,10,10,8,100,10,10,8,8,8,8,8,8,10,21,12,6,5,20,14,7,100,10,5,80,5,5,55,10,30,13,18,5,5,14,3,20,45,20,20,20,10,10,10,10,10,10,7,30,10,85,43,20,15,15,25,10,13,5,5,4,4,4,40,35,27,10,10,10,10,10,5,7,7,7,7,10,5,10,13,10,4,3,3,10,10,10,150,10,10,10,10,10,10,10,270,20,20,20,20,20,10,10,6,6,3,3,98,28,4,103,11,76,10,50,8,27,11,3,3,3,3,3,3,3]
hauteur1 = [271,290,303,323,339,354,366,595,601,606,611,615,619,623,627,631,635,639,639,0,0,120,105,90,90,105,120,240,132,121,115,126,161,168,176,630,636,639,620,624,626,608,614,596,601,580,591,552,573,567,499,546,526,514,536,493,556,566,576,587,596,607,581,590,122,88,105,96,112,78,73,93,97,109,324,318,309,307,348,351,296,287,277,267,257,250,355,362,380,361,428,421,446,439,449,467,482,467,52,46,38,31,30,27,24,21,18,15,12,12,23,28,39,50,61,72,72,83,103,184,95,271,282,277,284,284,295,295,305,306,316,322,250,253,257,260,264,267,270]
hauteur2 = [137,115,97,70,50,30,10,10,10,10,10,10,10,10,10,10,10,6,5,418,720,50,50,50,50,50,50,48,28,10,5,5,5,7,7,10,8,5,10,5,3,10,7,10,7,10,5,20,5,4,80,35,20,20,20,30,45,36,30,20,10,3,7,5,119,35,17,15,15,15,5,15,5,5,8,18,30,37,2,7,10,10,10,10,10,5,7,67,25,85,15,5,20,10,10,15,10,6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,30,10,10,10,100,154,12,-10,-5,10,5,10,5,10,5,5,6,3,3,3,3,3,3,3]

def rect(maSurface):
    pygame.draw.rect(maSurface, (100, 100, 100), (350, 271, 6, 137), 4)
    pygame.draw.rect(maSurface, (100, 100, 100), (354, 290, 10, 115), 4)
    pygame.draw.rect(maSurface, (100, 100, 100), (366, 303, 6, 97), 10)
    pygame.draw.rect(maSurface, (100, 100, 100), (377, 323, 6, 70), 7)
    pygame.draw.rect(maSurface, (100, 100, 100), (386, 339, 6, 50), 5)
    pygame.draw.rect(maSurface, (100, 100, 100), (394, 354, 6, 30), 5)
    pygame.draw.rect(maSurface, (100, 100, 100), (402, 366, 4, 10), 3)
    #triangle vert en bas à droite
    pygame.draw.rect(maSurface, (255, 255, 0), (869, 595, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (858, 601, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (848, 606, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (838, 611, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (827, 615, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (816, 619, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (805, 623, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (794, 627, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (783, 631, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (772, 635, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (763, 639, 8, 6), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (783, 639, 100, 5), 2)
    #les cotés
    pygame.draw.rect(maSurface, (255, 255, 0), (340, 0, 9, 418), 4)
    pygame.draw.rect(maSurface, (255, 255, 0), (936, 0, 9, 720), 2)
    #les lignes vertes
    pygame.draw.rect(maSurface, (255, 255, 0), (617, 120, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (657, 105, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (697, 90, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (737, 90, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (777, 105, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (818, 120, 8, 50), 3)
    #ligne rouge
    pygame.draw.rect(maSurface, (255, 255, 0), (566, 240, 10, 48), 3)
    #truc vert qui est en haut
    pygame.draw.rect(maSurface, (255, 255, 0), (536, 132, 21, 28), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (545, 121, 12, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (551, 115, 6, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (539, 126, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (535, 161, 20, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (536, 168, 14, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (536, 176, 7, 7), 3)
    #triangle vert en bas à gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (396, 630, 100, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (498, 636, 10, 8), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (510, 639, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (396, 620, 80, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (477, 624, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (483, 626, 5, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (396, 608, 55, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (451, 614, 10, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (395, 596, 30, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (426, 601, 13, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (395, 580, 18, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (413, 591, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (394, 552, 5, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (394, 573, 14, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (400, 567, 3, 4), 3)
    #truc bleu qui est en bas a droite
    pygame.draw.rect(maSurface, (255, 255, 0), (826, 499, 20, 80), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (798, 546, 45, 35), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (811, 526, 20, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (819, 514, 20, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (805, 536, 20, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (831, 493, 10, 30), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (791, 556, 10, 45), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (785, 566, 10, 36), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (778, 576, 10, 30), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (773, 587, 10, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (766, 596, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (768, 607, 7, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (798, 581, 30, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (800, 590, 10, 5), 3)
    #truc rouge qui est en haut
    pygame.draw.rect(maSurface, (255, 255, 0), (418, 122, 85, 119), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (461, 88, 43, 35), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (439, 105, 20, 17), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (450, 96, 15, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (427, 112, 15, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (474, 78, 25, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (481, 73, 10, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (505, 93, 13, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (517, 97, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (504, 109, 5, 5), 3)
    #triangles blancs sur la droite
    pygame.draw.rect(maSurface, (255, 255, 0), (847, 324, 4, 8), 2)
    pygame.draw.rect(maSurface, (255, 255, 0), (853, 318, 4, 18), 4)
    pygame.draw.rect(maSurface, (255, 255, 0), (859, 309, 4, 30), 4)
    pygame.draw.rect(maSurface, (255, 255, 0), (866, 307, 40, 37), 5)
    pygame.draw.rect(maSurface, (255, 255, 0), (873, 348, 35, 2), 5)
    pygame.draw.rect(maSurface, (255, 255, 0), (883, 351, 27, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (869, 296, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (877, 287, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (883, 277, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (891, 267, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (900, 257, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (905, 250, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (889, 355, 7, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (896, 362, 7, 67), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (889, 380, 7, 25), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (903, 361, 7, 85), 3)
    #truc rouge en bas a droite
    pygame.draw.rect(maSurface, (255, 255, 0), (859, 428, 10, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (863, 421, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (866, 446, 10, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (860, 439, 13, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (863, 449, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (872, 467, 4, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (873, 482, 3, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (869, 467, 3, 6), 3)
    #le plafond
    pygame.draw.rect(maSurface, (255, 255, 0), (349, 52, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (359, 46, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (369, 38, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (380, 31, 150, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (530, 30, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (540, 27, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (550, 24, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (560, 21, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (570, 18, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (580, 15, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (590, 12, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (600, 12, 270, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (852, 23, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (870, 28, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (880, 39, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (894, 50, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (906, 61, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (925, 72, 10, 30), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (914, 72, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (920, 83, 6, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (930, 103, 6, 10), 3)

    #truc vert en haut à gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (535, 184, 3, 100), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (385, 95, 3, 154), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (439, 271, 98, 12), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (411, 282, 28, -10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (405, 277, 4, -5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (418, 284, 103, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (521, 284, 11, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (425, 295, 76, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (502, 295, 10, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (432, 305, 50, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (482, 306, 8, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (439, 316, 27, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (444, 322, 11, 6), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (386, 250, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (389, 253, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (392, 257, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (394, 260, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (396, 264, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (399, 267, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (402, 270, 3, 3), 3)

    #trait blanc bas gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (338, 420, 5, 295), 3)

    #trait blanc à droite (lanceur)
    pygame.draw.rect(maSurface, (255, 255, 0), (909, 150, 2, 563), 3)




inProgress = True
temps = pygame.time.Clock()

def test_collision(rect):
   balle = pygame.Rect((balle_x - rayon_balle, balle_y - rayon_balle), (18, 18))
   if balle.colliderect(rect):
       return True
   else:
      return False

while inProgress:
    for event in pygame.event.get():
       if event.type == MOUSEBUTTONDOWN:
           x,y = event.pos
       if event.type == pygame.QUIT:
            inProgress = False
            
    maSurface.fill(NOIR)
    pygame.draw.circle(maSurface, BLANC, (floor(balle_x),floor(balle_y)), rayon_balle)
    rect(maSurface)
    balle_x = balle_x + balle_vitesse[0]
    balle_y = balle_y + balle_vitesse[1]
    balle_vitesse[1] = balle_vitesse[1] + gravité
    if (balle_y > hauteur):
        balle_vitesse[1] = balle_vitesse[1] * -0.05


    if balle_x + rayon_balle >= largeur:
        balle_x = largeur - rayon_balle
        balle_vitesse[0] = -balle_vitesse[0]
    else:
        if  balle_x < rayon_balle:
            balle_x = rayon_balle
            balle_vitesse[0] = -balle_vitesse[0]

    if balle_y + rayon_balle >= hauteur:
        balle_y = hauteur - rayon_balle
        balle_vitesse[1] = -balle_vitesse[1]
    else:
        if balle_y < rayon_balle:
            balle_y = rayon_balle
            balle_vitesse[1] = -balle_vitesse[1]

    for i in range(0,len(largeur1)):
        if test_collision(((largeur1[i],hauteur1[i]),(largeur2[i],hauteur2[i]))) == True:
            largeur3 = largeur1[i] + largeur2[i]
            hauteur3 = hauteur1[i] + hauteur2[i]
            if balle_x >= largeur1[i] -6  and balle_x <= largeur1[i] + 6 and balle_x + rayon_balle >= largeur1[i] and balle_x - rayon_balle <= largeur3:
                balle_vitesse[0] = -balle_vitesse[0]
            if balle_x >= largeur3 -6  and balle_x <= largeur3 +6 and balle_x + rayon_balle >= largeur1[i] and balle_x - rayon_balle <= largeur3:
                balle_vitesse[0] = -balle_vitesse[0]
            if balle_y >= hauteur1[i] -6 and balle_y <= hauteur1[i] +6 and balle_y + rayon_balle >= hauteur1[i] and balle_y - rayon_balle <= hauteur3:
                balle_vitesse[1] = -balle_vitesse[1]
            if balle_y >= hauteur3 -6   and balle_y <= hauteur3 +6  and balle_y + rayon_balle >= hauteur1[i] and balle_y - rayon_balle <= hauteur3:
                balle_vitesse[1] = -balle_vitesse[1]



    pygame.display.flip()
    temps.tick(60)

pygame.display.quit()
pygame.quit()


