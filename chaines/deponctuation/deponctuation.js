//-----------------------------------------------
// Fonction deponctuer
//-----------------------------------------------
// Elle supprime d'une chaîne les caractères don-
// nés en paramètre.
//-----------------------------------------------


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function deponctuer(chaine, liste) {
    for (let char of liste) {
        chaine = chaine.replace(char, "");
    }
    return chaine;
}


//-----------------------------------------------
// Application
//-----------------------------------------------

let chaine = "C'est, un exemple! de ponctuation.";
let caracteres = ",.!'";
let deponctuee = deponctuer(chaine, caracteres);

console.log("Chaine de départ :", chaine);
console.log("Chaine deponctuée :", deponctuee);


//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensée et optimisée du code, utili-
// sant des noms de variables courts et combinant
// certaines opérations pour réduire la taille du
// code. Pour la beauté du geste !

const D=(c,l="")=>
    c.replace(new RegExp(`[${l}]`, 'g'), '');


//-----------------------------------------------
// Version commentee
//-----------------------------------------------
// Proche de la version raccourcie, mais avec des
// commentaires concis pour expliquer les etapes
// principales de la fonction.

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
