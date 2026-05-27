"""Ce travail a été réalisé par PATHMARANJAN Kuruparan en BUT 1 informatique groupe Venus 18/01/2026 """
from math import *                                  #Importation de la bibliothèque math    
from json import *                                  #Importation de la bibliothèque json
from s101 import *                                  #Importation du fichier s101

#Question 1
def create_answer_from_text_file(fichier):
    """
    fichier (fichier en paramètre) : contient le nom et les réponses de chaque élèves
    revnoie un dictionnaire prenant en clé le nom des élèves et en valeur leur réponses dans un tableau
    Fonction qui sstocke dans un dictionnaire (clé : nom des élèves, valeur : tableau de réponses) les réponses de chaque élèves et leur noms
    """
    f = open(fichier)                               #Ouverture du fichier
    lignes = f.readlines()                          #Lecture du fichier et stockage dans une variable
    f.close()                                       #Fermeture du fichier
    dico={}                                         #Création d'un dictionnaire
    i = 0                                           #Initialisation d'une variable
    while i < len(lignes):                          #Boucle pour parcourir chaque les lignes
        cut = lignes[i].split(":")                  #Découpe ou il y a  : 
        scores = cut[1].split("/")                  #Découpe ou il y a /
        j = 0                                       #Initialisation d'une variable
        rep = []                                    #Création d'un tableau
        while j < len(scores):                      #Boucle pour parcourir chaque caractère de la ligne
            rep.append(int(scores[j]))              #Ajout dans le tableau
            j += 1                                  #Incrémentation de 1
        dico[cut[0]]=rep                            #Ajout dans le dictionnaire
        i += 1                                      #Incrémentation de 1
    return dico                                     #Renvoie le dictionnaire


#Question 2
def Euclidean_distance(tab1,tab2):
    """
    tab1 (tableau en paramètre) : contient les réponses d'un élève
    tab2 (tableau en paramètre) : contient les réponses d'un autre élève
    Fonction qui calcul la différence de réponses entre ces deux réponses (tableau)
    """
    i = 0                                           #Initialisation d'une variable
    total = 0                                       #Initialisation d'une variable
    while i < len(tab1):                            #Boucle pour parcourir les tableaux
        total += (tab1[i]-tab2[i])**2               #Calcul de chaque réponses et addition avec le total
        i += 1                                      #Incrémentation de 1
    return sqrt(total)                              #Renvoie la racine carré du total


#Question 3
def Euclidean_house(reponse,references):
    """
    reponse (tableau en paramètre) : contient les réponses d'un elève
    references (tableau en paramètre) : contient les réponses des maisons 
    Fonctions qui attibut la maison correspondant à l'élève en fonction des réponses (similarité)
    """
    i = 1                                                       #Initialisation d'une variable
    min = Euclidean_distance(reponse,references[0]["answer"])   #Stokage du retour de la fonction Euclidean_distance avec en paramètre la réponse de l'élève et la réponse de la 1ère maison
    pos = 0                                                     #Stockage de la position de la maison dans le tableau
    while i < len (references):                                 #Boucle pour parcourir le tableau des maisons
        res=Euclidean_distance(reponse,references[i]["answer"]) #Stockage retour de la fonction Euclidean_distance avec en paramètre la réponse de l'élève et la réponse de la i ère maison
        if res <= min:                                          #Condition pour vérifier lequel est le minimum                                   
            min = res                                           #Si condition vrai alors le minimum change
            pos = i                                             #Changement de la position par la position du nouveau minimum
        i += 1                                                  #Incrémentation de 1
    return references[pos]["house"]                             #Renvoie la maison correspondant aux réponses de l'élève


