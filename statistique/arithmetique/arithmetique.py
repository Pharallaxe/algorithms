# -----------------------------------------------
# arithmetique
# -----------------------------------------------
# Permet de realiser une moyenne a partir d'une 
# liste de plusieurs valeurs.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def arithmetique(liste):

    return sum(nbr for nbr in liste) / len(liste)



# -----------------------------------------------
# Application
# -----------------------------------------------

liste = [12, 14, 16, 8, 6, 18]
moyenne = arithmetique(liste)
print("La moyenne est", round(moyenne, 2))



# -----------------------------------------------
# Version golf
# -----------------------------------------------

A=lambda l:sum(v for v in l)/len(l)

# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

def arithmetique_detaillee(liste):
    nbr_valeurs = len(liste)
    somme = 0

    for i in range(0, nbr_valeurs):
        valeur = liste[i]
        somme += valeur

    moyenne = somme / nbr_valeurs

    return moyenne


# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def arithmetique_commentee(liste):

    # Calculer de la longueur de la liste.
    nbr_valeurs = len(liste)

    # Initialiser la somme a 0.
    somme = 0

    # De 0 a la longueur de la liste,
    for i in range(0, nbr_valeurs):
        
        # Récupérer la valeur à l'index i.
        valeur = liste[i]

        # Ajouter ce nombre a la somme.
        somme += valeur

    # Calculer de la moyenne arithmetique.
    moyenne = somme / nbr_valeurs

    # Retourner la moyenne arithmetique calculee.
    return moyenne









#