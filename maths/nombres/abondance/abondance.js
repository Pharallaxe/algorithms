//-----------------------------------------------
// abondance 
/*-----------------------------------------------
/ Fonction qui retourne l'abondance d'un nombre.
/ L'abondance c'est le rapport entre la somme des
/ diviseurs du nombre et le nombre lui-même.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

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
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

let A=n=>n<1?null:[...Array(n-1)].reduce((acc,_,i
)=>n%++i?acc:acc+i,0)/n;


//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

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
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */

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