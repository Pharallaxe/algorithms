# -----------------------------------------------
# Fonctions romain <=> entier
# -----------------------------------------------
# Ensemble de fonctions qui permettent de conver-
# tir des entiers en écriture romaine et inverse-
# ment et de faire des opérations. 
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

# Convertit un nombre romain en entier.
def vers_entier(chaine):
    double = {
        "CM": 900, "CD": 400, "XC": 90, "XL": 40,
        "IX": 9, "IV": 4 }
    unique = { 
        "M": 1000, "D": 500, "C": 100, "L": 50,
        "X": 10, "V": 5, "I": 1 }
    
    entier = 0
    i = 0
    
    while i < len(chaine):
        if (i < len(chaine) - 1 and
            chaine[i:i + 2] in double):
            entier += double[chaine[i:i + 2]]
            i += 2
        else:
            entier += unique[chaine[i]]
            i += 1
    return str(entier)


# Convertit une entier en nombre romain.
def vers_romain(nombre):
    int_rom = [
        (1000, "M" ), (900, "CM"), (500,  "D"),
        ( 400, "CD"), (100,  "C"), ( 90, "XC"),
        (  50,  "L"), ( 40, "XL"), ( 10,  "X"),
        (   9, "IX"), (  5,  "V"), (  4, "IV"),
        (   1,  "I")
    ]
    
    romain = []
    for i, num in int_rom:
        while nombre >= i:
            nombre -= i
            romain.append(num)
    return "".join(romain)

# Retourne le resultat de l'operation entre deux
# nombres romains : ce dernier ne doit pas être
# plus petit que 0.

def romain_op(str1, str2, op, nombre = False):
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a // b
    }
    nombre1 = int(vers_entier(str1))
    nombre2 = int(vers_entier(str2))
    resultat = ops[op](nombre1, nombre2)
    if nombre:
        resultat = vers_romain(resultat)
    return resultat


# -----------------------------------------------
# Application
# -----------------------------------------------

romain_1 = "XVII"
romain_2 = "IX"
nombre_3 = 562

# Conversion des romains en nombres entiers.
nombre_1 = vers_entier(romain_1)
nombre_2 = vers_entier(romain_2)
romain_3 = vers_romain(nombre_3)

# Application de l'operation.
resultat = romain_op(romain_1, romain_2, "+")

# Affichage des resultats
print(f"1) {romain_1} est egal {nombre_1}")
print(f"2) {romain_2} est egal {nombre_2}")
print(f"3) {nombre_3} est egal {romain_3}")
print(f"4) {romain_1} + {romain_2} = {resultat}")



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !


# En reflexion d'une solution efficace....



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

# Convertit un nombre romain en entier.
def vers_entier(chaine):
    
    # Créer un dictionnaire de valeurs doubles.
    double = {"CM": 900, "CD": 400, "XC": 90,
              "XL": 40, "IX": 9, "IV": 4}
    
    # Créer un dictionnaire de valeurs uniques.
    unique = {"M": 1000, "D": 500, "C": 100,
              "L": 50, "X": 10, "V": 5, "I": 1}

    # Initialiser une variable entier à 0.
    entier = 0
    
    # Initialiser l'index à 0.
    i = 0
    
    # Boucler pour parcourir la chaîne.
    while i < len(chaine):
        
        # Vérifier su un double caractères existe
        # dans le dictionnaire des doubles.
        if (i < len(chaine) - 1 and
            chaine[i:i + 2] in double):
            
            # Ajouter la valeur correspondante.
            entier += double[chaine[i:i + 2]]
            
            # Avancer de deux caractères.
            i += 2
            
        else:
            # Ajouter la valeur à l'entier.
            entier += unique[chaine[i]]
            
            # Avancer d'un caractère.
            i += 1
            
    # Retourner le nombre entier converti.
    return str(entier)

# Convertit une entier en nombre romain.
def vers_romain(nombre):
    # Lister des entiers et les valeurs romaines.
    int_rom = [(1000, "M"), (900, "CM"),
               (500, "D"), (400, "CD"),
               (100, "C"), (90, "XC"), (50, "L"),
               (40, "XL"), (10, "X"), (9, "IX"),
               (5, "V"), (4, "IV"), (1, "I")]

    # Lister pour stocker les caractères romains.
    romain = []
    
    # Boucler pour parcourir les valeurs entières
    # et leurs correspondants romains.
    for i, num in int_rom:
        
        # Tant que nombre est superieur ou égal
        # à la valeur entière.
        while nombre >= i:
            
            # Soustraire la valeur entière.
            nombre -= i
            
            # Ajouter le caractère romain.
            romain.append(num)
            
    # Retourner la chaîne de caractères formée
    # des caractères romains.
    return "".join(romain)


# Retourne le resultat de l'operation entre deux
# nombres romains :
def romain_op(str1, str2, op, nombre = False):
    # Créer un dictionnaire des opérations.
    ops = {"+": lambda a, b: a + b,
           "-": lambda a, b: a - b,
           "*": lambda a, b: a * b,
           "/": lambda a, b: a // b}
    
    # Convertir les nombres romains en entiers.
    nombre1 = int(vers_entier(str1))
    nombre2 = int(vers_entier(str2))
    
    # Effectue l'opération sur les deux entiers.
    resultat = ops[op](nombre1, nombre2)
    
    # Si demandé,
    if nombre:
        
        # convertir le résultat en nombre romain.
        resultat = vers_romain(resultat)
        
    # Retourner le résultat de l'opération.
    return resultat









#