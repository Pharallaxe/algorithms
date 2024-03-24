# -----------------------------------------------
# puissances
# -----------------------------------------------
# Fonction qui renvoie les n premieres puissances
# d'un nombre donne excepte celle 0.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def puissances(nombre, puissance):
    liste = list()
    
    for i in range(1,puissance+1):
        liste += [pow(nombre,i)]
        
    return liste
    
    
    
# -----------------------------------------------
# Application
# -----------------------------------------------

nombre = 2
puissance = 16
res = puissances(nombre, puissance)

print(f"Les {puissance} premieres ", end="")
print(f"puisances de {nombre} sont", end="")
print(f" {res}")



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

P=lambda n,p:[*map(lambda i:n**i,range(1,p+1))]



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def puissances(nombre, puissance):
    
    liste = list()
    
    for i in range(1,puissance+1):
        res = pow(nombre,i)
        liste.append(res)
        
    return liste



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Proche de la version raccourcie, mais avec des
# commentaires concis pour expliquer les etapes
# principales de la fonction.

def puissances(nombre, puissance):
    
    # Initialiser une liste vide.
    liste = list()
    
    # Pour i allant de 1 a puissance + 1.
    for i in range(1,puissance+1):
        
        # Calculer la puissance.
        res = pow(nombre,i)
        
        # Ajouter la puissance a la liste.
        liste.append(res)
        
    # Retourner la liste.
    return liste
    
    
    







#