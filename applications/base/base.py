# -----------------------------------------------
# Fonction Base
# -----------------------------------------------
# Fonction convertissant un nombre une base vers
# une autre..
# -----------------------------------------------



# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def base(nombre, depart, fin):
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = 0
    
    # Conversion du nombre en base 10
    for chiffre in nombre[::-1]:
        val = val * depart + base.index(chiffre)
    
    # Conversion de la base 10 à la base finale
    convertis = []
    while val > 0:
        val, reste = divmod(val, fin)
        convertis.append(base[reste])
    
    # Retourner le résultat
    return ''.join(convertis[::-1] or '0')



# -----------------------------------------------
# Application
# -----------------------------------------------

chaine1 = "1010"
depart1 = 2
arrivee1 = 10
res_1 = base(chaine1, depart1, arrivee1)
conv_1 = f"{depart1} vers {arrivee1}"
print(f"{chaine1} de {conv_1} donne : {res_1}")


chaine2 = "48"
depart2 = 10
arrivee2 = 3
res_2 = base(chaine2, depart2, arrivee2)
conv_2 = f"{depart2} vers {arrivee2}"
print(f"{chaine2} de {conv_2} donne : {res_2}")



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

B=lambda n,d,f,b="0123456789ABCDEFGHIJKLMNOPQRST\
UVWXYZ":''.join([b[v%f]for v in[sum([b.index(c)*d
**i for i,c in enumerate(n[::-1])])]][::-1])or'0'



# -----------------------------------------------
# Version détaillée
# -----------------------------------------------
# Cette version permet de suivre pas à pas l'exé-
# cution de la fonction.

def base_detaillee(nombre, depart, fin):
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = 0
    
    nombre_inv = list(nombre)[::-1]
    longueur = len(nombre_inv)
    
    for i in range(0, longueur):
        base_index = base.index(nombre_inv[i])
        val +=  base_index * depart ** i
    
    conv = []
    
    if val == 0:
        return "0"
    else:
        while val >= fin - 1:
            ch_base_fin  = val % fin
            conv.append(base[ch_base_fin])
            val = val // fin
        
        if val != 0:
            conv.append(base[val])
            
        retour = ''.join(conv)
        
        return retour



# -----------------------------------------------
# Version commentée
# -----------------------------------------------
# Similaire à la version détaillée, mais avec des
# commentaires concis afin d'expliquer les étapes
# principales de la fonction.

def base(nombre, depart, fin):
    
    # Définir les symboles des les bases.
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Initialiser la val convertie en base 10.
    val = 0
    
    # Inverser la chaîne.
    nombre_inv = list(nombre)[::-1]
    
    # Récupérer la longueur de la chaine.
    longueur = len(nombre_inv)
    
    # Convertir la base départ vers la base 10.
    for i in range(0, longueur):
        
        # Trouver l'index du symbole.
        base_index = base.index(nombre_inv[i])
        
        # Ajouter la val convertie à la base 10.
        val +=  base_index * depart ** i
    
    # Initialiser une liste.
    convertis = []
    
    # Si la val est 0,
    if val == 0:
        
        # Retourner 0.
        return "0"
    
    # Sinon,
    else:
        
        # Convertir de la base 10 vers "fin".
        while val >= fin - 1:
            
            # Calculer le chiffre dans la base
            # de destination.
            ch_base_fin  = val % fin
            
            # Ajouter le chiffre à la liste des
            # chiffres convertis.
            convertis.append(base[ch_base_fin])
            
            # Mettre à jour la val pour le
            # prochain chiffre.
            val = val // fin
        
        # Si la val est différente de 0.
        if val != 0:
            
            # Ajouter le dernier chiffre.
            convertis.append(base[val])
        
        # Concaténer tous les chiffres.
        retour = ''.join(convertis)
        
        # Retourner le résultat.
        return retour









#