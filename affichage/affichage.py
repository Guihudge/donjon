import sys
import time
import os

def entree():
    while True:
        nb_car = input("<Joueur> : ")
        try:
            int(nb_car)
            break
        except ValueError:
            print(" Entrez un nombre.")
    return int(nb_car)

def intro():
    print(" +----------------------------------------------------------------------------+")
    print(" |                                                                            |")
    print(" |                             Bienvenu(e) dans :                             |")
    print(" |                                                                            |")
    print(" |                      LE DONJON DE L'EMPIRE DES CHATS.                      |")
    print(" |                                                                            |")
    print(" |                                                                            |")
    print(" |                             Un jeu textuel ...                             |")
    print(" |                                                                            |")
    print(" |                                 En 2019...                                 |")
    print(" |                                                                            |")
    print(" |                                                                            |")
    print(" |                                                                            |")
    print(" |                                                                            |")
    print(" |                                                                            |")
    print(" |               (Merci beaucoup au défi pour ce nom pourri...)               |")
    print(" +----------------------------------------------------------------------------+")

def menu():
    print("\n \n ")
    print(" Voici le menu!")
    print(" 1) Jouer (le plus important).")
    print(" 2) Charger une Sauvegarde.")
    print(" 3) Option (ne sert à rien).")
    print(" 4) Quitter ")

    while True:

        rep = entree()
        if rep == 1:
            return
        elif rep == 2:
            print(" Inexistant pour l'instant.")
        elif rep == 3:
            print(" Je n'ai rien à mettre ici. Si vous avez des idées, dites-le moi.")
        elif rep == 4:
            print(" Rageux!")
            time.sleep(6)
            sys.exit()
        else:
            print(" On a dit un nombre compris entre 1 et 4.")
            time.sleep(2)
            intro()
            menu()


