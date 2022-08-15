import pygame, sys, os
from pygame.locals import *
pygame.init()

maSurface = pygame.display.set_mode((1280,720))
pygame.display.set_caption('NIGHT MISSION PINBALL')

def menu_Paramètre(maSurface):
    police_Titre = pygame.font.Font('PKMN-Pinball.ttf', 40)
    textP = police_Titre.render("Settings",True, (255,0,0))
    maSurface.blit(textP, (150, 100))

    police_Text = pygame.font.Font('PKMN-Pinball.ttf', 25)
    Coord = [(270,200),(270,275),(270,350),(270,425),(270,500),(270,575),(600,650)]
    Couleur = [(30,144,255),(255,255,255)]
    Texte = ["Number Of Balls", "Free Game Score", "Forward Incline Angle", "Ball Speed", "Tilt Effect", "Tilt Sensitivity", "Click Here To Check Controls"]
    text = ["text1","text2","text3","text4","text5","text6"]
    for i in range(0,6):
        text[i] = police_Text.render(Texte[i],True, Couleur[0])
        maSurface.blit(text[i], Coord[i])
    text6 = police_Text.render(Texte[6],True, Couleur[1])
    maSurface.blit(text6, Coord[6])

    Rouge=[(255,0,0)] 
    police = pygame.font.SysFont('arial',60)
    Coord_rect=[(910,190,60,50),(850,265,180,50),(910,340,60,50),(910,415,60,50),(910,490,60,50),(910,565,60,50)]
    Couleur2=[(30,144,255)]
    CoordMoins=[(860, 175),(805, 250),(860, 325),(830, 400),(830, 475),(830, 550)]
    CoordPlus=[(1005, 175),(1060, 250),(1005, 325),(1035, 400),(1035, 475),(1035, 550)]
    textMoins=["textMoins","textMoins2","textMoins3","textMoins4","textMoins5","textMoins6"]
    textPlus=["textPlus","textPlus2","textPlus3","textPlus4","textPlus5","textPlus6"]
    for i in range(0,6):
        pygame.draw.rect(maSurface,Couleur2[0],Coord_rect[i],5)
        textMoins[i] = police.render("-",True, Rouge[0])
        maSurface.blit(textMoins[i], CoordMoins[i])
        textPlus[i] = police.render("+",True, Rouge[0])
        maSurface.blit(textPlus[i], CoordPlus[i])

    Image_Avion4 = pygame.image.load(os.path.join('Avion_4.png'))
    Image_Avion4.set_colorkey((0,0,0))
    maSurface.blit(Image_Avion4, (45,570))
    Image_Explode = pygame.image.load(os.path.join('Explode.png'))
    Image_Explode.set_colorkey((0,0,0))
    maSurface.blit(Image_Explode, (81,180))


    Pos_ligne=[(176, 540),(176, 450),(176, 360),(106, 540),(106, 450),(106, 360)]
    Pos2_ligne=[(176, 515),(176, 425),(176, 335),(106, 515),(106, 425),(106, 335)]
    BLANC = (255,255,255)
    for i in range(0,6):
        pygame.draw.line(maSurface, BLANC, Pos_ligne[i], Pos2_ligne[i],5)
 
    textNbBall = police_Text.render("1",True, Rouge[0])
    maSurface.blit(textNbBall, (932, 196))
    textFreeGameScore = police_Text.render("0000000",True, Rouge[0])
    maSurface.blit(textFreeGameScore, (866, 271))
    textAngle = police_Text.render("0",True, Rouge[0])
    maSurface.blit(textAngle, (932, 346))
    textSpeed = police_Text.render("1",True, Rouge[0])
    maSurface.blit(textSpeed, (932, 420))
    textTiltEffect = police_Text.render("1",True, Rouge[0])
    maSurface.blit(textTiltEffect, (932, 496))
    textSensitivity = police_Text.render("1",True, Rouge[0])
    maSurface.blit(textSensitivity, (932, 570))

    

