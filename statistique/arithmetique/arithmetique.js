//-----------------------------------------------
// arithmetique 
/*-----------------------------------------------
/ Permet de realiser une moyenne a partir d'une 
/ tableau de plusieurs valeurs.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function arithmetique(tableau) {

    let somme = tableau.reduce((a, b) => a + b);
    
    return somme / tableau.length;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let tableau = [12, 14, 16, 8, 6, 18];
let moyenne = arithmetique(tableau);
moyenne = moyenne.toFixed(2)
console.log("La moyenne est", moyenne);



//-----------------------------------------------
// Version golf
//-----------------------------------------------

let A=(l)=>l.reduce((a,b)=>a+b)/l.length;



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function arithmetique_detaillee(tableau) {

    let nbr_valeurs = tableau.length;
    let somme = 0;

    for (let i = 0; i < nbr_valeurs; i++) {
        let valeur = tableau[i];
        somme += valeur;
    }

    let moyenne = somme / nbr_valeurs;

    return moyenne;
}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function arithmetique_commentee(tableau) {

    // Calculer de la longueur de la tableau.
    let nbr_valeurs = tableau.length;

    // Initialiser la somme a 0.
    let somme = 0;

    // De 0 a la longueur du tableau,
    for (let i = 0; i < nbr_valeurs; i++) {

        // Récupérer la valeur à l'index i.
        let valeur = tableau[i];

        // Ajouter ce nombre a la somme.
        somme += valeur;
    }

    // Calculer de la moyenne arithmetique.
    let moyenne = somme / nbr_valeurs;

    // Retourner la moyenne arithmetique calculee.
    return moyenne;
}









//