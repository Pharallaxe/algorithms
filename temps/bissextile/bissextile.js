//-----------------------------------------------
// Fonction bissextile
//-----------------------------------------------
// Fonction indiquant si une année est bissextile
// en suivant les règles du calendrier grégorien.
//-----------------------------------------------

//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function bissextile(annee) {
    if (annee % 400 === 0) {
        return true;
    } else if (annee % 100 === 0) {
        return false;
    } else if (annee % 4 === 0) {
        return true;
    } else {
        return false;
    }
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let texte = ["n'est pas", "est"];
let annees = [1900, 2000, 2024];
for (let annee of annees) {

    let est_bis = bissextile(annee);

    let res = annee + " ";

    if (est_bis) {
        res += "est";
    } else {
        res += "n'est pas";
    }
    res += " bissextile.";

    console.log(res);
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

let B=a=>a%400==0||(a%100!=0&&a%4==0)



//-----------------------------------------------
// Version commentée
//-----------------------------------------------
// Similaire à la version détaillée, mais avec des
// commentaires concis afin d'expliquer les étapes
// principales de la fonction.

// On va du plus large vers le plus court.

function bissextile_commentee(annee) {
    // Si une année est divisible par 400, elle
    // est bissextile.
    if (annee % 400 === 0) {
        return true;
    }
    
    // Sinon, si une année est divisible par 100,
    // sauf 400, elle n'est pas bissextile.
    else if (annee % 100 === 0) {
        return false;
    }
    
    // Sinon, si une année est divisible par 4,
    // elle est bissextile
    else if (annee % 4 === 0) {
        return true;
    }
    
    // Sinon, c'est une année quelconque, enfin,
    // sauf si c'est votre anniversaire.
    else {
        return false;
    }
}









//