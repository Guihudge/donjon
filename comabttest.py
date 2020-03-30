import sys
from combat import combat
from affichage.affichage import *
import time

joueur = {"PV": 100, "attaque": 20, "attaque_spe": 50, "coup_attaque_spe": 15, "point_attaque_spe": 50, "point_magie": 30, "coup_soin": 10, "pv_soin": 40, "coupt_boule_feu": 20, "attaque_boule_feu": 35}
enemie = {"PV": 50, "attaque": 10}
init = {"pv_max_joueur": 100, "pv_max_enemie": 50, "point_magi_max": 30, "point_attaque_spé_max": 50}

def entree():
    while True:
        nb_car = input("<Joueur> : ")
        try:
            int(nb_car)
            break
        except ValueError:
            print(" Entrez un nombre.")
    return int(nb_car)

def deplacement (porte, x, y):
    nord, sud, est, ouest = porte
    direction = False

    print("")
    print(" Tu es en [{},{}]\n".format(x, y))

    while direction == False:

        if nord == 1:
            print(" 1) Aller au Nord.")
        if sud == 1:
            print(" 2) Aller au Sud.")
        if est == 1:
            print(" 3) Aller à l'Est.")
        if ouest == 1:
            print(" 4) Aller à l'Ouest.")

        print("")

        rep = entree()

        print("")

        if rep == 1 and nord == 1:
            print(" Tu te déplaces vers le Nord.\n")
            y = y-1
            print(" Tu es désormais en [{},{}]\n".format(x, y))
            time.sleep(1)

            return x, y
        if rep == 2 and sud == 1:
            print(" Tu te déplaces vers le Sud.\n")
            y = y + 1
            print(" Tu es désormais en [{},{}]\n".format(x, y))
            time.sleep(1)

            return x, y
        if rep == 3 and est == 1:
            print(" Tu te déplaces vers l'Est.\n")
            x = x + 1
            print(" Tu es désormais en [{},{}]\n".format(x, y))
            time.sleep(1)

            return x, y
        if rep == 4 and ouest == 1:
            print(" Tu te déplaces vers l'Ouest.\n")
            x = x - 1
            print(" Tu es désormais en [{},{}]\n".format(x, y))
            time.sleep(1)

            return x, y

