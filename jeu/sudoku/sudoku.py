# -----------------------------------------------
# sudoku_solveur
# -----------------------------------------------
# Fonction pour resoudre un sudoku de taille 4 ou
# 9 et qui n'es pas un sudoku tres complexe a re-
# soudre.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def sudoku_solveur(grille):
    taille = len(grille)
    mini = int(taille**0.5)
    
    # Resoud la grille.
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


    # Determine si une case est valide.
    def valider_case(y, x, num):
        
        # Verifier la ligne.
        if num in grille[y]:
            return False
        
        # Verifier la colonne.
        if any(grille[y0][x] == num for y0 in
               range(taille)):
            return False
        
        # Verifier la sous-grille.
        y0, x0 = (y//mini)*mini, (x//mini)*mini
        
        for j in range(0, mini):
            for i in range(0, mini):
                if grille[y0 + j][x0 + i] == num:
                    return False  

        return True

    return grille if resoudre() else None


# -----------------------------------------------
# Application
# -----------------------------------------------

# Creer une grille de taille 9
sudoku_9 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

# Resoudre le Sudoku
resultat_9 = sudoku_solveur(sudoku_9)
print("\n")
print("Resolution du sudoku de taille 9")
if resultat_9:
    for ligne in resultat_9:
        print("".join([str(i) for i in ligne]))
else:
    print("Aucune solution trouvee.")

print("\n")
print("\n")

# Creer une grille de taille 4
sudoku_4 = [
    [4, 0, 0, 3],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [2, 0, 4, 0]
]

# Resoudre le Sudoku
resultat_4 = sudoku_solveur(sudoku_4)
print("Resolution du sudoku de taille 4")
if resultat_4:
    for ligne in resultat_4:
        print("".join([str(i) for i in ligne]))
else:
    print("Aucune solution trouvee.")

print("\n")
print("\n")

# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

# XD Plus complique ici avec la recursion, si une
# idee vous vient...

def SR(g):
 t=len(g);m=int(t**0.5)
 for R, C in[(r,c)for r in range(t)for c in range
        (t)if not g[r][c]]:
  rr,cc= (R//m)*m,(C//m)*m
  U=set(range(1,t+1))- ({g[R][c]for c in range(t)
        }|{g[r][C]for r in range(t)}|{g[rr+r][cc+
        c]for r in range(m)for c in range(m)})
  if len(U)==1:g[R][C]=U.pop();return SR(g)
 return g



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def sudoku_solveur_detaillee(grille):
    taille = len(grille)
    sous_taille = int(taille**0.5)
    
    # Resoud la grille.
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


    # Determine si une case est valide.
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

    # Principal
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

def sudoku_solveur_commentee(grille):
    # Determiner la taille du côte de la grille.
    taille = len(grille)
    
    # Determiner celle du sous-carre.
    sous_taille = int(taille**0.5)
    
    
    # Resoud la grille.
    def resoudre():
        
        # Pour y, de 0 a taille,
        for y in range(taille):
            
            # et pour chaque x, de 0 a taille
            for x in range(taille):
                
                # si la case en y et x est vide,
                if grille[y][x] == 0:
                    
                    # tenter de remplir la case,
                    # et retourner le numero.
                    return remplir_case(y, x)
        
        # Retourner vrai pour avancer.
        return True
    
    # Tente de remplir une case de la grille.
    def remplir_case(y, x):
        
        # Parcourir tous les numero possibles.
        for numero in range(1, taille + 1):
            
            # Si le numero n'est pas deja dans
            # la ligne et, la col et le sous-
            # carre.
            if valider_case(y, x, numero):
                
                # Remplir la case avec le numero.
                grille[y][x] = numero
                
                # Apeller recursivement la fonc-
                # tion pour continuer.
                if resoudre():
                    
                    # Retourner vrai.
                    return True
                
                # Annuler la derniere modifica-
                # tion, si la solution n'est pas
                # trouvee
                grille[y][x] = 0
        
        # Et donc retourner faux !
        return False


    # Determine si une case est valide.
    def valider_case(y, x, numero):
        
        # Pour chaque valeur de 0 a taille,
        for x0 in range(taille):
            
            # si cette valeur est presente dans
            # la ligne,
            if grille[y][x0] == numero:
                
                # retourner faux.
                return False
            
        # Pour chaque valeur de 0 a taille,
        for y0 in range(taille):
            
            # si cette valeur est presente dans
            # la colonne,
            if grille[y0][x] == numero:
                
                # retourner faux.
                return False
            
        # Initialiser le depart pour les lignes.
        y0 = (y // sous_taille) * sous_taille
        
        # Initialiser le depart des colonne.
        x0 = (x // sous_taille) * sous_taille
        
        # Pour j, de 0 a sous taille,
        for j in range(0, sous_taille):
            
            # Pour i, de 0 a sous-taille,
            for i in range(0, sous_taille):
                
                # di la valeur de la case couran-
                # te est egale a celle de numero
                if grille[y0 + j][x0 + i] == numero:
                    
                    # retourner faux.
                    return False
                
        # Sinon retourner vrai.
        return True


    # Si la fonction renvoie une solution,
    if resoudre():
        
        # retourner la grille resolue.
        return grille
    
    # Sinon,
    else:
        
        # ne rien retourner.
        return None









#