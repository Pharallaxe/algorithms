//-----------------------------------------------
// Fonction palindrome
/*-----------------------------------------------
/ Un palindrome, c'est une chaîne qui de gauche à
/ droite, et de droite à gauche possède les memes
/ caractères.
//---------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function palindrome(chaine) {
    chaine = chaine
        .toLowerCase()
        .replace(" ", "");

    for (let char of chaine) {
        if (char.match(/[a-z0-9]/)) {
            resultat += char;
        }
    }

    let chaineInverse = [...resultat]
        .reverse()
        .join('');

    return resultat === chaineInverse;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let chaine = "Esope reste ici et se repose";
let est_Palindrome = palindrome(chaine);
let estOuPas = est_Palindrome ?
    "est" : "n'est pas";
console.log(
    `"${chaine}" ${estOuPas} un palindrome.`
);



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensée et optimisée du code, utili-
// sant des noms de variables courts et combinant
// certaines opérations pour réduire la taille du
// code. Pour la beauté du geste !

function palindrome_golf(ch) {
    let r = [...ch.toLowerCase()].filter(c =>
        /[a-z0-9]/ .test(c)).join("");
    return r === [...r].reverse().join("");}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------
// Proche de la version raccourcie, mais avec des
// commentaires concis pour expliquer les etapes
// principales de la fonction.


function palindrome_commentee(chaine) {

    // Convertir la chaine en minuscules.
    chaine = chaine.toLowerCase();

    // Supprimer les espaces.
    chaine = chaine.replace(" ", "");

    // Definir une chaine vide.
    let resultat = "";

    // Parcourir chaque caractere de la chaine.
    for (let char of chaine) {

        // Verifier si char est alphanumerique.
        if (char.match(/[a-z0-9]/)) {

            // Ajouter char au resultat.
            resultat += char;
        }
    }

    // Enregistrer la chaine inversee.
    let chaineInverse = resultat
        .split("")
        .reverse()
        .join("");

    // Retourner le resultat.
    return resultat === chaineInverse;
}









//