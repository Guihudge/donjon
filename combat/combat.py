import random

def entree():
    while True:
        nb_car = input()
        try:
            int(nb_car)
            break
        except ValueError:
            print(" <Joueur> : ")
    return int(nb_car)

def aff_menu_princ():
    print(" 1) Attaque.")
    print(" 2) Magie.")
    print(" 3) Infos.")
    print("")


def aff_menu_attck():
    print(" 1) Attaque normale.")
    print(" 2) Attaque spéciale.")
    print(" 3) Retour.")


def aff_menu_magie():
    print(" 1) Soin.")
    print(" 2) Boule de feu.")
    print(" 3) Retour.")


def aff_info(pv_joueur, point_attack_spc, point_magie, pv_ennemy):
    print("\n")
    print(" PV joueur : ", pv_joueur, "/", " 100")
    print(" Point(s) attaque spéciale : ", point_attack_spc, "/", " 50")
    print(" Point(s) de magie:", point_magie, "/", " 30")
    print(" PV monstre : ", pv_ennemy, "/", " 50")


def attack(attack, liste_attaque, personne):
    x = random.choice(liste_attaque)
    if x == 1:
        if personne == 1:
            print(" Le monstre a perdu ", attack, "points de vie.")
        elif personne == 2:
            print(" Tu as perdu ", attack, "points de vie.")
    else:
        print(" Attaque ratée.")
        attack = 0
    return attack


def verif():
    test = False

    print(" Es-tu sûr(e) ?")
    print(" 1) Oui.")
    print(" 2) Non.")

    verif = entree()

    if verif == 1:
        test = True
    if verif == 2:
        test = False

    return test

def combat (dico_joueur, dico_enemie):

    win_player = False
    win_ennemy = False

    pv_joueur = dico_joueur.get("PV")
    attack_joueur = dico_joueur.get("attaque")

    attack_joueur_spc = dico_joueur.get("attaque_spe")
    cout_attack_spc = dico_joueur.get("coup_attaque_spe")
    point_attack_spc = dico_joueur.get("point_attaque_spe")

    point_magie = dico_joueur.get("point_magie")

    cout_soin = dico_joueur.get("coup_soin")
    pv_soin = dico_joueur.get("pv_soin")
    cout_boule_feu = dico_joueur.get("coupt_boule_feu")
    attaque_boule_feu = dico_joueur.get("attaque_boule_feu")

    pv_ennemy = dico_enemie.get("PV")
    attack_ennemy = dico_enemie.get("attaque")

    while win_player == False and win_ennemy == False:

        ok = 0

        while ok == 0:

            aff_menu_princ()

            rep = entree()
            if rep == 1:

                aff_menu_attck()

                rep2 = entree()

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
                        print(" Pas assez de point d'attaque spéciale.")

                if rep2 == 3:
                    print(" Retour.")


            elif rep == 2:
                aff_menu_magie()
                rep_m = entree()

                if rep_m == 1 and point_magie > cout_soin:
                    pv_joueur = pv_joueur + pv_soin
                    print(" Tu récupères ", pv_soin, " points de vie.")

                    point_magie = point_magie - cout_soin
                    ok = 1

                else:
                    print(" Pas assez de point de magie.")

                if rep_m == 2 and point_magie > cout_boule_feu:
                    a = attack(attaque_boule_feu, [1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 1)

                    pv_ennemy = pv_ennemy - a
                    point_magie = point_magie - cout_boule_feu
                    ok = 1

                else:
                    print(" Pas assez de point de magie.")

                if rep_m == 3:
                    print(" Retour.")



            elif rep == 3:
                aff_info(pv_joueur, point_attack_spc, point_magie, pv_ennemy)

            elif rep == 4:
                print(" Es-tu sûr ?")
                ok = 1

            else:
                print(" Erreur!")

        a = attack(attack_ennemy, [0, 1, 1, 1, 1], 2)
        pv_joueur = pv_joueur - a

        if pv_ennemy <= 0:
            win_player = True
        elif pv_joueur <= 0:
            win_ennemy = True

    return win_player