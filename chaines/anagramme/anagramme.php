<?php
# -----------------------------------------------
# Fonctions anagramme
# -----------------------------------------------
# Identifie si deux chaines sont anagrammes, donc
# si elles sont composees des mêmes lettres exac-
# tement.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

function anagramme($str1, $str2) {
    $str_A = str_split(strtoupper($str1));
    sort($str_A);

    $str_B = str_split(strtoupper($str2));
    sort($str_B);

    return implode('', $str_A) ===
        implode('', $str_B);
}



# -----------------------------------------------
# Application
# -----------------------------------------------

$str1 = "listen";
$str2 = "silent";
$sontAnagram = anagramme($str1, $str2);
$chaine = $sontAnagram ? "sont" : "ne sont pas";
echo "Les chaînes $chaine des anagrammes.";



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

$A=function($B,$C){return count_chars(strtoupper(
$B),1)==count_chars(strtoupper($C),1);};



# -----------------------------------------------
# Version detaillee
# -----------------------------------------------
# Cette version permet de suivre pas a pas l'exe-
# cution de la fonction.

function anagramme_detaillee($str_1, $str_2) {

    // TRAITER LA PREMIER CHAINE.
    $str_1 = strtoupper($str_1);
    $sorted_1 = str_split($str_1);
    sort($sorted_1);
    $chaine_fin_1 = implode('', $sorted_1);


    // TRAITER LA DEUXIEME CHAINE.
    $str_2 = strtoupper($str_2);
    $sorted_2 = str_split($str_2);
    sort($sorted_2);
    $chaine_fin_2 = implode('', $sorted_2);

    $res = $chaine_fin_1 === $chaine_fin_2;

    return $res;
}



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

function anagramme_commentee($str_1, $str_2) {

    // TRAITER LA PREMIER CHAINE.
    // La reduire en miniscule.
    $str_1 = strtoupper($str_1);

    // La decouper en tableau.
    $sorted_1 = str_split($str_1);

    // Trier ce tableau par ordre alphabétique.
    sort($sorted_1);

    // Le transformer en chaine.
    $chaine_fin_1 = implode('', $sorted_1);


    // TRAITER LA DEUXIEME CHAINE.
    // La reduire en miniscule.
    $str_2 = strtoupper($str_2);

    // La decouper en tableau.
    $sorted_2 = str_split($str_2);

    // Trier ce tableau par ordre alphabétique.
    sort($sorted_2);

    // Le transformer en chaine.
    $chaine_fin_2 = implode('', $sorted_2);

    // Comparer les deux chaines.
    $res = $chaine_fin_1 === $chaine_fin_2;

    // Retourner le resultat.
    return $res;
}

?>