<?php
# -----------------------------------------------
# Fonction palindrome
# -----------------------------------------------
# Un palindrome, c'est une chaîne qui de gauche a
# droite, et de droite a gauche possede les memes
# caracteres.
# -----------------------------------------------


# -----------------------------------------------
# Version courte
# -----------------------------------------------
# Cette version permet de comprendre le contexte
# de la fonction et sa logique.

function palindrome($chaine) {
    $chaine = strtolower($chaine);

    $chaine = str_replace(" ", "", $chaine);

    $resultat = "";

    foreach (str_split($chaine) as $char) {
        if (ctype_alnum($char)) {
            $resultat .= $char;
        }
    }

    $chaineInverse = strrev($chaine);

    return $chaine === $chaineInverse;
}



# -----------------------------------------------
#  Application
# -----------------------------------------------

$chaine = "Esope reste ici et se repose";
$estPalindrome = palindrome($chaine);
$estOuPas = $estPalindrome ? "est" : "n'est pas";
echo "La chaîne \"$chaine\" $estOuPas un palindrome.";



# -----------------------------------------------
# Version golf
# -----------------------------------------------
# Version condensee et optimisee du code, utili-
# sant des noms de variables courts et combinant
# certaines operations pour reduire la taille du
# code. Pour la beaute du geste !

$P=function($c){$r=implode(array_filter(str_split
(strtolower(str_replace(" ","",$c))),'ctype_alnum
'));return$r==strrev($r);};



# -----------------------------------------------
# Version commentee
# -----------------------------------------------
# Similaire a la version detaillee, mais avec des
# commentaires concis afin d'expliquer les etapes
# principales de la fonction.

function palindrome_commentee($chaine) {

    // Convertir la chaîne en minuscules.
    $chaine = strtolower($chaine);

    // Supprimer les espaces.
    $chaine = str_replace(" ", "", $chaine);

    // Initialiser le resultat.
    $resultat = "";

     // Parcourir chaque caractere de la chaîne.
     foreach (str_split($chaine) as $char) {

        // Si le caractere est alphanumerique,
        if (ctype_alnum($char)) {

            // Ajouter le caractere au resultat.
            $resultat .= $char;
        }
    }

    // Enregistrer la chaîne inversee.
    $chaineInverse = strrev($chaine);

    // Retourner le resultat.
    return $chaine === $chaineInverse;
}









#