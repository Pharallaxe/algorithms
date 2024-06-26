//-----------------------------------------------
// Fonction rendre_monnaie
/*-----------------------------------------------
/ Calcule le rendu de monnaie en fonction du prix
/ et des quantites des differentes pieces.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function rendre_monnaie(prx, x20, x10, x5, x2, x1)
{
    let donne = (x20 * 20 + x10 * 10 + x5 * 5 +
                 x2 * 2 + x1 * 1);
    let somme = donne - prx;
    let rendus = [];
    for (let monnaie of [20, 10, 5, 2, 1]) {
        let rendu = parseInt(somme / monnaie);
        somme -= rendu * monnaie;
        rendus.push(rendu);
    }
    return somme >= 0 ? rendus : [0, 0, 0, 0, 0];
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let prix = 47;       // Prix de l'article en euros
let x20 = 2; // Nbre de billets de 20 euros donnes
let x10 = 2; // Nbre de billets de 10 euros donnes
let x5  = 1;  // Nbre de billets de 5 euros donnes
let x2  = 3;  // Nbre de pieces de 2 euros donnees
let x1  = 4;   // Nbre de pieces de 1 euro donnees

// Calcul de la monnaie a rendre
let monnaie_rendue = rendre_monnaie(
    prix, x20, x10, x5, x2, x1
);

// Affichage du resultat
console.log("Monnaie a rendre :");
console.log("20 euros :", monnaie_rendue[0]);
console.log("10 euros :", monnaie_rendue[1]);
console.log("5 euros  :", monnaie_rendue[2]);
console.log("2 euros  :", monnaie_rendue[3]);
console.log("1 euro   :", monnaie_rendue[4]);

//-----------------------------------------------
// Version Golf
//-----------------------------------------------

let R=(p,a,b,c,d,e)=>{let s=a*20+b*10+c*5+d*2+e-p
    ,R=[];for(let m of[20,10,5,2,1]) {let r=Math.
    floor(s/m);s-=r*m;R.push(r)}return s>=0?R:[0,
    0,0,0,0];}


//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function rendre_monnaie_detaille(prx, x20, x10,
    x5, x2, x1) {

    let donne = ( x20 * 20 + x10 * 10 + x5 * 5 +
        x2 * 2 + x1 * 1);

    let somme = donne - prx;

    if (somme < 1) {
        return [0, 0, 0, 0, 0];
    } else {
        let monnaies = [20, 10, 5, 2, 1];
        let rendus = [];
        for (let monnaie of monnaies) {
            let rendu = parseInt(somme / monnaie);
            somme -= rendu * monnaie;
            rendus.push(rendu);
        }
        return rendus;
    }
}

//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function rendre_monnaie_commentee(prx, x20, x10,
    x5, x2, x1) {

    // Calculer le montant total de la monnaie.
    let donne = ( x20 * 20 + x10 * 10 + x5 * 5 +
        x2 * 2 + x1 * 1);

    // Calculer la somme a rendre.
    let somme = donne - prx;

    // Si la somme est negative ou 0
    if (somme < 1) {

        // Retourner une liste de zeros.
        return [0, 0, 0, 0, 0];
    
    // Sinon,
    } else {

        // Initialiser une liste vide.
        let rendus = [];
        
        // Definir les differentes de monnaie.
        let monnaies = [20, 10, 5, 2, 1];
        
        // Parcourir chaque denomination.
        for (let monnaie of monnaies) {
            
            // Identifier les pieces rendues.
            let rendu = parseInt(somme/monnaie);
            somme -= rendu * monnaie;
            rendus.push(rendu);
        }
        return rendus;
    }
}









//