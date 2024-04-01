# -----------------------------------------------
# spirale
# -----------------------------------------------
# Permet de réaliser une spirale partant de haut
# à gauche.
#
# Ex :
#
#   + + + + + + + + + + + + + + + + + + + + + + +
#                                               +
#   + + + + + + + + + + + + + + + + + + + + +   +
#   +                                       +   +
#   +   + + + + + + + + + + + + + + + + +   +   +
#   +   +                               +   +   +
#   +   +   + + + + + + + + + + + + +   +   +   +
#   +   +   +                       +   +   +   +
#   +   +   +   + + + + + + + + +   +   +   +   +
#   +   +   +   +               +   +   +   +   +
#   +   +   +   +   + + + + +   +   +   +   +   +
#   +   +   +   +   +       +   +   +   +   +   +
#   +   +   +   +   +   + + +   +   +   +   +   +
#   +   +   +   +   +           +   +   +   +   +
#   +   +   +   +   + + + + + + +   +   +   +   +
#   +   +   +   +                   +   +   +   +
#   +   +   +   + + + + + + + + + + +   +   +   +
#   +   +   +                           +   +   +
#   +   +   + + + + + + + + + + + + + + +   +   +
#   +   +                                   +   +
#   +   + + + + + + + + + + + + + + + + + + +   +
#   +                                           +
#   + + + + + + + + + + + + + + + + + + + + + + +
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def hors_grille(T, dj, di):
    return dj < 0 or dj >= T or di < 0 or di >= T


def si_coche(grille, T, dj, di, plein):
    if hors_grille(T, dj, di): 
        return False
    
    return grille[dj][di] == plein


def spirale(T, plein, vide):
    grille = [
        [vide for _ in range(T)]
        for _ in range(T)
    ]
    
    grille[0][0] = plein
    
    voisins =      [[0,1],[1, 0],[ 0,-1],[-1, 0]]
    voisins_diag = [[1,1],[1,-1],[-1,-1],[-1, 1]]
    courant = [0, 0]
    
    index = 0
    compteur = 1
    
    # Boucler pour effectuer la spirale.
    while True:
        
        # Obtenir les coordonnées actuelles.
        j, i = courant
        dj, di = voisins[index]
        Lj, Li = voisins_diag[(index) % 4]
        
        # Vérifier les conditions de terminaison
        # de la spirale.
        if (compteur > 3 or
           (not hors_grille(T, j + Lj, i +Li) and
            grille[j + Lj][i + Li] == plein)):
            return grille
        
        # Vérifier les conditions pour changer de
        # direction ou continuer.
        if (
            hors_grille(T, j + dj, i + di) or
            si_coche(
                grille,
                T,
                j + 2 * dj,
                i + 2 * di,
                plein)
            ):
            index = (index + 1) % 4
            compteur += 1
            
        else :
            grille[j + dj][i + di] = plein
            courant = [j + dj, i + di]
            compteur = 0


# -----------------------------------------------
# Application
# -----------------------------------------------

PLEIN = "+"
VIDE = " "
grille = spirale(23, PLEIN, VIDE)
print(f"\nSpirale avec des '{PLEIN}'\n")
for ligne in grille:
    print(" ".join(ligne))
    
    
 
# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

# Retourne vrai si la case est en dehors de la
# grille. Preferez l'écriture de la fonction
# hors_grille.
def hors_grille_det(T, dj, di):

    if (dj < 0 or dj >= T or  di < 0 or di >= T):
        return True
    else :
        return False


# Retourne vrai si l'on est sur la grille et que
# la case courante est pleine.
def si_coche_det(grille, T, dj, di, plein):
    if hors_grille_det(T, dj, di): 
        return False
    
    return grille[dj][di] == plein


