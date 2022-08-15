import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
maSurface = pygame.display.set_mode((1280, 720))


inProgress = True


a, b, c, d, e, f, g, h, i, j = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

Image_Missile2 = pygame.image.load('missile2.png')
Image_Missile = pygame.image.load('missile.png')
police = pygame.font.Font("PKMN-Pinball.ttf", 20)
S = police.render("S", True, (255, 0, 0))
S2 = police.render("S", True, (0, 255, 0))
Q = police.render("Q", True, (255, 0, 0))
Q2 = police.render("Q", True, (0, 255, 0))

while inProgress:
    a+=1
    b+=1
    c+=1
    d+=1
    e+=1
    f+=1
    g+=1
    h+=1
    i+=1
    j+=1
    if a==10:
        a=0
        maSurface.blit(Image_Missile2, (1028, 215))
    if b > 120:
        b=0
        maSurface.blit(Image_Missile, (1028, 215))
    if c==20:
        c=0
        maSurface.blit(Image_Missile2, (1070, 268))
    if d > 120:
        d=0
        maSurface.blit(Image_Missile, (1070, 268))
    if e==45:
        e=0
        maSurface.blit(Image_Missile2, (1116, 320))
    if f > 120:
        f=0
        maSurface.blit(Image_Missile, (1116, 320))
    if g==60:
        g=0
        maSurface.blit(Image_Missile2, (1160, 375))
    if h > 120:
        h=0
        maSurface.blit(Image_Missile, (1160, 375))
    if i==60:
        i=0
        maSurface.blit(S, (1155, 505))
        maSurface.blit(Q, (1155, 680))
    if j > 120:
        j=0
        maSurface.blit(S2, (1155, 505))
        maSurface.blit(Q2, (1155, 680))


    for event in pygame.event.get():








        
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()
