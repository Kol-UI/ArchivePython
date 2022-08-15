import pygame, sys
from pygame.locals import *
pygame.init()

maSurface = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Pinball Night-Mission')

def Game_Right(maSurface,police,policenight):

    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    darkBlue = (0,0,128)
    white = (255,255,255)
    black = (0,0,0)
    pink = (255,200,200)
    
    pygame.draw.line(maSurface,white,(0,0),(0,720),11)
    pygame.draw.line(maSurface,white,(0,720),(1280,720),11)
    pygame.draw.line(maSurface,white,(1280,720),(1280,0),11)
    pygame.draw.line(maSurface,white,(1280,0),(0,0),11)
    
    pygame.draw.line(maSurface,white,(340,1),(340,720),11)
    pygame.draw.line(maSurface,white,(940,1),(940,720),11)
    
    pygame.draw.rect(maSurface,white,(940,550,245,170),5)

    pygame.draw.rect(maSurface,white,(940,445,245,98),5)
    
    text = police.render("SUBLOGIC",True,(white))
    maSurface.blit(text,(1015,10))

    text = policenight.render("Night",True,(white))
    maSurface.blit(text,(970,50))

    text = policenight.render("M",True,(white))
    maSurface.blit(text,(1183,148))

    text = policenight.render("i",True,(white))
    maSurface.blit(text,(1216,238))

    text = policenight.render("s",True,(white))
    maSurface.blit(text,(1200,303))

    text = policenight.render("s",True,(white))
    maSurface.blit(text,(1200,368))

    text = policenight.render("i",True,(white))
    maSurface.blit(text,(1216,458))

    text = policenight.render("o",True,(white))
    maSurface.blit(text,(1198,528))

    text = policenight.render("n",True,(white))
    maSurface.blit(text,(1200,593))

police = pygame.font.SysFont("arial",40)
policenight = pygame.font.SysFont("arial",110)
Game_Right(maSurface,police,policenight)

inProgress = True
while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
pygame.quit()


