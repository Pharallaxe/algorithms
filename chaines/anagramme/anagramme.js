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

function anagramme(str1, str2) {
    let str_A = str1.toLowerCase();
    let str_B = str2.toLowerCase();

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
console.log(`"${str1}" et "${str2}" ${chaine
} des anagrammes.`);



//-----------------------------------------------
// Version golf
//-----------------------------------------------

const A=(s1,s2)=>s1.toUpperCase().split``.sort()
.join``==s2.toUpperCase().split``.sort().join``



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function anagramme_detaillee(chaine_1, chaine_2){

    // TRAITER LA PREMIER CHAINE.
    let chaine_1 = chaine_1.toLowerCase();
    let tableau_1 = chaine_1.split("");
    let triee_1 = tableau_1.sort();
    let chaine_fin_1 = triee_1.join("");

    // TRAITER LA DEUXIEME CHAINE.
    let chaine_2 = chaine_2.toLowerCase();
    let tableau_2 = chaine_2.split("");
    let triee_2 = tableau_2.sort();
    let chaine_fin_2 = triee_2.join("");


    let res = chaine_fin_1 === chaine_fin_2

    return res
}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function anagramme_commentee(chaine_1, chaine_2){

    // TRAITER LA PREMIER CHAINE.
    // La reduire en miniscule.
    let chaine_1 = chaine_1.toLowerCase();

    // La decouper en tableau.
    let tableau_1 = chaine_1.split("");

    // Trier ce tableau par ordre alphabétique.
    let triee_1 = tableau_1.sort();

    // Le transformer en chaine.
    let chaine_fin_1 = triee_1.join("");

    // TRAITER LA DEUXIEME CHAINE.
    // La reduire en miniscule.
    let chaine_2 = chaine_2.toLowerCase();

    // La decouper en tableau.
    let tableau_2 = chaine_2.split("");

    // Trier ce tableau par ordre alphabétique.
    let triee_2 = tableau_2.sort();

    // Le transformer en chaine.
    let chaine_fin_2 = triee_2.join("");


    // Comparer les deux chaines.
    let res = chaine_fin_1 === chaine_fin_2

    // Retourner le resultat.
    return res
}









//