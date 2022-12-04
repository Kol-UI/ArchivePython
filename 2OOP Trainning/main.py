import time

messageBienvenue = "Ouais une nouvelle journée de travail commence !"
messagePause = "On ferai bien une petite pause ?"
messageMidi = "On irai bien manger un truc ?"
messageBientotFini = "Courage dans 10 minutes c'est la fin !"

def main(messageBienvenue, messagePause, messageMidi, messageBientotFini):
    print(messageBienvenue)
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
                if heures == 1:
                    print(secondes, "S ", minutes, "M ", heures, "H")
                    print(messagePause)
                elif heures == 3:
                    print(secondes, "S ", minutes, "M ", heures, "H")
                    print(messageMidi)
                elif heures == 6:
                    print(secondes, "S ", minutes, "M ", heures, "H")
                    print(messagePause)
                heures += 1

            elif minutes == 50:
                if heures == 8:
                    print(messageBientotFini)
            else:
                print(secondes, "S ", minutes, "M ", heures, "H")
        else:
            print(secondes, "S ", minutes, "M ", heures, "H")

main(messageBienvenue, messagePause, messageMidi, messageBientotFini)