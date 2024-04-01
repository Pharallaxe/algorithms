<?php

# -----------------------------------------------
# Fonction factorielle
# -----------------------------------------------
# Calcul du produit des entiers de 1 a n, où n un
# entier positif est passe en argument.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

function factorielle($nombre) {
    $produit = 1;
    
    for ($i = 1; $i <= $nombre; $i++) {
        $produit *= $i;
    }
    
    return $produit;
}



# -----------------------------------------------
# Application
# -----------------------------------------------

$resultat = factorielle(6);
echo "La factorielle de 6 est $resultat";



# -----------------------------------------------
# Version golf
# -----------------------------------------------

$F=fn($n)=>array_product(range(1,$n));



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

function factorielle_commentee($nombre) {
 
    // Initialiser du produit a 1.
    $produit = 1;
    
    // De 1 a nombre,
    for ($i = 1; $i <= $nombre; $i++) {
   
     // Multiplier par le nombre courant.
     $produit *= $i;
    }
    
    // Retourner la factorielle calculee.
    return $produit;
   }





   



#