# -----------------------------------------------
# Fonction deponctuer
# -----------------------------------------------
# Elle supprime d'une chaine les caractères don-
# nés en paramètre.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

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

D=lambda c,l:''.join(x for x in c if x not in l)



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def deponctuer_commentee(chaine, liste):
    
    # Pour chaque caractère de la la liste,
    for char in liste:
        
        # Remplacer le caractère par rien.
        chaine = chaine.replace(char, "")
    
    # Retourner la chaine modifiée.
    return chaine









#