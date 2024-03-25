# -----------------------------------------------
# Fonction deponctuer
# -----------------------------------------------
# Elle supprime d'une chaine les caractères don-
# nés en paramètre.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def deponctuer(chaine, liste):

    for char in liste:
        chaine = chaine.replace(char, "")
    
    return chaine



# -----------------------------------------------
# Application
# -----------------------------------------------

chaine = "C'est, un exemple! de ponctuation."
caracteres = ",.!'"

deponctuee = deponctuer(chaine, caracteres)

print("Chaine de depart :", chaine)
print("Chaine sans ponctuation :", deponctuee)



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

D=lambda c,l:''.join(x for x in c if x not in l)



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Proche de la version raccourcie, mais avec des
# commentaires concis pour expliquer les etapes
# principales de la fonction.

def deponctuer_commentee(chaine, liste):
    
    # Pour chaque caractère de la la liste,
    for char in liste:
        
        # Remplacer le caractère par rien.
        chaine = chaine.replace(char, "")
    
    # Retourner la chaine modifiée.
    return chaine









#