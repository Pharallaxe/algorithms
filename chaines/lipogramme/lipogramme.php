<?php
# -----------------------------------------------
#  Fonction Base
# -----------------------------------------------
#  Un lipogramme est une chaine de caracteres qui
#  ne contient aucun caractere donne, comme le e.
# -----------------------------------------------

function lipogramme($chaine, $lettre) {
    $chaine = strtolower($chaine);
    $lettre = strtolower($lettre);

    $chaine = str_replace(" ", "", $chaine);

    return strpos($chaine, $lettre) === false;
}



# -----------------------------------------------
#  Application
# -----------------------------------------------

$chaine = "Le ver de terre";
$lettre = "e";
$est_lipogramme = lipogramme($chaine, $lettre);
echo '"' . $chaine . '"';
if ($est_lipogramme) {
    echo " est ";
}
else {
    echo " n'est pas ";
}

echo "un lipogramme en '" . $lettre ."'.";



# -----------------------------------------------
#  Version golf
# -----------------------------------------------

$L=function($c,$l){return strpos(str_replace(' ',
'',strtolower($c)),strtolower($l))===0;};



# -----------------------------------------------
#  Version commentee
# -----------------------------------------------

function lipogramme_commentee($chaine, $lettre) {
    
    // Convertir en minuscules
    $chaine = strtolower($chaine);
    $lettre = strtolower($lettre);

    // Supprimer les espaces
    $chaine = str_replace(" ", "", $chaine);

    // Retourner le resultat.
    return strpos($chaine, $lettre) === false;
}