//-----------------------------------------------
// ecart_type 
/*-----------------------------------------------
/ L'ecart-type est la racine carree de la varian-
/ ce. Il indique a quel point les valeurs indivi-
/ duelles d'un ensemble de donnees s'ecartent de
/ la moyenne de cet ensemble. 
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function ecart_type(liste) {

    let moyenne  = liste.reduce((acc, x) => acc +
        x ) / liste.length;

    let variance = liste.reduce((acc, x) => acc +
        (x - moyenne) ** 2, 0) / liste.length;


    return Math.sqrt(variance);
}

//-----------------------------------------------
// Application
//-----------------------------------------------

let liste = [12, 14, 16, 8, 6, 18];
let E_T = ecart_type(liste);
console.log("L'écart-type est :", E_T.toFixed(2));



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

const ET=l=>Math.sqrt(l.reduce((a,x)=>a+(x-(m=l.
reduce((s,n)=>s+n,0)/l.length))**2,0)/l.length);



//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

function ecart_type_detaillee(liste) {

    let longueur = liste.length;
    let somme = 0;

    for (let courant of liste) {
        somme += courant;
    }

    let moyenne = somme / longueur;

    let somme_carres = 0;

    for (let courant of liste) {
        let ecart = courant - moyenne;
        let carre_ecart = Math.pow(ecart, 2);
        somme_carres += carre_ecart;
    }

    let variance = somme_carres / longueur;
    let ecart_type = Math.sqrt(variance);

    return ecart_type;
}



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */


function ecart_type_commentee(liste) {

    // Récupérer la longueur de la liste.
    let longueur = liste.length;

    // Initialiser la somme à 0.
    let somme = 0;

    // Pour chaque nombre dans la liste à étudier
    for (let courant of liste) {

        // Ajouter ce nombre à la somme
        somme += courant;
    }

    // Diviser la sommer par le nombre de termes.
    let moyenne = somme / longueur;

    // Calculer la somme des carrés des écarts.
    let somme_carres = 0;

    // Pour chaque terme de la liste à étudier.
    for (let courant of liste) {

        // Calculer l'écart entre le nombre et la moyenne.
        let ecart = courant - moyenne;

        // Calculer le carré de l'écart.
        let carre_ecart = Math.pow(ecart, 2);

        // Ajouter le carré de l'écart à la somme.
        somme_carres += carre_ecart;
    }

    // Diviser la somme des carrés la longueur..
    let variance = somme_carres / longueur;

    // Calculer la racine carrée de la variance.
    let ecart_type = Math.sqrt(variance);

    // Retourner l'écart-type résultant.
    return ecart_type;
}









//