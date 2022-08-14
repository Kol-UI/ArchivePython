
from bases import*
from possibles import*
from merge import *
from justGetTenGUI import *
import pygame, sys
pygame.font.init()


def Victory(surface, score_max):                                #def qui permet de changer complètement l'affichage de la fenetre de jeu pour créer un écran de Victoire
    n = 6
    pygame.mixer.music.load("M_Bison_Yes.wav")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    monImage = pygame.image.load("fond (blanc).jpg")
    surface.blit(monImage, (0, 0))
    monImage = pygame.image.load("fond_Victory.jpg")
    surface.blit(monImage, (0, 0))
    fontObj = pygame.font.Font('police.ttf', 30)
    texteEND = fontObj.render("VICTORY", True, BLACK)
    texteRect = texteEND.get_rect()
    texteRect.topleft = (n*100 +100, 100)
    surface.blit(texteEND, texteRect)
    fontEND = pygame.font.Font('police.ttf', 20)
    texteEND = fontEND.render("try again", True, BLACK)
    texteRect = texteEND.get_rect()
    texteRect.topleft = (n*100 +100, 350)
    surface.blit(texteEND, texteRect)
    texteEND = fontEND.render("just click", True, BLACK)
    texteRect = texteEND.get_rect()
    texteRect.topleft = (n*100 +100, 370)
    surface.blit(texteEND, texteRect)
    texteScore = fontObj.render("Score :", True, BLACK)
    texteRect = texteScore.get_rect()
    texteRect.topleft = (n*100+100, 150)
    surface.blit(texteScore, texteRect)
    texteEND = fontObj.render(str(score_max), True, BLACK)
    texteRect = texteEND.get_rect()
    texteRect.topleft = (n*100+225, 150)
    surface.blit(texteEND, texteRect)
    pygame.display.update()
    if click(10):
        return

def stat_affichage(surface, score_max, n):                  #def qui permet d'affiché les stat de la partie ne cours, le titre au dessu du tableau , le score ect ( tout le teste afficher sur la fenetre pendant la phase de jeu

    pygame.display.set_caption('Just Get Ten')
    monImage = pygame.image.load("fond.jpg")
    surface.blit(monImage, (0, 0))
    fontScore = pygame.font.Font('police.ttf', 30)
    texteScore = fontScore.render("Score :", True, WHITE)
    texteRect = texteScore.get_rect()
    texteRect.topleft = (n*100+100, 200)
    surface.blit(texteScore, texteRect)
    fontEND = pygame.font.Font('police.ttf', 30)
    texteEND = fontEND.render(str(score_max), True, WHITE)
    texteRect = texteEND.get_rect()
    texteRect.topleft = (n*100+250, 200)
    surface.blit(texteEND, texteRect)
    texteScore = fontScore.render("Reset :", True, WHITE)
    texteRect = texteScore.get_rect()
    texteRect.topleft = (n*100+100, 300)
    surface.blit(texteScore, texteRect)
    font15 = pygame.font.Font('police.ttf', 20)
    texteScore = font15.render("press space", True, WHITE)
    texteRect = texteScore.get_rect()
    texteRect.topleft = (n*100+100, 330)
    surface.blit(texteScore, texteRect)
    fontObj = pygame.font.Font('police.ttf', 48)
    texteSurface = fontObj.render("Just Get Ten", True, WHITE)
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (250, 5)
    surface.blit(texteSurface, texteRect)

def game_over(surface, score_max):                  #def qui permet de changer complètement l'affichage de la fenetre de jeu pour crée un écran de game over ( défaite)
    pygame.mixer.music.load("Sad_Game_Over.wav")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    fontObj = pygame.font.Font('police.ttf', 48)
    monImage = pygame.image.load("fond.jpg")
    surface.blit(monImage, (0, 0))
    texteEND = fontObj.render("GAME OVER", True, WHITE)
    texteRect = texteEND.get_rect()
    texteRect.topleft = (250, 200)
    surface.blit(texteEND, texteRect)
    fontEND = pygame.font.Font('police.ttf', 20)
    texteEND = fontEND.render("just click for try again", True, WHITE)
    texteRect = texteEND.get_rect()
    texteRect.topleft = (250, 300)
    surface.blit(texteEND, texteRect)
    fontScore = pygame.font.Font('police.ttf', 30)
    texteScore = fontScore.render("Score :", True, WHITE)
    texteRect = texteScore.get_rect()
    texteRect.topleft = (350, 350)
    surface.blit(texteScore, texteRect)
    fontEND = pygame.font.Font('police.ttf', 30)
    texteEND = fontEND.render(str(score_max), True, WHITE)
    texteRect = texteEND.get_rect()
    texteRect.topleft = (400, 400)
    surface.blit(texteEND, texteRect)
    pygame.display.update()
    if click(10):
        return

def condition_victoire(n, tableau, surface, score_max):                 ##def qui permet de créer une boucle dans le jeu, elle vérifie pour chaque case si un coup est possible, si oui elle return True si non False car aucun coup
    if verif_coup_possible(n, tableau):                                 #car aucun coup ne peut être joué donc le joueur a perdu la partie
        return True
    else:
        print("aucun coup possible perdu")
    return False


