# -----------------------------------------------
# Fonction disarium
# -----------------------------------------------
# Un "disarium number" est un nombre qui est égal
# à la somme de ses chiffres élevés à la puissan-
# de leur index plus un dans le nombre.
# Ex. : 1^1 + 3^2 + 5^3 = 135
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def disarium(nombre):
    nombre_str = str(nombre)
    longueur = len(nombre_str)
    
    somme = sum(int(nombre_str[i]) ** (i + 1) for
                i in range(longueur))
        
    return somme == nombre



# -----------------------------------------------
# Application
# -----------------------------------------------

nombres = [120, 133, 135, 145]
for nb in nombres:
    res = disarium(nb)
    if res:
        print(f"{nb} est disarium.")
    else:
        print(f"{nb} n'est pas disarium.")



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

D=lambda n:sum(int(str(n)[i])**(i+1)for i in 
range(len(str(n))))==n



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def disarium_explication(nombre): #
    nombre_str = str(nombre)
    longueur = len(nombre_str)

    somme = 0

    for i in range(0, longueur):
        chiffre = int(nombre_str[i])
        puissance = i + 1
        somme += chiffre ** puissance
        
    return somme == nombre



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.


def disarium_commentee(nombre): #
    # Convertir le nombre en chaîne.
    nombre_str = str(nombre)
    
    # Calculer la longueur de la chaîne.
    longueur = len(nombre_str)
    
    # Initialiser la somme des chiffres à zéro.
    somme = 0
    
    # Parcourir chaque chiffre dans la chaîne.
    for i in range(0, longueur):
        # Convertir le caractère en chiffre.
        chiffre = int(nombre_str[i])
        
        # Définir la puissance en fonction de l'index.
        puissance = i + 1
        
        # Ajouter la puissance du chiffre à la somme.
        somme += chiffre ** puissance
    
    # Retourner la solution.
    return somme == nombre









#