def config_parametres(maSurface,parametres):
    police_Text = pygame.font.Font('PKMN-Pinball.ttf', 25)
    Coord_param_jeu=[(932, 196),(866, 271),(932, 346),(932, 420),(932, 496),(932, 570)]
    Rouge=[(255,0,0)]
    param_jeu=["textNbBall","textFreeGameScore","textAngle","textSpeed","textTiltEffect","textSensitivity"]
    if parametres["nombreBall2"] >1 and x >= 850  and y >210 and x <= 880 and y <=225:
        parametres["nombreBall2"] -= 1
        pygame.draw.rect(maSurface, (0,0,0), (916,196,48,38))
        param_jeu[0] = police_Text.render(str(parametres["nombreBall2"]),True, Rouge[0])
        maSurface.blit(param_jeu[0], Coord_param_jeu[0])              
    elif parametres["nombreBall2"] <5 and x >= 1000  and y >200 and x <= 1030 and y <=225:
        parametres["nombreBall2"] +=1
        pygame.draw.rect(maSurface, (0,0,0), (916,196,48,38))
        param_jeu[0] = police_Text.render(str(parametres["nombreBall2"]),True, Rouge[0])
        maSurface.blit(param_jeu[0], Coord_param_jeu[0])
    
    if parametres["free_game_score2"] > 0 and x >=795   and y >280 and x <= 825 and y <=300:
        parametres["free_game_score2"] -= 100000
        if parametres["free_game_score2"] < 1000000:
            pygame.draw.rect(maSurface, (0,0,0), (855,271,170,38))
            param_jeu[1] = police_Text.render("0"+str(parametres["free_game_score2"]),True, Rouge[0])
            maSurface.blit(param_jeu[1], Coord_param_jeu[1])
        if parametres["free_game_score2"] == 0:
            pygame.draw.rect(maSurface, (0,0,0), (855,271,170,38))
            param_jeu[1] = police_Text.render("0000000",True, Rouge[0])
            maSurface.blit(param_jeu[1], Coord_param_jeu[1])
        elif parametres["free_game_score2"] == 1000000:
            pygame.draw.rect(maSurface, (0,0,0), (855,271,170,38))
            param_jeu[1] = police_Text.render(" 900000",True, Rouge[0])
            maSurface.blit(param_jeu[1], Coord_param_jeu[1])
    elif parametres["free_game_score2"] < 1000000 and x >=1050   and y >270 and x <= 1080 and y <=300:
        parametres["free_game_score2"] += 100000
        if parametres["free_game_score2"] < 1000000:
            pygame.draw.rect(maSurface, (0,0,0), (855,271,170,38))
            param_jeu[1] = police_Text.render("0"+str(parametres["free_game_score2"]),True, Rouge[0])
            maSurface.blit(param_jeu[1], Coord_param_jeu[1])
        elif parametres["free_game_score2"] >= 1000000:
            pygame.draw.rect(maSurface, (0,0,0), (855,271,170,38))
            param_jeu[1] = police_Text.render(" 1000000",True, Rouge[0])
            maSurface.blit(param_jeu[1], Coord_param_jeu[1])

    if parametres["angle_incline2"] > 0 and x >=850   and y >360 and x <= 880 and y <=375:
        parametres["angle_incline2"] -= 1
        if parametres["angle_incline2"] < 10:
            pygame.draw.rect(maSurface, (0,0,0), (914,346,53,38))
            param_jeu[2] = police_Text.render(str(parametres["angle_incline2"]),True, Rouge[0])
            maSurface.blit(param_jeu[2], Coord_param_jeu[2])
    elif parametres["angle_incline2"] < 10 and x >=1005   and y >350 and x <= 1030 and y <=375:
        parametres["angle_incline2"] += 1
        if parametres["angle_incline2"] < 10:
            pygame.draw.rect(maSurface, (0,0,0), (914,346,53,38))
            param_jeu[2] = police_Text.render(str(parametres["angle_incline2"]),True, Rouge[0])
            maSurface.blit(param_jeu[2], Coord_param_jeu[2])
        elif parametres["angle_incline2"] >= 10:
            pygame.draw.rect(maSurface, (0,0,0), (914,346,53,38))
            param_jeu[2] = police_Text.render(" 10",True, Rouge[0])
            maSurface.blit(param_jeu[2], (914, 346))
            
    if parametres["Ball_speed2"] > 1 and x >=825 and y >430 and x <= 850 and y <=450:
        parametres["Ball_speed2"] -= 1
        pygame.draw.rect(maSurface, (0,0,0), (914,420,53,38))
        param_jeu[3] = police_Text.render(str(parametres["Ball_speed2"]),True, Rouge[0])
        maSurface.blit(param_jeu[3], Coord_param_jeu[3])
    elif parametres["Ball_speed2"] <3 and x >=1035   and y >430 and x <= 1060 and y <=450:
        parametres["Ball_speed2"] += 1
        pygame.draw.rect(maSurface, (0,0,0), (914,420,53,38))
        param_jeu[3] = police_Text.render(str(parametres["Ball_speed2"]),True, Rouge[0])
        maSurface.blit(param_jeu[3], Coord_param_jeu[3])
            
    if parametres["Tilt_effect2"] > 1 and x >=825 and y >505 and x <= 850 and y <=525:
        parametres["Tilt_effect2"] -= 1
        pygame.draw.rect(maSurface, (0,0,0), (914,496,53,38))
        param_jeu[4] = police_Text.render(str(parametres["Tilt_effect2"]),True, Rouge[0])
        maSurface.blit(param_jeu[4], Coord_param_jeu[4])
    elif parametres["Tilt_effect2"] < 10 and x >=1035 and y >505 and x <= 1060 and y <=525:
        parametres["Tilt_effect2"] += 1
        pygame.draw.rect(maSurface, (0,0,0), (914,496,53,38))
        param_jeu[4] = police_Text.render(str(parametres["Tilt_effect2"]),True, Rouge[0])
        maSurface.blit(param_jeu[4], Coord_param_jeu[4])
        
    if parametres["Tilt_sensitivity2"] > 1 and x >=825 and y >580 and x <= 850 and y <=605:
        parametres["Tilt_sensitivity2"] -= 1
        pygame.draw.rect(maSurface, (0,0,0), (914,570,53,38))
        param_jeu[5] = police_Text.render(str(parametres["Tilt_sensitivity2"]),True, Rouge[0])
        maSurface.blit(param_jeu[5], Coord_param_jeu[5])
    elif parametres["Tilt_sensitivity2"] < 3 and x >=1035   and y >580 and x <= 1060 and y <=605:
        parametres["Tilt_sensitivity2"] += 1
        pygame.draw.rect(maSurface, (0,0,0), (914,570,53,38))
        param_jeu[5] = police_Text.render(str(parametres["Tilt_sensitivity2"]),True, Rouge[0])
        maSurface.blit(param_jeu[5], Coord_param_jeu[5])
    print(parametres)
    return parametres