# Construit la spirale.
def spirale_detaillee(T, plein, vide):
    
    grille = []

    for j in range(T):
        ligne = []
        for i in range(T):
            ligne.append(vide)
        grille.append(ligne)
    grille[0][0] = plein

    voisins =      [[0,1],[1, 0],[ 0,-1],[-1, 0]]
    voisins_diag = [[1,1],[1,-1],[-1,-1],[-1, 1]]
    
    courant = [0, 0]
    index = 0
    compteur = 1

    # Boucler pour effectuer la spirale.
    while True:
        
        # Obtenir les coordonnées actuelles.
        j = courant[0]
        i = courant[1]
        
        dj = voisins[index][0]
        di = voisins[index][1]
        
        Lj = voisins_diag[(index) % 4][0]
        Li = voisins_diag[(index) % 4][1]
        
        # Vérifier les conditions de terminaison
        # de la spirale.
        if (compteur > 3 or (not hors_grille_com(
            T,j+Lj,i+Li) and grille[j + Lj][i +
            Li] == plein)):

            return grille
        
        
        # Vérifier les conditions pour changer de
        # direction ou continuer.
        if (hors_grille_det(T, j + dj, i + di)
            or si_coche_det(grille, T, j + 2 *
            dj, i + 2 * di, plein)):
            
            index = (index + 1) % 4
            compteur += 1
        
        else :
            grille[j + dj][i + di] = plein
            courant = [j + dj, i + di]
            compteur = 0    
 
 

# -----------------------------------------------
# Version commentee
# -----------------------------------------------
   
# Retourne vrai si la case est en dehors de la
# grille. Preferez l'écriture de la fonction
# hors_grille.
def hors_grille_com(T, dj, di):
    # Si
    if (
        # dj est plus petit que 0, ou
        dj < 0 or
        
        # dj plus grand ou égal à T, ou
        dj >= T or
        
        # di est plus petit que 0, ou
        di < 0 or
        
        # di plus grand ou égal à T,
        di >= T):
        
        # Retourner vrai.
        return True
    
    # Sinon,
    else :
        
        # Retourner faux
        return False


# Retourne vrai si l'on est sur la grille et que
# la case courante est pleine.
def si_coche_com(grille, T, dj, di, plein):
    
    # Verifier si on est sur la grille.
    if hors_grille_com(T, dj, di): 
        return False
    
    # Vérifier si la valeur de la case courante
    # est egal à plein.
    return grille[dj][di] == plein


# Construit la spirale.
def spirale_commentee(T, plein, vide):
    
    # Créer une grille vide.
    grille = []
    
    # De 0 à T,
    for j in range(T):
        
        # créer une nouvelle ligne.
        ligne = []
        
        # et de 0 à T,
        for i in range(T):
            
            # ajouter "vide" à la ligne.
            ligne.append(vide)
        
        # Ajouter cette ligne à la grille
        grille.append(ligne)
    
    # Valoriser la case 0-0 du caractere plein.
    grille[0][0] = plein
    
    # Determiner les voisins cardinaux.
    voisins =      [[0,1],[1, 0],[ 0,-1],[-1, 0]]
    
    # Determiner les voisins diagonaux.
    voisins_diag = [[1,1],[1,-1],[-1,-1],[-1, 1]]
    
    # Determinier la case courante.
    courant = [0, 0]
    
    # Initialiser un index a 0.
    index = 0
    
    # Iniatialiser un compteurur a 1.
    compteur = 1
    
    # Boucler pour effectuer la spirale
    while True:
        
        # Récupérer la ligne de la case courante.
        j = courant[0]
        
        # Récupérer la col de la case courante.
        i = courant[1]
        
        # Récupérer la ligne du prochain voisin.
        dj = voisins[index][0]
        
        # Récupérer la col du prochain voisin.
        di = voisins[index][1]
        
        # Récupérer la ligne du prochain voisin
        # diagonal.
        Lj = voisins_diag[(index) % 4][0]
        
        # Récupérer la col du prochain voisin
        # diagonal.
        Li = voisins_diag[(index) % 4][1]
        
        # Vérifier les conditions de terminaison
        # de la spirale.
        # Si 
        if (
            # le compteur est plus grand que 3, ou
            compteur > 3 or
            # ou que l'on est en dehors,
           (not hors_grille_com(T,j+Lj,i+Li) and
            # et que la case courant est pleine,
            grille[j + Lj][i + Li] == plein)):
            
            # retourner la grille.
            return grille
        
        # Si
        if (
            # on est en dehors d ela grille,
            hors_grille_com(T, j + dj, i + di) or
            
            # ou si la case est déja cochée.
            si_coche_com(grille, T, j + 2 * dj,
                i + 2 * di, plein)
            ):
            
            # Changer de direction.
            index = (index + 1) % 4
            
            # Incrémenter le compteur.
            compteur += 1
        
        # Sinon,
        else :
            # valoriser à aux index requis, la
            # grille de "plein".
            grille[j + dj][i + di] = plein
            
            # Changer la valeur courante.
            courant = [j + dj, i + di]
            
            # Reinitialiser le compteur a 0.
            compteur = 0









#