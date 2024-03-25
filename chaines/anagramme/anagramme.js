//-----------------------------------------------
// Fonction anagramme
/*-----------------------------------------------
/ Identifie si deux chaines sont anagrammes, donc
/ si elles sont composées des mêmes lettres exac-
/ tement.
//----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function anagramme(str1, str2) {
    let str_A = str1.toUpperCase();
    let str_B = str2.toUpperCase();

    let A_sorted=str_A.split('').sort().join('');
    let B_Sorted=str_B.split('').sort().join('');

    return A_sorted === B_Sorted;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let str1 = "listen";
let str2 = "silent";
let sont_anag = anagramme(str1, str2);
let chaine = sont_anag ? "sont" : "ne sont pas";
console.log(`Les chaînes ${str1} et ${str2} ${
    chaine} des anagrammes.`);



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

const A=(s1,s2)=>s1.toUpperCase().split``.sort()
.join``==s2.toUpperCase().split``.sort().join``



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Proche de la version raccourcie, mais avec des
/ commentaires concis pour expliquer les etapes
/ principales de la fonction. */

function anagramme(str1, str2) {

    // Convertir les chaînes en majuscules.
    let str_A = str1.toUpperCase();
    let str_B = str2.toUpperCase();

    // Trier les deux chaines.
    let A_sorted=str_A.split('').sort().join('');
    let B_Sorted=str_B.split('').sort().join('');

    // Vérifier l'équivalence des chaines.
    return A_sorted === B_Sorted;
}









//