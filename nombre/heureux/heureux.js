//-----------------------------------------------
// Fonction 
/*-----------------------------------------------
/  Convertir entre differentes bases numeriques.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function heureux(nombre) {

    if (nombre < 10) {
        nombre = nombre ** 2;
    }

    while (nombre > 9) {
        let total = 0;

        for (let num of nombre.toString()) {
            total += parseInt(num) ** 2;
        }
        nombre = total;
    }

    return nombre === 1;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

for (let nb = 10; nb < 16; nb++) {
    let res = heureux(nb);
    if (res) {
        console.log(nb, "est heureux.");
    }
    else {
        console.log(nb, "n'est pas heureux.");
    }
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------

let H=n=>(g=k=>k<10?k:g([...k+''].reduce((a,b)=>a
+b*b,0)))(n)==1;



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function heureux_commentee(nombre) {

    // Si le nombre est inferieur a 10.
    if (nombre < 10) {

        // Élever le nombre au carre.
        nombre = nombre ** 2;
    }

    // Tant que le nombre est superieur a 9.
    while (nombre > 9) {

        // Initialiser total a 0.
        let total = 0;

        // Parcourir chaque chiffre.
        for (let num of nombre.toString()) {

            // Ajouter le carre au total.
            total += parseInt(num) ** 2;
        }
        // Mettre à jour le nombre.
        nombre = total;
    }

    // Retourner vrai si le nombre est egal a 1.
    return nombre === 1;
}









//