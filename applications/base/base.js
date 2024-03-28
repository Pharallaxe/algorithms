//-----------------------------------------------
// Fonction Base
/*-----------------------------------------------
/ Fonction convertissant un nombre une base vers
/ une autre..
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

function base(nb, depart, fin) {
    let base = "0123456789"
    base += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let val = 0;
    
    
    // Conversion du nombre en base 10.
    for (let ch of nb.split('').reverse()) {
        val = val * depart + base.indexOf(ch);
    }
    
    // Conversion vers de la base finale.
    let convertis = [];
    while (val > 0) {
        let reste = val % fin;
        val = Math.floor(val / fin);
        convertis.unshift(base[reste]);
    }
    
    return convertis.join('') || '0';
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let ch1 = "1010";
let depart1 = 2;
let arrivee1 = 10;
let res1 = base(ch1, depart1, arrivee1);
let conv1 = `${depart1} vers ${arrivee1}`;
console.log(`${ch1} de ${conv1} = ${res1}`);

let ch2 = "48";
let depart2 = 10;
let arrivee2 = 3;
let res2 = base(ch2, depart2, arrivee2);
let conv2 = `${depart2} vers ${arrivee2}`;
console.log(`${ch2} de ${conv2} = ${res2}`);



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

const B=(n,d,f)=>(e="ABCDEFGHIJKLMNOPQRSTUVWXYZ"+
"0123456789",v=0,n.split``.map(c=>v=v*d+e.indexOf
(c)),c=[],(g=(v=>v>0&&(r=v%f,c.unshift(e[r]),g(v/
f))))(v),c.join``||'0')



//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

function base_detaillee(nombre, depart, fin) {
    let base = "0123456789"
    base += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let val = 0;
    
    let nombre_inv = nombre.split('').reverse();
    let longueur = nombre_inv.length;
    
    for (let i = 0; i < longueur; i++) {
        let base_i = base.indexOf(nombre_inv[i]);
        val += base_i * Math.pow(depart, i);
    }
    
    let convertis = [];
    
    if (val === 0) {
        return "0";
    } else {
        while (val >= fin - 1) {
            let ch_base_fin = val % fin;
            convertis.unshift(base[ch_base_fin]);
            val = Math.floor(val / fin);
        }
        
        if (val !== 0) {
            convertis.unshift(base[val]);
        }
        
        return convertis.reverse().join('');
    }
}



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */

function base_commentee(nombre, depart, fin) {

    // Definir les symboles des les bases.
    let base = "0123456789"
    base += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Initialiser la val convertie en base 10.
    let valeur = 0;

    // Inverser la chaîne.
    let nombre_inv = nombre.split('').reverse();

    // Convertir la base depart vers la base 10.
    for (let i = 0; i < nombre_inv.length; i++) {

        // Trouver l'index du symbole.
        let base_i = base.indexOf(nombre_inv[i]);
        
        // Ajouter la val convertie a la base 10.
        valeur += base_i * Math.pow(depart, i);
    }

    // Initialiser une liste.
    let convertis = [];

    // Si la valeur est 0.
    if (valeur === 0) {

        // Retourner 0.
        return "0";

    // Sinon,
    } else {

        // Convertir de la base 10 vers "fin".
        while (valeur >= fin - 1) {

            // Calculer le chiffre dans la base
            // de destination.
            let ch_base_fin = valeur % fin;

            // Ajouter le chiffre a la liste des
            // chiffres convertis.
            convertis.push(base[ch_base_fin]);

            // Mettre a jour la valeur pour le
            //prochain chiffre.
            valeur = Math.floor(valeur / fin);
        }

        // Si la valeur est differente de 0.
        if (valeur !== 0) {

            // Ajouter le dernier chiffre.
            convertis.push(base[valeur]);
        }

        // Concatener tous les chiffres.
        let res = convertis.reverse().join('');

        // Retourn le resultat.
        return res
    }
}









//