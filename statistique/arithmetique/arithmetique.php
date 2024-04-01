<?php
# -----------------------------------------------
# arithmetique
# -----------------------------------------------
# Permet de realiser une moyenne a partir d'une 
# tableau de plusieurs valeurs.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------

function arithmetique($tableau) {

    return array_sum($tableau) / count($tableau);

}



# -----------------------------------------------
# Application
# -----------------------------------------------

$tableau = [12, 14, 16, 8, 6, 18];
$moyenne = arithmetique($tableau);
echo "La moyenne est " . round($moyenne, 2);



# -----------------------------------------------
# Version golf
# -----------------------------------------------

$A=fn($l)=>array_sum($l)/count($l);



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

function arithmetique_detaillee($tableau) {

    $nbr_valeurs = count($tableau);
    $somme = 0;

    for ($i = 0; $i < $nbr_valeurs; $i++) {
        $valeur = $tableau[$i];
        $somme += $valeur;
    }

    $moyenne = $somme / $nbr_valeurs;

    return $moyenne;
}



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

function arithmetique_commentee($tableau)
{
    // Calculer la longueur du tableau.
    $nbr_valeurs = count($tableau);

    // Initialiser la somme a 0.
    $somme = 0;

    // De 0 a la longueur du tableau,
    for ($i = 0; $i < $nbr_valeurs; $i++) {

        // Récupérer la valeur à l'index i.
        $valeur = $tableau[$i];

        // Ajouter ce nombre a la somme.
        $somme += $valeur;
    }

    // Calculer la moyenne arithmetique.
    $moyenne = $somme / $nbr_valeurs;

    // Retourner la moyenne arithmetique calculee.
    return $moyenne;
}









?>