import time

joueur = {"PV": 100, "attaque": 20, "attaque_spe": 50, "coup_attaque_spe": 15, "point_attaque_spe": 50, "point_magie": 30, "coup_soin": 10, "pv_soin": 40, "coupt_boule_feu": 20, "attaque_boule_feu": 35}


def entree():
    while True:
        nb_car = input()
        try:
            int(nb_car)
            break
        except ValueError:
            print("Entrez un nombre.")
    return int(nb_car)

def salle(x, y, joueur):
    if x == 0 and y == 0:
        print("Bravo, tu est arriver à la salle du bosse, mais maitenant bonne chance face au terrible et redouter \n \n")
        time.sleep(2)
        print("(effet de suspense, music stressante) ..............")
        time.sleep(5)
        print("CHAT BLANC DE MAMIE JACKLINE")

        chat_de_mamie = {"PV": 150, "attaque": 30}

        #combat**

        #fin
    if x == 1 and y == 0:
        print("Te voici dans un entre d'un monstre sans nom il s'ajit des :")
        time.sleep(4)
        print("CHAT NINJA MARON DE JEREMY")

        chat_ninja = {"PV": 100, "attaque": 20}

        #combat

        nord = 0
        sud = 0
        est = 1
        ouest = 1

        return nord, sud, est, ouest

    if x == 2 and y == 0:
        print("Tu semble être dans une salle des coffre. Tu as de coffre devant toi, tu choisi(e) un:")
        print("1) Un coffre bleu")
        print("2) Un coffre rouge")
        rep = entree()

        if rep == 1:
            print("Tu trouve une superbe amulette dans une boite. Tu ouvre la boite et met l'amulette. Tu te sent bizzar")
            print("Bravo, tu viens de perdre 5 point d'attaque; tu ragarde alors le dos de l'amulette et tu vois marqué:")
            print('"Made in China"')
            print("dsl pour toi")
            joueur["attaque_spe"] = joueur.get("attaque_spe")- 5

        elif rep ==2:
            print("tu as de la chance, tiens + 50PV")
            time.sleep(7)
            print("It's a prank!! (gamin de 3 ans)")
        else:
            print("biens essayé petit joueur. ")
            time.sleep(7)
            print("AU GOULAG!!!!!!!")

        nord = 0
        sud = 1
        est = 0
        ouest = 1

        return nord, sud, est, ouest

    if x == 0 and y == 1:
        print("Tu est tombé contre un groupe de redoutable gobelin vert")
        print("Tu as de la chance, ils sont désorganiser et pas trés habile, mais ils sont 3")

        goblin = {"PV": 100, "attaque": 20}

        # combat goblin
        # combat goblin
        # combat goblin

        nord = 0
        sud = 1
        est = 1
        ouest = 0

        return nord, sud, est, ouest

    if x== 1 and y == 1:
        print("Bonjour et bienvenue à toi dans l'entre des chat (le jeu). Nous allons te comptre l'histoire de ce jeux.")
        time.sleep(3)
        print("pensser à dire à Roger de d'écrire l'histoire")

        nord = 0
        sud = 0
        est = 1
        ouest = 1

        return nord, sud, est, ouest

    if x == 2 and y == 1:
        print("tu est dans une salle de banquet. Tout est PV son restorer et tout tes point de magie")
        print("Chanceux")

        joueur["PV"] = 100
        joueur["point_magie"] = 30

        nord = 1
        sud = 1
        est = 0
        ouest = 1

        return nord, sud, est, ouest

    if x == 0 and y == 2:
        print("Pas de cahne. il fait noire dans cette pièce. tu as l'impression de voire trois coffre devant toi")
        print("Il doit surement y avoire un gros butain dans un de ces coffre")
        print("Donne un nombre entre 1 et 3")

        rep = entree()

        if rep == 1:
            print("bravo, tu a gagner 15 HP")
            joueur["PV"] = joueur.get("PV") + 15

        if rep == 2:
            print("Tu a ouvert le coffre, tu attend...")
            time.sleep(4)
            print("Rien ne se passe")
            print("Bon bha temps pis")

        if rep == 3:
            print("tu voie un nuage rouge étrange, il a la forme d'un diable")
            time.sleep(2)
            print("Et Bam, -15 points de vie, DSL mon vieux")
            joueur["PV"] = joueur.get("PV") - 15
        elif rep > 3:
            print("Bien tester mon petit........")
            time.sleep(0.3)
            print("Tu est aussi prévisible qu'un feux vert. Pour la painne.....")
            time.sleep(1)
            print("Hum.....")
            time.sleep(0.8)
            print("Alors voyons....")
            time.sleep(0.9)
            print("Bon Ok je trouve pas part maintenant")

        nord = 1
        sud = 0
        est = 1
        ouest = 0

        return nord, sud, est, ouest

    if x == 1 and y == 2:
        print("Une SAlle vide avec rien, sauf un réateur à fusion nucléaire avec un panneau")
        print("sur le panneau il y a écrit: \n NE PAS TOUCHER SVP \n Albert")

        nord = 0
        sud = 0
        est = 1
        ouest = 1

        return nord, sud, est, ouest

    if x == 2 and y == 2:
        print("Tu est devant un dragon")
        print("Adieux")
        print("Dragon: tu as oser pénétrer dans mon domaine")
        print("Dragon: Tu doit payer cette afront de ta vie")
        print("Narrateur: psst, tu peux utiliser ctrl+C au cas ou sa tourne mal")
        print("Dragon: tes pas mort toi?")
        print("Narrateur: Ah, j'avais oublié. re-ADIEUX")
        print("Dragon: Maintenant à toi de mourir joueur. TON HEURE EST VENUE. sous réserve d'accptation du développeur")

        Dragon = {"PV": 500, "attaque": 40}

        #combat Dragon

        nord = 1
        sud = 0
        est = 0
        ouest = 1

        return nord, sud, est, ouest


print("test salle")
x = int(input("x?"))
y = int(input("y?"))

rep = salle(x, y, joueur)
print(rep)