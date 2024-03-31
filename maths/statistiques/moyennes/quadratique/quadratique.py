# -----------------------------------------------
# quadratique
# -----------------------------------------------
# Cette fonction calcule la moyenne quadratique.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def quadratique(liste):
    somme_carres = sum(x ** 2 for x in liste)
    return (somme_carres / len(liste)) ** 0.5

# -----------------------------------------------
# Application
# -----------------------------------------------

liste = [12, 14, 16, 8, 6, 18]
moyenne = quadratique(liste)
print("La moyenne est", round(moyenne, 2))

# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

Q=lambda l:(sum(x**2 for x in l)/len(l))**0.5



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def quadratique_detaillee(liste):
    nbr_valeurs = len(liste)
    somme = 0
    
    for i in range(0, nbr_valeurs):
        valeur = liste[i]
        carre = valeur ** 2
        somme += carre
        
    division = somme / nbr_valeurs
    moyenne = division ** 0.5

    return moyenne

# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.


def quadratique_commentee(liste):
    
    # Recuperer le nombre de valeurs.
    nbr_valeurs = len(liste)
    
    # Initialiser une somme à 9.
    somme = 0
    
    # De 0 à nombre de valeurs,
    for i in range(0, nbr_valeurs):
        
        # recuperer la valeur de la liste à l'in-
        # dex i,
        valeur = liste[i]
        
        # elever cette valeur au carre, et
        carre = valeur ** 2
        
        # ajouter ce carre a la somme.
        somme += carre
    
    # Diviser la somme par le nombre de valeurs.
    division = somme / nbr_valeurs
    
    # Effecturer la racine carrée du resultat.
    moyenne = division ** 0.5

    # Retourner la moyenne ainsi calculee.
    return moyenne









#