def salle(x, y, joueur):
    if x == 0 and y == 0:
        print(" Bravo! Tu es arrivé(e) à la salle du boss. Maintenant, nous te souhaitons bonne chance pour faire face au terrible et redouté... \n")
        time.sleep(2)
        print(" (Effet de suspense, musique stressante) ..............\n")
        time.sleep(5)
        print(" <[CHAT BLANC DE MAMIE JACKLINE]>")

        chat_de_mamie = {"PV": 150, "attaque": 30}

        issue = combat.combat(joueur, chat_de_mamie)

        if issue:
            print(" Bien joué! Tu as gagné! Mais malheureusement, c'est la fin du jeux.")
            print(" Merci d'avoir joué!")
            sys.exit(0)
        elif issue == False:
            print(" Tu as perdu, au revoir.")
            time.sleep(6)
            sys.exit(0)

        #fin
    if x == 1 and y == 0:
        print(" Te voici dans l'entre d'une tribu de monstres sans nom. Il s'agit des :")
        time.sleep(4)
        print(" CHATS NINJAS MARRONS DE JEREMY")

        chat_ninja = {"PV": 100, "attaque": 20}

        issue = combat.combat(joueur, chat_ninja)

        if issue:
            print(" Tu as gagné le combat. Félicitation!")
        elif issue == False:
            print(" Tu as perdu le combat. Dommage!")
            print(" FIN")
            time.sleep(6)
            sys.exit(0)

        nord = 0
        sud = 0
        est = 1
        ouest = 1

        return nord, sud, est, ouest

    if x == 2 and y == 0:
        print(" Tu sembles être dans une salle où il y a des coffres. Tu as deux coffres devant toi : un rouge et un bleu. Tu décides d'en ouvrir un:")
        print(" 1) Le coffre bleu.")
        print(" 2) Le coffre rouge.")
        rep = entree()

        if rep == 1:
            print(" Tu trouves une superbe amulette dans une boîte. Tu ouvres la boîte et mets l'amulette. Tu te sens bizzare.")
            print(" Bravo! Tu viens de perdre 5 points d'attaque. Tu regardes alors le dos de l'amulette et tu y vois marquer:")
            print(' "Made in China".')
            print(" Désolé pour toi!")
            joueur["attaque_spe"] = joueur.get("attaque_spe")- 5

        elif rep ==2:
            print(" Tu as de la chance, tiens + 50PV!")
            time.sleep(7)
            print(" It's a prank!! (gamin de 3 ans)")
            time.sleep(2)
        else:
            print(" Bien essayé petit joueur. ")
            time.sleep(7)
            print(" AU GOULAG!!!!!!!")

        nord = 0
        sud = 1
        est = 0
        ouest = 1

        return nord, sud, est, ouest

    if x == 0 and y == 1:
        print(" Tu es tombé(e) contre un groupe de redoutables gobelins verts.")
        print(" Tu as de la chance. Ils sont désorganisés et pas trés habiles, mais ils sont 3.")

        goblin = {"PV": 100, "attaque": 20}

        issue = combat.combat(joueur, goblin)

        if issue:
            print(" Tu as gagné le combat!")
        elif issue == False:
            print(" Tu as perdu le combat!")
            print(" FIN")
            time.sleep(6)
            sys.exit(0)

        issue = combat.combat(joueur, goblin)

        if issue:
            print(" Tu as gagné le combat!")
        elif issue == False:
            print(" Tu as perdu le combat!")
            print(" FIN")
            time.sleep(6)
            sys.exit(0)

        issue = combat.combat(joueur, goblin)

        if issue:
            print(" Tu as gagné le combat!")
        elif issue == False:
            print(" Tu as perdu le combat!")
            print(" FIN")
            time.sleep(6)
            sys.exit(0)

        nord = 0
        sud = 1
        est = 1
        ouest = 0

        return nord, sud, est, ouest

    if x== 1 and y == 1:
        print("")
        print(" Bonjour et bienvenu(e) à toi dans : Le Donjon De L'Empire Des Chats. Nous allons te conter l'histoire de ce jeu.")
        time.sleep(3)
        print(" Pensez à dire à Roger d'écrire l'histoire.\n")
        time.sleep(3)

        nord = 0
        sud = 0
        est = 1
        ouest = 1

        return nord, sud, est, ouest

    if x == 2 and y == 1:
        print(" Tu est dans une salle de banquet. Tous tes PVs sont restorés et tous tes points de magie aussi.")
        print(" Chanceux!")

        joueur["PV"] = 100
        joueur["point_magie"] = 30

        nord = 1
        sud = 1
        est = 0
        ouest = 1

        return nord, sud, est, ouest

    if x == 0 and y == 2:
        print(" Pas de chance. Il fait noir dans cette pièce. Tu as l'impression de voir trois coffres devant toi.")
        print(" Il doit sûrement y avoir un gros butin dans l'un de ces coffres.")
        print(" Donne un nombre entre 1 et 3.")

        rep = entree()

        if rep == 1:
            print(" Bravo! Tu as gagné 15 HP")
            joueur["PV"] = joueur.get("PV") + 15

        if rep == 2:
            print(" Tu as ouvert le coffre, tu attends...")
            time.sleep(4)
            print(" Rien ne se passe.")
            print(" Bon, bah tant pis!")

        if rep == 3:
            print(" Tu vois un nuage rouge étrange. Il a la forme d'un diable.")
            time.sleep(2)
            print(" Et Bam! -15 points de vie.")
            print(" Désolé, mon vieux! C'est la vie!")
            joueur["PV"] = joueur.get("PV") - 15
        elif rep > 3:
            print(" Bien essayé mon petit........")
            time.sleep(0.3)
            print(" Tu es aussi prévisible qu'un feux vert. Pour la peine.....")
            time.sleep(1)
            print(" Hum.....")
            time.sleep(0.8)
            print(" Alors voyons....")
            time.sleep(0.9)
            print(" Bon Ok, je trouve pas. Pars maintenant!")

        nord = 1
        sud = 0
        est = 1
        ouest = 0

        return nord, sud, est, ouest

    if x == 1 and y == 2:
        print(" Une salle vide avec rien.")
        print(" Attends..., si! Regardes bien!")
        print(" C'est un réacteur à fusion nucléaire avec un panneau.")
        print(" Sur le panneau, il y a écrit: \n NE PAS TOUCHER SVP \n Albert.")

        nord = 0
        sud = 0
        est = 1
        ouest = 1

        return nord, sud, est, ouest

    if x == 2 and y == 2:
        print(" Tu es devant un dragon.")
        print(" Adieu")
        print("")
        print(" Dragon: - Tu as osé pénétrer dans mon domaine?")
        print(" Dragon: - Tu dois payer cet affront. Payer de ta vie!")
        print("")
        print(" Narrateur: - Psst... Tu peux utiliser Ctrl+C au cas où, si ça venait à mal tourné.")
        print("")
        print(" Dragon: - T'es pas mort toi?")
        print("")
        print(" Narrateur: - Ah, j'avais oublié. re-ADIEU!")
        print("")
        print(" Dragon: Maintenant, à toi de mourir, jeune joueur. TON HEURE EST VENUE. (Sous réserve d'acceptation du développeur.)")

        Dragon = {"PV": 500, "attaque": 40}

        issue = combat.combat(joueur, Dragon)

        if issue:
            print(" Tu as gagné le combat. Sincèrement, toutes mes félicitations!")
        elif issue == False:
            print(" Tu as perdu le combat. En même temps, vu le dragon, je comprends...")
            print(" FIN")
            time.sleep(6)
            sys.exit(0)

        nord = 1
        sud = 0
        est = 0
        ouest = 1

        return nord, sud, est, ouest




#Début aventure
x = 1
y = 1

intro()
menu()

porte = salle(x, y, joueur)

while True:
    coord = deplacement(porte, x, y)
    x, y = coord
    porte = salle(x,y,joueur)