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
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function automorphe(nombre) {
    var longueur = nombre.toString().length;

    var carre = nombre ** 2;

    var carre_str = carre.toString();
    var carre_fin = carre_str.slice(-longueur);
    var carre_fin_nombre = parseInt(carre_fin);

    return carre_fin_nombre == nombre;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let nombres = [125, 76, 89, 5];
for (let nb of nombres) {
    console.log(nb)
    let res = automorphe(nb);
    console.log(res)
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
// Version condensée et optimisée du code, utili-
// sant des noms de variables courts et combinant
// certaines opérations pour réduire la taille du
// code. Pour la beauté du geste !

let A=n=>(c=n**2,c.toString().endsWith(n));



//-----------------------------------------------
// Version commentee
//-----------------------------------------------
// Proche de la version raccourcie, mais avec des
// commentaires concis pour expliquer les etapes
// principales de la fonction.


function automorphe_explication(nombre) {
    // Récupérer la longueur du nombre.
    var longueur = nombre.toString().length;

    // Elever le nombre au carré.
    var carre = nombre ** 2;

    // Convertir en string.
    var carre_str = carre.toString();

    // Récupérer la fin du carré.
    var carre_fin = carre_str.slice(-longueur);

    // Convertir la fin du carré en nombre.
    var carre_fin_nombre = parseInt(carre_fin);

    // Retourner la solution.
    return carre_fin_nombre == nombre;
}