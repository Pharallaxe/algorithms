//-----------------------------------------------
// Fonction Base
//-----------------------------------------------
// Un lipogramme est une chaine de caracteres qui
// ne contient aucun caractere donne, comme le e.
//-----------------------------------------------


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function lipogramme(chaine, lettre) {
    chaine = chaine.toLowerCase();
    lettre = lettre.toLowerCase();

    chaine = chaine.replace(" ", "");

    return chaine.indexOf(lettre) === -1;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let chaine = "Le ver de terre.";
let lettre = "e";
let estLipogramme = lipogramme(chaine, lettre);
let estOuPas =
    estLipogramme ? "est" : "n'est pas";
console.log(
    `"${estOuPas}" un
    lipogramme en "${lettre}".`
);
    


//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensée et optimisée du code, utili-
// sant des noms de variables courts et combinant
// certaines opérations pour réduire la taille du
// code. Pour la beauté du geste !

let lipogramme=(c,l)=>(c=c.toLowerCase()
 .replace(" ",'')).indexOf(l.toLowerCase())==-1



//-----------------------------------------------
// Version commentee
//-----------------------------------------------
// Proche de la version raccourcie, mais avec des
// commentaires concis pour expliquer les etapes
// principales de la fonction.

function lipogramme(chaine, lettre) {

    // Convertir en minuscules
    chaine = chaine.toLowerCase();
    lettre = lettre.toLowerCase();

    // Supprimer les espaces
    chaine = chaine.replace(" ", "");

    // Retourner le resultat.
    return chaine.indexOf(lettre) === -1;
}









//