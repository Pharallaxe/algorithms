//-----------------------------------------------
// info
/*-----------------------------------------------
/ Il est conseille d'aller consulter l'algorithme
/ des nombres premiers avant toute chose.
/----------------------------------------------*/

//-----------------------------------------------
// diviseurs
/*-----------------------------------------------
/ Un diviseur est un nombre qui divise un entier
/ en part equitable dans laisser de reste.
/ Ex : 8 est diviseur de 24 => 3 * 8 = 24, mais 6
/ est aussi diviseur de 24 => 4 * 6 = 24. En re-
/ vanche, 5 n'est pas diviseur de 24 car 5 * 4 =
/ 20, il faut encore 4 pour compléter 24.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function diviseurs(nombre) {
    return Array
        .from({length: nombre}, (_, i) => i + 1)
        .filter(i => nombre % i === 0);

}



//-----------------------------------------------
// Application
//-----------------------------------------------

let nombres = [8, 24, 100, 120];

for (let nb of nombres) {
    let res = diviseurs(nb);
    console.log("Les diviseurs de " + nb +
        " sont " + res);
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

let D=(N)=>Array.from({length:N},(_, i)=>i+1)
.filter(i=>N%i===0);



//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

function diviseurs_detaillee(nombre){
    let diviseurs_liste = [];
    
    for (let i = 1; i <= nombre; i++) {
        if (nombre % i === 0) {
            diviseurs_liste.push(i);
        }
    }
    
    return diviseurs_liste;
}



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */

function diviseurs_commentee(nombre) {
    // Initialiser une liste pour les diviseurs.
    let diviseurs_liste = [];
    
    // De 1 à nombre,
    for (let i = 1; i <= nombre; i++) {
        
        // si le reste de la division de nombre
        // par i est egal à 0,
        if (nombre % i === 0) {
            
            // Ajouter i à la liste des diviseurs.
            diviseurs_liste.push(i);
        }
    }
    
    // Retourne la liste des diviseurs.
    return diviseurs_liste;
}









//