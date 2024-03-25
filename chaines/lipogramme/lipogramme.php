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

$ch = "Le ver de terre";
$let = "e";
$estLipogramme = lipogramme($ch, $let);
$est = $estLipogramme ? "est" : "n'est pas";
echo $ch." $est"." un lipogramme en '".$let."'.";



# -----------------------------------------------
#  Version golf
# -----------------------------------------------
#  Version condensee et optimisee du code, utili-
#  sant des noms de variables courts et combinant
#  certaines operations pour reduire la taille du
#  code. Pour la beaute du geste !


$l=function($c,$l){return strpos(str_replace(' ',
'',strtolower($c)),strtolower($l))===0;};



# -----------------------------------------------
#  Version commentee
# -----------------------------------------------
#  Similaire a la version detaillee, mais avec des
#  commentaires concis pour expliquer les etapes
#  principales de la fonction.

function lipogramme_commentee($chaine, $lettre) {
    // Convertir en minuscules
    $chaine = strtolower($chaine);
    $lettre = strtolower($lettre);

    // Supprimer les espaces
    $chaine = str_replace(" ", "", $chaine);

    // Retourner le resultat.
    return strpos($chaine, $lettre) === false;
}