#Question 4
def Euclidean_repartition(dico,references):            
    """
    dico (dictionnaire en paramètre) :  contient les noms (clé) et réponses (valeurs) de chaque élèves
    references (tableau en paramètre) : contient les réponses des maisons
    Fonction qui attribut en fonction des réponses des élèves et de la maison, la maison qui leur convient le plus et stocke cela dans un dictionnaire
    """         
    dico_maison={}                                              #Création d'un dictionnaire
    i = 0                                                       #Initialisation d'une varible
    eleves = list(dico)                                         #Stockage des clés du dictionnaire
    while i < len(dico):                                        #Boucle pour parcourir le dictionnaire
        maison = Euclidean_house(dico[eleves[i]],references)    #Stockage retour de la fonction Euclidean_repartition avec en paramètre la réponse de la i ème élève et les réponses des maisons
        dico_maison[eleves[i]] = maison                         #Ajout d'élèment dans le dictionnaire (clé : nom de l'élève ; valeur : maison accordé)
        i += 1                                                  #Incrémentation de 1
    return dico_maison                                          #Renvoie un dictionnaire avec pour chaque élève sa maison accorée


#Partie vérification de l'efficacité : 
fichier = open('affectation_premiere_annee.json','r')              #Ouverture du fichier affectation_premiere_annee.json qui contient les affectations données par le choixpeau à chaque élèves
choixpeau = load(fichier)                                          #Stockage du contenu du fichier dans une variable
fichier.close()                                                    #Fermeture du fichier affectation_premiere_annee.json

reponse_eleves_s102 = create_answer_from_text_file('questionnaire_premiere_annee_10q.txt')    #Affectation effectué par la nouvelle méthode

fichier_house_ref = open('houses_ref.json','r')                     #Ouverture du fichier house_ref.json qui contient les réponses aux questions des créateurs des maisons
house_ref = load(fichier_house_ref)                                 #Stockage du contenu du fichier dans une variable
fichier_house_ref.close()                                           #Fermeture du fichier house_ref.json

nombre_erreur = (nb_erreurs(Euclidean_repartition(reponse_eleves_s102,house_ref),choixpeau))  #Calcul du nombre d'erreur par rapport à la prédiction du choixpeau
print("Cette méthode présente ",nombre_erreur/len(reponse_eleves_s102)*100,"% d'erreurs")     #Affichage du poucentage d'erreurs

"""
Dans cette question, la consigne n'est pas assez clair et illogique car comparer avec l'affectation du choixpeau donne envirion 50% (résultat eu lors de la saé101) ce qui représente beaucoup alors que cette méthode doit être meilleur.
De plus, comparer avec une autre méthode qui donne aussi des érreurs n'est pas logique donc nous avons comparer avec le fichier affectation_première_annee.json qui contenait les vrai affectations.
"""

#Question 5
fichier_houses_multiple_refs = open('houses_multiple_refs.json','r')  #Ouverture du fichier houses_multiple_refs.json qui contient les réponses des 10 magiciens qui représente chaque maison
houses_multiple_ref = load(fichier_houses_multiple_refs)              #Stockage du contenu du fichier dans une variable
fichier_houses_multiple_refs.close()                                  #Fermeture du fichier houses_multiple_refs.json

nombre_erreur_methode2 = (nb_erreurs(Euclidean_repartition(reponse_eleves_s102,houses_multiple_ref),choixpeau))     #Calcul du nombre d'erreur par rapport à la prédiction du choixpeau
print("La méthode du professeur Binns présente ",nombre_erreur_methode2/len(reponse_eleves_s102)*100,"% d'erreurs") #Affichage du poucentage d'erreurs

"""
Appliquer la méthode donné par le professeur Binns améliore la précision en donnant un taux d'erreur d'environ 16,12%.
"""

