# -----------------------------------------------
# sudoku_solveur
# -----------------------------------------------
# Fonction pour résoudre un sudoku de taille 4 ou
# 9 et qui n'es pas un sudoku très complexe à ré-
# soudre.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def resoudre_sudoku(grille):
    taille = len(grille)
    mini = int(taille**0.5)
    
    # Résoud la grille.
    def resoudre():
        for y in range(taille):
            for x in range(taille):
                if grille[y][x] == 0:
                    for n in range(1, taille+1):
                        if valider_case(y, x, n):
                            grille[y][x] = n
                            if resoudre():
                                return True
                            grille[y][x] = 0
                    return False
        return True


    # Détermine si une case est valide.
    def valider_case(y, x, num):
        
        # Vérifier la ligne
        if num in grille[y]:
            return False
        
        # Vérifier la colonne
        if any(grille[y0][x] == num for y0 in
               range(taille)):
            return False
        
        # Vérifier la sous-grille
        y0, x0 = (y//mini)*mini, (x//mini)*mini
        if any(grille[y0 + j][x0 + i] == num for
               j in range(mini) for i in range(
                   mini)):
            return False

        return True

    return grille if resoudre() else None



# -----------------------------------------------
# Application
# -----------------------------------------------

# Créer une grille de taille 9
sudoku_9 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Résoudre le Sudoku
resultat_9 = resoudre_sudoku(sudoku_9)
print("\n")
print("Résolution du sudoku de taille 9")
if resultat_9:
    for ligne in resultat_9:
        print("".join([str(i) for i in ligne]))
else:
    print("Aucune solution trouvée.")

print("\n")
print("\n")

# Créer une grille de taille 4
sudoku_4 = [
    [4, 0, 0, 3],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [2, 0, 4, 0]
]

# Résoudre le Sudoku
resultat_4 = resoudre_sudoku(sudoku_4)
print("Résolution du sudoku de taille 4")
if resultat_4:
    for ligne in resultat_4:
        print("".join([str(i) for i in ligne]))
else:
    print("Aucune solution trouvée.")

print("\n")
print("\n")

# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

# XD Plus compliqué ici avec la récursion, si une
# idée vous vient...

def S(g):
 t=len(g);m=int(t**0.5)
 def R():
  for y in range(t):
   for x in range(t):
    if g[y][x]==0:
     for n in range(1,t+1):
      if V(y,x,n):
       g[y][x]=n
       if R():return True
       g[y][x]=0
     return False
  return True
 V=lambda y,x,n: all(n not in g[y] and not any(g[
  y0][x]==n for y0 in range(t)) and not any(g[y0+
  j][x0+i]==n for j in range(m) for i in range(m)
  )for x0 in [(x//m)*m]for y0 in[(y//m)*m])
 return g if R() else None


# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def resoudre_sudoku(grille):
    taille = len(grille)
    sous_taille = int(taille**0.5)
    
    # Résoud la grille.
    def resoudre():
        for y in range(taille):
            for x in range(taille):
                if grille[y][x] == 0:
                    return remplir_case(y, x)
        return True
    
    # Tente de remplir une case de la grille.
    def remplir_case(y, x):
        for numero in range(1, taille + 1):
            if valider_case(y, x, numero):
                grille[y][x] = numero
                if resoudre():
                    return True
                grille[y][x] = 0

        return False


    # Détermine si une case est valide.
    def valider_case(y, x, numero):
        
        for x0 in range(taille):
            if grille[y][x0] == numero:
                return False
            
        for y0 in range(taille):
            if grille[y0][x] == numero:
                return False
            
        y0 = (y // sous_taille) * sous_taille
        x0 = (x // sous_taille) * sous_taille
        
        for j in range(0, sous_taille):
            for i in range(0, sous_taille):
                if grille[y0 + j][x0 + i] == numero:
                    return False  
                
        return True

    if resoudre():
        return grille
    else:
        return None


# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

def resoudre_sudoku(grille):
    # Déterminer la taille du côté de la grille.
    taille = len(grille)
    
    # Déterminer celle du sous-carré.
    sous_taille = int(taille**0.5)
    
    
    # Résoud la grille.
    def resoudre():
        
        # Pour y, de 0 à taille,
        for y in range(taille):
            
            # et pour chaque x, de 0 à taille
            for x in range(taille):
                
                # si la case en y et x est vide,
                if grille[y][x] == 0:
                    
                    # tenter de remplir la case,
                    # et retourner le numéro.
                    return remplir_case(y, x)
        
        # Retourner vrai pour avancer.
        return True
    
    # Tente de remplir une case de la grille.
    def remplir_case(y, x):
        
        # Parcourir tous les numéro possibles.
        for numero in range(1, taille + 1):
            
            # Si le numéro n'est pas déjà dans
            # la ligne et, la colonne et le sous-
            # carré.
            if valider_case(y, x, numero):
                
                # Remplir la case avec le numéro.
                grille[y][x] = numero
                
                # Apeller récursivement la fonc-
                # tion pour continuer.
                if resoudre():
                    
                    # Retourner vrai.
                    return True
                
                # Annuler la dernière modifica-
                # tion, si la solution n'est pas
                # trouvée
                grille[y][x] = 0
        
        # Et donc retourner faux !
        return False


    # Détermine si une case est valide.
    def valider_case(y, x, numero):
        
        # Pour chaque valeur de 0 à taille,
        for x0 in range(taille):
            
            # si cette valeur est présente dans
            # la ligne,
            if grille[y][x0] == numero:
                
                # retourner faux.
                return False
            
        # Pour chaque valeur de 0 à taille,
        for y0 in range(taille):
            
            # si cette valeur est présente dans
            # la colonne,
            if grille[y0][x] == numero:
                
                # retourner faux.
                return False
            
        # Initialiser le depart pour les lignes.
        y0 = (y // sous_taille) * sous_taille
        
        # Initialiser le depart des colonnes.
        x0 = (x // sous_taille) * sous_taille
        
        # Pour j, de 0 à sous taille,
        for j in range(0, sous_taille):
            
            # Pour i, de 0 à sous-taille,
            for i in range(0, sous_taille):
                
                # di la valeur de la case couran-
                # te est égale à celle de numéro
                if grille[y0 + j][x0 + i] == numero:
                    
                    # retourner faux.
                    return False
                
        # Sinon retourner vrai.
        return True


    # Si la fonction renvoie une solution,
    if resoudre():
        
        # retourner la grille résolue.
        return grille
    
    # Sinon,
    else:
        
        # ne rien retourner.
        return None









#