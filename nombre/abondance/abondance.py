# -----------------------------------------------
# abondance
# -----------------------------------------------
# Fonction qui retourne l'abondance d'un nombre.
# L'abondance c'est le rapport entre la somme des
# diviseurs du nombre sauf lui même et le nombre
# lui-même.

# Ex : L'abondance de 28  est de 1. En effet, ses
# diviseurs sont 1, 2, 4, 7, 14. Leur somme égale
# 28. C'est un nombre parfait. Lorsque l'abondan-
# ce est au dessus de 1, on dit que c'est un nom-
# bre abondant. Si elle est en-deça de 1, on dira
# qu'il est déficient.
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

A=lambda n:(D:=sum(i for i in range(1, n)if n%i==
0))/n if n>=1 else None



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

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