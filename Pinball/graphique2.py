import pygame, sys, os
from pygame.locals import *

def Game_Commun(maSurface):
    pygame.draw.line(maSurface, (255, 255, 255), (340, 0), (340, 720), 5)
    pygame.draw.line(maSurface, (255, 255, 255), (940, 0), (940, 720), 5)

    pygame.draw.line(maSurface, (255, 255, 255), (0, 0), (0, 720), 5)

def Game_Center(maSurface):
    pygame.draw.arc(maSurface, (255, 255, 255), (660, 10, 285, 275), 0, 1.45, 10)  #Arc en haut à droite
    
    Couleur = [(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 55, 0),(255, 55, 0),(255, 55, 0),(255, 55, 0),(255, 55, 0),(255, 55, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(225, 0, 0),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 55, 0),(255, 55, 0),(255, 55, 0),(255, 55, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255, 247, 0),(255,255,255),(255,255,255),(255, 255, 255),(255, 255, 255),(255, 0, 174),(255, 0, 174)]
    Position_1 = [(885, 589),(885, 589),(345, 0),(940, 0),(342, 415),(400, 370),(910, 150),(600, 16),(530, 35),(380, 35),(342, 70),(385, 95),(445, 330),(535, 285),(535, 285),(400, 270),(555, 113),(555, 113),(555, 160),(418, 120),(502, 120),(418, 240),(525, 99),(418, 120),(525, 99),(620, 120),(660, 105),(700, 90),(740, 90),(780, 105),(820, 120),(570, 240),(909, 243),(845, 328),(898, 368),(885, 388),(845,498),(845,498),(833,487),(762,601),(770,611),(445,471),(445,548),(433,563),(443,578),(516,601),(516,601),(456, 330),(481, 317),(506, 304),(493, 68),(510, 81),(865, 418),(876, 448),(876, 493),(856, 438),(879, 591),(882, 591),(760, 641),(881, 643),(414, 592),(516, 641),(394, 641),(394, 550),(394, 550),(370, 470),(395, 470),(420, 470),(845, 338),(868, 357)]
    Position_2 = [(940, 589),(885, 720),(345, 410),(940, 720),(405, 370),(342, 260),(910, 720),(825, 16),(600, 16),(530, 35),(380, 35),(385, 250),(385, 250),(445, 330),(535, 130),(535, 270),(535, 130),(555, 160),(535, 190),(418, 240),(502, 240),(502, 240),(502, 120),(486, 69),(486, 69),(620, 170),(660, 155),(700, 140),(740, 140),(780, 155),(820, 170),(570, 285),(845,328),(898,368),(885,388),(909,458),(845,578),(833,487),(762,601),(770,611),(845,578),(445,548),(433,563),(443,578),(508,611),(445,471),(508,611),(478, 320),(503, 307),(528, 294),(507, 79),(524, 92),(876, 448),(876, 493),(856, 438),(865, 418),(879, 535),(760, 641),(882, 641),(881, 592),(516, 641),(394, 641),(394, 550),(414, 592),(370, 550),(370, 550),(395, 490),(420, 490),(865, 354),(887, 371)]
    Taille = [2, 3, 10, 11, 10, 10, 3, 10, 10, 10, 10, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 3, 3, 3, 8, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 5, 5]
    for i in range(0, len(Position_1)):
        pygame.draw.line(maSurface, Couleur[i], Position_1[i], Position_2[i],Taille[i])


    policeBonus = pygame.font.Font("PKMN-Pinball.ttf", 13)  # Police des Bonus

    textA = policeBonus.render("A", True, (255, 0, 174))  # Lettre Bonus A
    maSurface.blit(textA, (843, 350))
    textB = policeBonus.render("B", True, (255, 0, 174))  # Lettre Bonus B
    maSurface.blit(textB, (864, 367))

    #Text Bonus
    textN = policeBonus.render("N", True, (255, 0, 174)) # Les prochaines lignes sont consacrées aux bonus "n""i""g""h""t" qui sont en haut
    maSurface.blit(textN, (633, 124))
    textI = policeBonus.render("I", True, (255, 0, 174))
    maSurface.blit(textI, (677, 109))
    textG = policeBonus.render("G", True, (255, 0, 174))
    maSurface.blit(textG, (713, 102))
    textH = policeBonus.render("H", True, (255, 0, 174))
    maSurface.blit(textH, (753, 109))
    textT = policeBonus.render("T", True, (255, 0, 174))
    maSurface.blit(textT, (793, 124))

    textF = policeBonus.render("F", True, (255, 0, 174)) # Les prochaines lignes sont consacrées aux bonus "f""l""y" qui sont au milieu
    maSurface.blit(textF, (465, 330))
    textL = policeBonus.render("L", True, (255, 0, 174))
    maSurface.blit(textL, (491, 317))
    textY = policeBonus.render("Y", True, (255, 0, 174))
    maSurface.blit(textY, (514, 306))
    
    textC = policeBonus.render("C", True, (255, 0, 174)) # Les prochaines lignes sont consacrées aux bonus "c""d" qui sont en haut
    maSurface.blit(textC, (500, 53))
    textD = policeBonus.render("D", True, (255, 0, 174))
    maSurface.blit(textD, (517, 66))

    # Bumper
    Couleur_2 = [(255, 55, 0),(255, 55, 0),(255, 0, 174),(255, 0, 174),(255, 0, 174),(255, 55, 0)]
    Position_3 = [(725, 260),(725, 260),(625, 215),(830, 215),(715, 360),(570, 385)]
    Rayon = [20,10,15,15,15,20]
    Taille = [5,3,0,0,0,5]
    for i in range(0, len(Taille)):
        pygame.draw.circle(maSurface,Couleur_2[i],Position_3[i],Rayon[i],Taille[i])