def Controls(maSurface,controls,police_Text_C):
    police_Titre = pygame.font.Font('PKMN-Pinball.ttf', 40)
    police_Text = pygame.font.Font('PKMN-Pinball.ttf', 20)
    police = pygame.font.SysFont('arial',60)

    textP = police_Titre.render("Controls",True, (255,0,0))
    maSurface.blit(textP, (150, 100))
    text1 = police_Text.render("Flipper Left",True, (30,144,255))
    maSurface.blit(text1, (200, 200))
    pygame.draw.rect(maSurface,(30,144,255),(514,195,50,50),5)
    text2 = police_Text.render("Flipper Right",True, (30,144,255))
    maSurface.blit(text2, (200, 275))
    pygame.draw.rect(maSurface,(30,144,255),(514,270,50,50),5)
    text3 = police_Text.render("Add Coins",True, (30,144,255))
    maSurface.blit(text3, (200, 350))
    pygame.draw.rect(maSurface,(30,144,255),(514,345,50,50),5)
    text4 = police_Text.render("Add Players",True, (30,144,255))
    maSurface.blit(text4, (200, 425))
    pygame.draw.rect(maSurface,(30,144,255),(514,420,50,50),5)
    text5 = police_Text.render("Launcheur Down",True, (30,144,255))
    maSurface.blit(text5, (200, 500))
    pygame.draw.rect(maSurface,(30,144,255),(514,495,50,50),5)
    text6 = police_Text.render("Launcheur Up",True, (30,144,255))
    maSurface.blit(text6, (200, 575))
    pygame.draw.rect(maSurface,(30,144,255),(514,570,50,50),5)
    text1 = police_Text.render("Tilt Left",True, (30,144,255))
    maSurface.blit(text1, (750, 200))
    pygame.draw.rect(maSurface,(30,144,255),(1050,195,50,50),5)
    text2 = police_Text.render("Tilt Right",True, (30,144,255))
    maSurface.blit(text2, (750, 275))
    pygame.draw.rect(maSurface,(30,144,255),(1050,270,50,50),5)
    text3 = police_Text.render("Tilt Bottom",True, (30,144,255))
    maSurface.blit(text3, (750, 350))
    pygame.draw.rect(maSurface,(30,144,255),(1050,345,50,50),5)

    text = police_Titre.render("Back Home",True,(255,255,255) )
    maSurface.blit(text, (800,600))

    Image_Avion3 = pygame.image.load(os.path.join('Avion_3.png'))
    Image_Avion3.set_colorkey((0,0,0))
    maSurface.blit(Image_Avion3, (520,100))
    maSurface.blit(Image_Avion3, (770,50))
    maSurface.blit(Image_Avion3, (340,30))
    maSurface.blit(Image_Avion3, (1000, 100))
    maSurface.blit(Image_Avion3, (70, 15))

    Coordonnees = [(0,0),(530, 205),(530, 280),(530, 355),(530, 430),(530, 505),(530, 585),(1066, 205),(1066, 280),(1066, 355)]
    CoordonneesF = [(0,0),(516,197),(516,272),(516,347),(516,422),(516,497),(516,572),(1052,197),(1052,272),(1052,347)]
    for i in range(1,10):
        if controls[i] == "K_UP" or controls[i] == "K_DOWN" or controls[i] == "K_RIGHT" or controls[i] == "K_LEFT":
            fleche1 = pygame.image.load(controls[i]+'.jpg')
            maSurface.blit(fleche1,CoordonneesF[i])
        else:
            text_Control = police_Text_C.render(controls[i],True, (255,255,255))
            maSurface.blit(text_Control,Coordonnees[i])
    

    
