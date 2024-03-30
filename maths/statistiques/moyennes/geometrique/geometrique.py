# -----------------------------------------------
# geometrique 
# -----------------------------------------------
# Permet de realiser une moyenne geometrique qui
# est plus insensible aux valeurs elevees que la
# moyenne arithmetique. Elle permet donc une es-
# timation meilleure des tendances centrales.

# Cette moyenne de n nombres (x1, x2,..., xn) est
# calculée en multipliant tous les nombres ensem-
# ble, puis en prenant la racine enième de ce mê-
# me produit.

# Formule : MG = (x1 * x2 * ... * xn) ** (1/n)

#------------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def geometrique(liste):
    produit = 1
    
    for valeur in liste:
        produit *= valeur
    
    return produit ** (1 / len(liste))



# -----------------------------------------------
# Application
# -----------------------------------------------

liste = [12, 14, 16, 8, 6, 18]
moyenne = geometrique(liste)
print("La moyenne est", round(moyenne, 2))



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

g=lambda l:(eval("*".join(map(str,l)))**(1/len(l)
))



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def geometrique_detaillee(liste):
    
    nbr_valeurs = len(liste)
    produit = 1
    
    for i in range(0, nbr_valeurs):
        valeur = liste[i]
        produit *= valeur
    
    enieme = 1 / nbr_valeurs
    moyenne = produit ** enieme
    
    return moyenne



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

def geometrique_commentee(liste):
    
    # Identifier la longueur de la liste.
    nbr_valeurs = len(liste)
    
    # Initialiser le produit a 1.
    produit = 1
    
    # De 0 a la longueur de la liste,
    for i in range(0, nbr_valeurs):
        
        # Récupérer la valeur à l'index i.
        valeur = liste[i]
        
        # Multiplier produit par cette valeur.
        produit *= valeur
    
    # Calculer le facteur enieme de la racine.
    enieme = 1 / nbr_valeurs
    
    # Effectuer la racine enieme du produit.
    moyenne = produit ** enieme
    
    # Retourner le resultat.
    return moyenne









#