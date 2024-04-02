//-----------------------------------------------
// Fonction Base
/*-----------------------------------------------
/ Un lipogramme est une chaine de caracteres qui
/ ne contient aucun caractere donne, comme le e.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function lipogramme(chaine, lettre) {
    chaine = chaine.toLowerCase();
    lettre = lettre.toLowerCase();

    chaine = chaine.replace(" ", "");

    return chaine.indexOf(lettre) === -1;
}



//-----------------------------------------------
// Application
//-----------------------------------------------


let chaine = "Le ver de terre";
let lettre = "e";
let est_lipogramme = lipogramme(chaine, lettre);

let res = "";
res += `"${chaine}" `;
res += est_lipogramme ? "est" : "n'est pas";
res += ` un lipogramme en '${lettre}'.`;
console.log(res);
    



//-----------------------------------------------
// Version golf
//-----------------------------------------------

let L=(c,l)=>(c=c.toLowerCase().replace(" ",'')).
indexOf(l.toLowerCase())==-1



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function lipogramme_commentee(chaine, lettre) {

    // Convertir en minuscules
    chaine = chaine.toLowerCase();
    lettre = lettre.toLowerCase();

    // Supprimer les espaces
    chaine = chaine.replace(" ", "");

    // Retourner le resultat.
    return chaine.indexOf(lettre) === -1;
}









//