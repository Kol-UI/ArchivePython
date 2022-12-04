import time
import random

Murloc, Guerrier, Lancier, Archer, Oracle, Sorciere, Chaman, Démoniste, Brute, GéantdesMers, Char, Elementaliste,\
ElementaireEau,Arcaniste, Pretresse, Murgul, Sirens, GardeRoyal, DragonEau, Esclavagiste, Esclaves, SerpentdesMers,\
Meduse, Poulpe, CréatureProfondeurs, Rampant, Crabe, ElementaireVide, ElementaireMarais\
    = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

def main(Murloc, Guerrier, Lancier, Archer, Oracle, Sorciere, Chaman, Démoniste, Brute, GéantdesMers, Char,
         Elementaliste, ElementaireEau, Arcaniste, Pretresse, Murgul, Sirens, GardeRoyal, DragonEau, Esclavagiste,
         Esclaves, SerpentdesMers, Meduse, Poulpe, CréatureProfondeurs, Rampant, Crabe, ElementaireVide,
         ElementaireMarais):

    i = 100
    secondes = 0
    heures = 0
    minutes = 0
    Dragon = 0

    while secondes < i:
        time.sleep(1)
        secondes += 1
        Dragon += 1
        if secondes == 60:
            secondes = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                heures += 1
                print("\n", secondes, "S ", minutes, "M ", heures, "H", )
            else:
                print("\n", secondes, "S ", minutes, "M ", heures, "H", )
        else:
            print("\n", secondes, "S ", minutes, "M ", heures, "H", )

            rnd = random.choice(['Murloc1','Murloc2','Murloc3','Murloc4', 'Murloc5', 'Murloc6', 'Guerrier1',
                                 'Guerrier2', 'Guerrier3', 'Lancier1', 'Lancier2', 'Archer1', 'Archer2', 'Oracle',
                                 'Sorciere', 'Chaman', 'Démoniste',
                                 'Brute', 'GéantdesMers', 'Char1', 'Char2', 'Elementaliste', 'ElementaireEau1',
                                 'ElementaireEau2','ElementaireEau3', 'Arcaniste', 'Pretresse', 'Murgul1', 'Murgul2',
                                 'Sirens', 'GardeRoyal','DragonEau', 'Esclavagiste', 'Esclaves1', 'Esclaves2',
                                 'SerpentdesMers', 'Meduse', 'Poulpe','CréatureProfondeurs', 'Rampant1', 'Rampant2',
                                 'Rampant3', 'Crabe', 'ElementaireVide1','ElementaireVide2', 'ElementaireVide3',
                                 'ElementaireMarais1','ElementaireMarais2','ElementaireMarais3'])
            if rnd == 'Murloc1':
                Murloc += 1
            elif rnd == 'Murloc2':
                Murloc += 1
            elif rnd == 'Murloc3':
                Murloc += 1
            elif rnd == 'Murloc4':
                Murloc += 1
            elif rnd == 'Murloc5':
                Murloc += 1
            elif rnd == 'Murloc6':
                Murloc += 1
            elif rnd == 'Guerrier1':
                Guerrier += 1
            elif rnd == 'Guerrier2':
                Guerrier += 1
            elif rnd == 'Guerrier3':
                Guerrier += 1
            elif rnd == 'Lancier1':
                Lancier += 1
            elif rnd == 'Lancier2':
                Lancier += 1
            elif rnd == 'Archer1':
                Archer += 1
            elif rnd == 'Archer2':
                Archer += 1
            elif rnd == 'Oracle':
                Oracle += 1
            elif rnd == 'Sorciere':
                Sorciere += 1
            elif rnd == 'Chaman':
                Chaman += 1
            elif rnd == 'Démoniste':
                Démoniste += 1
            elif rnd == 'Brute':
                Brute += 1
            elif rnd == 'GéantdesMers':
                GéantdesMers += 1
            elif rnd == 'Char1':
                Char += 1
            elif rnd == 'Char2':
                Char += 1
            elif rnd == 'Elementaliste':
                Elementaliste += 1
            elif rnd == 'ElementaireEau1':
                ElementaireEau += 1
            elif rnd == 'ElementaireEau2':
                ElementaireEau += 1
            elif rnd == 'ElementaireEau3':
                ElementaireEau += 1
            elif rnd == 'Arcaniste':
                Arcaniste += 1
            elif rnd == 'Pretresse':
                Pretresse += 1
            elif rnd == 'Murgul1':
                Murgul += 1
            elif rnd == 'Murgul2':
                Murgul += 1
            elif rnd == 'Sirens':
                Sirens += 1
            elif rnd == 'GardeRoyal':
                GardeRoyal += 1
            elif rnd == 'DragonEau':
                DragonEau += 1
            elif rnd == 'Esclavagiste':
                Esclavagiste += 1
            elif rnd == 'Esclaves1':
                Esclaves += 1
            elif rnd == 'Esclaves2':
                Esclaves += 1
            elif rnd == 'SerpentdesMers':
                SerpentdesMers += 1
            elif rnd == 'Meduse':
                Meduse += 1
            elif rnd == 'Poulpe':
                Poulpe += 1
            elif rnd == 'CréatureProfondeurs':
                CréatureProfondeurs += 1
            elif rnd == 'Rampant1':
                Rampant += 1
            elif rnd == 'Rampant2':
                Rampant += 1
            elif rnd == 'Rampant3':
                Rampant += 1
            elif rnd == 'Crabe':
                Crabe += 1
            elif rnd == 'ElementaireVide1':
                ElementaireVide += 1
            elif rnd == 'ElementaireVide2':
                ElementaireVide += 1
            elif rnd == 'ElementaireVide3':
                ElementaireVide += 1
            elif rnd == 'ElementaireMarais1':
                ElementaireMarais += 1
            elif rnd == 'ElementaireMarais2':
                ElementaireMarais += 1
            elif rnd == 'Elementaire Marais3':
                ElementaireMarais += 1

            print('\n', Murloc, 'Murloc', Guerrier, 'Guerrier', Lancier, 'Lancier', Archer, 'Archer', Oracle, 'Oracle',
                  Sorciere, 'Sorciere\n', Chaman, 'Chaman', Démoniste, 'Démoniste', Brute, 'Brute',
                  GéantdesMers, 'GéantdesMers', Char, 'Char', Elementaliste, 'Elementaliste',
                  ElementaireEau, 'ElementaireEau', Arcaniste, 'Arcaniste', Pretresse, 'Pretresse\n', Murgul, 'Murgul',
                  Sirens, 'Sirens', GardeRoyal, 'GardeRoyal', DragonEau, 'DragonEau', Esclavagiste, 'Esclavagiste',
                  Esclaves, 'Esclaves\n', Esclaves, 'Esclaves', SerpentdesMers, 'SerpentdesMers', Meduse, 'Meduse',
                  Poulpe, 'Poulpe', CréatureProfondeurs, 'CréatureProfondeurs', Rampant, 'Rampant\n', Crabe, 'Crabe',
                  ElementaireVide, 'ElementaireVide', ElementaireMarais, 'ElementaireMarais')
            print('\n', Dragon, 'Dragon')

main(Murloc, Guerrier, Lancier, Archer, Oracle, Sorciere, Chaman, Démoniste, Brute, GéantdesMers, Char,
         Elementaliste, ElementaireEau, Arcaniste, Pretresse, Murgul, Sirens, GardeRoyal, DragonEau, Esclavagiste,
         Esclaves, SerpentdesMers, Meduse, Poulpe, CréatureProfondeurs, Rampant, Crabe, ElementaireVide,
         ElementaireMarais)