//-----------------------------------------------
// Fonction solveur
/*-----------------------------------------------
/ Voici l'algorithme qui permet la resolution des
/ equations du second degre. Un mathematicien ce-
/ lebre du IXe siecle, Al-Khwarizmi, par deforma-
/ tion successive, a donne son nom a ce terme mê-
/ me d'algorithme. 
//---------------------------------------------*/

//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

// Resoud les equations dans l'ensemble des reels
function solveur_reel(a, b, c) {
    let delta = b ** 2 - 4 * a * c;
    let solutions = [];

    // Delta = 0, une solution
    if (delta === 0) {
        solutions.push(-b / (2 * a));
    }

    // Delta > 0, deux solutions
    else if (delta > 0) {
        let sq_del = Math.sqrt(delta);
        let x1 = (-b - sq_del) / (2 * a);
        let x2 = (-b + sq_del) / (2 * a);
        solutions.push(
            Math.min(x1, x2),
            Math.max(x1, x2)
        );
    }
    return solutions;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

// Equation a deux solutions.
let equation_1 = [1, -3, 2];
let sol_1 = solveur_reel(...equation_1);
sol_1 = sol_1.join(", ")
console.log(`Les solutions sont {${sol_1}}`);

// Equation a une solution.
let equation_2 = [1, -2, 1];
let sol_2 = solveur_reel(...equation_2);
sol_2 = sol_2.join(", ")
console.log(`Les solutions sont {${sol_2}}`);


//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

S=(a,b,c)=>(F=e=>e.toFixed(2),D=b**2-4*a*c,s=D===
0?[-b/(2*a)]:D>0?(d=Math.sqrt(D),x1=(-b-d)/(2*a),
x2=(-b+d)/(2*a),[Math.min(x1,x2),Math.max(x1,x2)]
):[])



//-----------------------------------------------
// Version commentee
//-----------------------------------------------
// Proche de la version raccourcie, mais avec des
// commentaires concis pour expliquer les etapes
// principales de la fonction.

function solveur_reel_commentee(a, b, c) {

    // Calculer le discriminant.
    let delta = b ** 2 - 4 * a * c;

    // Initialiser le tableau de solutions.
    let solutions = [];

    // Si delta = 0,
    if (delta === 0) {

        // ajouter la solution unique au tableau.
        solutions.push(-b / (2 * a));
    }

    // Si delta > 0
    else if (delta > 0) {

        // calculer le carré de delta ;
        let sq_del = Math.sqrt(delta);

        // trouver les racines ;
        let x1 = (-b - sq_del) / (2 * a);
        let x2 = (-b + sq_del) / (2 * a);

        // ajouter les solutions dans l'ordre.
        solutions.push(Math.min(x1, x2));
        solutions.push(Math.max(x1, x2));
    }

    // Retourner le tableau de solutions
    return solutions;
}



//-----------------------------------------------
// Version courte pour les complexes
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.


// Resoud les equations dans les complexes.
function solveur_complexe(a, b, c) {
    let delta = b ** 2 - 4 * a * c;
    let solutions = [];

    if (delta >= 0) {
        return solveur_reel(a, b, c);
    }

    // Delta < 0, solutions complexes
    else {
        let sq_del = Math.sqrt(-delta);
        let Reel = -b / (2 * a);
        let Img = sq_del / (2 * a);

        Reel = Reel.toFixed(1);
        Img = Img.toFixed(1);
        ImgNeg = (-Img).toFixed(1)

        solutions.push(`${Reel} + ${Img}i`);
        solutions.push(`${Reel} + ${ImgNeg}i`);

    }

    return solutions;
}



//-----------------------------------------------
// Application pour les complexes
//-----------------------------------------------

let equation_3 = [1, 2, 5];
let sol_3 = solveur_reel(...equation_3);
sol_3 = sol_3.join(", ")
console.log(`Les solutions sont {${sol_3}}`);









//