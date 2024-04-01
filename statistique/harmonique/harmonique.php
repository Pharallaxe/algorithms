<?php

# -----------------------------------------------
# harmonique 
# -----------------------------------------------
# Cette moyenne de n nombres (x1, x2,..., xn) est
# calculee en divisant le nombre de valeurs par
# la somme des inverses de chaque valeur.

# Cette moyenne de n nombres (x1, x2,..., xn) est
# calculee en divisant le nomùbre de valeurs par
# la somme des inverses de chaque valeur.

#                           N
# Formule : MH = --------------------------
#                (1/x1 + 1/x2 + ... + 1/xn)

#----------------------------------------------*/


# -----------------------------------------------
#  Version courte
# -----------------------------------------------

function harmonique($tableau) {

    $inverses = array_map(fn($n)=>1/$n,$tableau);
    
    $somme = array_sum($inverses);
    
    return count($tableau) / $somme;
}



# -----------------------------------------------
#  Application
# -----------------------------------------------

# Si pendant une heure vous faites 50 km/h, puis
# pendant encore une heure 90 km/h, c'est comme
# si vous aviez fait pendant deux heures....

$tableau = array(50, 90);
$moyenne = harmonique($tableau);
$moyenne = number_format($moyenne, 2);
echo "La moyenne est " . round($moyenne, 2);



# -----------------------------------------------
# Version golf
# -----------------------------------------------

$H=fn($l)=>count($l)/array_reduce($l,fn($a,$n)=>
$a+1/$n,0);



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

function harmonique_detaillee($tableau) {

    $nbr_valeurs = count($tableau);
    $somme = 0;
    
    for ($i = 0; $i < $nbr_valeurs; $i++) {
        $valeur = $tableau[$i];
        $somme += 1 / $valeur;
    }

    $moyenne = $nbr_valeurs / $somme;
    
    return $moyenne;
}



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

function harmonique_commentee($tableau) {
    
    // Identifier la longueur de la tableau.
    $nbr_valeurs = count($tableau);
    
    // Initialiser la somme a 0.
    $somme = 0;
    
    // De 0 a la longueur de la tableau,
    for ($i = 0; $i < $nbr_valeurs; $i++) {
        
        // Recuperer la valeur a l'index i.
        $valeur = $tableau[$i];
        
        // Ajouter l'inverse de cette valeur a la
        // somme.
        $somme += 1 / $valeur;
    }

    // Calculer la moyenne.
    $moyenne = $nbr_valeurs / $somme;
    
    // Retourner la moyenne.
    return $moyenne;
}









?>