import time
import random

Soldat, Intercepteur, Transport, Char, Corvette, Vaisseau = 0,0,0,0,0,0

def main(Soldat, Intercepteur, Transport, Char, Corvette, Vaisseau):

    i = 100
    secondes = 0
    minutes = 0
    heures = 0

    while secondes < i :
        time.sleep(1)
        secondes += 1
        Soldat += 1

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

            rnd = random.choice(['Soldat1', 'Soldat2', 'Soldat3', 'Soldat4', 'Soldat5', 'Intercepteur0',
                                 'Intercepteur1' 'Transport0', 'Transport1', 'GrandTransport', 'Char0', 'Char1',
                                 'Corvette0', 'Corvette1', 'Vaisseau0', 'Vaisseau1'])

            if rnd == 'Soldat1':
                Soldat += 1
            elif rnd == 'Soldat2':
                Soldat += 2
            elif rnd == 'Soldat3':
                Soldat += 3
            elif rnd == 'Soldat4':
                Soldat += 4
            elif rnd == 'Soldat5':
                Soldat += 5
            elif rnd == 'Intercepteur0':
                Soldat += 1
            elif rnd == 'Intercepteur1':
                Intercepteur += 1
            elif rnd == 'Transport0':
                Soldat += 1
            elif rnd == 'Transport1':
                Transport += 1
                Soldat += 12
            elif rnd == 'GrandTransport':
                Transport += 1
                Soldat += 25
                Char += 1
            elif rnd == 'Char0':
                Soldat += 1
            elif rnd == 'Char1':
                Char += 1
            elif 'Corvette0':
                Soldat += 1
            elif 'Corvette1':
                Corvette += 1
            elif 'Vaisseau0':
                Soldat += 1
            elif 'Vaisseau1':
                Vaisseau += 1


            print('\n',Soldat,'Soldat',Intercepteur,'Intercepteur',Transport,'Transport',Char,'Char',Corvette,
                  'Corvette',Vaisseau,'Vaisseau')

main(Soldat, Intercepteur, Transport, Char, Corvette, Vaisseau)