# -----------------------------------------------
# spirale_ulam
# -----------------------------------------------
# Cette spirale est une méthode simple qui permet
# de représenter les nombres premiers. Ainsi, ils
# forment des motifs qui n'ont jamais était réel-
# lement expliqués.
#
# Ex : de 0 à 576
# __________@___@___________@___________@________
# ____________@_______________________@_______@__
# __@_______@_______________@___________@________
# @___________________@_______@___@_______@___@__
# ______@___________@___________________@___@____
# ________@_______@___@__________________________
# ______________________@___@___________@_______@
# @_______@___@_______@_______________@_______@__
# ______________________@___@_______@____________
# ____@_______@___@___________@___@___@__________
# __@___@___@___@___@_______@_______________@____
# ____________________@___@___@__________________
# __________@_______@_____@_@___@___@___@_______@
# ____________@___@___@__________________________
# ______________@_______@________________________
# @___@_______@___@_______@_______@___@_______@__
# ______@_______@___________@___________@___@____
# ________________@_______________________@______
# ______@___@___________@_______@_______@________
# @_______@_______________________@______________
# __@___________@_______@___@____________________
# ____________@___@_______@___________@_______@__
# __@___________________@___@___________@________
# ____@_______________________@___@______________
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def spirale_ulam(n):
    grille = [[5, 4, 3], [6, 1, 2], [7, 8, 9]]
    inc = 6
    dernier = 9
    
    while inc < n * 2:
        b0 = grille[0]

        # Traiter la ligne du bas.
        if inc % 4 == 2:
            grille = [grille[i] +
                [len(b0) - i + dernier]
                for i in range(0, len(grille))]
            dernier += len(grille)
        
        # Traiter la ligne du haut.
        elif inc % 4 == 3:
            grille.insert(0,
                [int(dernier + i)
                for i in range(len(b0), 0, -1)])
            dernier += len(b0)+1
        
        # Traiter la ligne de gauche.
        elif inc % 4 == 0:
            grille = [
                [dernier + i] + grille[i]
                for i in range(0, len(grille))]
            dernier += len(grille)
        
        # Traiter la ligne de droite.
        elif inc % 4 == 1:
            grille.append(
                [dernier + i
                for i in range(0, len(b0))])
            dernier += len(b0) - 1
            
        inc += 1
    
    return grille



# -----------------------------------------------
# Application
# -----------------------------------------------

# Fonction pour le nombre de caractère minimal.
# par case.
def nombre_caracteres(grille):
    liste = [x for lig in grille for x in lig]
    maxi = max(liste)
    maxi_str = str(maxi)
    return len(maxi_str)

# Fonction identifier la primarite d'un nombre.
def premier(n):
    return n > 1 and all(n % i for i in range(2,
        int(n ** 0.5) + 1))

# Exemple de spirale de Ulam de taille 6.
LARGEUR = 12
grille = spirale_ulam(LARGEUR)
maxi = nombre_caracteres(grille)

print("Spirale avec tous les nombres")
for j in range(0,len(grille)):
    print([f"{{:{maxi}d}}".format(i)
           for i in grille[j]])

print("\nSpirale avec les nombres premiers")
for j in range(0,len(grille)):
    print([
        f"{{:{maxi}d}}".format(grille[j][i])
        if premier(grille[j][i])
        else " " * maxi
        for i in range(0,len(grille[0]))])

print("\nSpirale en motif")
for j in range(0,len(grille)):
    print("_".join([
        "@"
        if premier(grille[j][i])
        else "_"
        for i in range(0,len(grille[0]))]))

# -----------------------------------------------
# Version golf
# -----------------------------------------------

def SU(n):
 b,i,d=[[5,4,3],[6,1,2],[7,8,9]],6,9
 while i<n*2:
  b0=b[0]
  if i%4==2:b=[b[j]+[len(b0)-j+d]for j in
   range(len(b))];d+=len(b)
  elif i%4==3:b.insert(0,[d+i for i in
   range(len(b0),0,-1)]);d+=len(b0)+1
  elif i%4==0:b=[[d+i]+b[j]for j in
   range(len(b))];d+=len(b)
  elif i%4==1:b.append([d+i for i in
   range(len(b0))]);d+=len(b0)-1
  i+=1
 return b



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

