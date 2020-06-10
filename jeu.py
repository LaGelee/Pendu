try:
    import random
    import os
    from tableau import dessinPendu
except Exception as error:       
    print("Unne erreur a été rencontrée")
    print("Error:",type(error))
    os.system('pause')

#fonction pour choisir un mot aléatoirement
def choisir_mot():
    f = open("dico.txt", "r")
    fichier = f.read()
    mot = fichier.split("\n")
    f.close()
    index = random.randint(0, len(mot)-1)
    return mot[index].upper()

#vérifier victoire
def endcheck(mot_cachee, mot, nb_chances):
    if "".join(mot_cachee) == mot:
        return "Victory"
    elif nb_chances == 6:
        return "Loose"
    else:
        return False 

#fonction pour rejouer
def replay():
    while True:
        r = str(input('Voulez vous rejouer ? (y/n) :'))
        if r == 'y' or r == 'Y' :
            jeu()
        elif r == 'n' or r == 'N':
            return

#fonction pour demander une lettre
def ask(mot):
    while True:
        guess = input("Lettre: ").upper()
        if guess == mot:
            return "Trouvé"
        elif len(guess) != 1:
            continue
        else:
            return guess

#jeu principale
def jeu():
    try:
        mot = choisir_mot()
        lettres_use = ""
        nb_chances = 0

        while True:
            mot_cachee = []
            for letters in mot:
                if letters in lettres_use:
                    mot_cachee.append(letters)
                else:
                    mot_cachee.append("*")
            
            if endcheck(mot_cachee, mot, nb_chances) == "Victory":
                print("")
                print("Gangé !")
                print("Vous avez trouvé:",mot)
                break
            elif endcheck(mot_cachee, mot, nb_chances) == "Loose":
                print(dessinPendu(nb_chances))
                print("Perdu !")
                print("Il fallait trouver:",mot)
                break
            
            os.system("cls")
            print(dessinPendu(nb_chances))
            print("Mot à trouver:",mot_cachee)
            print("Utilisées:",lettres_use)
            print('')
            guess = ask(mot)
            if guess == "Trouvé":
                print("")
                print("Gangé !")
                print("Vous avez trouvé:",mot)
                break
            else:
                if guess in lettres_use:
                    continue
                else:
                    lettres_use += guess
                    if guess  not in mot:
                        nb_chances += 1
        replay()
    except Exception as error:       
        print("Unne erreur a été rencontrée")
        print("Error:",type(error))
        os.system('pause')

jeu()

"""
Enregistrer le score
Optimisation
"""
