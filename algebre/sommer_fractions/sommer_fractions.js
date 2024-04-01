//-----------------------------------------------
// sommer_fractions
//-----------------------------------------------
// Fonction qui permet d'ajouter deux fracions en-
// tre elles avec un même denominateur.
//-----------------------------------------------


//-----------------------------------------------
// Version courte
//-----------------------------------------------

function sommer_fractions (nbr1, nbr2) {
    let [num1,den1]=nbr1.split("/").map(Number);
    let [num2,den2]=nbr2.split("/").map(Number);
    
    let den = (den1===den2) ? den1 : den1 * den2;
    let num1_mult = num1 * den2;
    let num2_mult = num2 * den1;
    
    return `${num1_mult + num2_mult}/${den}`;
};



//-----------------------------------------------
// Application
//-----------------------------------------------

let nombre1 = "4/9";
let nombre2 = "12/3";
let res = sommer_fractions(nombre1, nombre2);
console.log(`${nombre1} + ${nombre2} = ${res}`);
// Affiche 120/27



//-----------------------------------------------
// Version golf
//-----------------------------------------------

const F=(n,N)=>{let[a,b]=n.split("/").map(Number)
,[c,d]=N.split("/").map(Number),D=(b===d)?b:b*d,A
=a*d,B=c*b;return`${A+B}/${D}`;};



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------

function sommer_fractions_detaillee(nbr_1, nbr_2)
{
    let num_den1 = nbr_1.split("/");
    let num_den2 = nbr_2.split("/");

    let numerateur1 = parseInt(num_den1[0]);
    let denominateur1 = parseInt(num_den1[1]);
    let numerateur2 = parseInt(num_den2[0]);
    let denominateur2 = parseInt(num_den2[1]);

    let den = 1;

    if (denominateur1 === denominateur2) {
        den = denominateur1;
    } else {
        den = denominateur1 * denominateur2;
    }

    numerateur1 = numerateur1 * denominateur2;
    numerateur2 = numerateur2 * denominateur1;

    return `${numerateur1 + numerateur2}/${den}`;
};



//-----------------------------------------------
// Version commentee
//-----------------------------------------------

function sommer_fractions_commentee(nbr_1, nbr_2)
{
    // Decouper les fractions en numerateurs et
    // denominateurs.
    let num_den1 = nbr_1.split("/");
    let num_den2 = nbr_2.split("/");

    // Convertir chaque element en nombre entier.
    let numerateur1 = parseInt(num_den1[0]);
    let denominateur1 = parseInt(num_den1[1]);
    let numerateur2 = parseInt(num_den2[0]);
    let denominateur2 = parseInt(num_den2[1]);

    // Initialiser le denominateur a 1, car il ne
    // peut être egal a 0.
    let den = 1;

    // Si les denominateurs sont egaux entre eux,
    if (denominateur1 === denominateur2) {
        
        // Utiliser l'un des denominateurs comme
        // denominateur commun.
        den = denominateur1;
    
    // Sinon,
    } else {
        
        // Calculer le denominateur commun.
        den = denominateur1 * denominateur2;
    }
    
    // Multiplier les numerateurs par les denomi-
    // nateurs adjacents.
    numerateur1 = numerateur1 * denominateur2;
    numerateur2 = numerateur2 * denominateur1;
    
    // Retourner le resultat.
    return `${numerateur1 + numerateur2}/${den}`;
};









//