//-----------------------------------------------
// strobogrammatique 
/*----------------------------------------------- 
/ Un nombre strobogrammatique peut se lire de la
/ même façon après avoir subi une rotation de 180
/ degrés.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function strobogrammatique(nombre) {
    const strobo = {
        "0": "0", "1": "1", "8": "8", "6": "9",
        "9": "6" };

    nombre = nombre.toString();

    let deb = 0;
    let fin = nombre.length - 1;

    for (deb, fin; fin >= deb; deb++, fin--) {

        let premier = nombre[deb];
        let dernier = nombre[fin];

        if (!(premier in strobo &&
            strobo[premier] === dernier)) {
                return false;
            }
    }

    return true;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let nombres = [88, 133, 96, 101];
for (let nb of nombres) {
    let res = strobogrammatique(nb);
    let strobo = "strobogrammatique"
    if (res) {
        console.log(`${nb} est ${strobo}`);
    }
    else {
        console.log(`${nb} n'est pas ${strobo}`);
    }
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------

const S=n=>{const s={"0":"0","1":"1","8":"8","6":
"9","9":"6"};return(n=n.toString(),([...n].every(
(c,i)=>c in s&&s[c]===n[n.length-1-i])))};



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function strobogrammatique_detaillee(nombre) {

    const strobo = {
        "0": "0",
        "1": "1",
        "8": "8",
        "6": "9",
        "9": "6"
    };

    if (typeof nombre === 'number') {
        nombre = nombre.toString();
    }

    let gauche = 0;
    let droite = nombre.length - 1;

    while (droite - gauche >= 0) {

        let premier = nombre[gauche];
        let dernier = nombre[droite];

        if (
            !(premier in strobo) ||
            !(dernier in strobo) ||
            premier !== strobo[dernier]
        ) {
            return false;
        }

        droite -= 1;
        gauche += 1;
    }

    return true;
}

//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function strobogrammatique_commentee(nombre) {

    // Définir un dictionnaire de correspondance.
    const strobo = {
        "0": "0",
        "1": "1",
        "8": "8",
        "6": "9",
        "9": "6"
    };

    // Vérifier si nombre est un entier.
    if (typeof nombre === 'number') {

        // Convertir le nombre en string.
        nombre = nombre.toString();
    }

    // Initialiser les index.
    let gauche = 0;
    let droite = nombre.length - 1;

    // Tant que la différence est positive,
    while (droite - gauche >= 0) {

        // Obtenir le premier chiffre.
        let premier = nombre[gauche];

        // Obtenir le dernier chiffre.
        let dernier = nombre[droite];

        // Si,
        if (
            // le premier n'est pas dans le
            // dictionnaire,
            !(premier in strobo) ||

            // le dernier n'est pas dans le
            // dictionnaire,
            !(dernier in strobo) ||

            // si le premier et le dernier sont
            // différents.
            premier !== strobo[dernier]
        ) {

            // Alors, retourner faux.
            return false;
        }

        // Décrémenter les index.
        droite -= 1;
        gauche += 1;
    }

    // Retourner le resultat.
    return true;
}









//