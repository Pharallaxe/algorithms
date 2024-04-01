# -----------------------------------------------
# Fonction rendre_monnaie
# -----------------------------------------------
# Calcule le rendu de monnaie en fonction du prix
# et des quantites des differentes pieces.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

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
x20 = 2      # Nbre de billets de 20 euros donnes
x10 = 2      # Nbre de billets de 10 euros donnes
x5 =  1       # Nbre de billets de 5 euros donnes
x2 =  3       # Nbre de pieces de 2 euros donnees
x1 =  4        # Nbre de pieces de 1 euro donnees

# Calcul de la monnaie a rendre
monnaie_rendue = rendre_monnaie(
    prix_article, x20, x10, x5, x2, x1
)

# Affichage du resultat
print("Monnaie a rendre :")
print("20 euros :", monnaie_rendue[0])
print("10 euros :", monnaie_rendue[1])
print("5 euros  :", monnaie_rendue[2])
print("2 euros  :", monnaie_rendue[3])
print("1 euro   :", monnaie_rendue[4])

# -----------------------------------------------
# Version golf
# -----------------------------------------------

def RM(p,a,b,c,d,e):
    s,R=a*20+b*10+c*5+d*2+e-p,[]
    for m in[20,10,5,2,1]:r,s=divmod(s,m);R+=[r]
    return R if s>=0 else[0,0,0,0,0]



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

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
# Version commentee
# -----------------------------------------------

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    # Calculer le montant total donne en monnaie.
    donne = (
        x20 * 20 +
        x10 * 10 +
        x5 * 5 +
        x2 * 2 +
        x1 * 1
    )
    
    # Calculer la somme a rendre.
    somme = donne - prix
    
    # Si la somme est negative ou 0
    if somme < 1:
        # Retourner une liste de zeros.
        return [0, 0, 0, 0, 0]
    
    # Sinon,
    else:
        # Initialiser une liste vide de stockage.
        rendus = []
        
        # Definir les differentes de monnaie.
        monnaies = [20, 10, 5, 2, 1]
        
        # Parcourir chaque denomination.
        for monnaie in monnaies:
            
            # Identifier les pieces rendues.
            rendu = somme // monnaie
            somme = somme - (rendu * monnaie)
            
            # Ajouter le nombre de pieces.
            rendus += [rendu]
        
        # Retourner la liste des rendus.
        return rendus









#