def jeu_propre(n, tableau, Z, proba):                                   #boucle primaire du jeu elle initialise la fenetre et se lance après avoir effectuer les boucles de jeu
    surface = pygame.display.set_mode((900, 900))
    pygame.display.set_caption('Just Get Ten')
    monImage = pygame.image.load("fond.jpg")
    surface.blit(monImage, (0, 0))
    pygame.display.update()

    inProgress = True
    while inProgress:                                               #boucle pour les évènements
        score_max = 0
        while condition_victoire(n, tableau, surface, score_max):   #boucle de jeu
            for i in range(0, n, 1):
                for j in range(0, n, 1):
                    if tableau[i][j] > score_max:                   #boucle qui permet de relever la valeur la plus élevée dans le tableau et donc le score du joueur
                        score_max = tableau[i][j]
            if score_max == 10:                                     #2nd condition de victoire si le joeur fait 10 alors appele de la fonction qui lance l'écran de victoire
                Victory(surface, score_max)
                return

            stat_affichage(surface, score_max, n)

            Z = []
            position = None
            pygame_affichage(n, tableau, Z, surface)
            while position == None:
                position = select_cellule(n, tableau, position)     #boucle qui permet de reset le jeu ou de lancer instantanément l'écran de victoire ou de defaite ( pour des tests)
                if position == (42, 42):                            # j'ai laissé cette fonctionnalité que je trouve pratique
                    return
                if position == (40, 40):
                    game_over(surface, score_max)
                    return
                if position == (41, 41):
                    Victory(surface, score_max)
                    return

            Z = [position]
            Z = propagation(n, tableau, position, Z)
            pygame_affichage(n, tableau, Z, surface)            #a ce moment le programe affiche le tableau avec les cellules propager par rapport au premier click( position)
            position = click(n)                                 # attente du 2nd click pour savoir ce que veut  faire le joueur soit merge les cellules sur une des casse blanche ou bien change de groupe de cellules

            if position in Z:                                   #si la position est dans le grp de cellule précédemment selectionné alors on effectue la modification a tableau
                a = Z.index(position)                           ##les lignes qui suivent permettent de remettre la position qui se trouve dans Z à son début ( car modification utilise les premières coordonée spour "fusionner" les cellules
                W = Z.pop(a)
                Z.reverse()
                Z.append(W)
                Z.reverse()
                tableau = modification(n, tableau, Z)
                tableau = gravity(n, tableau, proba)
            elif position not in Z:
                if adjacent_équivalent(n, tableau, position):   #si la position n'est pas dans Z on modifie alors Z ce qui relance les if/ elif " if position in Z: " et "elif position not in Z:"
                    Z = [position]
                else:
                    jeu_propre(n, tableau, Z, proba)


        if 1:                                                   #ici ce if et tjr vrais mais cela permet d'y rentré toujours quand on sort de la boucle le précedent, cela permet aussi de faire un return sans que le for qui suit
            game_over(surface, score_max)                       #ne soit en dehors du code
            return
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                inProgress = False


def jeu(n , proba):                                 #def qui permet de relancer un nouveau jeu ( nouveau plateau en fonction de n)
    tableau = nouveaux_tableau(n, proba)
    print()
    print(tableau)
    print()
    Z = []
    jeu_propre(n, tableau, Z, proba)                #elle appelle à la fin la boucle de jeu principale donc avec les nouvelles données



def option(proba):                                  #def qui permet de crée une fenetre d'option avant de commencer on peut donc choissir la taille du tableau que l'on souhaite
    inProgress = True
    while inProgress:
        surface = pygame.display.set_mode((900, 900))
        pygame.display.set_caption('Option :')
        monImage = pygame.image.load("fond.jpg")
        surface.blit(monImage, (0, 0))
        pygame.draw.rect(surface, RED, pygame.Rect(200, 300, 100, 100), 2)
        pygame.draw.rect(surface, ORANGE, pygame.Rect(400, 300, 100, 100), 2)
        pygame.draw.rect(surface, GREEN, pygame.Rect(600, 300, 100, 100), 2)
        fontOpt = pygame.font.Font('police.ttf', 20)
        texteEND = fontOpt.render("selectionner un taille de tableau", True, WHITE)
        texteRect = texteEND.get_rect()
        texteRect.topleft = (230, 200)
        surface.blit(texteEND, texteRect)
        fontOpt = pygame.font.Font('police.ttf', 40)
        texteEND = fontOpt.render("Option :", True, WHITE)
        texteRect = texteEND.get_rect()
        texteRect.topleft = (350, 150)
        surface.blit(texteEND, texteRect)
        texteEND = fontOpt.render("4", True, WHITE)
        texteRect = texteEND.get_rect()
        texteRect.topleft = (235, 335)
        surface.blit(texteEND, texteRect)
        texteEND = fontOpt.render("5", True, WHITE)
        texteRect = texteEND.get_rect()
        texteRect.topleft = (435, 335)
        surface.blit(texteEND, texteRect)
        texteEND = fontOpt.render("6", True, WHITE)
        texteRect = texteEND.get_rect()
        texteRect.topleft = (640, 335)
        surface.blit(texteEND, texteRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            if event.type == MOUSEBUTTONDOWN :
                print(event.pos[0], event.pos[1])
                x, y = event.pos[0], event.pos[1]
                print("x =",x , "y=" ,y)
                if 200<= x <= 300 and 300 <= y <= 400:
                    n = 4
                    print("lancer du jeu avec n = 4")
                    jeu(n, proba)
                if 400<= x <= 500 and 300 <= y <= 400:
                    n = 5
                    print("lancer du jeu avec n = 5")
                    jeu(n, proba)
                if 600<= x <= 700 and 300 <= y <= 400:
                    n = 6
                    print("lancer du jeu avec n = 6")
                    jeu(n, proba)



proba = (0.05, 0.30, 0.6)           #variable globale qui comprend les probabilités de "pop" de chaque nouveau chiffre
option(proba)                       #appel de la fonction option qui permet de lancer l'ensemble du jeu
