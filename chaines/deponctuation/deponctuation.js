//-----------------------------------------------
// Fonction deponctuer
/*-----------------------------------------------
/ Elle supprime d'une chaîne les caractères don-
/ nés en paramètre.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function deponctuer(chaine, liste) {
    for (let char of liste) {
        chaine = chaine.replace(char, "");
    }
    return chaine;
}


//-----------------------------------------------
// Application
//-----------------------------------------------

let chaine= "C'est, un exemple! de ponctuation.";
let caracteres = ",.!'";
let deponctuee = deponctuer(chaine, caracteres);

console.log("Chaine de départ :", chaine);
console.log("Chaine deponctuée :", deponctuee);


//-----------------------------------------------
// Version golf
//-----------------------------------------------

let D=(c,l="")=>c.replace(new RegExp(`[${l}]`,
'g'),'');


//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function deponctuer_commentee(chaine, liste) {

    // Pour chaque caractère de la liste,
    for (let char of liste) {

        // Remplacer le caractère par rien.
        chaine = chaine.replace(char, "");
    }
    // Retourner la chaine modifiée.
    return chaine;
}









//
