import pygame, sys, os
from pygame.locals import *
pygame.init()


def Game_Commun(maSurface):
    pygame.draw.line(maSurface, (255, 255, 255), (340, 0), (340, 720), 5)
    pygame.draw.line(maSurface, (255, 255, 255), (940, 0), (940, 720), 5)

    pygame.draw.line(maSurface, (255, 255, 255), (0, 0), (0, 720), 5)

def Game_Center(maSurface):
    pygame.draw.line(maSurface, (255, 255, 255), (885, 589), (940, 589), 2)  # ligne horizontale contenant le ressort
    pygame.draw.line(maSurface, (25, 255, 255), (885, 589), (885, 720), 3)  # ligne verticale contenant le ressort

    pygame.draw.line(maSurface, (255, 255, 255), (345, 0), (345, 410), 10)    #Ligne en gras à gauche
    pygame.draw.line(maSurface, (255, 255, 255), (940, 0), (940, 720), 11)    #Ligne en gras à droite
    pygame.draw.line(maSurface, (255, 255, 255), (342, 415), (405, 370), 10)  #Triangle gauche
    pygame.draw.line(maSurface, (255, 255, 255), (400, 370), (342, 260), 10)  #Triangle Gauche
    pygame.draw.line(maSurface, (50, 100, 255), (910, 150), (910, 720), 3)  # Barre bleu d'ejection de la bille
    pygame.draw.arc(maSurface, (255, 255, 255), (660, 10, 285, 275), 0, 1.45, 10)  #Arc en haut à droite
    pygame.draw.line(maSurface, (255, 255, 255), (600, 16), (825, 16), 10)  # Barre haute horizontale à gauche de l'arc
    pygame.draw.line(maSurface, (255, 255, 255), (530, 35), (600, 16), 10)  # Barre haute à gauche en diagonal centrer
    pygame.draw.line(maSurface, (255, 255, 255), (380, 35), (530, 35), 10)  # Barre haute à gauche horizontale
    pygame.draw.line(maSurface, (255, 255, 255), (342, 70), (380, 35), 10)  # Barre haute à gauche en diagonal
    pygame.draw.line(maSurface, (255, 0, 0), (385, 95), (385, 250), 3)    #Ligne en haut à gauche
    pygame.draw.line(maSurface, (255, 0, 0), (445, 330), (385, 250), 3)  #Triangle Gauche objet
    pygame.draw.line(maSurface, (255, 0, 0), (535, 285), (445, 330), 3)  # Triangle Gauche objet
    pygame.draw.line(maSurface, (255, 0, 0), (535, 285), (535, 130), 3)    #Ligne verticale en haut à droite de l'objet
    pygame.draw.line(maSurface, (255, 0, 0), (400, 270), (535, 270), 3)    #Ligne horizontale en haut centrale objet
    pygame.draw.line(maSurface, (255, 0, 0), (555, 113), (535, 130), 3)    #Ligne diagonale en haut à droite de l'objet
    pygame.draw.line(maSurface, (255, 0, 0), (555, 113), (555, 160), 3)    #Ligne Verticale en haut à droite objet gauche
    pygame.draw.line(maSurface, (255, 0, 0), (555, 160), (535, 190), 3)  # Ligne diagonale en haut à droite de l'objet

    pygame.draw.line(maSurface, (255, 255, 0), (418, 120), (418, 240), 3)    #Ligne verticale en haut à gauche objet gauche
    pygame.draw.line(maSurface, (255, 255, 0), (502, 120), (502, 240), 3)    #Ligne Verticale en haut à droite objet gauche
    pygame.draw.line(maSurface, (255, 255, 0), (418, 240), (502, 240), 3)    #Ligne horizontale en haut centrale objet
    pygame.draw.line(maSurface, (255, 255, 0), (525, 99), (502, 120), 3)    #Ligne diagonale en haut à droite de l'objet
    pygame.draw.line(maSurface, (255, 255, 0), (418, 120), (486, 69), 3)    #Ligne diagonale en haut à gauche de l'objet
    pygame.draw.line(maSurface, (255, 255, 0), (525, 99), (486, 69), 3)  # Ligne diagonale en haut au milieu de l'objet

    pygame.draw.line(maSurface, (0, 224, 2), (620, 120), (620, 170), 8)  # Ligne verticale en haut 1
    pygame.draw.line(maSurface, (0, 224, 2), (660, 105), (660, 155), 8)  # Ligne verticale en haut 2
    pygame.draw.line(maSurface, (0, 224, 2), (700, 90), (700, 140), 8)  # Ligne verticale en haut 3
    pygame.draw.line(maSurface, (0, 224, 2), (740, 90), (740, 140), 8)  # Ligne verticale en haut 4
    pygame.draw.line(maSurface, (0, 224, 2), (780, 105), (780, 155), 8)  # Ligne verticale en haut 5
    pygame.draw.line(maSurface, (0, 224, 2), (820, 120), (820, 170), 8)  # Ligne verticale en haut 6
    pygame.draw.line(maSurface, (0, 224, 2), (570, 240), (570, 285), 5)  # Ligne verticale en haut 7

    pygame.draw.line(maSurface, (255, 255, 255), (909, 225), (845, 310), 5)  # barre haute triangle droit
    pygame.draw.line(maSurface, (255, 255, 255), (845, 310), (898, 350), 5)  # barre bas triangle droit
    pygame.draw.line(maSurface, (255, 255, 255), (898, 350), (885, 370), 5)  # barre haut triangle 2 droit
    pygame.draw.line(maSurface, (255, 255, 255), (885, 370), (909, 440), 5)  # barre bas triangle 2 droit

    pygame.draw.line(maSurface,(255,255,255),(845,480),(845,560),5) # Triangle en bas à droite
    pygame.draw.line(maSurface,(255,255,255),(845,480),(833,453),5)
    pygame.draw.line(maSurface,(255,255,255),(833,453),(762,583),5)
    pygame.draw.line(maSurface,(255,255,255),(762,583),(770,593),5)
    pygame.draw.line(maSurface,(255,255,255),(770,593),(845,560),5)

    pygame.draw.line(maSurface,(255,255,255),(445,450),(445,530),5) # Triangle en bas à gauche
    pygame.draw.line(maSurface,(255,255,255),(445,530),(440,535),5)
    pygame.draw.line(maSurface,(255,255,255),(440,535),(445,540),5)
    pygame.draw.line(maSurface,(255,255,255),(445,540),(495,583),5)
    pygame.draw.line(maSurface,(255,255,255),(495,583),(445,450),5)

    policeBonus = pygame.font.Font("PKMN-Pinball.ttf", 20)  # Police des Bonus
    pygame.draw.line(maSurface, (255, 255, 255), (845, 320), (865, 336), 5)  # Ligne Bonus lettre A
    textA = policeBonus.render("A", True, (70, 72, 255))  # Lettre Bonus A
    maSurface.blit(textA, (832, 336))
    pygame.draw.line(maSurface, (255, 255, 255), (868, 339), (888, 355), 5)  # Ligne Bonus lettre B
    textB = policeBonus.render("B", True, (255, 0, 0))  # Lettre Bonus B
    maSurface.blit(textB, (861, 355))


    pygame.draw.circle(maSurface, (255, 0, 0), (725, 260), 20, 5) #bumper cercle centre
    pygame.draw.circle(maSurface, (255, 0, 0), (725, 260), 10, 3) # cercle dans le bumper
    pygame.draw.circle(maSurface, (255, 255, 255), (625, 215), 15, 0)
    pygame.draw.circle(maSurface, (255, 255, 255), (830, 215), 15, 0)
    pygame.draw.circle(maSurface, (255, 255, 255), (715, 360), 15, 0)
    pygame.draw.circle(maSurface, (255, 255, 255), (570, 385), 20, 5) #bumper cercle bas gauche

    pygame.draw.line(maSurface, (0, 255, 255), (865, 400), (876, 430), 3)  # barre bas triangle 2 droit
    pygame.draw.line(maSurface, (0, 255, 255), (876, 430), (876, 475), 3)  # ligne verticale contenant le ressort
    pygame.draw.line(maSurface, (0, 255, 255), (876, 475), (856, 420), 3)  # ligne verticale contenant le ressort
    pygame.draw.line(maSurface, (0, 255, 255), (856, 420), (865, 400), 3)  # ligne verticale contenant le ressort

    pygame.draw.line(maSurface, (70, 120, 25), (879, 589), (879, 515), 8)  # ligne verticale contenant le ressort

    pygame.draw.line(maSurface, (70, 120, 25), (875, 589), (760, 638), 3)  # ligne verticale contenant le ressort
    pygame.draw.line(maSurface, (70, 120, 25), (760, 638), (882, 638), 3)  # ligne verticale contenant le ressort
    pygame.draw.line(maSurface, (70, 120, 25), (882, 638), (882, 589), 3)  # ligne verticale contenant le ressort


