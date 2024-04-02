# -----------------------------------------------
# harmonique
# -----------------------------------------------
# Permet de realiser une moyenne harmonique. Elle
# permet d'etablir une moyenne plus significative
# dans certains domaines, comme celui du calcul
# des vitesses?

# Cette moyenne de n nombres (x1, x2,..., xn) est
# calculee en divisant le nombre de valeurs par la
# somme des inverses de chaque valeur.

#                           N
# Formule : MH = --------------------------
#                (1/x1 + 1/x2 + ... + 1/xn)

# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def harmonique(liste):
    somme = sum(1 / n for n in liste)
    return len(liste) / somme



# -----------------------------------------------
# Application
# -----------------------------------------------

liste = [50, 90]
moyenne = harmonique(liste)
print("La moyenne est", round(moyenne, 2))



# -----------------------------------------------
# Version golf
# -----------------------------------------------

H=lambda l:len(l)/sum(1/n for n in l)



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

def harmonique_detaillee(liste):
    
    nbr_valeurs = len(liste)
    somme = 0
    
    for i in range(0, nbr_valeurs):
        valeur = liste[i]
        somme += 1 / valeur

    moyenne = nbr_valeurs / somme
    
    return moyenne



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def harmonique_commentee(liste):
    
    # Identifier la longueur de la liste.
    nbr_valeurs = len(liste)
    
    # Initialiser la somme a 0.
    somme = 0
    
    # De 0 a la longueur de la liste,
    for i in range(0, nbr_valeurs):
        
        # Récupérer la valeur à l'index i.
        valeur = liste[i]
        
        # Ajouter l'inverse de cette valeur à la
        # somme.
        somme += 1 / valeur

    # Calculer la moyenne.
    moyenne = nbr_valeurs / somme
    
    # Retourner la moyenne.
    return moyenne









#