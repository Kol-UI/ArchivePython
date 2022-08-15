import pygame, sys, os
from pygame.locals import *

def Player(maSurface,police,player):
    Position_2 = [(250,70),(250,180),(250,290),(250,400)]
    text = police.render("00",True,(178,34,34))
    maSurface.blit(text,Position_2[player -1])
