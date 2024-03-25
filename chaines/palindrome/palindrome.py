# -----------------------------------------------
# Fonction palindrome
# -----------------------------------------------
# Un palindrome, c'est une chaîne qui de gauche à
# droite, et de droite à gauche possède les memes
# caractères.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

def palindrome(chaine):
    chaine = chaine.lower()
    chaine.replace(" ", "")

    resultat = []

    for char in chaine:
        if char.isalnum():
            char = char.lower();
            resultat.append(char)


    chaine = ''.join(resultat)
    chaine_reversed =  chaine[::-1]
    
    return chaine == chaine_reversed



# -----------------------------------------------
# Application
# -----------------------------------------------

chaine = "Esope reste ici et se repose"
est_palindrome = palindrome(chaine)
chaine = ["n'est pas", "est"][est_palindrome]
print(f'Le chaine "{chaine}" est un palindromme.')



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

P=lambda c:(c:=''.join(x.lower()for x in c if
                       x.isalnum()))==c[::-1]



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Proche de la version raccourcie, mais avec des
# commentaires concis pour expliquer les etapes
# principales de la fonction.

def palindrome_explication(chaine):
    
    # Convertir en minuscules.
    chaine = chaine.lower()
    
    # Supprimer les espaces.
    chaine.replace(" ", "")
    
    # Definir une liste vide.
    resultat = []

    # Parcourir chaque caractere de la chaine.
    for char in chaine:
        
        # Verifier si char est alphanumerique.
        if char.isalnum():
            
            # Convertir en minuscule.
            char = char.lower();
            
            # Ajouter à la liste resultat
            resultat.append(char)


    # Concatener les caracteres..
    chaine = ''.join(resultat)
    
    # Enregistrer la chaine inversee. 
    chaine_reversed =  chaine[::-1]
    
    # Retourner le resultat.
    return chaine == chaine_reversed









#