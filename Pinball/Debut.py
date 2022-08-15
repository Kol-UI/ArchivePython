import pygame, sys, os
from pygame.locals import *
from transition_avion_qui_monte import *
pygame.init()

maSurface = pygame.display.set_mode((1280,720))
pygame.display.set_caption('NIGHT MISSION PINBALL')
inProgress = True

    
def menuPrincipal(maSurface):
    fond = pygame.image.load("1461531751326.png").convert()
    maSurface.blit(fond, (0,0))
    police = pygame.font.Font("PKMN-Pinball.ttf", 50)
    textPlay = police.render("P L A Y",True, (255,255,255))
    maSurface.blit(textPlay, (262, 50))
    textSettingsControls = police.render("controls",True, (255,255,255))
    maSurface.blit(textSettingsControls, (262, 181))
    textGeneric = police.render("generic",True, (255,255,255))
    maSurface.blit(textGeneric, (262, 301))
    textInstructions = police.render("instructions",True, (255,255,255))
    maSurface.blit(textInstructions, (262, 430))
    textExit = police.render("EXIT",True, (255,255,255))
    maSurface.blit(textExit, (262, 561))
    Image_Avion_Menu = pygame.image.load(os.path.join('avion-transparent.png'))
    maSurface.blit(Image_Avion_Menu, (900, 100))
    maSurface.blit(Image_Avion_Menu, (900, 300))
    maSurface.blit(Image_Avion_Menu, (900, 500))
    pygame.draw.rect(maSurface, (255,255,255),(255,45,285,85),5) # rectangle de play
    pygame.draw.rect(maSurface, (255,255,255),(255,181,374,75),5) # rectangle de controls
    pygame.draw.rect(maSurface, (255,255,255),(255,301,300,75),5) # rectangle de generic
    pygame.draw.rect(maSurface, (255,255,255),(255,431,510,75),5) # rectangle de instructions
    pygame.draw.rect(maSurface, (255,255,255),(256,556,213,85),5) # rectangle de exit
    

menuPrincipal(maSurface)
while inProgress:
    for event in pygame.event.get():                       
        if event.type == QUIT:
            inProgress = False
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            print(x,y)
            if x >=256 and y >558 and x <=467 and y <=638: # bouton exit
                inProgress = False
            elif x >=256 and y >183 and x <=626 and y <=253: # bouton controls
                from Parametre import *
            elif x >=255 and y >433 and x <=763 and y <=503: # bouton instructions
                from init import *
            elif x >=254 and y >45 and x <= 539 and y <=128: # bouton play
                from ChoixDifficulte import *
        pygame.display.update()
pygame.quit()
