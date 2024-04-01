//-----------------------------------------------
// sudoku_solveur 
/*-----------------------------------------------
/ Fonction pour resoudre un sudoku de taille 4 ou
/ 9 et qui n'es pas un sudoku tres complexe a re-
/ soudre.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function sudoku_solveur(grille) {
    let taille = grille.length;
    let mini = Math.sqrt(taille);

    // Resoud la grille.
    function resoudre() {
        for (let y = 0; y < taille; y++) {
            for (let x = 0; x < taille; x++) {
                if (grille[y][x] == 0) {
                    for (let n=1;n<=taille; n++){
                        if (valider_case(y,x,n)){
                            grille[y][x] = n;
                            if (resoudre()) {
                                return true;
                            }
                            grille[y][x] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    // Determine si une case est valide.
    function valider_case(y, x, num) {

        // Verifier la ligne
        if (grille[y].includes(num)) {
            return false;
        }

        // Verifier la colonne
        for (let y0 = 0; y0 < taille; y0++) {
            if (grille[y0][x] == num) {
                return false;
            }
        }

        // Verifier la sous-grille
        let y0 = Math.floor(y / mini) * mini;
        let x0 = Math.floor(x / mini) * mini;

        for (let j = 0; j < mini; j++) {
            for (let i = 0; i < mini; i++) {
                if (grille[y0 + j][x0 + i]==num){
                    return false;
                }
            }
        }

        return true;
    }

    return resoudre() ? grille : null;
}


//-----------------------------------------------
// Application
//-----------------------------------------------

// Grille Sudoku de taille 9
let sudoku_9 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
];

// Resoudre le Sudoku de taille 9
let resultat_9 = sudoku_solveur(sudoku_9);
console.log("")
console.log("Resolution du sudoku de taille 9");
if (resultat_9) {
    for (let ligne of resultat_9) {
        console.log(ligne.join(""));
    }
} else {
    console.log("Aucune solution trouvee.");
}

console.log("\n\n");

// Grille Sudoku de taille 4
let sudoku_4 = [
    [4, 0, 0, 3],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [2, 0, 4, 0]
];

// Resoudre le Sudoku de taille 4
let resultat_4 = sudoku_solveur(sudoku_4);
console.log("Resolution du sudoku de taille 4");
if (resultat_4) {
    for (let ligne of resultat_4) {
        console.log(ligne.join(""));
    }
} else {
    console.log("Aucune solution trouvee.");
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------

let SR=g=>{let t=g.length,m=Math.sqrt(t);for(let
R=0;R<t;R++){for(let C= 0;C<t;C++){if(!g[R][C]){
let s=Math.floor(R/m)*m,d=Math.floor(C/m)*m,U=new
Set(Array.from({length:t},(_,i)=>i+1).filter(N=>!
[...g[R].slice(),...g.map(w=>w[C]),...Array.from(
{length:m},(_,r)=>Array.from({length:m},(_,c)=>g[
s+r][d+c])).flat()].includes(N)));if(U.size===1){
g[R][C]=[...U][0];return SR(g);}}}}return g;}



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function sudoku_solveur_commentee(grille) {

    let taille = grille.length;
    let mini = Math.sqrt(taille);

    // Resoud la grille.
    function resoudre() {
        for (let y = 0; y < taille; y++) {
            for (let x = 0; x < taille; x++) {
                if (grille[y][x] == 0) {
                    return remplir_case(y, x);
                }
            }
        }
        return true;
    }

    // Tente de remplir une case de la grille.
    function remplir_case(y, x) {
        for (let num = 1; num <= taille; num++) {
            if (valider_case(y, x, num)) {
                grille[y][x] = num;
                if (resoudre()) {
                    return true;
                }
                grille[y][x] = 0;
            }
        }
        return false;
    }

    // Determine si une case est valide.
    function valider_case(y, x, num) {
        for (let x0 = 0; x0 < taille; x0++) {
            if (grille[y][x0] == num) {
                return false;
            }
        }

        for (let y0 = 0; y0 < taille; y0++) {
            if (grille[y0][x] == num) {
                return false;
            }
        }
        let y0 = Math.floor(y / mini) * mini;
        let x0 = Math.floor(x / mini) * mini;

        for (let j = 0; j < mini; j++) {
            for (let i = 0; i < mini; i++) {
                if (grille[y0 + j][x0 + i]==num){
                    return false;
                }
            }
        }
        return true;
    }

    // Principal
    if (resoudre()) {
        return grille;
    }
    else {
        return null;
    }
}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function sudoku_solveur_commentee(grille) {

    // Determiner la taille du côte de la grille.
    let taille = grille.length;
    
    // Determiner celle du sous-carre.
    let mini = Math.sqrt(taille);

    // Resoud la grille.
    function resoudre() {

        // Pour y, de 0 a taille,
        for (let y = 0; y < taille; y++) {

            // et pour chaque x, de 0 a taille
            for (let x = 0; x < taille; x++) {

                // si la case en y et x est vide,
                if (grille[y][x] == 0) {

                    // tenter de remplir la case,
                    // et retourner le numero.
                    return remplir_case(y, x);
                }
            }
        }
        // Retourner vrai pour avancer.
        return true;
    }

    // Tente de remplir une case de la grille.
    function remplir_case(y, x) {

        // Parcourir tous les numero possibles.
        for (let num = 1; num <= taille; num++) {

            // Si le numero n'est pas deja dans
            // la ligne et, la Conne et le sous-
            // carre.
            if (valider_case(y, x, num)) {

                // Remplir la case avec le numero.
                grille[y][x] = num;

                // Apeller recursivement la fonc-
                // tion pour continuer.
                if (resoudre()) {

                    // Retourner vrai.
                    return true;
                }

                // Annuler la derniere modifica-
                // tion, si la solution n'est pas
                // trouvee.
                grille[y][x] = 0;
            }
        }
        // Et donc retourner faux !
        return false;
    }

    // Determine si une case est valide.
    function valider_case(y, x, num) {

        // Pour chaque valeur de 0 a taille,
        for (let x0 = 0; x0 < taille; x0++) {

            // si cette valeur est presente dans
            // la ligne,
            if (grille[y][x0] == num) {

                // retourner faux.
                return false;
            }
        }
        // Pour chaque valeur de 0 a taille,
        for (let y0 = 0; y0 < taille; y0++) {

            // si cette valeur est presente dans
            // la colonne,
            if (grille[y0][x] == num) {

                // retourner faux.
                return false;
            }
        }
        // Initialiser le depart pour les lignes.
        let y0 = Math.floor(y / mini) * mini;

        // Initialiser le depart des colonnes.
        let x0 = Math.floor(x / mini) * mini;

        // Pour j, de 0 a sous taille,
        for (let j = 0; j < mini; j++) {

            // Pour i, de 0 a sous-taille,
            for (let i = 0; i < mini; i++) {

                // si la valeur de la case couran-
                // te est egale a celle de numero
                if (grille[y0 + j][x0 + i]==num){

                    // retourner faux.
                    return false;
                }
            }
        }
        // Sinon retourner vrai.
        return true;
    }

    // Si la fonction renvoie une solution,
    if (resoudre()) {
        // retourner la grille resolue.
        return grille;
    }
    // Sinon,
    else {
        // ne rien retourner.
        return null;
    }
}









//