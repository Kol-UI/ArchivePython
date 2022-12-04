from Jeu import *
import pygame
from pygame.locals import *


pygame.init() #On inialise pygame
Board = pygame.display.set_mode((1000, 1000))    #On défini les dimensions de ka fenêtre pygame
Board.fill((80,255,80))
pygame.display.set_caption('Bataille Navale')    #On écrit le titre de la fenêtre
newGame = Jeu(Board)
newGame.start()
pygame.quit()
