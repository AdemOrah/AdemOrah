#Exercice 1:
#Créez un programme demandant à un utilisateur d'entrer un entier et retournez-lui 
#le carré. Si le nombre est positif, retournez-lui aussi la racine carrée.

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
    nom_animal = ('Entrer un nom: '())
    couleur_animal = ('Entrer une couleur: '())
    lieu_animal = ('Entrer un lieu:' ())
    reponse = nom_animal + couleur_animal + lieu_animal
    return reponse (f'Jai trouve un {} de couleur {} dans mon lieu préféré: {} ')