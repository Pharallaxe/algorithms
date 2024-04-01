//-----------------------------------------------
// harmonique 
/*-----------------------------------------------
/ Permet de realiser une moyenne harmonique. Elle
/ permet d'etablir une moyenne plus significative
/ dans certains domaines, comme celui du calcul
/ des vitesses?

/ Cette moyenne de n nombres (x1, x2,..., xn) est
/ calculee en divisant le nomùbre de valeurs par
/ la somme des inverses de chaque valeur.

/                           N
/ Formule : MH = --------------------------
                 (1/x1 + 1/x2 + ... + 1/xn)

/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function harmonique(tableau) {
    let somme = tableau.reduce((a,b)=>a+(1/b),0);
    return tableau.length / somme;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

// Si pendant une heure vous faites 50 km/h, puis
// pendant encore une heure 90 km/h, c'est comme
// si vous aviez fait pendant deux heures....

let tableau = [50, 90]
let moyenne = harmonique(tableau);
moyenne = moyenne.toFixed(2)
console.log("La moyenne est", moyenne)



//-----------------------------------------------
// Version golf
//-----------------------------------------------

let H=l=>l.length/l.reduce((a,n)=>a+1/n,0);



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function harmonique_detaillee(tableau) {
    let longueur = tableau.length;
    let somme = 0;
    
    for (let i = 0; i < longueur; i++) {
        let valeur = tableau[i];
        somme += 1 / valeur;
    }

    let moyenne = longueur / somme;
    
    return moyenne;
}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function harmonique_commentee(tableau) {
    
    // Identifier la longueur de la tableau.
    let longueur = tableau.length;
    
    // Initialiser la somme a 0.
    let somme = 0;
    
    // De 0 a la longueur de la tableau,
    for (let i = 0; i < longueur; i++) {
        
        // Recuperer la valeur a l'index i.
        let valeur = tableau[i];
        
        // Ajouter l'inverse de la valeur à la
        // somme.
        somme += 1 / valeur;
    }

    // Calculer la moyenne.
    let moyenne = longueur / somme;
    
    // Retourner la moyenne.
    return moyenne;
}









//