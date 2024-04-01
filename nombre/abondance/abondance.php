<?php

# -----------------------------------------------
# abondance
# -----------------------------------------------
# Fonction qui retourne l'abondance d'un nombre.
# L'abondance c'est le rapport entre la somme des
# diviseurs du nombre sauf lui même et le nombre
# lui-même.

# Ex : L'abondance de 28  est de 1. En effet, ses
# diviseurs sont 1, 2, 4, 7, 14. Leur somme égale
# 28. C'est un nombre parfait. Lorsque l'abondan-
# ce est au dessus de 1, on dit que c'est un nom-
# bre abondant. Si elle est en-deça de 1, on dira
# qu'il est déficient.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

function abondance($nombre) {
    if ($nombre < 1) {
        return null;
    }
    
    $somme_diviseurs = array_sum(
        array_filter(
            range(1, $nombre - 1),
            function($i) use ($nombre) {
                return $nombre % $i == 0;
            }
        )
    );
    
    return $somme_diviseurs / $nombre;
}



# -----------------------------------------------
# Application
# -----------------------------------------------

$nombres1 = [2, 6, 28, 24, 120, 30240, 997920];

foreach ($nombres1 as $nb) {
    $res = abondance($nb);

    $affichage = "$nb est ";
    if ($res == 1) {
        $affichage .= "parfait";
    } else if ($res < 1) {
        $affichage .= "déficient";
    } else {
        $affichage .= "abondant";
    }
    $res = sprintf("%.2f", $res);
    $affichage .= " (abondance de $res).\n";
    echo $affichage;
}



# -----------------------------------------------
# Version golf
# -----------------------------------------------

$A=function($n){return($D=array_sum(array_filter(
range(1,$n-1),fn($i)=>$n%$i==0)))/$n>=1?$D/$n:
null;};



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

function abondance_detaillee($nombre) {
    if ($nombre < 1) {
        return null;
    }
    
    $somme_diviseurs = 0;
    
    for ($i = 1; $i < $nombre; $i++) {
        if ($nombre % $i == 0) {
            $somme_diviseurs += $i;
        }
    }
    
    $abondance = $somme_diviseurs / $nombre;
    
    return $abondance;
}



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

function abondance_commentee($nombre) {

    // Si le nombres est inférieur à 1,
    if ($nombre < 1) {

        // Retourner null.
        return null;
    }
    
    // Initialiser la somme des diviseurs à 0.
    $somme_diviseurs = 0;
    
    // De 1 à nombres,
    for ($i = 1; $i < $nombre; $i++) {

        // Si le nombre est divisible par i.
        if ($nombre % $i == 0) {

            // alors ajouter i à la somme.
            $somme_diviseurs += $i;
        }
    }
    
    // Calculer l'abondance en divisant la somme
    // par le nombre.
    $abondance = $somme_diviseurs / $nombre;
    
    // Retourner l'abondance.
    return $abondance;
}









?>