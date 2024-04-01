//-----------------------------------------------
// montagne 
/*-----------------------------------------------
/ Cette fonction permet de dessiner quelques mon-
/ tagnes sous forme ASCII.
/ 
/ Ex: 
/                     /\
/                    /  \
/                   /    \
/                  /      \              /\
/     /\          /        \            /  \
/    /  \        /          \    /\    /    \
/   /    \  /\  /            \  /  \  /      \
/  /      \/  \/              \/    \/        \
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function montagne(sommets) {
    let paysage = [];
    let max = Math.max(...sommets)

    for (let j = 0; j <= max; j++) {
        let ligne = "";

        for (let el of sommets) {
            if (el < j + 1) {
                ligne += " ".repeat(2 * el);
            } else {
                ligne += " ".repeat(j) + "/"
                    + " ".repeat(2 *(el - j - 1))
                    + "\\" + " ".repeat(j);
            }
        }
        paysage.push(ligne.trimEnd());

    }
    return paysage.reverse().join("\n");
}


//-----------------------------------------------
// Application
//-----------------------------------------------

let sommets = [4, 2, 8, 3, 5];
let montagnes = montagne(sommets);
console.log(montagnes);



//-----------------------------------------------
// Version golf
//-----------------------------------------------

const M=s=>{let p=[],m=Math.max(...s);for(let j=0
;j<=m;j++){let l="";for(let e of s)l+=e<j+1?" "
.repeat(2*e):" ".repeat(j)+"/"+" ".repeat(2*(e-j-
1))+"\\"+" ".repeat(j);p.push(l.trimEnd())}
return p.reverse().join("\n")}



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function montagne_detaillee(sommets) {

    let paysage = [];
    let max = Math.max(...sommets);
    let longueur = sommets.length;

    for (let j = 0; j <= max; j++) {

        let ligne = "";

        for (let i = 0; i < longueur ; i++) {

            let el = sommets[i];

            if (el < j + 1) {
                ligne += " ".repeat(2 * el);
            }
            else {
                ligne += " ".repeat(j);
                ligne += "/";
                ligne += " ".repeat(2*(el-j-1));
                ligne += "\\";
                ligne += " ".repeat(j);
            }
        }

        paysage.push(ligne.trimEnd());
    }

    paysage = paysage.reverse();
    paysage = paysage.join("\n");
    
    return paysage;
}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function montagne_commentee(sommets) {

    // Initialiser une liste paysage.
    let paysage = [];

    // Identifier le plus haut des sommets
    let max = Math.max(...sommets);

    // Identifier le nombre de sommets.
    let longueur = sommets.length;
    
    // De 0 a max,
    // ou du sol au plus haut des sommets,
    for (let j = 0; j <= max; j++) {

        // Initialiser une nouvelle ligne.
        let ligne = "";

        // De 0 au nombre de sommets,
        // ou pour chaque sommet,
        for (let i = 0; i < longueur ; i++) {

            // recuperer le sommet courant.
            let el = sommets[i];

            // Si le sommet en cours est plus pe-
            // tit que le plus hauts des sommets
            if (el < j + 1) {

                // Ajouter 2 * el " " a ligne.
                ligne += " ".repeat(2 * el);
            
            // Sinon,
            } else {

                // Ajouter j espaces a la ligne.
                ligne += " ".repeat(j);

                // Ajouter "/" a la ligne.
                ligne += "/";

                // Ajouter 2*(el-j-1) espaces a
                // la ligne.
                ligne += " ".repeat(2*(el-j-1));

                // Ajouter "\" a la ligne.
                ligne += "\\";

                // Ajouter j espaces a la ligne.
                ligne += " ".repeat(j);
            }
        }

        // Ajouter la ligne sans espaces a la fin
        // au paysage.
        paysage.push(ligne.trimEnd());
    }

    // Renverser l'ensemble du paysage.
    paysage = paysage.reverse();

    // Ajouter un saut a la ligne a chaque ligne.
    paysage = paysage.join("\n");
    
    // Retourner le paysage.
    return paysage;
}










//