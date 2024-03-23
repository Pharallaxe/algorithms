<?php
# -----------------------------------------------
# Fonction palindrome
# -----------------------------------------------
# Un palindrome, c'est une chaîne qui de gauche à
# droite, et de droite à gauche possède les memes
# caractères.
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
# Version condensée et optimisée du code, utili-
# sant des noms de variables courts et combinant
# certaines opérations pour réduire la taille du
# code. Pour la beauté du geste !

function palindrome_golf($c) {
    $r=implode(array_filter(str_split(strtolower(
     str_replace(" ", "", $c))), 'ctype_alnum'));
      return $r === strrev($r);
   }



# -----------------------------------------------
# Version commentée
# -----------------------------------------------
# Similaire à la version détaillée, mais avec des
# commentaires concis afin d'expliquer les étapes
# principales de la fonction.

function palindrome_commentee($chaine) {

    // Convertir la chaîne en minuscules.
    $chaine = strtolower($chaine);

    // Supprimer les espaces.
    $chaine = str_replace(" ", "", $chaine);

    // Initialiser le résultat.
    $resultat = "";

     // Parcourir chaque caractère de la chaîne.
     foreach (str_split($chaine) as $char) {

        // Si le caractère est alphanumérique,
        if (ctype_alnum($char)) {

            // Ajouter le caractère au résultat.
            $resultat .= $char;
        }
    }

    // Enregistrer la chaîne inversée.
    $chaineInverse = strrev($chaine);

    // Retourner le resultat.
    return $chaine === $chaineInverse;
}









#