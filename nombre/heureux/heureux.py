# -----------------------------------------------
# heureux
# -----------------------------------------------
# Un nombre heureux a la somme des carrés de ses
# chiffres et ce de manière récursive donne 1.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def heureux(nombre):
    if nombre < 10:
        nombre = nombre ** 2
        
    while nombre > 9:
        total = 0
        
        for num in str(nombre):
            total += int(num) ** 2
        nombre = total
        
    return nombre == 1

# -----------------------------------------------
# Application
# -----------------------------------------------

for nb in range(10,16):
    res = heureux(nb)
    if res:
        print(f"{nb} est heureux.")
    else:
        print(f"{nb} n'est pas heureux.")



# -----------------------------------------------
# Version golf
# -----------------------------------------------

H=lambda n:(lambda g:g(g,n)==1)(lambda s,k:k if k
<10 else s(s,sum(int(x)**2 for x in str(k))))



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def heureux_commentee(nombre):
    
    # Si le nombre est inférieur à 10.
    if nombre < 10:
        
        # Elever le nombre au carre.
        nombre = nombre ** 2
        
    # Tant que le nombre est inferieur à 9.
    while nombre > 9:
        
        # Initialiser total a 0.
        total = 0
        
        # Parcourir chaque chiffre dans le nombre.
        for num in str(nombre):
            
            # Ajouter le carré au total.
            total += int(num) ** 2
            
        # Mettre à jour le nombre.
        nombre = total
        
    # Retourner le restultat.
    return nombre == 1









#