# -----------------------------------------------
# fascinant
# -----------------------------------------------
# Un nombre est fascinant répond à certains cri-
# tères : lorsqu'il est multiplié par 2 et par 3,
# les chiffres du nombre initial, du double et du
# triple de ce nombre sont différents et contien-
# nent tous les chiffres de 1 à 9 une seule fois.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def fascinant(nombre):
    chaine_1 = str(nombre)
    
    if not len(chaine_1) > 3:
        return False
    
    chaine_2 = str(nombre * 2)
    chaine_3 = str(nombre * 3)
    
    resultat = chaine_1 + chaine_2 + chaine_3
    
    for i in range(1, 10):
        if str(i) not in resultat:
            return False
        
    return True



# -----------------------------------------------
# Application
# -----------------------------------------------

nombres = [108, 133, 192, 5832]
for nb in nombres:
    res = fascinant(nb)
    if res:
        print(f"{nb} est fascinant.")
    else:
        print(f"{nb} n'est pas fascinant.")



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

F=lambda n:all(str(i)in str(n)+str(2*n)+str(3*n)
for i in range(1,10))and len(str(n))>3



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Proche de la version raccourcie, mais avec des
# commentaires concis pour expliquer les etapes
# principales de la fonction.

def fascinant_commentee(nombre):
    # Convertir le nombre en string.
    chaine_1 = str(nombre)
    
    # Vérifier qu'il y a plus de 2 chiffres.
    if not len(chaine_1) > 2:
        return False
    
    # Convertir les nombres et ses multiples.
    chaine_2 = str(nombre * 2)
    chaine_3 = str(nombre * 3)
    
    # Concaténer les trois chaines.
    resultat = chaine_1 + chaine_2 + chaine_3
    
    # Pour chaque chiffre de 0 à 9,
    for i in range(1, 10):
        
        # Vérifier s'il est présent.
        if str(i) not in resultat:
            return False
        
    return True








#