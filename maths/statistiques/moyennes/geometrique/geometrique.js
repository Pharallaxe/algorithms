//-----------------------------------------------
// geometrique 
/*-----------------------------------------------
/ Permet de realiser une moyenne geometrique qui
/ est plus insensible aux valeurs elevees que la
/ moyenne arithmetique. Elle permet donc une es-
/ timation meilleure des tendances centrales.

/ Cette moyenne de n nombres (x1, x2,..., xn) est
/ calculée en multipliant tous les nombres ensem-
/ ble, puis en prenant la racine enième de ce mê-
/ me produit.

/ Formule : MG = (x1 * x2 * ... * xn) ** (1/n)

/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function geometrique(tableau) {

    let produit = tableau.reduce((a, b) => a * b);

    return produit ** (1 / tableau.length);
}

//-----------------------------------------------
// Application
//-----------------------------------------------

let tableau = [12, 14, 16, 8, 6, 18];
let moyenne = geometrique(tableau);
console.log("La moyenne est",moyenne.toFixed(2));



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

let G=(l)=>tableau.reduce((a,b)=>a*b)**(1/l.length)


//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

function geometrique_detaillee(tableau) {

    let nbr_valeurs = tableau.length;
    
    let produit = 1;

    for (let i = 0; i < nbr_valeurs; i++) {
        let valeur = tableau[i];
        produit *= valeur;
    }

    return produit ** (1 / nbr_valeurs);
}



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */

function geometrique_commentee(tableau) {

    // Identifier la longueur de la tableau.
    let nbr_valeurs = tableau.length;
    
    // Initialiser le produit a 1.
    let produit = 1;

    // De 0 a la longueur du tableau,
    for (let i = 0; i < nbr_valeurs; i++) {

        // Récupérer la valeur à l'index i.
        let valeur = tableau[i];

        // Multiplier produit par cette valeur.
        produit *= valeur;
    }

    // Calculer le facteur de la racine.
    let enieme = 1 / nbr_valeurs;

    // Effectuer la racine enieme du produit.
    let $moyenne = produit ** enieme;

    // Retourner le resultat.
    return $moyenne;
}









//