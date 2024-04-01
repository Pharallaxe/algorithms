# -----------------------------------------------
# quadratique
# -----------------------------------------------
# Cette fonction calcule la moyenne quadratique.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

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

Q=lambda l:(sum(x**2 for x in l)/len(l))**0.5



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

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