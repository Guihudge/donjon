import random


def aff_menu_princ():
    print("1) attaque")
    print("2) magie")
    print("3) info")


def aff_menu_attck():
    print("1) attaque normale")
    print("2) attaque spécial")


def aff_menu_magie():
    print("1) Soin")
    print("2) boule de feu")


def aff_info():
    print("\n")
    print("PV joueur : ", pv_joueur, "/", pv_joueur_max)
    print("point attaque spécial : ", point_attack_spc, "/", point_attack_spc_max)
    print("point de magie:", point_magie, "/", point_magie_max)
    print("PV monstre : ", pv_ennemy, "/", pv_ennemy_max)


def attack(attack, liste_attaque, personne):
    x = random.choice(liste_attaque)
    if x == 1:
        if personne == 1:
            print("Moins ", attack, "point de vie pour le monstre")
        elif personne == 2:
            print("Moins ", attack, "point de vie")
    else:
        print("attaque raté")
        attack = 0
    return attack


def verif():
    verif = 0
    test = False

    print("Êtes-vous sure?")
    print("1) oui")
    print("2) non")

    verif = int(input())

    if verif == 1:
        test = True
    if verif == 2:
        test = False

    return test