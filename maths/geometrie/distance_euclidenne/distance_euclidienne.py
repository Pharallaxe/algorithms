# -----------------------------------------------
# distance_euclidienne
# -----------------------------------------------
# La distance euclidienne représente la mesure de
# la longueur de la ligne droite entre des points
# dans un espace à n dimensions. Ici n = deux.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def distance_euclidienne(*points):
    
    distances = 0
    
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        
        distances += ((x1-x2)**2+(y1-y2)**2)**0.5
    
    return distances



# -----------------------------------------------
# Application
# -----------------------------------------------

# Définition de 4 points avec leurs coordonnées.
point1 = (0, 0)
point2 = (3, 4)
point3 = (6, 8)
point4 = (9, 0)

# Calcul de la distance totale entre ces points.
dist_totale = round(distance_euclidienne(point1,
point2, point3, point4), 2)

# Affichage du résultat.
print("La distance entre les points est de :",
      dist_totale)

# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

D=lambda *points:sum(((x1-x2)**2+(y1-y2)**2)**0.5
for (x1,y1),(x2,y2) in zip(points,points[1:]))


# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

def distance_euclidienne_detaillee(*points):
    
    somme_distances = 0
    
    for i in range(len(points) - 1):
        
        point_actuel = points[i]
        x_actuel, y_actuel = point_actuel
        
        point_suivant = points[i + 1]
        x_suivant, y_suivant = point_suivant
        
        terme_1 = (x_suivant - x_actuel) ** 2
        terme_2 = (y_suivant - y_actuel) ** 2
        dist = (terme_1 + terme_2) ** 0.5
        
        somme_distances += dist
    
    return somme_distances



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

def distance_euclidienne_commentee(*points):
    
    # Initialiser la somme des distances à 0.
    somme_distances = 0
    
    # Parcourir les paire de points consécutifs.
    for i in range(len(points) - 1):
        
        # Extraire les coord. du point actuel.
        point_actuel = points[i]
        x_actuel, y_actuel = point_actuel
        
        # Extraire les coord. du point suivant.
        point_suivant = points[i + 1]
        x_suivant, y_suivant = point_suivant
        
        # Calculer la distance entre les points.
        # RACINE CARREE((X2 - X1)² + (Y2 - Y1)²).
        
        # Carré de l'écart entre X2 et X1.
        terme_1 = (x_suivant - x_actuel) ** 2
        
        # Carré de l'écart entre Y2 et Y1.
        terme_2 = (y_suivant - y_actuel) ** 2
        
        # Racine carrée des deux termes.
        dist = (terme_1 + terme_2) ** 0.5
        
        # Ajouter la distance calculée à la somme.
        somme_distances += dist
    
    # Retourner la somme totale des distances
    return somme_distances









#