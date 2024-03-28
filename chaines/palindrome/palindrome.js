//-----------------------------------------------
// Fonction palindrome
/*-----------------------------------------------
/ Un palindrome, c'est une chaine qui de gauche a
/ droite, et de droite a gauche possede les memes
/ caracteres.
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
    
    let resultat = [...chaine]
        .filter(char => char.match(/[a-z0-9]/))
        .join('');

    let chaineInverse = [...resultat]
        .reverse()
        .join('');

    return resultat === chaineInverse;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let str = "Esope reste ici et se repose";
let estPalindrome = P(str);
let pal = "palindromme"

if (estPalindrome) {
    console.log(`"${str}" est un ${pal}.`);
} else {
    console.log(`"${str}" n'est pas un ${pal}.`);
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

const P=(c)=>(r=[...c.toLowerCase()].filter(e=>
/[a-z0-9]/.test(e)).join(""),r==[...r].reverse().
join(""))



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Proche de la version raccourcie, mais avec des
/ commentaires concis pour expliquer les etapes
/ principales de la fonction. */


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