import time
import random

Zer, Dron, Roach, Hydra, Banne, Que, Spor, Spin, Over, Muta, Brood, Vigi, Ultra, Infest, Terran, Corrup, Vipe, Swarm, Chang, Nyd, Rod, Sac, Gardien = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
Elem, BigElem = 0,0

def main(Zer, Dron, Roach, Hydra, Banne, Que, Spor, Spin, Over, Muta, Brood, Vigi, Ultra, Infest, Terran, Corrup, Vipe,
         Swarm, Chang, Nyd, Rod, Sac, Gardien, Elem, BigElem):
    i = 100
    secondes = 0
    heures = 0
    minutes = 0

    while secondes < i:
        time.sleep(1)
        secondes += 1
        if secondes == 60:
            secondes = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                heures += 1
                print("\n", secondes, "S ", minutes, "M ", heures, "H",)
            else:
                print("\n", secondes, "S ", minutes, "M ", heures, "H", )
        else:
            print("\n", secondes, "S ", minutes, "M ", heures, "H", )
        # ici

        rnd = random.choice(['Zergling', 'Z', 'Zerg', 'ZLing', 'MoreZling', 'MoreZergling', 'MoreZ', 'MoreZerg', 'Drone', 'Roach', 'R', 'Hydra', 'H', 'Banne', 'Que', 'Spor',
                             'Spin', 'Over', 'Muta', 'Brood', 'Vigi', 'Ultra', 'Infest', 'Terran', 'Corrup', 'Vipe',
                             'Swarm', 'Chang', 'Nyd', 'Rod', 'Sac', 'Raid', 'RoachRush', 'ZergRush', 'Investation', 'Trap', 'RoachRavager', 'Drop', 'BBQ', 'Gardien'])
        if rnd == 'Zergling':
            Zer += 1
        elif rnd == 'MoreZergling':
            Zer += 1
        elif rnd == 'Z':
            Zer += 2
        elif rnd == 'MoreZ':
            Zer += 2
        elif rnd == 'Zerg':
            Zer += 3
        elif rnd == 'MoreZerg':
            Zer += 3
        elif rnd == 'Zling':
            Zer += 4
        elif rnd == 'MoreZling':
            Zer += 4
        elif rnd == 'Drone':
            Dron += 1
        elif rnd == 'Roach':
            Roach += 1
            Elem += 1
        elif rnd == 'R':
            Roach += 2
            Elem += 1
        elif rnd == 'Hydra':
            Hydra += 1
            Elem += 1
        elif rnd == 'H':
            Hydra += 2
            Elem += 1
        elif rnd == 'Banne':
            Banne += 1
            Elem += 1
        elif rnd == 'Que':
            Que += 1
            Elem += 1
        elif rnd == 'Spor':
            Spor += 1
        elif rnd == 'Spin':
            Spin += 1
        elif rnd == 'Over':
            Over += 1
        elif rnd == 'Muta':
            Muta += 1
            Elem += 1
        elif rnd == 'Brood':
            Brood += 1
            BigElem += 1
        elif rnd == 'Vigi':
            Vigi += 1
        elif rnd == 'Ultra':
            Ultra += 1
            BigElem += 1
        elif rnd == 'Infest':
            Infest += 1
            Elem += 1
        elif rnd == 'Terran':
            Terran += 1
        elif rnd == 'Corrup':
            Corrup += 1
            Elem += 1
        elif rnd == 'Vipe':
            Vipe += 1
            Elem += 1
        elif rnd == 'Swarm':
            Swarm += 1
            Elem += 1
        elif rnd == 'Chang':
            Chang += 1
        elif rnd == 'Nyd':
            Nyd += 1
            BigElem += 1
        elif rnd == 'Rod':
            Rod += 1
            Elem += 1
        elif rnd == 'Sac':
            Sac += 1
            Elem += 1
        elif rnd == 'Gardien':
            Gardien += 1
            Elem += 1
        elif rnd == 'Raid':
            Muta += 3
            Elem += 1
        elif rnd == 'RoachRush':
            Roach += 3
            Elem += 1
        elif rnd == 'ZergRush':
            Zer += 5
            Roach += 3
            Hydra += 2
            Banne += 2
            BigElem += 1
        elif rnd == 'Investation':
            Infest += 1
            Terran += 2
            Elem += 1
        elif rnd == 'Trap':
            Banne += 3
            Elem += 1
        elif rnd == 'RoachRavager':
            Roach += 2
            Sac += 1
            BigElem += 1
        elif rnd == 'Drop':
            Zer += 6
            Over += 1
        elif rnd == 'BBQ':
            Zer += 2
            Dron += 2

        print('\n', Zer, 'Zergling', Dron, 'Drone', Roach, 'Roach', Hydra, 'Hydra', Banne, 'Banne', Que, 'Que\n',
              Spor, 'Spor', Spin, 'Spin', Over, 'Over', Muta, 'Muta', Brood, 'Brood', Vigi, 'Vigi\n', Ultra, 'Ultra',
              Infest, 'Infest', Terran, 'Terran', Corrup, 'Corrup', Vipe, 'Vipe', Swarm, 'Swarm\n', Chang, 'Chang',
              Nyd, 'Nyd', Rod, 'Rod', Sac, 'Sac', Gardien, 'Gardien')
        print(Elem, 'Elem', BigElem, 'BigElem')

main(Zer, Dron, Roach, Hydra, Banne, Que, Spor, Spin, Over, Muta, Brood, Vigi, Ultra, Infest, Terran, Corrup, Vipe,
     Swarm, Chang, Nyd, Rod, Sac, Gardien, Elem, BigElem)