#Question 6
def insertion_position_NN(answer,ref,neighbors):
    """
    answer (tableau en paramètre) : contient les réponses d'un élève
    ref (dictionnaire en paramètre) : contient le nom de la maison ainsi que les réponses du fondateurs de maison
    neighbors (dictionnaire en paramètre) : contient les noms des maisons proche de la réponse de l'élève
    Fonction qui renvoie l'indice ou il faut insérer ref dans neighbors pour que ce dernier reste trié du plus proche au moins proche
    """
    distance_ref_answer = Euclidean_distance(answer,ref["answer"])                          #Stockage du renvoie de la fonction Euclidiean_distance qui indique la distance entre answer et la réponse de ref
    i = 0                                                                                   #Initialisation d'une variable
    while i < len(neighbors):                                                               #Boucle qui parcours le dictionnaire neighbors
        distance_voisin_answer = Euclidean_distance(answer,neighbors[i]["answer"])          #Stockage du renvoie de la fonction Euclidiean_distance qui indique la distance entre answer et la réponse du i ème neighbor
        if distance_ref_answer <= distance_voisin_answer :                                  #Condition qui vérifie si la distance entre le ref et l'eleve est inférieur à la distance entre l'eleve et le voisin dans neighbor 
            return i                                                                        #Renvoie i
        i += 1                                                                              #Incrémentation de 1
    return len(neighbors)                                                                   #Renvoie la taille du dictionnaire neighbors car ref sera insérer à la fin du dictionnaire

#Question 7
def insertion_NN(answer,ref,neighbors,k):
    """
    answer (tableau en paramètre) : contient les réponses d'un élève
    ref (dictionnaire en paramètre) : contient le nom de la maison ainsi que les réponses du fondateurs de maison
    neighbors (dictionnaire en paramètre) : contient les noms des maisons proche de la réponse de l'élève
    k (entier en paramètre) : entier qui doit : len(neighbors) <= k.  
    Fonction qui ajoute la ref dans le tableau neighbors au bon endroit, sachant que le tableau neighbors doit être de taille au plus k.
    """
    indice = insertion_position_NN(answer,ref,neighbors)        #Stockage de l'indice ou il faut ajouter ref
    if indice < k:                                              #Condition qui vérifie qui l'indice est inférieur à k
        neighbors.insert(indice,ref)                            #Ajout dans le tableau neighbors à l'indice indice ref
        if len(neighbors) > k:                                  #Condition qui vérifie si la taille du tableau neighbors et supérieur à k
            neighbors.pop()                                     #Suppression du dernier élément de neighbors

#Question 8 
def NN(answer,neighbors,k):
    """
    answer (tableau en paramètre) : contient les réponses d'un élève
    neighbors (dictionnaire en paramètre) : contient les noms des maisons proche de la réponse de l'élève
    k (entier en paramètre) : entier qui doit : len(neighbors) <= k.  
    Fonction qui retourne un tableau des k plus proches voisins triés du plus proche au moins proche
    """
    tab_voisins = []
    i = 0
    while i < len(neighbors):
        insertion_NN(answer, neighbors[i], tab_voisins, k)
        i += 1
    return tab_voisins

#Question 9
def NN_house(neighbors):
    """
    neighbors (dictionnaire en paramètre) : contient les noms des maisons proche de la réponse de l'élève
    Fonction qui renvoie la maison affecter à l'élève en fonction de ces voisins proche
    """
    tab_proche = [{"house" : "Serpentard" ,"frequency" : 0 },
                  {"house" : "Poufsouffle" , "frequency" : 0}, 
                  {"house" : "Serdaigle" , "frequency" : 0},
                  {"house" : "Gryffondor" , "frequency" : 0}]           #tableau contenant le nom des maisons ainsi que leurs frequence mis à 0 
    i = 0                                                               #Initialisation d'une variable
    max = 0                                                             #Initialisation d'une variable
    house = ""                                                          #Initialisation d'une variable
    while i < len(neighbors):                                           #Boucle qui parcourt le dictionnaire neighbors
        maison = neighbors[i]["house"]                                  #Stocke dans la varible maison le nom de la i ème maison
        j = 0                                                           #Initialisation d'une variable
        while j < len(tab_proche):                                      #Boucle qui parcourt le tableau de fréquence de chaque maison
            if tab_proche[j]["house"] == maison:                        #Condition pour vérifier si les maisons sont similaire
                tab_proche[j]["frequency"] += 1                         #Incrémentation de 1 de la fréquence de la maison
                if tab_proche[j]["frequency"] > max :                   #Condition pour vérifier le maximum de la fréquence d'une maison
                    max = tab_proche[j]["frequency"]                    #Modification du maximum de la fréquence de la maison
                    house = tab_proche[j]["house"]                      #Modification du nom de la maison la plus présente 
            j += 1                                                      #Incrémentation de 1
        i += 1                                                          #Incrémentation de 1
    i = 0                                                               #Initialisation d'une variable
    tab_deux_proche = []                                                #Initialisation d'un tableau
    while i < len(tab_proche):                                          #Boucle qui parcourt le tableau de la fréquence des maison
        if tab_proche[i]["frequency"] == max:                           #Condition qui vérifie le maximum 
            tab_deux_proche.append(tab_proche[i]["house"])              #Ajout dans le tableau des deux proches voisins
        i += 1                                                          #Incrémentation d'une variable
    house = tab_deux_proche[0]                                          #Stockage de la maison dans une variable
    return house                                                        #Renvoi de la maison affectée à l'élève

