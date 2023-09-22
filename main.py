# Word_Counter
# Crée le 29 Août
# Fait par Zhenchen Xu

# variables
global text
global space
global answer5
global answer2
space = 0
continue1 = True
answer5 = 'non'


def count_word():
    global space
    for i in text1:
        if i.isspace():
            space = space + 1
        else:
            space = space


# mot de bienvenue
print('Bievenue au word counter, une programme qui permet de compter plusieurs aspects de votre text.')
print(
    'Veuillez noter que vous ne pouvez pas avoir d\'espace entre votre paragraphes. Donc pas de 3 petit points à gauche de l\'écran.')

# permettre l'utilisateur de continuer de compter le nombre de mots sans avoir à recommencer le programme
while continue1 == True:
    space = 0
    if answer5 == 'non':
        print('')
        # insérer le text
        text1 = (input(str('Insérez votre text ici: ')))

    else:
        print('')

    global answer2
    # input pour savoir ce que le utilisateur veut faire
    answer2 = input(
        str('Voici les options|   enter -  1 pour compter le nombre de mot, 2 pour compter le nombre de caractère, 3 pour compter les espaces: '))

    # trouver ce que l'utilisateur veut:
    if answer2 == '1':
        # compter le nombre d'espace +1 pour le n.de mot
        count_word()
        print('Votre text contient ', space + 1, ' mots.')
    elif answer2 == '2':
        answer3 = input(
            str('Voulez vous compter le nombre de caractère avec ou sans les espace (1 pour avec 2 pour sans):'))
        if answer3 == '1':
            # compter et afficher le n. de caractère
            print('Votre text contient ', len(text1), ' charactères(avec espaces).')
        else:
            # compter le n.espace
            count_word()
            print('Votre text contient ', len(text1) - space, ' charactères(sans espace).')
    else:
        # compter le n.espace
        count_word()
        print('Votre text contient ', space, ' espaces.')

    # demander si l'utilisateur veut continuer de utiliser le compteur de mots
    answer4 = input(str('Voulez vous continuer d\'utiliser le word counter? (indiquez par oui ou non): '))
    if answer4 == 'oui':
        answer5 = input(str('Voulez vous réutiliser le même text?(indiquez oui ou non): '))
    else:
        continue1 = False
