# -----------------------------------------------
# info
# -----------------------------------------------
# Il est conseille d'aller consulter l'algorithme
# des nombres premiers avant toute chose.
# -----------------------------------------------

# -----------------------------------------------
# diviseurs
# -----------------------------------------------
# Un diviseur est un nombre qui divise un entier
# en part equitable dans laisser de reste.
# Ex : 8 est diviseur de 24 => 3 * 8 = 24, mais 6
# est aussi diviseur de 24 => 4 * 6 = 24. En re-
# vanche, 5 n'est pas diviseur de 24 car 5 * 4 =
# 20, il faut encore 4 pour compléter 24.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def diviseurs(nombre):
    return [i for i in range(1, nombre + 1) 
             if nombre % i == 0]

# -----------------------------------------------
# Application
# -----------------------------------------------

nombres = [8, 24, 100, 120]
for nombre in nombres:
    res = diviseurs(nombre)
    print(f"Les diviseurs de ", end="")
    print(f"{nombre} sont {res}")



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

D=lambda N:[i for i in range(1,N+1)if N%i==0]



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def diviseurs_detaillee(nombre):
    diviseurs_liste = []
    
    for i in range(1, nombre + 1):
        if nombre % i == 0:
            diviseurs_liste.append(i)
    
    return diviseurs_liste



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

def diviseurs_commentee(nombre):
    # Initialiser une liste pour les diviseurs.
    diviseurs_liste = []
    
    # De 1 à nombre,
    for i in range(1, nombre + 1):
        
        # si le reste de la division de nombre
        # par i est egal à 0,
        if nombre % i == 0:
            
            # Ajouter i à la liste des diviseurs.
            diviseurs_liste.append(i)
    
    # Retourne la liste des diviseurs.
    return diviseurs_liste









#