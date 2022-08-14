from JeffersonShell import *
import pygame, sys
 from pygame.locals import *


size = (700, 500)
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 pygame.init()


def displayCylinder(mySurface,cylinder,i):
    mySurface = screen.fill(BLACK)
    i = key
    cylinder = cylinder(key)


def displayCylinders(mySurface,cylinder):
    cylinder.draw(RED)


def enterKey(mySurface,n):
    for i, letter in enumerate(text):
        return n
    pygame.font.init(n, GREEN)


def rotateCylinder(cylinder,i,up=True):
    if up = True:
        textpos = text.get_rect.up(i)
    else:
        tewtpos = text.get_rect.down(i)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True