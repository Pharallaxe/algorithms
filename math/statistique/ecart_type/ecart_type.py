# -----------------------------------------------
# ecart-type
# -----------------------------------------------
# L'ecart-type est la racine carree de la varian-
# ce. Il indique a quel point les valeurs indivi-
# duelles d'un ensemble de donnees s'ecartent de
# la moyenne de cet ensemble. 
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def ecart_type(liste):
    longueur = len(liste)
    somme = sum(liste)
    
    moy = somme / longueur
    carres = sum((x - moy) ** 2 for x in liste)
    
    return (carres / longueur) ** 0.5



# -----------------------------------------------
# Application
# -----------------------------------------------

liste = [12, 14, 16, 8, 6, 18]
variance = ecart_type(liste)
print("L'ecart type des valeurs est",
      round(variance, 2))

# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

ET=lambda l:((sum((x-(sum(l)/len(l)))**2 for x in
l)/len(l))**0.5)



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def ecart_type_detaillee(liste):

    longueur = len(liste)
    somme = 0
    somme_carres = 0

    for courant in liste:
        somme += courant

    moyenne = somme / longueur
    

    for courant in liste:
        ecart = courant - moyenne
        carre_ecart = ecart ** 2
        somme_carres += carre_ecart

    variance = somme_carres / longueur
    ecart_type = variance ** 0.5

    return ecart_type



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

def ecart_type_commentee(liste):

    # Recuperer la longueur de la liste.
    longueur = len(liste)

    # Initialiser la somme a 0.
    somme = 0

    # Calculer la somme des carres des ecarts.
    somme_carres = 0
    
    # Calculer de la moyenne de la liste.
    for courant in liste:

        # Ajouter ce nombre a la somme.
        somme += courant

    # Diviser la sommer par le nombre de termes.
    moyenne = somme / longueur

    # Pour chaque terme de la liste a etudier.
    for courant in liste:

        # Calculer l'ecart entre le nombre et la
        # moyenne.
        ecart = courant - moyenne

        # Calculer le carre de l'ecart.
        carre_ecart = ecart ** 2

        # Ajouter le carre de l'ecart a la somme.
        somme_carres += carre_ecart

    # Calculer de la variance.
    variance = somme_carres / longueur

    # Calculer la racine carree de la variance.
    ecart_type = variance ** 0.5

    # Retourner l'ecart-type resultant.
    return ecart_type









#