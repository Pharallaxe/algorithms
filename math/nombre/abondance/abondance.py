# -----------------------------------------------
# abondance
# -----------------------------------------------
# Fonction qui retourne l'abondance d'un nombre.
# L'abondance c'est le rapport entre la somme des
# diviseurs du nombre et le nombre lui-même.
# -----------------------------------------------

def abondance(nombre):
    if nombre < 1:
        return None
    
    somme_diviseurs = sum(
        i
        for i in range(1,nombre)
        if nombre % i == 0)
    
    return somme_diviseurs / nombre



# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

nombres = [2, 6, 28, 24, 120, 30240, 997920]

for nb in nombres:
    res = abondance(nb)
    
    affichage = f"{nb} est "
    if res == 1:
        affichage += "parfait"
    elif res < 1 :
        affichage += "deficient"
    else:
        affichage += "abondant"
    affichage += f" (abondance de {res})."
    print(affichage)



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

A=lambda n:(D:=sum(i for i in range(1, n)if n%i==
0))/n if n>=1 else None



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def abondance_detaillee(nombre):
    
    if nombre < 1:
        return None
    
    somme_diviseurs = 0
    
    for i in range(1, nombre):
        if nombre % i == 0:
            somme_diviseurs += i
    
    abondance = somme_diviseurs / nombre
    
    return abondance



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

def abondance_detaillee(nombre):
    
    # Si le nombres est inférieur à 1,
    if nombre < 1:
        
        # Retourner null.
        return None
    
    # Initialiser la somme des diviseurs à 0.
    somme_diviseurs = 0
    
    # De 1 à nombres,
    for i in range(1, nombre):
        
        # Si le nombre est divisible par i.
        if nombre % i == 0:
            
            # alors ajouter i à la somme.
            somme_diviseurs += i
            
    # Calculer l'abondance en divisant la somme
    # par le nombre.
    abondance = somme_diviseurs / nombre
    
    # Retourner l'abondance.
    return abondance









#