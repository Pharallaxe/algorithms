# -----------------------------------------------
# Fonction rendre_monnaie
# -----------------------------------------------
# Calcul le rendu de monnaie en fonction du prix
# et des quantités des différentes pièces.
# -----------------------------------------------


# -----------------------------------------------
# Version Courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    donne = ( x20 * 20 + x10 * 10 + x5 * 5
             + x2 * 2+ x1 * 1)
    somme = donne - prix
    rendus = []
    for monnaie in [20, 10, 5, 2, 1] :
        rendu = somme // monnaie
        somme -= rendu * monnaie
        rendus.append(rendu)
    return (rendus if somme >= 0
                   else [0, 0, 0, 0, 0])


# -----------------------------------------------
# Application
# -----------------------------------------------

prix_article = 47    # Prix de l'article en euros
x20 = 2      # Nbre de billets de 20 euros donnés
x10 = 2      # Nbre de billets de 10 euros donnés
x5 = 1        # Nbre de billets de 5 euros donnés
x2 = 3        # Nbre de pièces de 2 euros données
x1 = 4         # Nbre de pièces de 1 euro données

# Calcul de la monnaie à rendre
monnaie_rendue = rendre_monnaie(
    prix_article, x20, x10, x5, x2, x1
)

# Affichage du résultat
print("Monnaie à rendre :")
print("20 euros :", monnaie_rendue[0])
print("10 euros :", monnaie_rendue[1])
print("5 euros  :", monnaie_rendue[2])
print("2 euros  :", monnaie_rendue[3])
print("1 euro   :", monnaie_rendue[4])

# -----------------------------------------------
# Version Golf
# -----------------------------------------------
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

def rendre_monnaie(p,a,b,c,d,e):
    s,R=a*20+b*10+c*5+d*2+e-p,[]
    for m in[20,10,5,2,1]:r,s=divmod(s,m);R+=[r]
    return R if s>=0 else[0,0,0,0,0]

# -----------------------------------------------
# Version Détaillée
# -----------------------------------------------
# Cette version permet de suivre pas à pas l'exé-
# cution de la fonction.

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    
    donne = (
        x20 * 20 +
        x10 * 10 +
         x5 *  5 +
         x2 *  2 +
         x1 *  1
        )
       
    somme = donne - prix
    
    if somme < 0:
        return [0, 0, 0, 0, 0]
    else:
        monnaies = [20, 10, 5, 2, 1] 
        rendus = []
        for monnaie in monnaies:
            rendu = somme // monnaie
            somme = somme - (rendu * monnaie)
            rendus += [rendu]
            
        return rendus

# -----------------------------------------------
# Version Commentée
# -----------------------------------------------
# Similaire à la version détaillée, mais avec des
# commentaires concis afin d'expliquer les étapes
# principales de la fonction.

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    # Calculer le montant total donné en monnaie.
    donne = (
        x20 * 20 +
        x10 * 10 +
        x5 * 5 +
        x2 * 2 +
        x1 * 1
    )
    
    # Calculer la somme à rendre.
    somme = donne - prix
    
    # Si la somme est négative ou 0
    if somme < 1:
        # Retourner une liste de zéros.
        return [0, 0, 0, 0, 0]
    
    # Sinon,
    else:
        # Initialiser une liste vide de stockage.
        rendus = []
        
        # Définir les différentes de monnaie.
        monnaies = [20, 10, 5, 2, 1]
        
        # Parcourir chaque dénomination.
        for monnaie in monnaies:
            
            # Identifier les pièces rendues.
            rendu = somme // monnaie
            somme = somme - (rendu * monnaie)
            
            # Ajouter le nombre de pièces.
            rendus += [rendu]
        
        # Retourner la liste des rendus.
        return rendus
