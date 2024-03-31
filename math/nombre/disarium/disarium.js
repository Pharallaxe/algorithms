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

let nombres = [120, 133, 135, 145];
for (let nb of nombres) {
    let res = disarium(nb);
    if (res) {
        console.log(nb, "est disarium.");
    }
    else {
        console.log(nb, "n'est pas disarium.");
    }
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !


/* En réflexion ;) */



//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

function disarium_detaillee(nombre) {
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
