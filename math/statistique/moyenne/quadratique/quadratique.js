//-----------------------------------------------
// quadratique
/*-----------------------------------------------
/  Cette fonction calcule la moyenne quadratique.
/----------------------------------------------*/



//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

let quadratique = (tableau) => {
    let somme = tableau.reduce((a,x)=>a+x**2,0);
    return Math.sqrt(somme / tableau.length);
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let tableau = [12, 14, 16, 8, 6, 18];
let moyenne = quadratique(tableau);
console.log("La moyenne est",moyenne.toFixed(2));



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

let Q=(l)=>Math.sqrt(l.reduce((a,x)=>a+x**2,0)/l
.length);



//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

function quadratique_detaillee(tableau) {
    let nbr_valeurs = tableau.length;
    let somme = 0;

    for (let i = 0; i < nbr_valeurs; i++) {
        let valeur = tableau[i];
        let carre = valeur ** 2;
        somme += carre;
    }

    let division = somme / nbr_valeurs;
    let moyenne = Math.sqrt(division);

    return moyenne;
}



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */

function quadratique_commentee(tableau) {
    
    // Recuperer le nombre de valeurs.
    let nbr_valeurs = tableau.length;
    
    // Initialiser une somme à 9.
    let somme = 0;
    
    // De 0 à nombre de valeurs,
    for (let i = 0; i < nbr_valeurs; i++) {
        
        // recuperer la valeur de la tableau à
        // l'index i,
        let valeur = tableau[i];
        
        // elever cette valeur au carre, et
        let carre = valeur ** 2;
        
        // ajouter ce carre a la somme.
        somme += carre;
    }
    
    // Diviser la somme par le nombre de valeurs.
    let division = somme / nbr_valeurs;
    
    // Effecturer la racine carrée du resultat.
    let moyenne = Math.sqrt(division);
    
    // Retourner la moyenne ainsi calculee.
    return moyenne;
}









//