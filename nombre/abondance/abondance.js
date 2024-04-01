//-----------------------------------------------
// abondance 
/*-----------------------------------------------
/ Fonction qui retourne l'abondance d'un nombre.
/ L'abondance c'est le rapport entre la somme des
/ diviseurs du nombre sauf lui même et le nombre
/ lui-même.

/ Ex : L'abondance de 28  est de 1. En effet, ses
/ diviseurs sont 1, 2, 4, 7, 14. Leur somme égale
/ 28. C'est un nombre parfait. Lorsque l'abondan-
/ ce est au dessus de 1, on dit que c'est un nom-
/ bre abondant. Si elle est en-deça de 1, on dira
/ qu'il est déficient.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function abondance(nombre) {
    if (nombre < 1) {
        return null;
    }
    
    let somme = Array
        .from({ length: nombre-1},(_,i) => i + 1)
        .filter(div => nombre % div === 0)
        .reduce((acc, div) => acc + div, 0);

    return somme / nombre;
}


//-----------------------------------------------
// Application
//-----------------------------------------------

let nombres = [2, 6, 28, 24, 120, 30240, 997920];

for (let nb of nombres) {
    let res = abondance(nb).toFixed(2);
    let affichage = `${nb} est `;
    if (res == 1) {
        affichage += "parfait";
    } else if (res < 1) {
        affichage += "deficient";
    } else {
        affichage += "abondant";
    }
    affichage += ` (abondance de ${res}).`;
    console.log(affichage);
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------

let A=n=>n<1?null:[...Array(n-1)].reduce((acc,_,i
)=>n%++i?acc:acc+i,0)/n;


//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function abondance_detaillee(nombre) {
    if (nombre < 1) {
        return null;
    }
    
    let somme = 0;

    for (let i = 1; i < nombre; i++) {
        if (nombre % i === 0) {
            somme += i;
        }
    }

    let abondance = somme / nombre;

    return abondance;
}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function abondance_commentee(nombre) {

    // Si le nombre est inférieur à 1,
    if (nombre < 1) {

        // Retourner null.
        return null;
    }
    
    // Initialiser la somme des diviseurs à 0.
    let somme = 0;

    // De 1 à nombres,
    for (let i = 1; i < nombre; i++) {

        // si le nombre est divisible par i,
        if (nombre % i === 0) {

            // alors ajouter i à la somme.
            somme += i;
        }
    }

    // Calculer l'abondance en divisant la somme
    // par le nombre.
    let abondance = somme / nombre;

    // Retourner l'abondance.
    return abondance;
}









//