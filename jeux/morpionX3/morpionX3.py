# -----------------------------------------------
# morpion
# -----------------------------------------------
# Identifie si une grille de morpion 3 x 3 con-
# tient une combinaison gagnante et retourne le
# gagnant.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def morpion(grille, vide):
    # Vérification des lignes et colonnes
    for i in range(3):
        if (grille[i][0] == grille[i][1] ==
            grille[i][2] != vide or
            grille[0][i] == grille[1][i] ==
            grille[2][i] != vide):
            
            return grille[i][0]
    
    # Vérification des diagonales
    if (grille[0][0] == grille[1][1] ==
        grille[2][2] != vide or
        grille[0][2] == grille[1][1] ==
        grille[2][0] != vide):
        
        return grille[1][1]

    return vide



# -----------------------------------------------
# Application
# -----------------------------------------------

# grille = [
#     ["X", "O", "X"],
#     [" ", "X", "O"],
#     ["O", " ", "X"]
# ]

# gagnant = morpion(grille, " ")
# if gagnant != " ":
#     print("Le gagnant est :", gagnant)
# else:
#     print("Aucun gagnant pour le moment.")
    
    
    
# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

M=lambda g,v:next((g[i][0]for i in range(3) if(g[
i][0]==g[i][1]==g[i][2]!=v)or(g[0][i]==g[1][i]==g
[2][i]!=v)),next((g[1][1]for _ in range(2)if(g[0]
[0]==g[1][1]==g[2][2]!=v)or(g[0][2]==g[1][1]==g[2
][0]!=v)),v))



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def morpion_detaillee(grille, vide):
    
    for i in range(3):
        if (grille[i][0] ==
            grille[i][1] == 
            grille[i][2] !=
            vide):
            
            return grille[i][0]
        
    for i in range(3):
        if (grille[0][i] ==
            grille[1][i] ==
            grille[2][i] !=
            vide):
            
            return grille[0][i]
        
    if (grille[0][0] ==
        grille[1][1] ==
        grille[2][2] !=
        vide):
        
        return grille[0][0]  
    
    if (grille[0][2] ==
        grille[1][1] ==
        grille[2][0] !=
        vide):
        
        return grille[0][2]  
    
    return vide



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

def morpion_commentee(grille, vide):
    # -------------------------------------------
    # Vérifier lignes.
    # -------------------------------------------
    for i in range(3):
        
        # Si les trois cases sont identiques,
        # et différent de vide
        if (grille[i][0] ==
            grille[i][1] == 
            grille[i][2] !=
            vide):
            
            # Le gagnant est sur la ligne i.
            return grille[i][0]
        
    # -------------------------------------------
    # Vérifier colonnes.
    # -------------------------------------------
    for i in range(3):
        
        # Si les trois cases sont identiques,
        # et différent de vide
        if (grille[0][i] ==
            grille[1][i] ==
            grille[2][i] !=
            vide):
            
            # Le gagnant est sur la colonne i.
            return grille[0][i]
        
    # --------------------------------------------
    # Vérifier la diagonale descendante.
    # --------------------------------------------
    # Si les trois cases sont identiques,
    # et différent de vide,
    if (grille[0][0] ==
        grille[1][1] ==
        grille[2][2] !=
        vide):
        
        # Le gagnant est sur la diagonale
        # principale.
        return grille[0][0]  
    
    # -------------------------------------------   
    # Vérifier la diagonale ascendante.
    # -------------------------------------------
        
    # Si les trois cases sont identiques,
    # et différent de vide,
    if (grille[0][2] ==
        grille[1][1] ==
        grille[2][0] !=
        vide):
        
        # Le gagnant est sur la diagonale
        # ascendante.
        return grille[0][2]  
    
    # Retourner aucun gagant
    return vide









#