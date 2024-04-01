
# -----------------------------------------------
# Fonction factorielle
# -----------------------------------------------
# Calcul du produit des entiers de 1 a n, où n un
# entier positif est passe en argument.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def factorielle(nombre):
    produit = 1
 
    for nombre_actuel in range(1, nombre + 1):
        produit *= nombre_actuel
 
    return produit



# -----------------------------------------------
# Application
# -----------------------------------------------

resultat = factorielle(6) 
print(f"La factorielle de 6 est : {resultat}")



# -----------------------------------------------
# Version golf
# -----------------------------------------------

F=lambda n: (lambda f:f(f,n))(lambda s,x:1 if x==
    0 else x*s(s,x-1))



# -----------------------------------------------
# Version commentee
# -----------------------------------------------


def factorielle_commentee(nombre):
 
 # Initialiser du produit a 1.
 produit = 1
 
 # De 1 a nombre,
 for nombre_actuel in range(1, nombre + 1):

  # Multiplier par le nombre courant.
  produit *= nombre_actuel
 
 # Retourner la factorielle calculee.
 return produit









#