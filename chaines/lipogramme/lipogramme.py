# -----------------------------------------------
# Fonction lipogramme
# -----------------------------------------------
# Un lipogramme est une chaine de caracteres qui
# ne contient aucun caractere donne, comme le e.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def lipogramme(chaine, lettre):
    chaine = chaine.lower()
    lettre = lettre.lower()
    
    chaine.replace(" ", "")
        
    return lettre not in chaine



# -----------------------------------------------
# Application
# -----------------------------------------------

chaine = "Le ver de terre."
lettre = "e"
est_lipogramme = lipogramme(chaine, lettre)
chaine = ["n'est pas", "est"][est_lipogramme]
print(f'"{chaine}" est un \
    lipogramme en "{lettre}".')



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

L=lambda s,l:l not in s.lower().replace(' ','')



# -----------------------------------------------
# Version commentée
# -----------------------------------------------
# Similaire à la version détaillée, mais avec des
# commentaires concis afin d'expliquer les étapes
# principales de la fonction.

def lipogramme(chaine, lettre):
    
    # Convertir en minuscules.
    chaine = chaine.lower()
    lettre = lettre.lower()

    # Supprimer les espaces.
    chaine.replace(" ", "")
    
    # Retourner le resultat.
    return lettre not in chaine









#