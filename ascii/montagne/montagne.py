# -----------------------------------------------
# montagne 
# -----------------------------------------------
# Cette fonction permet de dessiner quelques mon-
# tagnes sous forme ASCII.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def montagne(sommets):
    paysage = []
    max_el = max(sommets)

    for j in range(max_el + 1):
        ligne = ""

        for el in sommets:
            if el < j + 1:
                ligne += " " * (2 * el)
            else:
                ligne += " " * j + "/" + " " * (2
                * (el - j - 1)) + "\\" + " " * j
        paysage.append(ligne.rstrip())

    return "\n".join(reversed(paysage))


# -----------------------------------------------
# Application
# -----------------------------------------------

sommets = [5, 3, 10, 3, 7]
montagnes = montagne(sommets)
print(montagnes)



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

M=lambda s:'\n'.join([''.join([' '*2*e if e<j+1
else' '*j+'/'+' '*(2*(e-j-1))+'\\'+' '*j for e in
s])for j in range(max(s)+1)][::-1])



# -----------------------------------------------
# Version detaillee
# /*-----------------------------------------------
# / Cette version permet de suivre pas a pas l'exe-
# / cution de la fonction.
# /-----------------------------------------------*/

def montagne_detaillee(sommets):
    
    paysage = []
    max_el = max(sommets)
    longueur = len(sommets)

    for j in range(max_el + 1):
        ligne = ""

        for i in range(0, longueur):
            el = sommets[i]
            if el < j + 1:
                ligne += " " * (2 * el)
            else:
                ligne += " " * j
                ligne += "/"
                ligne += " " * (2 * (el - j - 1))
                ligne += "\\" + " " * j
                
        paysage.append(ligne.rstrip())

    paysage = reversed(paysage)
    paysage = "\n".join(paysage)

    return paysage


# -----------------------------------------------
# Version commentee
# /*-----------------------------------------------
# / Similaire a la version detaillee, mais avec des
# / commentaires concis afin d'expliquer les etapes
# / principales de la fonction.
# /-----------------------------------------------*/

def montagne_commentee(sommets):
    
    # Initialiser une liste paysage.
    paysage = []

    # Identifier le plus haut des sommets
    max_el = max(sommets)
    
    # Identifier le nombre de sommets.
    longueur = len(sommets)

    # De 0 à max,
    # ou du sol au plus haut des sommets,
    for j in range(max_el + 1):

        # Initialiser une nouvelle ligne.
        ligne = ""

        # De 0 au nombre de sommets,
        # ou pour chaque sommet,
        for i in range(0, longueur):
            
            # récupérer le sommet courant.
            el = sommets[i]

            # Si le sommet en cours est plus
            # petit que le plus hauts des sommets
            if el < j + 1:
                
                # Ajouter 2 * el " " à ligne.
                ligne += " " * (2 * el)
            
            # Sinon
            else:
                
                # Ajouter j espaces à la ligne.
                ligne += " " * j
                
                # Ajouter "/" à la ligne.
                ligne += "/"
                
                # Ajouter 2*(el-j-1) espaces à
                # la ligne.
                ligne += " " * (2 * (el - j - 1))
                
                # Ajouter "\" à la ligne.
                ligne += "\\"
                
                # Ajouter j espaces à la ligne.
                ligne += " " * j
                
        # Ajouter la ligne sans espaces à la fin
        # au paysage.
        paysage.append(ligne.rstrip())

    # Renverser l'ensemble du paysage.
    paysage = reversed(paysage)

    # Ajouter un saut à la ligne à chaque ligne.
    paysage = "\n".join(paysage)

    # Retourner le paysage.
    return paysage









#