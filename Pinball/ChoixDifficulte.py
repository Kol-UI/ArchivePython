import pygame, sys, os
from pygame.locals import *
pygame.init()

maSurface = pygame.display.set_mode((1280,720))
pygame.display.set_caption('NIGHT MISSION PINBALL')

def menuDifficulté(maSurface):
    fond = pygame.image.load("1461531751326.png").convert()
    maSurface.blit(fond, (0,0))
    police = pygame.font.Font("PKMN-Pinball.ttf", 50)
    policeGameMode = pygame.font.Font("PKMN-Pinball.ttf", 60)
    textGameMode = policeGameMode.render("Game Mode",True, (255, 255, 255))
    textEasy = police.render("Easy", True, (0, 255, 0))
    textNormal = police.render("Normal", True, (255, 255, 0))
    textHard = police.render("Hard", True, (255, 0, 0))
    textReturn = police.render("Return", True, (255, 255, 255))
    textEditor = police.render("Editor", True, (0, 0, 255))
    maSurface.blit(textGameMode, (30, 30))
    maSurface.blit(textEditor, (50, 300))
    maSurface.blit(textEasy, (400, 300))
    maSurface.blit(textNormal, (650, 300))
    maSurface.blit(textHard, (1000, 300))
    maSurface.blit(textReturn, (964, 620))
    pygame.draw.rect(maSurface, (0,0,255),(45,295,270,85),5)
    pygame.draw.rect(maSurface, (0,255,0),(393,295,202,85),5)
    pygame.draw.rect(maSurface, (255,255,0),(645,295,292,85),5)
    pygame.draw.rect(maSurface, (255,0,0),(995,295,200,85),5)
    pygame.draw.rect(maSurface, (255,255,255),(960,615,295,85),5)


menuDifficulté(maSurface)
inProgress = True
while inProgress:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            print(x,y)
            if x >=961 and y >615 and x <=1253 and y <=696: # bouton return
                from Debut import *
        elif event.type == QUIT:
            inProgress = False
    pygame.display.update()
pygame.quit()
