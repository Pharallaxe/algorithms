# -----------------------------------------------
# Fonctions anagramme
# -----------------------------------------------
# Identifie si deux chaines sont anagrammes, donc
# si elles sont composées des mêmes lettres exac-
# tement.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def anagramme(chaine1, chaine2):
    
    chaine_A = chaine1.upper()
    chaine_B = chaine2.upper()
    
    A_sorted = sorted(chaine_A)
    B_Sorted = sorted(chaine_B)
    
    return A_sorted == B_Sorted



# -----------------------------------------------
# Application
# -----------------------------------------------

ch1 = "listen"
ch2 = "silent"
sont_anagrammes = anagramme(ch1, ch2)
chaine = ["ne sont pas", "sont"][sont_anagrammes]
print(f"Les chaînes {chaine} des anagrammes.")



# -----------------------------------------------
# Version golf
# -----------------------------------------------

A=lambda s,S:sorted(s.upper())==sorted(S.upper())



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def anagramme_commentee(chaine1, chaine2):
    
    # Convertir les chaineaînes en majuscules.
    chaine_A = chaine1.upper()
    chaine_B = chaine2.upper()
    
    # Trier les deux chaines.
    A_sorted = sorted(chaine_A)
    B_Sorted = sorted(chaine_B)
    
    # Verifier l'equivalence des chaines.
    return A_sorted == B_Sorted









#