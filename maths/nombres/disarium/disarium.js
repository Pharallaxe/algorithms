//-----------------------------------------------
// Fonction disarium
/*-----------------------------------------------
/ Un "disarium number" est un nombre qui est égal
/ à la somme de ses chiffres élevés à la puissan-
/ de leur index plus un dans le nombre.
/ Ex. : 1^1 + 3^2 + 5^3 = 135
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.


function disarium(nombre) {
    
    let somme = nombre
        .toString()
        .split('')
        .reduce((acc, chiffre, i) => acc +
        Math.pow(parseInt(chiffre), i + 1), 0);

    return somme === nombre;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let nombre1 = 135;
let res1 = disarium(nombre1);
let chaine1 = res1 ? "est" : "n'est pas";
console.log(`${nombre1} ${chaine1} disarium.`);

let nombre2 = 133;
let res2 = disarium(nombre2);
let chaine2 = res2 ? "est" : "n'est pas";
console.log(`${nombre2} ${chaine2} disarium.`);



//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

function disarium_explication(nombre) {
    let nombre_str = nombre.toString();
    let longueur = nombre_str.length;
    
    let somme = 0;
    
    for (let i = 0; i < longueur; i++) {
        let chiffre = parseInt(nombre_str[i]);
        let puissance = i + 1;
        somme += Math.pow(chiffre, puissance);
    }
    
    return somme === nombre;
}



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */

function disarium_commentee(nombre) {
    // Convertir le nombre en chaîne.
    let nombre_str = nombre.toString();
    
    // Calculer la longueur de la chaîne.
    let longueur = nombre_str.length;
    
    // Initialiser la somme des chiffres a zéro.
    let somme = 0;
    
    // Parcourir chaque chiffre dans la chaîne.
    for (let i = 0; i < longueur; i++) {
        // Convertir le caractère en chiffre.
        let chiffre = parseInt(nombre_str[i]);
        
        // Définir la puissance en fonction de l'index.
        let puissance = i + 1;
        
        // Ajouter la puissance du chiffre à la somme.
        somme += Math.pow(chiffre, puissance);
    }
    
    // Retourner la solution
    return somme === nombre;
}









//