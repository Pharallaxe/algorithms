<?php

# -----------------------------------------------
# Fonction bissextile
# -----------------------------------------------
# Fonction indiquant si une année est bissextile
# en suivant les règles du calendrier grégorien.
# -----------------------------------------------

# -----------------------------------------------
# Version Courte
# -----------------------------------------------

function bissextile($annee) {
    if ($annee % 400 === 0) {
        return true;
    } else if ($annee % 100 === 0) {
        return false;
    } else if ($annee % 4 === 0) {
        return true;
    } else {
        return false;
    }
}



# -----------------------------------------------
# Application
# -----------------------------------------------

$texte = ["n'est pas", "est"];
$annees = [1900, 2000, 2024];
foreach ($annees as $annee) {

    $est_bis = bissextile($annee);

    echo $annee . " ";

    if ($est_bis) {
        echo "n'est pas";
    } else {
        echo "est";
    }

    echo " bissextile.\n";
}



# -----------------------------------------------
# Version Golf
# -----------------------------------------------

$B=function($a){return $a%400==0||($a%100!=0&&$a%
4==0);};



# -----------------------------------------------
# Version Commentée
# -----------------------------------------------

function bissextile_commentee($annee) {
    // Si une année est divisible par 400, elle
    // est bissextile.
    if ($annee % 400 === 0) {
        return true;
    }
    
    // Sinon, si une année est divisible par 100,
    // sauf 400, elle n'est pas bissextile.
    else if ($annee % 100 === 0) {
        return false;
    }
    
    // Sinon, si une année est divisible par 4,
    // elle est bissextile
    else if ($annee % 4 === 0) {
        return true;
    }
    
    // Sinon, c'est une année quelconque, enfin,
    // sauf si c'est votre anniversaire.
    else {
        return false;
    }
}









?>