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


win_player = False
win_ennemy = False

pv_joueur_max = 100
pv_joueur = pv_joueur_max
attack_joueur = 20

attack_joueur_spc = 30
cout_attack_spc = 15
point_attack_spc_max = 20
point_attack_spc = point_attack_spc_max

point_magie_max = 30
point_magie = point_magie_max

cout_soin = 10
pv_soin = 40
cout_boule_feu = 20
attaque_boule_feu = 35

pv_ennemy_max = 50
pv_ennemy = pv_ennemy_max
attack_ennemy = 10

while win_player == False and win_ennemy == False:

    ok = 0

    while ok == 0:

        aff_menu_princ()

        rep = int(input())
        if rep == 1:

            aff_menu_attck()

            rep2 = int(input())

            if rep2 == 1:
                a = attack(attack_joueur, [0, 1, 1, 1], 1)
                pv_ennemy = pv_ennemy - a
                ok = 1
            if rep2 == 2:
                if point_attack_spc > cout_attack_spc:
                    a = attack(attack_joueur_spc, [0, 1, 1, 1], 1)
                    pv_ennemy = pv_ennemy - a
                    point_attack_spc = point_attack_spc - cout_attack_spc
                    ok = 1

                else:
                    print("Pas assez de point d'attaque spécial.")


        elif rep == 2:
            aff_menu_magie()
            rep_m = int(input())

            if rep_m == 1 and point_magie > cout_soin:
                pv_joueur = pv_joueur + pv_soin
                print("plus ", pv_soin, " pv")

                point_magie = point_magie - cout_soin
                ok = 1

            else:
                print("pas asser de point de magie")

            if rep_m == 2 and point_magie > cout_boule_feu:
                a = attack(attaque_boule_feu, [1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 1)

                pv_ennemy = pv_ennemy - a
                point_magie = point_magie - cout_boule_feu
                ok = 1

            else:
                print("pas asser de point de magie")



        elif rep == 3:
            aff_info()

        elif rep == 4:
            print("Êtes-vous sûre?")
            ok = 1

        else:
            print("erreur")

    a = attack(attack_ennemy, [0, 1, 1, 1, 1], 2)
    pv_joueur = pv_joueur - a

    if pv_ennemy <= 0:
        win_player = True
    elif pv_joueur <= 0:
        win_ennemy = True