def add_controls(maSurface,police_Text_C,C_Place,controls,carac):
    if C_Place > 0:
        if C_Place == 1:
            if carac == "K_UP" or carac == "K_DOWN" or carac == "K_RIGHT" or carac == "K_LEFT":
                fleche = pygame.image.load(carac+'.jpg')
                maSurface.blit(fleche,(516,197))
                controls[1] = carac
            else :
                pygame.draw.rect(maSurface,(0,0,0),(516,197,46,46))
                text = police_Text_C.render(carac,True, (255,255,255))
                maSurface.blit(text, (530, 205))
                controls[1] = carac
            C_Place = 0
        if C_Place == 2:
            if carac == "K_UP" or carac == "K_DOWN" or carac == "K_RIGHT" or carac == "K_LEFT":
                fleche = pygame.image.load(carac+'.jpg')
                maSurface.blit(fleche,(516,272))
                controls[2] = carac
            else: 
                pygame.draw.rect(maSurface,(0,0,0),(516,272,46,46))
                text = police_Text_C.render(carac,True, (255,255,255))
                maSurface.blit(text, (530, 280))
                controls[2] = carac
            C_Place = 0
        if C_Place == 3:
            if carac == "K_UP" or carac == "K_DOWN" or carac == "K_RIGHT" or carac == "K_LEFT":
                fleche = pygame.image.load(carac+'.jpg')
                maSurface.blit(fleche,(516,347))
                controls[3] = carac
            else:
                pygame.draw.rect(maSurface,(0,0,0),(516,347,46,46))
                text = police_Text_C.render(carac,True, (255,255,255))
                maSurface.blit(text, (530, 355))
                controls[3] = carac
            C_Place = 0
        if C_Place == 4:
            if carac == "K_UP" or carac == "K_DOWN" or carac == "K_RIGHT" or carac == "K_LEFT":
                fleche = pygame.image.load(carac+'.jpg')
                maSurface.blit(fleche,(516,422))
                controls[4] = carac
            else:    
                pygame.draw.rect(maSurface,(0,0,0),(516,422,46,46))
                text = police_Text_C.render(carac,True, (255,255,255))
                maSurface.blit(text, (530, 430))
                controls[4] = carac
            C_Place = 0
        if C_Place == 5:
            if carac == "K_UP" or carac == "K_DOWN" or carac == "K_RIGHT" or carac == "K_LEFT":
                fleche = pygame.image.load(carac+'.jpg')
                maSurface.blit(fleche,(516,497))
                controls[5] = carac
            else:    
                pygame.draw.rect(maSurface,(0,0,0),(516,497,46,46))
                text = police_Text_C.render(carac,True, (255,255,255))
                maSurface.blit(text, (530, 505))
                controls[5] = carac
            C_Place = 0
        if C_Place == 6:
            if carac == "K_UP" or carac == "K_DOWN" or carac == "K_RIGHT" or carac == "K_LEFT":
                fleche = pygame.image.load(carac+'.jpg')
                maSurface.blit(fleche,(516,572))
                controls[6] = carac
            else:    
                pygame.draw.rect(maSurface,(0,0,0),(516,572,46,46))
                text = police_Text_C.render(carac,True, (255,255,255))
                maSurface.blit(text, (530, 585))
                controls[6] = carac
            C_Place = 0
        if C_Place == 7:
            if carac == "K_UP" or carac == "K_DOWN" or carac == "K_RIGHT" or carac == "K_LEFT":
                fleche = pygame.image.load(carac+'.jpg')
                maSurface.blit(fleche,(1052,197))
                controls[7] = carac
            else:    
                pygame.draw.rect(maSurface,(0,0,0),(1052,197,46,46))
                text = police_Text_C.render(carac,True, (255,255,255))
                maSurface.blit(text, (1066, 205))
                controls[7] = carac
            C_Place = 0
        if C_Place == 8:
            if carac == "K_UP" or carac == "K_DOWN" or carac == "K_RIGHT" or carac == "K_LEFT":
                fleche = pygame.image.load(carac+'.jpg')
                maSurface.blit(fleche,(1052,272))
                controls[8] = carac
            else:
                pygame.draw.rect(maSurface,(0,0,0),(1052,272,46,46))
                text = police_Text_C.render(carac,True, (255,255,255))
                maSurface.blit(text, (1066, 280))
                controls[8] = carac
            C_Place = 0
        if C_Place == 9:
            if carac == "K_UP" or carac == "K_DOWN" or carac == "K_RIGHT" or carac == "K_LEFT":
                fleche = pygame.image.load(carac+'.jpg')
                maSurface.blit(fleche,(1052,347))
                controls[9] = carac
            else:
                pygame.draw.rect(maSurface,(0,0,0),(1052,347,46,46))
                text = police_Text_C.render(carac,True, (255,255,255))
                maSurface.blit(text, (1066, 355))
                controls[9] = carac
            C_Place = 0


