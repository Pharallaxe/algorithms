# -----------------------------------------------
# strobogrammatique
# -----------------------------------------------
# Un nombre strobogrammatique peut se lire de la
# même façon après avoir subi une rotation de 180
# degrés.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def strobogrammatique(nombre):
    chifs = ["0", "1", "8", "6", "9"]
    corrs = ["0", "1", "8", "9", "6"]
    
    if isinstance(nombre, int):
        nombre = str(nombre)
    
    for i in range(len(nombre) // 2 + 1):
        chif = nombre[i]
        corr = nombre[len(nombre) - 1 - i]
        
        if chif not in chifs or \
            corrs[chifs.index(chif)] != corr:
            return False
            
    return True



# -----------------------------------------------
# Application
# -----------------------------------------------

nombres = [88, 133, 96, 101]
for nb in nombres:
    res = strobogrammatique(nb)
    strobo = "strobogrammatique";
    if res:
        print(f"{nb} est {strobo}.")
    else:
        print(f"{nb} n'est pas {strobo}.")



# -----------------------------------------------
# Version golf
# -----------------------------------------------

S=lambda n:all(str(n)[i]in"01869"and"01896"["018\
69".index(str(n)[i])]==str(n)[~i]for i in range(\
len(str(n))//2+1))



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

def strobogrammatique_detaillee(nombre):
    strobo = {
        "0" : "0",
        "1" : "1",
        "8" : "8",
        "6" : "9",
        "9" : "6"
        }
    
    if type(nombre) is int:
        nombre = str(nombre)
        
    gauche = 0
    droite = len(nombre) - 1
    
    while droite - gauche >= 0:
        premier = nombre[gauche]
        dernier = nombre[droite]
        if (
            not premier in strobo.keys() or
            not dernier in strobo.keys() or
            premier != strobo[dernier]
            ):
            return False
        
        droite -= 1
        gauche += 1
        
    return True



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def strobogrammatique_commentee(nombre):
    
    # Définir un dictionnaire de correspondance.
    strobo = {
        "0" : "0",
        "1" : "1",
        "8" : "8",
        "6" : "9",
        "9" : "6"
        }
    
    # Vérifier si le type du nombre est entier.
    if type(nombre) is int:
        
        # Convertir le nombre en chaîne.
        nombre = str(nombre)
    
    # Initialiser les index.
    gauche = 0
    droite = len(nombre) - 1
    
    # Tant que la différence est supérieure ou
    # égale à 0.
    while droite - gauche >= 0:
        
        # Obtenir le premier chiffre.
        premier = nombre[gauche]
        
        # Obtenir le dernier chiffre.
        dernier = nombre[droite]
        
        # Si,
        if (
            # le premier n'est pas dans le
            # dictionnaire.
            not premier in strobo.keys() or
            
            # le dernier n'est pas dans le
            # dictionnaire.
            not dernier in strobo.keys() or
            
            # si le premier et le dernier sont
            # différents.
            premier != strobo[dernier]
            ):
            
            # Retourner faux.
            return False
        
        # Décrémenter les index.
        droite -= 1
        gauche += 1
    
    # Retourner le resultat.
    return True









#