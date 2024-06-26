# -----------------------------------------------
# sommer_fractions
# -----------------------------------------------
# Fonction qui permet d'ajouter deux fracions en-
# tre elles avec un même denominateur.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

def sommer_fractions(nombre1, nombre2):
    num1, den1 = map(int, nombre1.split("/"))
    num2, den2 = map(int, nombre2.split("/"))
    
    den = den1 if den1 == den2 else den1 * den2
    num1 = num1 * den2
    num2 = num2 * den1
    
    return f"{num1 + num2}/{den}"



# -----------------------------------------------
# Application
# -----------------------------------------------

nombre1 = "4/9"
nombre2 = "12/3"
res = sommer_fractions(nombre1, nombre2)
print(res)



# -----------------------------------------------
# Version golf
# -----------------------------------------------

F=lambda n1,n2:str(int(n1.split('/')[0])*int(n2
.split('/')[1])+int(n2.split('/')[0])*int(n1
.split('/')[1]))+"/"+str(int(n1.split('/')[1])*
int(n2.split('/')[1]))



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

def sommer_fractions_detaillee(nombre1, nombre2):
    num_den1 = nombre1.split("/")
    num_den2 = nombre2.split("/")

    numerateur_1 = int(num_den1[0])
    denominateur_1 = int(num_den1[1])
    numerateur_2 = int(num_den2[0])
    denominateur_2 = int(num_den2[1])

    den = 1

    if denominateur_1 == denominateur_2:
        den = denominateur_1
    else :
        den = denominateur_1 * denominateur_2
        
    numerateur_1 = numerateur_1 * denominateur_2
    numerateur_2 = numerateur_2 * denominateur_1
    
    return f"{numerateur_1 + numerateur_2}/{den}"



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

def sommer_fractions_commentee(nombre1, nombre2):
    
    # Decouper les fractions en numerateurs et
    # denominateurs.
    num_den1 = nombre1.split("/")
    num_den2 = nombre2.split("/")

    # Convertir de chaque element en entiers.
    numerateur_1 = int(num_den1[0])
    denominateur_1 = int(num_den1[1])
    numerateur_2 = int(num_den2[0])
    denominateur_2 = int(num_den2[1])

    # Initialiser le denominateur a 1, car il
    # ne peut être egal a 0.
    den = 1

    # Si les denominateurs sont egaux entre eux,
    if denominateur_1 == denominateur_2:
        
        # associer la valeur de l'un des denomi-
        # nateur a celui de fin.
        den = denominateur_1
    
    # Sinon,
    else :
        
        # Multiplier les deux denominateurs.
        den = denominateur_1 * denominateur_2
    
    # Multiplier les numerateurs par les denomi-
    # nateurs adjacents.
    numerateur_1 = numerateur_1 * denominateur_2
    numerateur_2 = numerateur_2 * denominateur_1
    
    # Retourner le resultat.
    return f"{numerateur_1 + numerateur_2}/{den}"









#