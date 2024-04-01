//-----------------------------------------------
// morpion
//-----------------------------------------------
// Identifie si une grille de morpion 3 x 3 con-
// tient une combinaison gagnante et retourne le
// gagnant. C'est une version non dynamique, elle
// ne prend en compte qu'une grille de morpion de
// 3 de côté.
//-----------------------------------------------


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function morpion(grille, vide) {
    
    // Aplatir la grille.
    let table = grille.reduce((a, b) => a.concat(
        b), []);

    // Définir toutes les solutions
    let lignes = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ];

    // Pour chaque combinaison,
    for (let i = 0; i < lignes.length; i++) {
        let [a, b, c] = lignes[i];
        if (table[a] === table[b] &&
            table[b] === table[c] &&
            table[a] !== vide) {
            return table[a]; 
        }
    }

    return null; 
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let grille = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", "X"]
];

let gagnant = morpion(grille, " ");
if (gagnant !== " ") {
    console.log("Le gagnant est :", gagnant);
} else {
    console.log("Aucun gagnant pour le moment.");
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------

let M=(g,v)=>(g.map((_,i)=>(g[i][0]==g[i][1]&&g[i
][1]==g[i][2]&& g[i][2]!=v)||(g[0][i]==g[1][i]&&g
[1][i]==g[2][i]&&g[2][i]!=v)?g[i][0]:"")[0])||(g[
1][1]!=v&&((g[0][0]==g[1][1]&&g[1][1]==g[2][2]&&g
[2][2]!=v)||(g[0][2]==g[1][1]&&g[1][1]==g[2][0]&&
g[2][0]!=v))?g[1][1]:v);



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function morpion_commentee(grille, vide) {
    
    // Aplatir la grille en un tableau à une
    // dimension
    let table = grille
        .reduce((a, b) => a.concat(b), []);

    // Définir toutes les solutions
    let lignes = [
        [0,1,2],[3,4,5],[6,7,8],// en lignes,
        [0,3,6],[1,4,7],[2,5,8],// en colonne, et
        [0,4,8],[2,4,6]         // en diagonales.
    ];

    // Pour chaque combinaison,
    for (let i = 0; i < lignes.length; i++) {

        // identifier les trois emplacements,
        let [a, b, c] = lignes[i];

        // Si les valeurs sont égales et diffé-
        // rentes de vide,
        if (table[a] === table[b] &&
            table[b] === table[c] &&
            table[a] !== vide) {

            // retourner la valeur courante.
            return table[a]; 
        }
    }

    // Retourner null s'il n'y a pas de gagnant.
    return null; 
}


//-----------------------------------------------
// Version alpha
//-----------------------------------------------

function morpion_alpha(grille, vide) {

    // Vérification des lignes et colonnes
    for (let i = 0; i < 3; i++) {
        if ((grille[i][0] === grille[i][1] &&
             grille[i][1] === grille[i][2] &&
             grille[i][2] !== vide) ||

            (grille[0][i] === grille[1][i] &&
             grille[1][i] === grille[2][i] &&
             grille[2][i] !== vide)) {
            return grille[i][0];
        }
    }
    
    // Vérification des diagonales
    if ((grille[0][0] === grille[1][1] &&
         grille[1][1] === grille[2][2] &&
         grille[2][2] !== vide) ||

        (grille[0][2] === grille[1][1] &&
         grille[1][1] === grille[2][0] &&
         grille[2][0] !== vide)) {
        return grille[1][1];
    }

    return vide;
}

//-----------------------------------------------
// Version beta
//-----------------------------------------------

function morpion_beta(grille, vide) {

    for (let i = 0; i < 3; i++) {
        if (grille[i][0] === grille[i][1] &&
            grille[i][1] === grille[i][2] &&
            grille[i][2] !== vide) {

            return grille[i][0];
        }
    }
    
    for (let i = 0; i < 3; i++) {
        if (grille[0][i] === grille[1][i] &&
            grille[1][i] === grille[2][i] &&
            grille[2][i] !== vide) {
            return grille[0][i];
        }
    }
    
    if (grille[0][0] === grille[1][1] &&
        grille[1][1] === grille[2][2] &&
        grille[2][2] !== vide) {

        return grille[0][0];
    }
    
    if (grille[0][2] === grille[1][1] &&
        grille[1][1] === grille[2][0] &&
        grille[2][0] !== vide) {

        return grille[0][2];
    }
    
    return vide;
}


//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function morpion_beta_commentee(grille, vide) {

    //-------------------------------------------
    // Vérifier lignes.
    //-------------------------------------------

    for (let i = 0; i < 3; i++) {

        // Si les trois cases sont identiques,
        // et différentes de vide,
        if (grille[i][0] === grille[i][1] &&
            grille[i][1] === grille[i][2] &&
            grille[i][2] !== vide) {

            // retourner le gagnant sur la ligne.
            return grille[i][0];
        }
    }
    
    //-------------------------------------------
    // Vérifier colonnes.
    //-------------------------------------------

    for (let i = 0; i < 3; i++) {

        // Si les trois cases sont identiques,
        // et différent de vide
        if (grille[0][i] === grille[1][i] &&
            grille[1][i] === grille[2][i] &&
            grille[2][i] !== vide) {

            // Retourner la valeur de la colonne.
            return grille[0][i];
        }
    }
    
    //--------------------------------------------
    // Vérifier la diagonale descendante.
    //--------------------------------------------

    // Si les trois cases sont identiques,
    // et différent de vide,

    if (grille[0][0] === grille[1][1] &&
        grille[1][1] === grille[2][2] &&
        grille[2][2] !== vide) {

        // Le gagnant est sur la diagonale
        // principale.
        return grille[0][0];
    }
    
    //-------------------------------------------
    // Vérifier la diagonale ascendante.
    //-------------------------------------------

    // Si les trois cases sont identiques,
    // et différent de vide,

    if (grille[0][2] === grille[1][1] &&
        grille[1][1] === grille[2][0] &&
        grille[2][0] !== vide) {

        // Le gagnant est sur la diagonale
        // ascendante.
        return grille[0][2];
    }
    
    // Retourner aucun gagnant
    return vide;
}









//