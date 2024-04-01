# -----------------------------------------------
# pgcd (plus grand commun diviseur)
# -----------------------------------------------
# Fonction qui identifie le nombre le plus grand 
# diviseur de deux autres nombres donnes.
# Avec 20 et 30, nous avons 10, car 
# - 20 => 1, 2, 4, 5, 10.
# - 30 => 1, 2, 3, 5, 10, 15.
# Il y a 1, 2, 5, 10 mais 10 est le plus grand.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def pgcd(nb1, nb2):
    if nb1 < nb2:
        nb1, nb2 = nb2, nb1
    
    while nb2 != 0:
        nb1, nb2 = nb2, nb1 % nb2
    
    return nb1



# -----------------------------------------------
# Application
# -----------------------------------------------

nbr_1 = 18
nbr_2 = 24
res = pgcd(nbr_1, nbr_2)

print(f"Le pgcd de {nbr_1} et {nbr_2} est {res}")



# -----------------------------------------------
# Version golf
# -----------------------------------------------

P=lambda n,N:n if not N else P(N,n%N)



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

def pgcd_detaillee(nombre_1, nombre_2):
    
    if nombre_1 < nombre_2:
        temporaire = nombre_1
        nombre_1 = nombre_2
        nombre_2 = temporaire
    
    while nombre_2 != 0:
        temporaire = nombre_2
        nombre_2 = nombre_1 % nombre_2
        nombre_1 = temporaire

    return nombre_1



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def pgcd_commentee(nombre_1, nombre_2):
    
    # Si le premier est inferieur au deuxieme,
    if nombre_1 < nombre_2:
        
        # On depose la valeur du premier dans une
        # variable temporaire.
        temporaire = nombre_1
        
        # On depose la valeur du deuxieme dans la
        # la variable du premier.
        nombre_1 = nombre_2
        
        # On depose la valeur de la variable tem-
        # poraire dans la variable du deuxieme.
        nombre_2 = temporaire
    
    # Tant que le deuxieme est different de zero.
    while nombre_2 != 0:
        
        # On depose la valeur du deuxieme dans une
        # variable temporaire.
        temporaire = nombre_2
        
        # On depose le resultat de la division du
        # premier par le deuxieme dans la varia-
        # ble du deuxieme.
        nombre_2 = nombre_1 % nombre_2
        
        # On depose la valeur de la variable tem-
        # poraire dans la variable du deuxieme.
        nombre_1 = temporaire

    return nombre_1









#