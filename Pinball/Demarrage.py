import pygame, sys, os
from pygame.locals import *
pygame.init()

maSurface = pygame.display.set_mode((1280,720))
pygame.display.set_caption('NIGHT MISSION PINBALL')
sonMenu = pygame.mixer.Sound("Pacific_RimB.wav")

def lanceurDemarrage(maSurface):
    sonMenu.play()
    font = pygame.image.load("1461531751326.png").convert()
    maSurface.blit(font, (0,0))
    policeDemarrage = pygame.font.Font("PKMN-Pinball.ttf", 50)
    textDemarrage = policeDemarrage.render("Click here to play", True, (255, 255, 255))
    maSurface.blit(textDemarrage, (300, 300))
    pygame.draw.rect(maSurface, (255,255,255),(295,295,725,85),5)


lanceurDemarrage(maSurface)
inProgress = True

while inProgress:
    for event in pygame.event.get():                       
        if event.type == QUIT:
            inProgress = False
        pygame.display.update()
pygame.quit()
