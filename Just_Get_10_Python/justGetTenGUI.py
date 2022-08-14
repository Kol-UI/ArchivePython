from bases import*
from possibles import*
from merge import *
import pygame, sys
from pygame.locals import *
                                #set des couleur pour en variable pour les appeler par la suite
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 128, 0)
VERT_FONCEE = (0, 128, 0)
BLERT = (0, 155, 155)
PURPLE = (128, 0, 255)
PINK = (255, 128, 192)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (192, 192, 192)

pygame.init()
pygame.font.init()

def celules(tableau, surface ,i ,j , B):        #def qui affiche sur la fenetre pygame une cellule avec ça couleur assosiée si elle est selectionnée ou non
    #print("tableau[i][j]=", tableau[i][j])
    x = i*100+50
    y = j*100+50
    if B == True:
        pygame.draw.rect(surface, WHITE, [y, x, 100, 100])      #ci B == True la cellule sera blanche et non de la couleur associer au chiffre
    else:
        if tableau[i][j] == 1:
            pygame.draw.rect(surface, GREEN, [y, x, 100, 100])
        elif tableau[i][j] == 2:
            pygame.draw.rect(surface, BLUE, [y, x, 100, 100])
        elif tableau[i][j] == 3:
            pygame.draw.rect(surface, ORANGE, [y, x, 100, 100])
        elif tableau[i][j] == 4:
            pygame.draw.rect(surface, VERT_FONCEE, [y, x, 100, 100])
        elif tableau[i][j] == 5:
            pygame.draw.rect(surface, BLERT, [y, x, 100, 100])
        elif tableau[i][j] == 6:
            pygame.draw.rect(surface, PURPLE, [y, x, 100, 100])
        elif tableau[i][j] == 7:
            pygame.draw.rect(surface, PINK, [y, x, 100, 100])
        elif tableau[i][j] == 8:
            pygame.draw.rect(surface, RED, [y, x, 100, 100])
        elif tableau[i][j] == 9:
            pygame.draw.rect(surface, YELLOW, [y, x, 100, 100])
        elif tableau[i][j] == 10:
            pygame.draw.rect(surface, GRAY, [y, x, 100, 100])

def it_that_WHITE(i, j, Z):     #fonction qui compare les coordonées de la cellule qui sont i, j et return True si la cellule doit être afficher en blanc ou non
    a = 0
    while a < len(Z):
        #print("Z[a]=", Z[a])
        val1 = Z[a][0]
        val2 = Z[a][1]
        #print("val1 =", val1)
        #print("val2 =", val2)
        if val1 == i and val2 == j:
            return True
        else:
            a += 1
    return False

def texte(tableau, surface, i,j):       #def qui affiche la valeur de la cellule dont les coordonnées sont envoyées en paramètre

    fontObj = pygame.font.Font('police.ttf', 48)
    x = i * 100 + 85
    y = j * 100 + 85
    chiffre = (tableau[i][j])
    texteSurface = fontObj.render(str(chiffre), True, BLACK)
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (y, x)
    surface.blit(texteSurface, texteRect)
    pygame.display.update()

def click(n):                   #def qui consiste à boucler sur tant que un évènement particuler n'est pas survenu elle return une liste de 2 valeur ex: (40,40) ou des coordonées qui se trouvent dans le tableau ex (0,4) en fonction
                                #d'ou le curseur de la souris se trouve
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == QUIT:
                end = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return 42, 42
                if event.key == K_F1:
                    return 41, 41
                if event.key == K_F2:
                    return 40, 40
            if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (1, 0, 0):
                x, y = event.pos[0], event.pos[1]
                #print("x= ", event.pos[0], "y =", event.pos[1])
                if x >= 50 and x <= n*100+50 and y >= 50 and y <= n*100+50:
                    #print("ci tu rentre")
                    i = 50
                    j = 150
                    for k in range(0, n, 1):
                        #print("k =", k)
                       #print('i =', i, 'j = ', j)
                        if x >= i and x <= j:
                            x = k
                            #print("x = ",x)
                            break
                        i += 100
                        j += 100
                    i = 50
                    j = 150
                    for k in range(0, n, 1):
                        #print("k =", k)
                        #print('i =', i, 'j = ', j)
                        if y >= i and y <= j:
                            y = k
                            #print("y = ",y)
                            break
                        i += 100
                        j += 100
                    end = False
                    print("x =", x, "y =", y)
                    return y, x



def pygame_affichage(n, tableau, Z, surface):       ##def qui affiche le tableau de cellule grace à une double boucle et en appelant les fonctions assignées à chaque opération
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            B = it_that_WHITE(i, j, Z)
            celules(tableau, surface, i, j, B)
            texte(tableau, surface, i, j)
    pygame.draw.rect(surface, WHITE, pygame.Rect(48, 48, n*100+3, n*100+3), 2)
    pygame.display.update()

def select_cellule(n, tableau, position):           #def qui permet de selectionner une cellule du tableau en foncton de des position return par la fonction click(n)
    if position == None:
        position = click(n)
    if position[0] >= 7:                            #ici la position n'est pas dans le tableau la fonction return quand meme la position car elle sera utiliser d'un autre manière
        return position
    if adjacent_équivalent(n, tableau, position):
        return position
    else:
        position = None                             #tant que la cellule selectionnée n'est pas d'adjacente équivalente on relance la fonction
        select_cellule(n, tableau, position)
