# -----------------------------------------------
# montagne 
# -----------------------------------------------
# Cette fonction permet de dessiner quelques mon-
# tagnes sous forme ASCII.

# Ex: 
#                     /\
#                    /  \
#                   /    \
#                  /      \              /\
#     /\          /        \            /  \
#    /  \        /          \    /\    /    \
#   /    \  /\  /            \  /  \  /      \
#  /      \/  \/              \/    \/        \
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

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

sommets = [4, 2, 8, 3, 5]
montagnes = montagne(sommets)
print(montagnes)



# -----------------------------------------------
# Version golf
# -----------------------------------------------

M=lambda s:'\n'.join([''.join([' '*2*e if e<j+1
else' '*j+'/'+' '*(2*(e-j-1))+'\\'+' '*j for e in
s])for j in range(max(s)+1)][::-1])



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

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
# -----------------------------------------------

def montagne_commentee(sommets):
    
    # Initialiser une liste paysage.
    paysage = []

    # Identifier le plus haut des sommets
    max_el = max(sommets)
    
    # Identifier le nombre de sommets.
    longueur = len(sommets)

    # De 0 a max,
    # ou du sol au plus haut des sommets,
    for j in range(max_el + 1):

        # Initialiser une nouvelle ligne.
        ligne = ""

        # De 0 au nombre de sommets,
        # ou pour chaque sommet,
        for i in range(0, longueur):
            
            # recuperer le sommet courant.
            el = sommets[i]

            # Si le sommet en cours est plus
            # petit que le plus hauts des sommets
            if el < j + 1:
                
                # Ajouter 2 * el " " a ligne.
                ligne += " " * (2 * el)
            
            # Sinon
            else:
                
                # Ajouter j espaces a la ligne.
                ligne += " " * j
                
                # Ajouter "/" a la ligne.
                ligne += "/"
                
                # Ajouter 2*(el-j-1) espaces a
                # la ligne.
                ligne += " " * (2 * (el - j - 1))
                
                # Ajouter "\" a la ligne.
                ligne += "\\"
                
                # Ajouter j espaces a la ligne.
                ligne += " " * j
                
        # Ajouter la ligne sans espaces a la fin
        # au paysage.
        paysage.append(ligne.rstrip())

    # Renverser l'ensemble du paysage.
    paysage = reversed(paysage)

    # Ajouter un saut a la ligne a chaque ligne.
    paysage = "\n".join(paysage)

    # Retourner le paysage.
    return paysage









#