#Question 10
def NN_repartition(reponses,ref,k):
    """
    reponses (dictionnaire en paramètre) : contient les réponses de chaque élèves
    ref (tableau de dictionnaire en paramètre) : contient les réponses des fondateurs des maisons
    k (entier en paramètre) : entier qui doit : len(neighbors) <= k.  
    """
    dico_maison_affecte={}                                              #Initialisation d'un dictionnaire
    i = 0                                                               #Initialisation d'une variable
    nom_eleves=list(reponses)                                           #Ajout des clé du dictionnaire reponses dans une variable
    while i < len(reponses):                                            #Boucle pour parcourir le dictionnaire reponses
        voisins_proche = NN(reponse_eleves_s102[nom_eleves[i]],ref,k)   #Stockage du renvoie de la fonction NN
        maison = NN_house(voisins_proche)                               #Stockage du renvoie de la fonction NN_house
        dico_maison_affecte[nom_eleves[i]] = maison                     #Ajout dans le nouveau dictionnaire pour chaque élève sa maison affectée
        i += 1                                                          #Incrémentation de 1
    return dico_maison_affecte                                          #Renvoie le dictionnaire

nombre_erreur_1 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,house_ref,1),choixpeau))/len(reponse_eleves_s102))*100)
nombre_erreur_2 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,house_ref,2),choixpeau))/len(reponse_eleves_s102))*100)
nombre_erreur_3 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,house_ref,3),choixpeau))/len(reponse_eleves_s102))*100)
nombre_erreur_4 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,house_ref,4),choixpeau))/len(reponse_eleves_s102))*100)
nombre_erreur_5 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,house_ref,5),choixpeau))/len(reponse_eleves_s102))*100)

pourcentage_erreur_1 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,houses_multiple_ref,1),choixpeau))/len(reponse_eleves_s102))*100)
pourcentage_erreur_2 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,houses_multiple_ref,2),choixpeau))/len(reponse_eleves_s102))*100)
pourcentage_erreur_3 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,houses_multiple_ref,3),choixpeau))/len(reponse_eleves_s102))*100)
pourcentage_erreur_4 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,houses_multiple_ref,4),choixpeau))/len(reponse_eleves_s102))*100)
pourcentage_erreur_5 = (((nb_erreurs(NN_repartition(reponse_eleves_s102,houses_multiple_ref,5),choixpeau))/len(reponse_eleves_s102))*100)

print("Pour k valant 1, il y a ", nombre_erreur_1 ," erreurs ce qui correspond à ", pourcentage_erreur_1 ,"%")
print("Pour k valant 2, il y a ", nombre_erreur_2 ," erreurs ce qui correspond à ", pourcentage_erreur_2 ,"%")
print("Pour k valant 3, il y a ", nombre_erreur_3 ," erreurs ce qui correspond à ", pourcentage_erreur_3 ,"%")
print("Pour k valant 4, il y a ", nombre_erreur_4 ," erreurs ce qui correspond à ", pourcentage_erreur_4 ,"%")
print("Pour k valant 5, il y a ", nombre_erreur_5 ," erreurs ce qui correspond à ", pourcentage_erreur_5 ,"%")