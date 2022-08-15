import time
from game import *
from graphique import *
from menu import *
import pygame, sys, os
from pygame.locals import *
pygame.init()

son = pygame.mixer.Sound("Pacific_RimB.wav")
#flipperD = pygame.mixer.Sound("SOUND5.wav")
flipperDdeb = pygame.mixer.Sound("SOUND5deb.wav")
flipperDfin = pygame.mixer.Sound("SOUND5fin.wav")
#flipperG = pygame.mixer.Sound("SOUND6.wav")
flipperGdeb = pygame.mixer.Sound("SOUND6deb.wav")
flipperGfin = pygame.mixer.Sound("SOUND6fin.wav")
coins = pygame.mixer.Sound("Coin.wav")
ressort = pygame.mixer.Sound("ressort.wav")

maSurface = pygame.display.set_mode((1280, 720))
fond = pygame.image.load("1461531751326.png").convert()
maSurface.blit(fond, (0,0))
pygame.display.set_caption('Night Mission Pinball')
inProgress = True

police_menu = pygame.font.SysFont('PKMN-Pinball.ttf', 40)
menu_principal = 0
game_play = 0
player = 0

coin = 0
partie = 0
push_spring = 0
entree_joueur = 0
page = 1
menu(maSurface, police_menu)
FPS = 60
fpsClock = pygame.time.Clock()
y = 592
z = 592
dunoir = pygame.image.load('dunoir.png')
spring = pygame.image.load('spring.png')
Position_1 = [(604,692.5),(613.69, 669.11),(617, 644),(613.69, 618.89),(604,585.5)]
Position_2 = [(604,585.5),(613.69, 618.89),(617, 644),(613.69, 669.11),(604,692.5)]
Position_3 = [(673, 692.5),(663.31, 669.11),(660, 644),(663.31, 618.89),(673,585.5)]
Position_4 = [(673,585.5),(663.31, 618.89),(660, 644),(663.31, 669.11),(673, 692.5)]
son.play()


while inProgress:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            carac = event.dict['unicode']
            if game_play == 0:
                if menu_principal == 0:
                    if carac == 'a' or carac == 'A':  # si on appuies sur la lettre A
                        game_play = 1
                        maSurface = pygame.display.set_mode((1280,720))
                        police = pygame.font.Font("PKMN-Pinball.ttf", 20)
                        Game_Commun(maSurface)
                        Game_Left(maSurface, police)
                        Game_Right (maSurface, police)
                        Game_Center(maSurface)
                        Balle(maSurface)
                        maSurface.blit(spring, (915,592))
                    if carac == 'b' or carac == 'B':
                        maSurface = pygame.display.set_mode((1280,720))
                        fond = pygame.image.load("783a0d66b7287375e7d6ff9b7df15d51.jpg").convert()
                        maSurface.blit(fond, (0,0))
                        menu_principal = 1
                        menu_Page(maSurface, police_menu, page)
                        page += 1
                if page == 10:
                    if event.key == K_SPACE:
                        maSurface = pygame.display.set_mode((1280,720))
                        fond = pygame.image.load("1461531751326.png").convert()
                        maSurface.blit(fond, (0,0))
                        menu(maSurface, police_menu)
                        menu_principal = 0
                        page = 1
                if page > 1 and page <= 9:
                    if event.key == K_SPACE:
                        maSurface = pygame.display.set_mode((1280,720))
                        fond = pygame.image.load("783a0d66b7287375e7d6ff9b7df15d51.jpg").convert()
                        maSurface.blit(fond, (0,0))
                        menu_Page(maSurface, police_menu, page)
                        page += 1
                        menu_principal = 1
            
            if game_play == 1:
                if entree_joueur == 0:
                    if player < 4 :
                        carac = event.dict['unicode']
                        if carac == 's' or carac == 'S':  # si on appuies sur la lettre S
                            player += 1
                            Player(maSurface,police,player)
                    if coin < player :
                        carac = event.dict['unicode']
                        if carac == 'q' or carac == 'Q': 
                            coin += 1
                            pygame.draw.rect(maSurface,(0,0,0),(45,655,130,40))
                            text = police.render(str(coin),True,(30,144,255))
                            maSurface.blit(text,(105,660,130,40))
                if partie == 0:
                    if push_spring == 0:
                        if event.key == K_DOWN:
                            entree_joueur = 1
                            maSurface.blit(dunoir, (915,592))
                            y += 5
                            z += 5
                            maSurface.blit(dunoir,(915,z))
                            maSurface.blit(spring,(915,y))
                            pygame.draw.line(maSurface, (255, 255, 255), (850, 720), (950, 720), 12)
                            pygame.display.update()
                            fpsClock.tick(FPS)
                            if y > 705:
                                push_spring = 1
                    if event.key == K_UP:
                        ressort.play()
                        
                        maSurface.blit(dunoir, (915,592))
                        maSurface.blit(spring,(915, 592))
                        pygame.display.update()
                        fpsClock.tick(FPS)
                        y = 592
                        z = 592
                        partie = 1
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if game_play == 1:
                    flipperGdeb.play()
                    
                    for i in range(0,4):
                        pygame.draw.line(maSurface,(0,0,0),(520, 644),Position_1[i],5)
                        pygame.draw.line(maSurface,(255,255,255),(520, 644),Position_1[i+1],5)
                        fpsClock.tick(FPS)
                        pygame.display.update()
            if event.key == K_RIGHT:
                if game_play == 1:
                    flipperDdeb.play()
                    
                    for i in range(0,4):
                        pygame.draw.line(maSurface,(0,0,0),(757, 644),Position_3[i],5)
                        pygame.draw.line(maSurface,(255,255,255),(757, 644),Position_3[i+1],5)
                        fpsClock.tick(FPS)
                        pygame.display.update()
        if event.type == KEYUP:
            if event.key == K_LEFT:

                if game_play == 1:
                    flipperGfin.play()
                    for i in range(0,4):
                        pygame.draw.line(maSurface,(0,0,0),(520, 644),Position_2[i],5)
                        pygame.draw.line(maSurface,(255,255,255),(520, 644),Position_2[i+1],5)
                        fpsClock.tick(FPS)
                        pygame.display.update()
            if event.key == K_RIGHT:

                if game_play == 1:
                    flipperDfin.play()
                    for i in range(0,4):
                        pygame.draw.line(maSurface,(0,0,0),(757, 644),Position_4[i],5)
                        pygame.draw.line(maSurface,(255,255,255),(757, 644),Position_4[i+1],5)
                        fpsClock.tick(FPS)
                        pygame.display.update()


            if event.key == K_a:

                if game_play == 1:
                    coins.play()

                        
        if event.type == QUIT:
            inProgress = False        
    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()