def spirale_ulam_detaillee(n):
    grille = [[5, 4, 3], [6, 1, 2], [7, 8, 9]]
    inc = 6
    dernier = 9
    
    while inc < n * 2:
        b0 = grille[0]
        
        # Traiter la ligne du bas.
        if inc % 4 == 2:
            n_grille = []
            for i in range(0, len(grille)):
                el = len(grille[0]) - i + dernier
                n_ligne = grille[i] + [el]
                n_grille.append(n_ligne)
            grille = n_grille

        # Traiter la ligne du haut.
        elif inc % 4 == 3:
            n_ligne = []
            for i in range(len(b0), 0, -1):
                n_ligne.append(dernier + i)
            grille.insert(0, n_ligne)
            dernier += len(b0) + 1

        # Traiter la colonne de gauche.
        elif inc % 4 == 0:
            for i in range(0, len(grille)):
                n_colonne = []
                for j in range(len(grille[i])):
                    n_colonne.append(dernier + j)
                grille[i]=[dernier+i] + grille[i]
            dernier += len(grille)

        # Traiter la colonne de droite.
        elif inc % 4 == 1:
            n_colonne = []
            for i in range(0, len(b0)):
                n_colonne.append(dernier + i)
            grille.append(n_colonne)
            dernier += len(b0) - 1
            
        inc += 1
    return grille



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def spirale_ulam_commentee(n):
    # Initialiser le premier carré de base.
    grille = [[5, 4, 3], [6, 1, 2], [7, 8, 9]]
    
    # Initialiser un increment à 6.
    inc = 6
    
    # Récupérer la dernier valeur de la grille.
    dernier = 9
    
    # Tant que increment est plus petit que 2n.
    while inc < n * 2:
        
        # Récupérer l'index 0 de la grille.
        b0 = grille[0]

        # TRAITER LA LIGNE DU BAS.
        if inc % 4 == 2:
            
            # initialiser une liste vide pour
            # stocker les résultats réalisés.
            n_grille = []

            # Itérer sur les indices de grille.
            for i in range(0, len(grille)):
                
                # Calculer le nouvel élément.
                el = len(grille[0]) - i + dernier
                
                # Ajouter le nouvel élément à la
                # liste correspondante dans la
                # grille.
                n_ligne = grille[i] + [el]
                
                # Ajouter la nouvelle liste à la
                # liste des résultats réalisés.
                n_grille.append(n_ligne)
                
            # Remplacer grille par la n_grille.
            grille = n_grille
        
        # TRAITER LA LIGNE DU HAUT.
        elif inc % 4 == 3:
            
            # initialiser une liste vide pour
            # stocker les résultats réalisés.            
            n_ligne = []
            
            # De longueur de b0 à 0, avec une in-
            # crémentation de -1.
            for i in range(len(b0), 0, -1):
                
                # Ajouter le prochain nombre.
                n_ligne.append(dernier + i)

            # Insérer la nouvelle ligne en haut
            # de la grille.
            grille.insert(0, n_ligne)

            # Mettre à jour la valeur de dernier.
            dernier += len(b0) + 1
        
        # TRAITER LA COLONNE DE GAUCHE.
        elif inc % 4 == 0:
            
            # Ajouter un nouvel élément en tête
            # de chaque ligne de la grille.
            
            # De 0 à la hauteur de la grille,
            for i in range(0, len(grille)):

                # initialiser une liste vide pour
                # stocker les résultats réalisés.                 
                n_colonne = []
                
                # De 0 à la largeur de la grille,
                for j in range(len(grille[i])):
                    
                    # ajouter le prochain nombre.
                    n_colonne.append(dernier + j)
                
                # Ajouter de la colonne.
                grille[i]=[dernier+i] + grille[i]

            # Mettre à jour la valeur de dernier.
            dernier += len(grille)

        # TRAITER LA COLONNE DE DROITE.
        elif inc % 4 == 1:
            
            # créer une nouvelle ligne à ajouter
            # à la fin de la grille.
            n_colonne = []
            
            # De 0 à longueur de b0,
            for i in range(0, len(b0)):
                
                # Ajouter le prochain nombre.
                n_colonne.append(dernier + i)

            # Ajouter la nouvelle ligne à la fin
            # de la grille.
            grille.append(n_colonne)

            # Mettre à jour la valeur de dernier.
            dernier += len(b0) - 1
        
        # Incrementer inc.
        inc += 1
    
    # Retourner la grille.
    return grille









#