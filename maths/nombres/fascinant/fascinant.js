//-----------------------------------------------
// fascinant
/*-----------------------------------------------
/ Un nombre est fascinant répond à certains cri-
/ tères : lorsqu'il est multiplié par 2 et par 3,
/ les chiffres du nombre initial, du double et du
/ triple de ce nombre sont différents et contien-
/ nent tous les chiffres de 1 à 9 une seule fois.
/---------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function fascinant(nombre) {
    const chaine_1 = String(nombre);
    
    if (chaine_1.length < 3) {
        return false;
    }
    
    const chaine_2 = String(nombre * 2);
    const chaine_3 = String(nombre * 3);
    
    const resultat = chaine_1 + chaine_2 + chaine_3;
    
    for (let i = 1; i <= 9; i++) {
        if (!resultat.includes(String(i))) {
            return false;
        }
    }
    
    return true;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let nombres = [108, 133, 192, 5832];
for (let nb of nombres) {
    let res = fascinant(nb);
    if (res) {
        console.log(nb, "est fascinant.");
    }
    else {
        console.log(nb, "n'est pas fascinant.");
    }
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

const F=n=>{let r=String(n)+String(2*n)+String(3*
n);return[...Array(9).keys()].every(i=>r.includes
(String(i+1)))&& String(n).length>3;};



//-----------------------------------------------
// Version commentée
//-----------------------------------------------
// Proche de la version raccourcie, mais avec des
// commentaires concis pour expliquer les étapes
// principales de la fonction.

function fascinant_commentee(nombre) {
    // Convertir le nombre en string.
    const chaine_1 = String(nombre);
    
    // Vérifier qu'il y a plus de 2 chiffres.
    if (chaine_1.length < 3) {
        return false;
    }
    
    // Convertir les nombres et ses multiples.
    const chaine_2 = String(nombre * 2);
    const chaine_3 = String(nombre * 3);
    
    // Concaténer les trois chaines.
    const resultat = chaine_1 + chaine_2 + chaine_3;
    
    // Pour chaque chiffre de 0 à 9,
    for (let i = 1; i <= 9; i++) {
        // Vérifier s'il est présent.
        if (!resultat.includes(String(i))) {
            return false;
        }
    }
    
    return true;
}









//