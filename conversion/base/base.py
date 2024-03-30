# -----------------------------------------------
# Fonction Base
# -----------------------------------------------
# Fonction convertissant un nombre une base vers
# une autre..
# -----------------------------------------------



# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def base(nombre, depart, fin):
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Conversion du nombre de la base de départ à
    # la base décimale
    decimal = 0
    for chiffre in str(nombre):
        decimal = decimal * depart + int(chiffre)

    # Conversion du nombre à la base de fin
    resultat = ""
    
    while decimal > 0:
        reste = decimal % fin
        resultat = base[reste] + resultat
        decimal //= fin

    return resultat

# -----------------------------------------------
# Application
# -----------------------------------------------

conversions = [
    ("1010", 2, 10),
    ("48", 10, 3)
]

for conversion in conversions:
    chaine = conversion[0]
    depart = conversion[1]
    arrivee = conversion[2]
    res = base(chaine, depart, arrivee)
    conv_1 = f"{depart} vers {arrivee}"
    print(f"'{chaine}' de {conv_1} donne {res}")
    
    

# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

# En reflexion d'une solution efficace.... 



# -----------------------------------------------
# Version détaillée
# -----------------------------------------------
# Cette version permet de suivre pas à pas l'exé-
# cution de la fonction.

def base_detaillee(nombre, depart, fin):
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = 0
    
    nombre_inv = list(nombre)[::-1]
    longueur = len(nombre_inv)
    
    for i in range(0, longueur):
        base_index = base.index(nombre_inv[i])
        val +=  base_index * depart ** i
    
    convertis = []
    
    if val == 0:
        return "0"
    else:
        while val >= fin - 1:
            ch_base_fin  = val % fin
            convertis.append(base[ch_base_fin])
            val = val // fin
        
        if val != 0:
            convertis.append(base[val])
        
        convertis.reverse()
        retour = ''.join(convertis)
        
        return retour



# -----------------------------------------------
# Version commentée
# -----------------------------------------------
# Similaire à la version détaillée, mais avec des
# commentaires concis afin d'expliquer les étapes
# principales de la fonction.

def base_commentee(nombre, depart, fin):
    
    # Définir les symboles des les bases.
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Initialiser la val convertie en base 10.
    val = 0
    
    # Inverser la chaîne.
    nombre_inv = list(nombre)[::-1]
    
    # Récupérer la longueur de la chaine.
    longueur = len(nombre_inv)
    
    # Convertir la base départ vers la base 10.
    for i in range(0, longueur):
        
        # Trouver l'index du symbole.
        base_index = base.index(nombre_inv[i])
        
        # Ajouter la val convertie à la base 10.
        val +=  base_index * depart ** i
    
    # Initialiser une liste.
    convertis = []
    
    # Si la val est 0,
    if val == 0:
        
        # Retourner 0.
        return "0"
    
    # Sinon,
    else:
        
        # Convertir de la base 10 vers "fin".
        while val >= fin - 1:
            
            # Calculer le chiffre dans la base
            # de destination.
            ch_base_fin  = val % fin
            
            # Ajouter le chiffre à la liste des
            # chiffres convertis.
            convertis.append(base[ch_base_fin])
            
            # Mettre à jour la val pour le
            # prochain chiffre.
            val = val // fin
        
        # Si la val est différente de 0.
        if val != 0:
            
            # Ajouter le dernier chiffre.
            convertis.append(base[val])
            
        # Inverser la liste des chiffres.
        convertis.reverse()
        
        # Concaténer tous les chiffres.
        retour = ''.join(convertis)
        
        # Retourner le résultat.
        return retour









#