def Game_Left(maSurface,police):
    Mots = ["1", "2", "3", "4", "CREDITS", "BALL"]
    Position_1 = [(157, 10), (157, 120), (157, 230), (157, 340), (38, 600), (210, 600)]
    Position_2 = [(40, 60, 260, 50), (40, 170, 260, 50), (40, 280, 260, 50), (40, 390, 260, 50), (40, 650, 140, 50), (200, 650, 100, 50)]

    for i in range(0, 6):
        text = police.render(Mots[i], True, (255, 255, 255))
        maSurface.blit(text, Position_1[i])
        pygame.draw.rect(maSurface, (255, 255, 255), Position_2[i], 5)

    Image_Avion = pygame.image.load(os.path.join('avion.png'))
    maSurface.blit(Image_Avion, (65, 460))

def Game_Right (maSurface,police):
    policenight = pygame.font.Font("PKMN-Pinball.ttf", 60)
    policenight2 = pygame.font.SysFont("arial", 110)
    
    Position_1 = [(0, 0), (0, 720), (1280, 720), (1280, 0)]
    Position_2 = [(0, 720), (1280, 720), (1280, 0), (0, 0)]
    for i in range(0, 4):
        pygame.draw.line(maSurface, (255, 255, 255), Position_1[i], Position_2[i], 11)
        
    pygame.draw.rect(maSurface, (255, 255, 255), (940, 550, 245, 170), 5)
    pygame.draw.rect(maSurface, (255, 255, 255), (940, 445, 245, 98), 5)

    text = police.render("SUBLOGIC", True, (255, 255, 255))
    maSurface.blit(text, (1015, 10))

    text = policenight.render("Night", True, (255, 255, 255))
    maSurface.blit(text, (970, 60))
        
    Mots = ["M", "i", "s", "s", "i", "o", "n"]
    Position = [(1183, 148), (1216, 238), (1200, 303), (1200, 368), (1216, 458), (1198, 528), (1200, 593)]
    for i in range(0, 7):
        text = policenight2.render(Mots[i], True, (255, 255, 255))
        maSurface.blit(text, Position[i])
    Image_Avion2 = pygame.image.load(os.path.join('Avion_2.png'))
    maSurface.blit(Image_Avion2, (970, 200))

def Balle(maSurface):
    pygame.draw.circle(maSurface, (255, 255, 255), (924, 579), 9, 9)

maSurface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Graphisme')

police = pygame.font.Font("PKMN-Pinball.ttf", 20)
Game_Commun(maSurface)
Game_Left(maSurface, police)
Game_Right (maSurface, police)
Game_Center(maSurface)
Balle(maSurface)




inProgress = True
while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
pygame.quit()
