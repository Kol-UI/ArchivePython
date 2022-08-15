import pygame, sys, os
from pygame.locals import *
pygame.init()


def Game_Commun(maSurface):
    pygame.draw.line(maSurface, (255, 255, 255), (340, 0), (340, 720), 5)
    pygame.draw.line(maSurface, (255, 255, 255), (940, 0), (940, 720), 5)

    pygame.draw.line(maSurface, (255, 255, 255), (0, 0), (0, 720), 5)

def Game_Center(maSurface):
    pygame.draw.arc(maSurface, (255, 255, 255), (660, 10, 285, 275), 0, 1.45, 10)  #Arc en haut à droite
    
    Couleur = [(255, 255, 255),(25, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(255, 0, 0),(255, 0, 0),(255, 0, 0),(255, 0, 0),(255, 0, 0),(255, 0, 0),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(225, 0, 0),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(30,144,255),(30,144,255),(30,144,255),(30,144,255),(30,144,255),(30,144,255),(30,144,255),(30,144,255),(30,144,255),(30,144,255),(30,144,255),(30, 144, 255),(30, 144, 255),(30, 144, 255),(30, 144, 255),(30, 144, 255),(255, 0, 0),(255, 0, 0),(255, 0, 0),(255, 0, 0),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(0, 224, 2),(255,255,255),(255,255,255),(255, 255, 255),(255, 255, 255),(30, 144, 255),(30, 144, 255)]
    Position_1 = [(885, 589),(885, 589),(345, 0),(940, 0),(342, 415),(400, 370),(910, 150),(600, 16),(530, 35),(380, 35),(342, 70),(385, 95),(445, 330),(535, 285),(535, 285),(400, 270),(555, 113),(555, 113),(555, 160),(418, 120),(502, 120),(418, 240),(525, 99),(418, 120),(525, 99),(620, 120),(660, 105),(700, 90),(740, 90),(780, 105),(820, 120),(570, 240),(909, 243),(845, 328),(898, 368),(885, 388),(845,498),(845,498),(833,487),(762,601),(770,611),(445,471),(445,548),(433,563),(443,578),(516,601),(516,601),(456, 330),(481, 317),(506, 304),(493, 68),(510, 81),(865, 418),(876, 448),(876, 493),(856, 438),(879, 591),(882, 591),(760, 641),(881, 643),(414, 592),(516, 641),(394, 641),(394, 550),(394, 550),(370, 470),(395, 470),(420, 470),(845, 338),(868, 357)]
    Position_2 = [(940, 589),(885, 720),(345, 410),(940, 720),(405, 370),(342, 260),(910, 720),(825, 16),(600, 16),(530, 35),(380, 35),(385, 250),(385, 250),(445, 330),(535, 130),(535, 270),(535, 130),(555, 160),(535, 190),(418, 240),(502, 240),(502, 240),(502, 120),(486, 69),(486, 69),(620, 170),(660, 155),(700, 140),(740, 140),(780, 155),(820, 170),(570, 285),(845,328),(898,368),(885,388),(909,458),(845,578),(833,487),(762,601),(770,611),(845,578),(445,548),(433,563),(443,578),(508,611),(445,471),(508,611),(478, 320),(503, 307),(528, 294),(507, 79),(524, 92),(876, 448),(876, 493),(856, 438),(865, 418),(879, 535),(760, 641),(882, 641),(881, 592),(516, 641),(394, 641),(394, 550),(414, 592),(370, 550),(370, 550),(395, 490),(420, 490),(865, 354),(887, 371)]
    Taille = [2,3,10,11,10,10,3,10,10,10,10,4,4,4,4,4,4,4,4,6,6,6,6,6,6,8,8,8,8,8,8,10,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,5,5,5,5,3,3,3,3,8,4,4,4,4,4,4,4,1,1,1,1,5,5]
    for i in range(0, len(Position_1)):
        pygame.draw.line(maSurface, Couleur[i], Position_1[i], Position_2[i],Taille[i])


    policeBonus = pygame.font.Font("PKMN-Pinball.ttf", 13)  # Police des Bonus

    textA = policeBonus.render("A", True, (30, 144, 255))  # Lettre Bonus A
    maSurface.blit(textA, (843, 350))
    textB = policeBonus.render("B", True, (30, 144, 255))  # Lettre Bonus B
    maSurface.blit(textB, (864, 367))

    #Text Bonus
    textN = policeBonus.render("N", True, (30, 144, 255)) # Les prochaines lignes sont consacrées aux bonus "n""i""g""h""t" qui sont en haut
    maSurface.blit(textN, (633, 124))
    textI = policeBonus.render("I", True, (30, 144, 255))
    maSurface.blit(textI, (677, 109))
    textG = policeBonus.render("G", True, (30, 144, 255))
    maSurface.blit(textG, (713, 102))
    textH = policeBonus.render("H", True, (30, 144, 255))
    maSurface.blit(textH, (753, 109))
    textT = policeBonus.render("T", True, (30, 144, 255))
    maSurface.blit(textT, (793, 124))

    textF = policeBonus.render("F", True, (30, 144, 255)) # Les prochaines lignes sont consacrées aux bonus "f""l""y" qui sont au milieu
    maSurface.blit(textF, (465, 330))
    textL = policeBonus.render("L", True, (30, 144, 255))
    maSurface.blit(textL, (491, 317))
    textY = policeBonus.render("Y", True, (30, 144, 255))
    maSurface.blit(textY, (514, 306))
    
    textC = policeBonus.render("C", True, (30, 144, 255)) # Les prochaines lignes sont consacrées aux bonus "c""d" qui sont en haut 
    maSurface.blit(textC, (500, 53))
    textD = policeBonus.render("D", True, (30, 144, 255))
    maSurface.blit(textD, (517, 66))

    # Bumper
    Couleur_2 = [(255, 0, 0),(255, 0, 0),(30, 144, 255),(30, 144, 255),(30, 144, 255),(255, 0, 0)]
    Position_3 = [(725, 260),(725, 260),(625, 215),(830, 215),(715, 360),(570, 385)]
    Rayon = [20,10,15,15,15,20]
    Taille = [5,3,0,0,0,5]
    for i in range(0, len(Taille)):
        pygame.draw.circle(maSurface,Couleur_2[i],Position_3[i],Rayon[i],Taille[i])


    #test
    #triangle blanc a gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (350, 271, 6, 137), 4)
    pygame.draw.rect(maSurface, (255, 255, 0), (354, 290, 10, 115), 4)
    pygame.draw.rect(maSurface, (255, 255, 0), (366, 303, 6, 97), 10)
    pygame.draw.rect(maSurface, (255, 255, 0), (377, 323, 6, 70), 7)
    pygame.draw.rect(maSurface, (255, 255, 0), (386, 339, 6, 50), 5)
    pygame.draw.rect(maSurface, (255, 255, 0), (394, 354, 6, 30), 5)
    pygame.draw.rect(maSurface, (255, 255, 0), (402, 366, 4, 10), 3)
    #triangles blancs sur la droite
    pygame.draw.rect(maSurface, (255, 255, 0), (847, 324, 4, 8), 2)
    pygame.draw.rect(maSurface, (255, 255, 0), (853, 318, 4, 18), 4)
    pygame.draw.rect(maSurface, (255, 255, 0), (859, 309, 4, 30), 4)
    pygame.draw.rect(maSurface, (255, 255, 0), (866, 307, 40, 37), 5)
    pygame.draw.rect(maSurface, (255, 255, 0), (873, 348, 35, 2), 5)
    pygame.draw.rect(maSurface, (255, 255, 0), (883, 351, 27, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (869, 296, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (877, 287, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (883, 277, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (891, 267, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (900, 257, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (905, 250, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (889, 355, 7, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (896, 362, 7, 67), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (889, 380, 7, 25), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (903, 361, 7, 85), 3)
    #le plafond
    pygame.draw.rect(maSurface, (255, 255, 0), (349, 52, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (359, 46, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (369, 38, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (380, 31, 150, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (530, 30, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (540, 27, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (550, 24, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (560, 21, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (570, 18, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (580, 15, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (590, 12, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (600, 12, 270, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (852, 23, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (870, 28, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (880, 39, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (894, 50, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (906, 61, 20, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (925, 72, 10, 30), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (914, 72, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (920, 83, 6, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (930, 103, 6, 10), 3)
    #triangle vert en bas à gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (407, 595, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (417, 600, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (427, 605, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (437, 611, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (447, 615, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (457, 619, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (467, 623, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (477, 627, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (487, 631, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (497, 635, 10, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (508, 640, 6, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (403, 584, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (399, 575, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (395, 564, 8, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (395, 556, 5, 6), 3)
    #triangle vert en bas à droite
    pygame.draw.rect(maSurface, (255, 255, 0), (869, 595, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (858, 601, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (848, 606, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (838, 611, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (827, 615, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (816, 619, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (805, 623, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (794, 627, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (783, 631, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (772, 635, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (763, 639, 8, 6), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (783, 639, 100, 5), 2)
    #les cotés
    pygame.draw.rect(maSurface, (255, 255, 0), (340, 0, 10, 418), 5)
    pygame.draw.rect(maSurface, (255, 255, 0), (936, 0, 10, 720), 2)
    #les lignes vertes
    pygame.draw.rect(maSurface, (255, 255, 0), (617, 120, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (657, 105, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (697, 90, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (737, 90, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (777, 105, 8, 50), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (818, 120, 8, 50), 3)
    #ligne rouge
    pygame.draw.rect(maSurface, (255, 255, 0), (566, 240, 10, 48), 3)
    #truc vert qui est en haut
    pygame.draw.rect(maSurface, (255, 255, 0), (536, 132, 21, 28), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (545, 121, 12, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (551, 115, 6, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (539, 126, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (535, 161, 20, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (536, 168, 14, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (536, 176, 7, 7), 3)
    #truc rouge qui est en haut
    pygame.draw.rect(maSurface, (255, 255, 0), (418, 122, 85, 119), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (461, 88, 43, 35), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (439, 105, 20, 17), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (450, 96, 15, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (427, 112, 15, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (474, 78, 25, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (481, 73, 10, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (505, 93, 13, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (517, 97, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (504, 109, 5, 5), 3)
    #truc bleu qui est en bas a droite
    pygame.draw.rect(maSurface, (255, 255, 0), (826, 499, 20, 80), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (798, 546, 45, 35), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (811, 526, 20, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (819, 514, 20, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (805, 536, 20, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (831, 493, 10, 30), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (791, 556, 10, 45), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (785, 566, 10, 36), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (778, 576, 10, 30), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (773, 587, 10, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (766, 596, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (768, 607, 7, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (798, 581, 30, 7), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (800, 590, 10, 5), 3)
    #truc rouge en bas à droite
    pygame.draw.rect(maSurface, (255, 255, 0), (859, 428, 10, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (863, 421, 5, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (866, 446, 10, 20), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (860, 439, 13, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (863, 449, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (872, 467, 4, 15), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (873, 482, 3, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (869, 467, 3, 6), 3)
    #truc vert en haut à gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (535, 184, 3, 100), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (385, 95, 3, 154), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (439, 271, 98, 12), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (411, 282, 28, -10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (405, 277, 4, -5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (418, 284, 103, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (521, 284, 11, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (425, 295, 76, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (502, 295, 10, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (432, 305, 50, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (482, 306, 8, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (439, 316, 27, 5), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (444, 322, 11, 6), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (386, 250, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (389, 253, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (392, 257, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (394, 260, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (396, 264, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (399, 267, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (402, 270, 3, 3), 3)
    #trait blanc bas gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (338, 420, 5, 295), 3)
    #trait blanc à droite (lanceur)
    pygame.draw.rect(maSurface, (255, 255, 0), (909, 150, 2, 563), 3)
    #suite du triangle vert en bas à gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (395, 573, 3, 70), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (395, 641, 100, 3), 3)
    #trait vert en bas à droite
    pygame.draw.rect(maSurface, (255, 255, 0), (876, 536, 7, 70), 3)
    #trait vert en bas à gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (885, 644, 2, 70), 3)
    #traits blanc en bas à gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (370, 470, 1, 80), 1)
    pygame.draw.rect(maSurface, (255, 255, 0), (370, 550, 20, 1), 1)
    pygame.draw.rect(maSurface, (255, 255, 0), (394, 552, 3, 3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (395, 470, 1, 20), 1)
    pygame.draw.rect(maSurface, (255, 255, 0), (420, 471, 1, 20), 1)
    #truc bleu en bas à gauche
    pygame.draw.rect(maSurface, (255, 255, 0), (514, 598, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (509, 588, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (504, 578, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (499, 568, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (494, 558, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (487, 548, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (480, 538, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (475, 528, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (470, 518, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (465, 508, -10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (445, 497, 15, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (445, 473, 3, 25), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (448, 486, 7, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (445, 507, 3, 40), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (446, 579, 10, -10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (456, 583, 10, -10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (465, 588, 10, -10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (475, 593, 10, -10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (485, 598, 10, -10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (493, 603, 8, -3), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (437, 559, 10, 10), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (444, 569, -4, 4), 3)
    pygame.draw.rect(maSurface, (255, 255, 0), (442, 557, 10, -7), 3)
    #ligne blanche horizontale en bas à droite
    pygame.draw.rect(maSurface, (255, 255, 0), (883, 590, 27, 1), 3)




def Game_Left(maSurface,police):
    Mots = ["1", "2", "3", "4", "CREDITS", "BALL"]
    Position_1 = [(160, 10), (160, 120), (160, 230), (160, 340), (38, 600), (210, 600)]
    Position_2 = [(40, 60, 260, 50), (40, 170, 260, 50), (40, 280, 260, 50), (40, 390, 260, 50), (40, 650, 140, 50), (200, 650, 100, 50)]

    for i in range(0, 6):
        text = police.render(Mots[i], True, (30, 144, 255))
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

    text = police.render("SUBLOGIC", True, (255, 0, 0))
    maSurface.blit(text, (1015, 10))

    text = policenight.render("Night", True, (30, 144, 255))
    maSurface.blit(text, (970, 60))
        
    Mots = ["M", "i", "s", "s", "i", "o", "n"]
    Position = [(1209, 148), (1230, 236), (1217, 318), (1217, 398), (1230, 478), (1217, 558), (1217, 634)]
    for i in range(0, 7):
        text = policenight2.render(Mots[i], True, (30, 144, 255))
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

    textAddPlayer = police.render("add  player", True, (30, 144, 255)) # "Add player" à droite
    maSurface.blit(textAddPlayer, (952, 452))
    
    textPress = police.render("press", True, (30, 144, 255)) # "Press S" à droite
    maSurface.blit(textPress, (1048, 505))
    textS = police.render("S", True, (255, 0, 0))
    maSurface.blit(textS, (1155, 505))
    maSurface.blit(textPress, (1048, 680))
    textQ = police.render("Q", True, (255, 0, 0))
    maSurface.blit(textQ, (1155, 680))


def Balle(maSurface):
    pygame.draw.circle(maSurface, (255, 255, 255), (924, 579), 9, 9)


maSurface = pygame.display.set_mode((1280, 720))
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
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            print(x,y)
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
pygame.quit
