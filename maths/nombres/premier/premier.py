# -----------------------------------------------
# premier
# -----------------------------------------------
# Un nombre premier est un nombre qui n'est divi-
# sible que par 1 ou par lui-même.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def premier(nombre):
    if nombre < 2:
        return False
    
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
        
    return True



# -----------------------------------------------
# Application
# -----------------------------------------------

nombres = [76, 101, 17, 58]
for nombre in nombres:
    res = premier(nombre)
    chaine = ["n'est pas", "est"][res]
    print(f"{nombre} {chaine} premier.")



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

P=lambda n:n>1 and all(n%i for i in range(2,int(n
**0.5)+1))



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def premier_detaillee(nombre):
    
    if nombre < 1:
        return False
    
    racine_carree = int(nombre ** 0.5)
    
    for entier in range(2, racine_carree + 1):
        reste = nombre % entier

        if reste == 0:
            return False
        
    return True


# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

def premier_commentee(nombre):
    
    # Si le nombre est inférieur a 2,
    if nombre < 1:
        
        # renvoyer False.
        return False
    
    # Calculer la racine carrée de nombre.
    racine_carree = int(nombre ** 0.5)
    
    # Pour les nombres de 2 à la racine carrée,
    for entier in range(2, racine_carree + 1):
        
        # Récupérer le reste de la division du
        # nombre par i 
        reste = nombre % entier
        
        # Si le reste est égal à 0,
        if reste == 0:
            
            # c'est que le nombre est divisble
            # par l'entier : on retourne False.
            return False
        
    # Si nombre n'est divisible par aucun nombre
    # entre 2 et sa racine carrée, alors il est
    # premier : on retourne True.
    return True









#