def Game_Left(maSurface,police):
    Mots = ["1", "2", "3", "4", "CREDITS", "BALL"]
    Position_1 = [(160, 10), (160, 120), (160, 230), (160, 340), (38, 600), (210, 600)]
    Position_2 = [(40, 60, 260, 50), (40, 170, 260, 50), (40, 280, 260, 50), (40, 390, 260, 50), (40, 650, 140, 50), (200, 650, 100, 50)]

    for i in range(0, 6):
        text = police.render(Mots[i], True, (255, 0, 174))
        maSurface.blit(text, Position_1[i])
        pygame.draw.rect(maSurface, (255, 255, 255), Position_2[i], 5)

    Image_Avion = pygame.image.load(os.path.join('avion.png'))
    maSurface.blit(Image_Avion, (65, 460))

def Game_Right (maSurface,police):
    policenight = pygame.font.Font("PKMN-Pinball.ttf", 60)
    policenight2 = pygame.font.Font("PKMN-pinball.ttf", 55)
    
    Position_1 = [(0, 0), (0, 720), (1280, 720), (1280, 0)]
    Position_2 = [(0, 720), (1280, 720), (1280, 0), (0, 0)]
    for i in range(0, 4):
        pygame.draw.line(maSurface, (255, 255, 255), Position_1[i], Position_2[i], 11)
        
    pygame.draw.rect(maSurface, (255, 255, 255), (940, 550, 245, 170), 5)
    pygame.draw.rect(maSurface, (255, 255, 255), (940, 445, 245, 98), 5)

    text = police.render("SUBLOGIC", True, (255, 55, 0))
    maSurface.blit(text, (1015, 10))

    text = policenight.render("Night", True, (255, 0, 174))
    maSurface.blit(text, (970, 60))
        
    Mots = ["M", "i", "s", "s", "i", "o", "n"]
    Position = [(1209, 148), (1230, 236), (1217, 318), (1217, 398), (1230, 478), (1217, 558), (1217, 634)]
    for i in range(0, 7):
        text = policenight2.render(Mots[i], True, (255, 0, 174))
        maSurface.blit(text, Position[i])

    Image_Avion2 = pygame.image.load(os.path.join('Avion_2.png')) # L'avion coté gauche
    maSurface.blit(Image_Avion2, (950, 145))

    Image_Missile = pygame.image.load(os.path.join('missile.png')) # Premier missile
    maSurface.blit(Image_Missile, (1028, 215))
    Image_Missile2 = pygame.image.load(os.path.join('missile.png')) # Deuxieme missile
    maSurface.blit(Image_Missile2, (1070, 268))
    Image_Missile3 = pygame.image.load(os.path.join('missile.png')) # Troisieme missile
    maSurface.blit(Image_Missile3, (1116, 320))
    Image_Missile4 = pygame.image.load(os.path.join('missile.png')) # Quatrieme missile
    maSurface.blit(Image_Missile4, (1160, 375))

    textAddPlayer = police.render("add  player", True, (255, 0, 174)) # "Add player" à droite
    maSurface.blit(textAddPlayer, (952, 452))
    
    textPress = police.render("press", True, (255, 0, 174)) # "Press S" à droite
    maSurface.blit(textPress, (1048, 505))
    textS = police.render("S", True, (255, 55, 0))
    maSurface.blit(textS, (1155, 505))
    maSurface.blit(textPress, (1048, 680))
    textQ = police.render("Q", True, (255, 55, 0))
    maSurface.blit(textQ, (1155, 680))


def Balle(maSurface):
    pygame.draw.circle(maSurface, (255, 255, 255), (924, 579), 9, 9)


'''maSurface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Graphisme')

police = pygame.font.Font("PKMN-Pinball.ttf", 20)
Game_Commun(maSurface)
Game_Left(maSurface, police)
Game_Right (maSurface, police)
Game_Center(maSurface)
Balle(maSurface)



inProgress = True
while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
pygame.quit'''
