# -----------------------------------------------
# Fonction pangramme
# -----------------------------------------------
# Un pangramme est une chaine de caractères qui
# contient toutes les lettres de l'alphabet.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def pangramme(chaine):
    lettres = set()
    for ch in chaine.lower():
        if ch.isalpha():
            lettres.add(ch)
    return len(lettres) == 26



# -----------------------------------------------
# Application
# -----------------------------------------------

chaine = "Portez ce vieux whisky"
chaine += "au juge blond qui fume"
est_pangr = pangramme(chaine)
if (est_pangr):
    print(f'"{chaine}" est un pangramme.')
else:
    print(f'"{chaine}" n\'est pas un pangramme.')



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

def p2(ch):return len(set(c.lower()for c in ch if
c.isalnum())) == 26

def p1(chaine):return len(set(filter(str.isalpha,
chaine.lower()))) == 26

p=lambda C:len(
    {c for c in C.lower() if c.isalpha()})==26



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def pangramme_detaillee(chaine):
    chaine = chaine.lower()
    liste = []
    
    for ch in chaine:
        if ch.isalnum():
            liste.append(ch)

    lettres = set(liste)
    alpha = len(lettres) == 26
    
    return alpha



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

def pangramme_commentee(chaine):
    
    # Convertir en minuscule.
    chaine = chaine.lower()

    # Créer une liste vide.
    liste = []
    
    # Boucler sur chaque caractère.
    for ch in chaine:
        
        # Si la le caractère est alphanumérique.
        if ch.isalnum():
            
            # Ajouter le caractère à la liste.
            liste.append(ch)

    # Convertir la liste en un ensemble.
    lettres = set(liste)
    
    # Verifier s'il y a 26 lettres.
    alpha = len(lettres) == 26
    
    # Retourner la réponse.
    return alpha









#