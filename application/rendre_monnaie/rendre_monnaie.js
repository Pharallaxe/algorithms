// -----------------------------------------------
// Fonction rendre_monnaie
// -----------------------------------------------
// Calcul le rendu de monnaie en fonction du prix
// et des quantites des differentes pieces.
// -----------------------------------------------

// -----------------------------------------------
// Version Courte
// -----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

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

// -----------------------------------------------
// Application
// -----------------------------------------------

let prix = 47;       // Prix de l'article en euros
let x20 = 2; // Nbre de billets de 20 euros donnes
let x10 = 2; // Nbre de billets de 10 euros donnes
let x5 = 1;   // Nbre de billets de 5 euros donnes
let x2 = 3;   // Nbre de pieces de 2 euros donnees
let x1 = 4;    // Nbre de pieces de 1 euro donnees

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

// -----------------------------------------------
// Version Golf
// -----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

function rendre_monnaie_golf(p,a,b,c,d,e) {
    let s=a*20+b*10+c*5+d*2+e-p,R=[];
    for (let m of[20,10,5,2,1])
        {let r=Math.floor(s/m);s-=r*m;R.push(r)}
    return s>=0?R:[0,0,0,0,0];
}

// -----------------------------------------------
// Version Detaillee
// -----------------------------------------------
// Cette version permet de suivre pas a pas l'exe-
// cution de la fonction.

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

// -----------------------------------------------
// Version Commentee
// -----------------------------------------------
// Similaire a la version detaillee, mais avec des
// commentaires concis afin d'expliquer les etapes
// principales de la fonction.

function rendre_monnaie_commentee(prx, x20, x10,
    x5, x2, x1) {

    // Calculer le montant total donne en monnaie.
    let donne = ( x20 * 20 + x10 * 10 + x5 * 5 +
        x2 * 2 + x1 * 1);

    // Calculer la somme a rendre.
    let somme = donne - prx;

    // Si la somme est negative ou 0
    if (somme < 1) {
        // Retourner une liste de zeros.
        return [0, 0, 0, 0, 0];
    } else {
        // Initialiser une liste vide de stockage.
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
