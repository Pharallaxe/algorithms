# -----------------------------------------------
# Fonction automorphe
# -----------------------------------------------
# Un palindrome, c'est une chaîne qui de gauche à
# droite, et de droite à gauche possède les memes
# caractères.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.


def automorphe(nombre):
    longueur = len(str(nombre))

    carre = nombre ** 2

    carre_str = str(carre)
    carre_fin = carre_str[-longueur:]
    carre_fin_nombre = int(carre_fin)

    return carre_fin_nombre == nombre



# -----------------------------------------------
# Application
# -----------------------------------------------

nombre = 76
res = automorphe(nombre)
chaine = ["n'est pas", "est"][res]
print(f"{nombre} {chaine} automorphe")



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

A=lambda n:str(n**2)[-len(str(n)):]==str(n)



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Proche de la version raccourcie, mais avec des
# commentaires concis pour expliquer les etapes
# principales de la fonction.

def automorphe(nombre):
    # Récupérer la longueur du nombre.
    longueur = len(str(nombre))

    # Elever le nombre au carré.
    carre = nombre ** 2

    # Convertir en string.
    carre_str = str(carre)

    # Récupérer la fin du carré.
    carre_fin = carre_str[-longueur:]

    # Convertir la fin du carré en nombre.
    carre_fin_nombre = int(carre_fin)

    # Retourner la solution.
    return carre_fin_nombre == nombre









#