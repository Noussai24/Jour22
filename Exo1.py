

# Boucles 1 ennocée:Écrire un programme qui choisit un nombre aléatoire entre 1 et 100 et demande à l'utilisateur de le deviner. 
#L'utilisateur a droit à un nombre limité de tentatives. 
# Après chaque tentative, le programme indique 
#si le nombre mystère est plus grand ou plus petit que la saisie de l'utilisateur.

import random

# Premier exercice : Deviner le nombre mystère
def deviner_le_nombre():
    nombre_mystere = random.randint(1, 100)
    print("Devinez le nombre mystère entre 1 et 100. Vous avez 5 tentatives.")

    for tentative in range(1, 6):
        guess = int(input(f"Tentative {tentative}: Entrez votre estimation : "))

        if guess == nombre_mystere:
            print("Félicitations ! Vous avez deviné le nombre mystère :", nombre_mystere)
            return
        elif guess < nombre_mystere:
            print("Le nombre mystère est plus grand.")
        else:
            print("Le nombre mystère est plus petit.")

        print("Il vous reste", 5 - tentative, "tentatives.")
    print("Vous avez épuisé toutes vos tentatives. Le nombre mystère était :", nombre_mystere)

# Deuxième exercice : Afficher une pyramide
def afficher_pyramide():
    hauteur = int(input("Entrez la hauteur de la pyramide : "))
    if hauteur <= 0:
        print("La hauteur doit être un entier positif.")
    else:
        for i in range(1, hauteur + 1):
            print(" " * (hauteur - i) + "*" * (2 * i - 1))

# Troisième exercice : Trouver le plus grand nombre
def trouver_plus_grand_nombre():
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    nombre3 = float(input("Entrez le troisième nombre : "))

    if nombre1 >= nombre2 and nombre1 >= nombre3:
        print("Le plus grand nombre est :", nombre1)
    elif nombre2 >= nombre1 and nombre2 >= nombre3:
        print("Le plus grand nombre est :", nombre2)
    else:
        print("Le plus grand nombre est :", nombre3)

# Quatrième exercice : Décoder un message
def decode_message(message):
    message_decode = "".join(chr(int(nombre)) for nombre in message.split())
    return message_decode

message_code = "72 101 108 108 111 44 32 87 111 114 108 100"
print("Le message décodé est :", decode_message(message_code))

# Cinquième exercice : Compter les palindromes
def compter_palindromes(liste_mots):
    return sum(1 for mot in liste_mots if mot == mot[::-1])

liste_mots = ["radar", "level", "python", "stats", "racecar"]
print("Nombre de palindromes dans la liste :", compter_palindromes(liste_mots))
