//-----------------------------------------------
// Fonction automorphe
/*-----------------------------------------------
/ Un nombre automorphe est un entier naturel dont
/ la suite des chiffres de son carré se termine
/ par celle du nombre lui-même.
//---------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function automorphe(nombre) {
    let longueur = nombre.toString().length;

    let carre = Math.pow(nombre, 2)
                    .toString()
                    .slice(-longueur);
    carre = parseInt(carre);

    return carre == nombre;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let nombres = [125, 76, 89, 625];
for (let nb of nombres) {
    let res = automorphe(nb);
    if (res) {
        console.log(nb, "est automorphe.");
    }
    else {
        console.log(nb, "n'est pas automorphe.");
    }
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------

let A=n=>(c=n**2,c.toString().endsWith(n));


//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function automorphe_detaillee(nombre) {
    // Récupérer la longueur du nombre.
    let longueur = nombre.toString().length;

    let carre = nombre ** 2;

    let carre_str = carre.toString();
    let carre_fin = carre_str.slice(-longueur);
    let carre_fin_nombre = parseInt(carre_fin);

    return carre_fin_nombre == nombre;
}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function automorphe_commentee(nombre) {
    // Récupérer la longueur du nombre.
    let longueur = nombre.toString().length;

    // Elever le nombre au carré.
    let carre = nombre ** 2;

    // Convertir en string.
    let carre_str = carre.toString();

    // Récupérer la fin du carré.
    let carre_fin = carre_str.slice(-longueur);

    // Convertir la fin du carré en nombre.
    let carre_fin_nombre = parseInt(carre_fin);

    // Retourner la solution.
    return carre_fin_nombre == nombre;
}









//