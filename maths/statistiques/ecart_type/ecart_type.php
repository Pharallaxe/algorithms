<?php

# -----------------------------------------------
# ecart_type
# -----------------------------------------------
# L'ecart-type est la racine carree de la varian-
# ce. Il indique a quel point les valeurs indivi-
# duelles d'un ensemble de donnees s'ecartent de
# la moyenne de cet ensemble. 
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

function ecart_type($liste) {
    $longueur = count($liste);
    $somme = array_sum($liste);
    
    $moyenne = $somme / $longueur;
    $carres = array_sum(
        array_map(
            function($x) use ($moyenne) {
                return ($x - $moyenne) ** 2;
            },
            $liste));
    
    return sqrt($carres / $longueur);
}

# -----------------------------------------------
# Application
# -----------------------------------------------

$liste = [12, 14, 16, 8, 6, 18];
$resultat = ecart_type_detaillee($liste);
echo "L'écart type est : " . round($resultat, 2);



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

$ET=fn($l)=>sqrt(array_reduce($l,fn($a,$x)=>$a+(
$x-($m=array_reduce($l,fn($s,$n)=>$s+$n,0)/count
($l)))**2,0)/count($l));


# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

function ecart_type_detaillee($liste) {

    $somme = 0;
    $somme_carres = 0;
    
    $longueur = count($liste);

    foreach ($liste as $courant) {
        $somme += $courant;
    }

    $moyenne = $somme / $longueur;

    foreach ($liste as $courant) {
        $ecart = $courant - $moyenne;
        $carre_ecart = pow($ecart, 2);
        $somme_carres += $carre_ecart;
    }

    $variance = $somme_carres / $longueur;
    $ecart_type = sqrt($variance);

    return $ecart_type;
}



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

function ecart_type_commentee($liste) {
    // Récupérer la longueur de la liste.
    $longueur = count($liste);

    // Calculer la somme des carrés des écarts.
    $somme_carres = 0;

    // Initialiser la somme à 0.
    $somme = 0;

    // Pour chaque nombre dans la liste à étudier
    foreach ($liste as $courant) {

        // Ajouter ce nombre à la somme
        $somme += $courant;
    }

    // Diviser la sommer par le nombre de termes.
    $moyenne = $somme / $longueur;

    // Pour chaque terme de la liste à étudier.
    foreach ($liste as $courant) {

        // Calculer l'écart entre le nombre et la moyenne.
        $ecart = $courant - $moyenne;

        // Calculer le carré de l'écart.
        $carre_ecart = pow($ecart,
            2
        );

        // Ajouter le carré de l'écart à la somme.
        $somme_carres += $carre_ecart;
    }

    // Diviser la somme des carrés la longueur..
    $variance = $somme_carres / $longueur;

    // Calculer la racine carrée de la variance.
    $ecart_type = sqrt($variance);

    // Retourner l'écart-type résultant.
    return $ecart_type;
}









?>