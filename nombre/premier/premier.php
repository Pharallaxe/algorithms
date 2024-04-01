<?php
# -----------------------------------------------
# premier
# -----------------------------------------------
# Un nombre premier est un nombre qui n'est divi-
# sible que par 1 ou par lui-même.
# -----------------------------------------------

# -----------------------------------------------
# Version courte
# -----------------------------------------------

function premier($nombre) {
    if ($nombre < 2) {
        return false;
    }

    if ($nombre === 2 || $nombre == 3) {
        
    }
    
    for ($i = 2; $i <= sqrt($nombre); $i++) {
        if ($nombre % $i === 0) {
            return false;
        }
    }
    
    return true;
}



# -----------------------------------------------
# Application
# -----------------------------------------------

$nombres = [76, 101, 17, 58];
foreach ($nombres as $nombre) {
    $res = $P($nombre);
    $chaine = $res ? "est" : "n'est pas";
    echo $nombre . " " . $chaine . " premier\n";
}



# -----------------------------------------------
# Version golf
# -----------------------------------------------

$P=fn($n)=>$n>1&&array_reduce(range(2,floor(sqrt(
$n))),fn($C,$i)=>$C&&$n%$i,1);



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------

function premier_detaillee($nombre) {
    if ($nombre < 1) {
        return false;
    }

    $racineCarree = floor(sqrt($nombre));

    for ($i = 2; $i <= $racineCarree; $i++) {
        $reste = $nombre % $i;

        if ($reste === 0) {
            return false;
        }
    }

    return true;
}



# -----------------------------------------------
# Version commentee
# -----------------------------------------------

function premier_commentee($nombre) {

    // Si le nombre est inférieur a 2,
    if ($nombre < 1) {

        // renvoyer False.
        return false;
    }

    // Calculer la racine carrée de nombre.
    $racineCarree = floor(sqrt($nombre));

    // Pour les nombres de 2 à la racine carrée,
    for ($i = 2; $i <= $racineCarree; $i++) {

        // Récupérer le reste de la division du
        // nombre par i 
        $reste = $nombre % $i;

        // Si le reste est égal à 0,
        if ($reste === 0) {

            // c'est que le nombre est divisble
            // par l'entier : on retourne False.
            return false;
        }
    }

    // Si nombre n'est divisible par aucun nombre
    // entre 2 et sa racine carrée, alors il est
    // premier : on retourne True.
    return true;
}









?>