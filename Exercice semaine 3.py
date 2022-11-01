#Exercice 1:
#Créez un programme demandant à un utilisateur d'entrer un entier et retournez-lui 
#le carré. Si le nombre est positif, retournez-lui aussi la racine carrée.

from ast import NodeVisitor, Yield
from tkinter.messagebox import QUESTION


def entrer_entier(a):
    a = 3
    entier = a ** 2    
    return entier

 # Exercice 2:
 #Créez un programme demandant à l'utilisateur un animal, une couleur et un lieu et 
 # retournez-lui la phrase suivante: J'ai trouvé un (nom de l'animal) 
 # de couleur (nom de la couleur) dans mon lieu préféré: (nom du lieu).
 #  Implémentez la fonction de sorte qu'elle ne prenne qu'un seul paramètre pour 
 # représenter les trois mots de l'utilisateur.

def user_animal():
    nom_animal = input('Entrer un nom: '())
    couleur_animal = input('Entrer une couleur: '())
    lieu_animal = ('Entrer un lieu:' ())
    reponse = nom_animal + couleur_animal + lieu_animal
    return f'Jai trouve un {nom_animal} de couleur {lieu_animal} dans mon lieu préféré: {lieu_animal} '
user_animal()

    # Exercice 3:
    #Créez un programme demandant à un utilisateur d'entrer sa date de fête, 
    # si la date est le 31 octobre, affichez un message souhaitant bonne fête
    #  à l'utilisateur, sinon affichez le message suivant: Ce n'est pas ta fête 
    # aujourd'hui :(.

def user_birtday():
    question = input('Quelle es la date de votre fête?: ')
    if question == ('31 Octobre'):
        print('Bonne fête')
    else:
        print('Ce nest pas ta fete aujourdhui')
user_birtday()
    # Exercice 4:
    #Créez un programme demandant à un utilisateur d'entrer sa date de fête 
    # et retournez-lui sa saison de naissance s'il est né dans l'hémisphère Nord.
    # (Vous pouvez assumer que les équinoxes et solstices ont lieu le 21 du mois.)

def utilsateur_fete():
    question = ('Quelle est votre date de fete?: ')
    

# Exercice 5: Créez une fonction demandant à un utilisateur un nombre pair et
#  un nombre impair, une fonction permettant de vérifier que les nombres ne
#  sont pas les deux pairs ou impairs, et affichez la phrase suivante: 
# Votre nombre impair est le x, votre nombre pair est le y et le résultat de
#  leur division est égal à z. Vous ne devez qu'afficher 3 chiffres après le
#  point.

def nombre(a):
    if a % 1 == 0:
        print ('Pair')
    else:
        print ('Impair')
nombre(43)   

def nombre(a):
    if a % 1 ==0:
        print ('Pair')
    else:
        print()


