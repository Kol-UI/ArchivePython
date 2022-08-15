import pygame, sys, os
from pygame.locals import *
pygame.init()

def menu(maSurface, polici):                                              
    Mots=["COPYRIGHT 1982 BY BRUCE A. ARTWICK","NEW VERSION BY TEAM ROCKET","SELECT OPERATING MODE :","A. REGULAR GAME MODE",
            "B. INSTRUCTIONS","<TYPE A OR B>"]
    Positions_1=[367,410,450,450,450,450]
    Positions_2=[210,245,320,355,390,450]
    for i in range(0, 6):
        title = polici.render((Mots[i]), True, (255, 255, 255))
        maSurface.blit(title, (Positions_1[i], Positions_2[i]))
    # C. DEMO MODE ?
    
def menu_Page(maSurface, polici, page):
    if page == 1:
        Mots=["NIGHT MISSION INSTRUCTIONS","CONTROLS :","LEFT FLIPPER = LEFT ARROW","RIGHT FLIPPER = RIGHT ARROW","STRIKER PULL =  F7 KEY",
              "STRIKER LESS =  F1 KEY","BALL LAUNCH = SPACE BAR","GAME STARTUP : INSERTS THE NUMBER OF COINS ACCORDING TO THE","NUMBER OF PLAYERS",
              "PRESS SPACE BAR FOR NEXT PAGE........."]
        Positions_1=[400,35,70,70,70,70,70,35,35,35]
        Positions_2=[50,125,160,195,230,265,300,375,410,670]
        for i in range(0, 10):
            text = polici.render((Mots[i]), True, (255, 255, 255))
            maSurface.blit(text, (Positions_1[i], Positions_2[i]))

   
    if page == 2:
        Mots=["SCORE DIGITS : DIGITS INDICATE SCORE.","FLASHING DIGITS INDICATE PLAYERS TURN.","TILT : BUMP TABLE RIGHT BY PRESSING ???.","BUMP TABLE LEFT BY PRESSING ????","GAME PAUSE : PRESS THE KEY P TO PAUSE THE GAME.",
              "PRESS ANY OTHER KEY TO RESUME PLAY.","PRESS THE P KEY MANY TIMES TO SINGLE STEP THE GAME.","SYSTEM RESTART : MACHINE MUST BE TURNED OFF AND ON AGAIN.","PRESS SPACE BAR FOR NEXT PAGE........."]
        Positions_1=[35,35,35,35,35,35,35,35,35]
        Positions_2=[50,85,160,195,270,305,340,415,670]
        for i in range(0, 9):
            text = polici.render((Mots[i]), True, (255, 255, 255))
            maSurface.blit(text, (Positions_1[i], Positions_2[i]))

        
    if page == 3:
        Mots=["SCORING","A,B,C,D,E,F,L,Y = 1000 & BONUS ADVANCE","NIGHT ROLLOVER = 1500 & BONUS ADVANCE","DROP ROLLOVERS = 2000","LARGE BUMPERS = 90",
              "SMALL BUMPERS = 50","OUTER SPINNER = 100 POINTS <500 LIT>","SEQUENCES :","FLY = 5000","DROP = 10.000","ABCD = ADVANCE BONUS MULTIPLIER","ROP BUT NOT D = LITES SPECIAL","NIGHT SEQUENCE = 10.000, LITES NIGHT ARROWS,",
              "AND ACTIVATES BOMB RELEASE LINE CITY TARGETS.","PRESS SPACE BAR FOR NEXT PAGE........."]
        Positions_1=[580,35,35,35,35,35,35,35,35,35,35,35,35,35,35]
        Positions_2=[50,125,160,195,230,265,300,375,410,445,480,515,550,585,670]
        for i in range(0, 15):
            text = polici.render((Mots[i]), True, (255, 255, 255))
            maSurface.blit(text, (Positions_1[i], Positions_2[i]))

    if page == 4:
        Mots=["SCORING <CONTINUED>","NIGHT AND ALL CITIES BOMBED AND ABCD LITES 25,000 POINT DIVE BOMB ARROW","BOMB RELEASE LINE ENTRY = 5000","DIVE BOMB CHUTE ENTRY = CLOSE D-LANE GATE (IF MODE HAS THIS FEATURE)",
              "CAPTIVE HOLE :","1ST TURNS ON NIGHT LANE LITES","2ND TURNS ON DROP ARROWS","3RD INCREASES OUTER SPINNER TO 500","4TH ROTATES DROP ARROWS","NIGHT LANE LITES: ROTATE USING EITHER FLIPPER.",
              "NEW BALL TURNS OFF SYSTEM. LANE LITE COMPLETION = 5000 POINTS","PRESS SPACE BAR FOR NEXT PAGE........."]
        Positions_1=[475,35,35,35,35,70,70,70,70,35,35,35]
        Positions_2=[50,125,180,235,290,325,360,395,430,485,540,670]
        for i in range(0, 12):
            text = polici.render((Mots[i]), True, (255, 255, 255))
            maSurface.blit(text, (Positions_1[i], Positions_2[i]))
            
    if page == 5:
        Mots=["SCORING <CONTINUED>","DIVE BOMB : INNER SPINNER = 200 & LITES","CITY LITES <1000 POINTS PER LITE>.","ALSO SPOTS ABCD TARGETS.","MULTI-BALL PLAY : IF NIGHT, FLY SEQUENCE ACTIVATES",
              "CHUTE HOLD GATE, BALLS IN CHUTE ARE HELD, AND BOMB AGAIN BALL GIVEN.","ABCD, BALL DRAIN, OR 4 BALLS IN CHUTE RELEASE ALL HELD BALLS.","MULTI-PLAYER : NIGHT SEQUENCE KEPT TRACK OF FOR EACH PLAYER",
              "TILT PENALTY : ONE BALL AND ANY CURRENT BONUS COUNTDOWN POINTS","PRESS SPACE BAR FOR NEXT PAGE........."]
        Positions_1=[475,35,35,35,35,35,35,35,35,35]
        Positions_2=[50,125,160,195,270,305,340,415,490,670]
        for i in range(0, 10):
            text = polici.render((Mots[i]), True, (255, 255, 255))
            maSurface.blit(text, (Positions_1[i], Positions_2[i]))
        
    if page == 6:
        Mots=["AWARDS","SPECIAL : D AFTER ROP GIVES FREE GAME AND 30.000 POINTS","FREE GAME SCORE EXCEEDED : FREE GAME","HIGH SCORE EXCEEDED : 3 FREE GAMES",
              "GENERALS STARS : ONE STAR PER EACH 1.000.000 POINTS.","STAR APPEAR ABOVE EACH PLAYERS SCORE DIGITS.","PRESS SPACE BAR FOR NEXT PAGE........."]
        Positions_1=[580,35,35,35,35,35,35]
        Positions_2=[50,125,200,275,350,385,670]
        for i in range(0, 7):
            text = polici.render((Mots[i]), True, (255, 255, 255))
            maSurface.blit(text, (Positions_1[i], Positions_2[i]))
        
    if page == 7:
        Mots=["OTHER FEATURES","JOYSTICK CONTROL : JOYSTICK FIRE BUTTONS CAN BE USED FOR FLIPPER CONTROL.","PUSH THE RIGHT STICK FOREWARD AND BACK FOR STRICKER CONTROL.","FIX MODE : HIT F I X TO ENTER THE FIX MODE.",
              "YOU CAN ADJUST 38 GAME VARIABLES USING THIS SYSTEM BY ENTERING", "NEW VALUES FOLLOWED BY RETURN.","HIT CLR TO EXIT BACK INTO GAME PLAY MODE.","HIGH SCORE DISK : INSERT FORMATTED DISK AND HIT CTRL R",
              "OR CTRL W TO READ OR WRITE THE CURRENT MODE AND HIGH SCORE.","PRESS SPACE BAR FOR NEXT PAGE........."]
        Positions_1=[520,35,35,35,35,35,35,35,35,35]
        Positions_2=[50,125,160,235,270,305,340,415,450,670]
        for i in range(0, 10):
            text = polici.render((Mots[i]), True, (255, 255, 255))
            maSurface.blit(text, (Positions_1[i], Positions_2[i]))

    if page == 8:
        Mots=["COLOR DESIGNER","SCREEN COLOR CAN BE MODIFIED USING THE COLOR DESIGNER SYSTEM.","THE FOLLOWING KEYS CONTROL COLOR:","F3  = HIGH/LOW RESOLUTION SELECT","F5  = COLOR NYBBLE CONTROL",
              "&   = SCREEN NYBBLE LSB CONTROL"," *   = SCREEN NYBBLE MSB CONTROL","=   = BORDER COLOR CONTROL","C   = BACKGROUND COLOR 0","THE BEST WAY TO GET FAMILIAR WITH THESE KEYS IS BY EXPERIMENTING.",
              "COLOR CHANGES AFFECT TEXT AS WELL AS GRAPHICS.","IF ALL TEXT VANISHES PRESS F5 TO GET SOME COLOR CONTRAST.","PRESS SPACE BAR FOR NEXT PAGE........."]
        Positions_1=[520,35,35,35,35,35,35,35,35,35,35,35,35]
        Positions_2=[50,125,160,235,270,305,340,375,415,490,525,560,670]
        for i in range(0, 13):
            text = polici.render((Mots[i]), True, (255, 255, 255))
            maSurface.blit(text, (Positions_1[i], Positions_2[i]))

    if page == 9:
        Mots=["GOOD LUCK ON YOUR NIGHT MISSION !!!","PRESS SPACE BAR FOR NEXT PAGE........."]
        Positions_1=[370,35]
        Positions_2=[350,670]
        for i in range(0, 2):
            text = polici.render((Mots[i]), True, (255, 255, 255))
            maSurface.blit(text, (Positions_1[i], Positions_2[i]))

#python.version


