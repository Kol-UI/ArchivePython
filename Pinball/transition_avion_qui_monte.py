import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
maSurface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('NIGHT MISSION PINBALL')

liste = [100,200,300,400]
y = 800
for i in range(0,4):
    ariane = pygame.image.load('avion.png')
    maSurface.blit(ariane,(liste[i],y))

inProgress = True

while inProgress: 
    y -= 5
    maSurface.blit(ariane,(100,y))
    maSurface.blit(ariane,(400,y))
    maSurface.blit(ariane,(700,y))
    maSurface.blit(ariane,(1000,y))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN: inProgress = False
        elif event.type == QUIT:
            inProgress = False
    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()