parametres = {"nombreBall2":1,"free_game_score2":0000000,"angle_incline2":0,"Ball_speed2":1,"Tilt_effect2":1,"Tilt_sensitivity2":1}
controls = {1:"K_UP",2:"K_DOWN",3:"K_LEFT",4:"K_RIGHT",5:"Q",6:"S",7:"T",8:"G",9:"Y"}
C_Place = 0
para = 0
police_Text_C = pygame.font.Font('PKMN-Pinball.ttf', 20)
menu_Paramètre(maSurface)
inProgress = True
while inProgress:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if para == 0 :
                if event.button == 1:
                    config_parametres(maSurface,parametres)
                if x >=591 and y >645 and x <= 1198 and y <=690:
                    maSurface = pygame.display.set_mode((1280,720))
                    Controls(maSurface,controls,police_Text_C)
                    para = 1
            else :
                if C_Place == 0:
                    if 516 < x < 562 and 197< y < 243:
                        pygame.draw.rect(maSurface,(64,212,126),(516,197,46,46))
                        C_Place = 1
                    elif 516 < x < 562 and 272 < y < 318:
                        pygame.draw.rect(maSurface,(64,212,126),(516,272,46,46))
                        C_Place = 2
                    elif 516 < x < 562 and 347 < y < 393:
                        pygame.draw.rect(maSurface,(64,212,126),(516,347,46,46))
                        C_Place = 3
                    elif 516 < x < 562 and 422 < y < 468:
                        pygame.draw.rect(maSurface,(64,212,126),(516,422,46,46))
                        C_Place = 4
                    elif 516 < x < 562 and 497 < y < 543:
                        pygame.draw.rect(maSurface,(64,212,126),(516,497,46,46))
                        C_Place = 5
                    elif 516 < x < 562 and 572 < y < 618:
                        pygame.draw.rect(maSurface,(64,212,126),(516,572,46,46))
                        C_Place = 6
                    elif 1052 < x < 1098 and 197 < y < 243:
                        pygame.draw.rect(maSurface,(64,212,126),(1052,197,46,46))
                        C_Place = 7
                    elif 1052 < x < 1098 and 272 < y < 318:
                        pygame.draw.rect(maSurface,(64,212,126),(1052,272,46,46))
                        C_Place = 8
                    elif 1052 < x < 1098 and 347 < y < 393:    
                        pygame.draw.rect(maSurface,(64,212,126),(1052,347,46,46))
                        C_Place = 9
                    elif 800 < x < 1115 and 600 < y < 660:
                        print("home")
        if event.type == KEYDOWN:
            carac = event.dict['key']
            f = 0
            if carac == 273:
                carac = "K_UP"
            elif carac == 274:
                carac = "K_DOWN"
            elif carac == 275:
                carac = "K_RIGHT"
            elif carac == 276:
                carac = "K_LEFT"
            else :
                carac = event.dict['unicode']
                carac = carac.upper()
            for i in range(1,10):
                if controls[i] == carac:
                    f += 1
            print(controls)
            print(C_Place)
            if f == 0:        
                add_controls(maSurface,police_Text_C,C_Place,controls,carac)
                C_Place = 0
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
pygame.quit()
