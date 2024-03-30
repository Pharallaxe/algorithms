//-----------------------------------------------
// Fonction factorielle
/*-----------------------------------------------
/ Calcul du produit des entiers de 1 a n, où n un
/ entier positif est passe en argument.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function factorielle(nombre) {
    let produit = 1;

    for (let i = 1; i <= nombre; i++) {
        produit *= i;
    }

    return produit;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

res = factorielle(6);
console.log(`La factorielle de 6 est ${res}`);

//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

const F=n=>[...Array(n)].reduce((p,_,i)=>p*(i+1),
1);



//-----------------------------------------------
// Version commentee
//-----------------------------------------------
// Proche de la version raccourcie, mais avec des
// commentaires concis pour expliquer les etapes
// principales de la fonction.

function factorielle_commentee(nombre) {

    // Initialiser du produit a 1.
    let produit = 1;

    // De 1 a nombre,
    for (let i = 1; i <= nombre; i++) {

        // multiplier par le nombre courant.
        produit *= i;

    }

    // Retourner la factorielle calculee.
    return produit;
}









//