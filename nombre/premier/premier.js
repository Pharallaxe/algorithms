//-----------------------------------------------
// premier
/*-----------------------------------------------
/ Un nombre premier est un nombre qui n'est divi-
/ sible que par 1 ou par lui-même.
/----------------------------------------------*/

//-----------------------------------------------
// Version courte
//-----------------------------------------------

function premier(nombre) {
    if (nombre < 2) {
        return false;
    }

    if (nombre === 2 || nombre === 3) {
        return true;
    }

    if (nombre % 2 === 0) {
        return false;
    }

    let rac = Math.floor(Math.sqrt(nombre));

    for (let i = 5; i <= rac; i += 2) {
        if (nombre % i === 0) {
            return false;
        }
    }

    return true;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let nombres = [76, 101, 17, 58];
nombres.forEach(function(nb) {
    let res = premier(nb);
    if (res) {
        console.log(`${nb} est premier.`);
    }
    else {
        console.log(`${nb} n'est pas premier.`);
    }
});



//-----------------------------------------------
// Version golf
//-----------------------------------------------

let P=n=>n>1 &&[...Array(Math.floor(Math.sqrt(n))
+1).keys()].slice(2).every(i=>n%i);



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function premier_detaillee(nombre) {

    if (nombre < 2) {
        return false;
    }

    if (nombre === 2 || nombre === 3) {
        return true;
    }

    if (nombre % 2 === 0) {
        return false;
    }

    let rac_carree = Math.sqrt(nombre);
    let rac_arrondie = Math.floor(rac_carree);

    for (let i = 5; i < rac_arrondie + 1; i+=2) {
        let reste = nombre % i;

        if (reste === 0) {
            return false;
        }
    }

    return true;
}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function premier_commentee(nombre) {

    // Si le nombre est inférieur a 2,
    if (nombre < 1) {

        // renvoyer False.
        return false;
    }

    // Calculer la racine carrée du nombre.
    let rac_carree = Math.sqrt(nombre);

    // Arrondir la racine carrée.
    let rac_arrondie = Math.floor(rac_carree);

    // Pour les nombres de 2 à la racine carrée,
    for (let i = 2; i <= rac_arrondie; i++) {

        // Récupérer le reste de la division du
        // nombre par i 
        let reste = nombre % i;

        // Si le reste est égal à 0,
        if (reste === 0) {

            // c'est que le nombre est divisble
            // par l'entier : on retourne False.
            return false;
        }
    }

    // Si nombre n'est divisible par aucun nombre
    // entre 2 et sa racine carrée, alors il est
    // premier : on retourne True.
    return true;
}









//