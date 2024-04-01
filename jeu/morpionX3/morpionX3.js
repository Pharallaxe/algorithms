//-----------------------------------------------
// morpion
//-----------------------------------------------
// Identifie si une grille de morpion 3 x 3 con-
// tient une combinaison gagnante et retourne le
// gagnant.
//-----------------------------------------------


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function morpion(grille, vide) {

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
// Application
//-----------------------------------------------

const grille = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", "X"]
];

const gagnant = morpion(grille, " ");
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
[1][i]==g[2][i]&& g[2][i]!=v)?g[i][0]:"")[0])||(g
[1][1]!=v&&((g[0][0]==g[1][1]&&g[1][1]==g[2][2]&&
g[2][2]!=v)||(g[0][2]==g[1][1]&&g[1][1]==g[2][0]
&&g[2][0]!=v))?g[1][1]:v);



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function morpion_detaillee(grille, vide) {

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

function morpion_commentee(grille, vide) {

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