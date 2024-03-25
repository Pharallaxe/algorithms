# -----------------------------------------------
# Fonction bissextile
# -----------------------------------------------
# Fonction indiquant si une année est bissextile
# en suivant les règles du calendrier grégorien.
# -----------------------------------------------



# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def bissextile(annee):
    if annee % 400 == 0:
        return True
    elif annee % 100 == 0:
        return False
    elif annee % 4 == 0:
        return True
    else:
        return False



# -----------------------------------------------
# Application
# -----------------------------------------------

texte = ["n'est pas", "est"]
annees = [1900, 2000, 2024]
for annee in annees:
    est_bis = bissextile(annee)
    chaine = texte[est_bis]
    print(f"{annee} {chaine} bissextile.")



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

B=lambda a:a%400==0 or(a%100!=0 and a%4==0)



# -----------------------------------------------
# Version commentée
# -----------------------------------------------
# Similaire à la version détaillée, mais avec des
# commentaires concis afin d'expliquer les étapes
# principales de la fonction.

# On va du plus large vers le plus court.

def bissextile(annee):
    # Si une année est divisible par 400, elle
    # est bissextile.
    if annee % 400 == 0:
        return True
    
    # Sinon, si une année est divisible par 100,
    # sauf 400, elle n'est pas bissextile.
    elif annee % 100 == 0:
        return False
    
    # Sinon, si une année est divisible par 4,
    # elle est bissextile
    elif annee % 4 == 0:
        return True
    
    # Sinon, c'est une année quelconque, enfin,
    # sauf si c'est votre anniversaire.
    else:
        return False









#