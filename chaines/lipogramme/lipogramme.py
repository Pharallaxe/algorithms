# -----------------------------------------------
# Fonction lipogramme
# -----------------------------------------------
# Un lipogramme est une chaine de caracteres qui
# ne contient aucun caractere donne, comme le e.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def lipogramme(chaine, lettre):
    chaine = chaine.lower()
    lettre = lettre.lower()
    
    chaine.replace(" ", "")
        
    return lettre not in chaine



# -----------------------------------------------
# Application
# -----------------------------------------------

ch = "Le ver de terre"
lettre = "e"
est_lipogramme = lipogramme(ch, lettre)

print(f'"{ch}"', end="")

if est_lipogramme:
    print(" est un", end="")
else:
    print(" n'est pas", end="")
    
print(f" un lipogramme en '{lettre}'.")



# -----------------------------------------------
# Version golf
# -----------------------------------------------

L=lambda s,l:l not in s.lower().replace(' ','')



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def lipogramme_commentee(chaine, lettre):
    
    # Convertir en minuscules.
    chaine = chaine.lower()
    lettre = lettre.lower()

    # Supprimer les espaces.
    chaine.replace(" ", "")
    
    # Retourner le resultat.
    return lettre not in chaine









#