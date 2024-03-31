<?php

// -----------------------------------------------
// geometrique 
// -----------------------------------------------
// Permet de realiser une moyenne geometrique qui
// est plus insensible aux valeurs elevees que la
// moyenne arithmetique. Elle permet donc une es-
// timation meilleure des tendances centrales.

// Cette moyenne de n nombres (x1, x2,..., xn) est
// calculée en multipliant tous les nombres ensem-
// ble, puis en prenant la racine enième de ce mê-
// me produit.

// Formule : MG = (x1 * x2 * ... * xn) ** (1/n)

//------------------------------------------------


// -----------------------------------------------
// Version courte
// -----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function geometrique($tableau) {
    $produit = 1;
    
    foreach ($tableau as $valeur) {
        $produit *= $valeur;
    }
    
    return pow($produit, 1 / count($tableau));
}



// -----------------------------------------------
// Application
// -----------------------------------------------

$tableau = [12, 14, 16, 8, 6, 18];
$moyenne = geometrique($tableau);
echo "La moyenne est " . round($moyenne, 2);



// -----------------------------------------------
// Version golf
// -----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

$G=function($l){return pow(array_product($l),1/
count($l));};



// -----------------------------------------------
// Version detaillee
// -----------------------------------------------
// Cette version permet de suivre pas a pas l'exe-
// cution de la fonction.

function geometrique_detaillee($tableau) {
    
    $longueur = count($tableau);

    $produit = 1;
    
    for ($i = 0; $i < $longueur ; $i++) {
        $valeur = $tableau[$i];
        $produit *= $valeur;
    }
    
    $enieme = 1 / $longueur;
    $moyenne = pow($produit, $enieme);
    
    return $moyenne;
}



// -----------------------------------------------
// Version commentee
// -----------------------------------------------
// Similaire a la version detaillee, mais avec des
// commentaires concis afin d'expliquer les etapes
// principales de la fonction.

function geometrique_commentee($tableau) {
    
    // Identifier la longueur de la tableau.
    $longueur = count($tableau);
    
    // Initialiser le produit a 1.
    $produit = 1;
    
    // De 0 a la longueur du tableau,
    for ($i = 0; $i < $longueur ; $i++) {

        // Récupérer la valeur à l'index i.
        $valeur = $tableau[$i];

        // Multiplier produit par cette valeur.
        $produit *= $valeur;
    }

    // Calculer le facteur enieme de la racine.
    $enieme = 1 / $longueur;
    
    // Effetcuer la racine enieme du produit.
    $moyenne = pow($produit, $enieme);
    
    // Retourner le resultat.
    return $moyenne;
}









?>