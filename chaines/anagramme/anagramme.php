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

function anagramme_detaillee($str1, $str2) {

    $str_A = strtoupper($str1);
    $str_B = strtoupper($str2);

    $A_sorted = str_split($str_A);
    sort($A_sorted);
    $A_sorted = implode('', $A_sorted);

    $B_Sorted = str_split($str_B);
    sort($B_Sorted);
    $B_Sorted = implode('', $B_Sorted);

    return $A_sorted === $B_Sorted;
}



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

function anagramme_explication($str1, $str2) {
    // Convertir les chaînes en majuscules.
    $str_A = strtoupper($str1);
    $str_B = strtoupper($str2);

    // Trier les deux chaines.

    // Spliter la premiere chaine.
    $A_sorted = str_split($str_A);

    // Trier la premiere chaine.
    sort($A_sorted);

    // Concatener la premiere chaine.
    $A_sorted = implode('', $A_sorted);

    // Spliter la premiere chaine.
    $B_Sorted = str_split($str_B);

    // Trier la premiere chaine.
    sort($B_Sorted);

    // Concatener la premiere chaine.
    $B_Sorted = implode('', $B_Sorted);

    // Verifier l'equivalence des chaines.
    return $A_sorted === $B_Sorted;
}

?>