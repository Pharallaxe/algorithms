<?php
# -----------------------------------------------
# Fonctions anagramme
# -----------------------------------------------
# Identifie si deux chaines sont anagrammes, donc
# si elles sont composées des mêmes lettres exac-
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
$sontAnagrammes = anagramme($str1, $str2);
$chaine = $sontAnagrammes ? "sont" : "ne sont pas";
echo "Les chaînes $chaine des anagrammes.";



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

function anagramme_golf($s1, $s2)
    {return count_chars(strtoupper($s1),1)
        ==count_chars(strtoupper($s2),1);}



# -----------------------------------------------
# Version détaillée
# -----------------------------------------------
# Cette version permet de suivre pas à pas l'exé-
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
    $A_sorted = str_split($str_A);
    sort($A_sorted);
    $A_sorted = implode('', $A_sorted);

    $B_Sorted = str_split($str_B);
    sort($B_Sorted);
    $B_Sorted = implode('', $B_Sorted);

    // Vérifier l'équivalence des chaines.
    return $A_sorted === $B_Sorted;
}

?>