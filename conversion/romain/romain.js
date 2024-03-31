//-----------------------------------------------
// Fonctions romain <=> entier
/*-----------------------------------------------
/ Ensemble de fonctions qui permettent de conver-
/ tir des entiers en écriture romaine et inverse-
/ ment et de faire des opérations. 
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

// Convertit un nombre romain en entier.
function vers_entier(ch) {
    const double = {
        "CM": 900, "CD": 400, "XC": 90, "XL": 40,
        "IX": 9, "IV": 4 
    };
    const unique = { 
        "M": 1000, "D": 500, "C": 100, "L": 50,
        "X": 10, "V": 5, "I": 1 
    };
    
    let entier = 0;
    let i = 0;
    
    while (i < ch.length) {
        if (i < ch.length - 1 &&
            ch.substring(i, i + 2) in double) {
            entier += double[ch.substring(i, i + 2)];
            i += 2;
        } else {
            entier += unique[ch[i]];
            i += 1;
        }
    }
    return String(entier);
}


// Convertit une entier en nombre romain.
function vers_romain(nombre) {
    const int_rom = [
        [1000, "M"], [900, "CM"], [500,  "D"],
        [400, "CD"], [100,  "C"], [ 90, "XC"],
        [ 50,  "L"], [ 40, "XL"], [ 10,  "X"],
        [  9, "IX"], [  5,  "V"], [  4, "IV"],
        [  1,  "I"]
    ];
    
    let romain = [];
    for (const [i, num] of int_rom) {
        while (nombre >= i) {
            nombre -= i;
            romain.push(num);
        }
    }
    return romain.join("");
}

// Retourne le resultat de l'operation entre deux
// nombres romains : ce dernier ne doit pas être
// plus petit que 0.
function romain_op(str1, str2, op,nombre=false) {
    const ops = {
        "+": (a, b) => a + b,
        "-": (a, b) => a - b,
        "*": (a, b) => a * b,
        "/": (a, b) => Math.floor(a / b)
    };
    const nombre1 = parseInt(vers_entier(str1));
    const nombre2 = parseInt(vers_entier(str2));
    let resultat = ops[op](nombre1, nombre2);
    if (nombre) {
        resultat = vers_romain(resultat);
    }
    return resultat;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

const rom_1 = "XVII";
const rom_2 = "IX";
const nombre3 = 562;

// Conversion des rom_s en nombres entiers.
const nombre1 = vers_entier(rom_1);
const nombre2 = vers_entier(rom_2);
const rom_3 = vers_romain(nombre3);

// Application de l'operation.
const res = romain_op(rom_1, rom_2, "+", true);

// Affichage des resultats
console.log(`1) ${rom_1} est egal ${nombre1}`);
console.log(`2) ${rom_2} est egal ${nombre2}`);
console.log(`3) ${nombre3} est egal ${rom_3}`);
console.log(`4) ${rom_1} + ${rom_2} = ${res}`);


//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !


/* En reflexion d'une solution efficace... */



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Proche de la version raccourcie, mais avec des
/ commentaires concis pour expliquer les etapes
/ principales de la fonction. */


// Convertit un nombre romain en entier.
function vers_entier_commentee(chaine) {
    
    // Créer un dictionnaire de valeurs doubles.
    const double={"CM": 900, "CD": 400, "XC": 90,
              "XL": 40, "IX": 9, "IV": 4};
    
    // Créer un dictionnaire de valeurs uniques.
    const unique ={"M": 1000, "D": 500, "C": 100,
              "L": 50, "X": 10, "V": 5, "I": 1};

    // Initialiser une variable entier à 0.
    let entier = 0;
    
    // Initialiser l'index à 0.
    let i = 0;
    
    // Boucler pour parcourir la chaîne.
    while (i < chaine.length) {
        
        // Vérifier si un double caractère existe
        // dans le dictionnaire des doubles.
        if (i < chaine.length - 1 &&
            chaine.substring(i, i+2) in double) {
            
            // Ajouter la valeur correspondante.
            entier += double[chaine.substring(i,
                i + 2)];
            
            // Avancer de deux caractères.
            i += 2;
            
        } else {
            // Ajouter la valeur à l'entier.
            entier += unique[chaine[i]];
            
            // Avancer d'un caractère.
            i += 1;
        }
    }
    
    // Retourner le nombre entier converti.
    return String(entier);
}


// Convertit une entier en nombre romain.
function vers_romain_commentee(nombre) {
    // Lister des entiers et valeurs romaines.
    const int_rom = [
        [1000, "M"], [900, "CM"], [500,  "D"],
        [400, "CD"], [100,  "C"], [ 90, "XC"],
        [ 50,  "L"], [ 40, "XL"], [ 10,  "X"],
        [  9, "IX"], [  5,  "V"], [  4, "IV"],
        [  1,  "I"]
    ];

    // Lister pour stocker les nombres romains.
    let romain = [];
    
    // Boucler sur chaque valeur entière et son
    // caractère correspondant romain.
    for (const [i, num] of int_rom) {
        
        // Tant que nombre est supérieur ou égal
        // à la valeur entière.
        while (nombre >= i) {
            
            // Soustraire la valeur entière.
            nombre -= i;
            
            // Ajouter le caractère romain.
            romain.push(num);
        }
    }
    
    // Retourner la chaîne de caractères formée
    // des caractères romains.
    return romain.join("");
}


// Retourne le resultat de l'operation entre deux
// nombres romains.
function romain_op_commentee(
    str1, str2, op, nombre=false
    ) {
    
    // Créer un dictionnaire des opérations.
    const ops = {
        "+": (a, b) => a + b,
        "-": (a, b) => a - b,
        "*": (a, b) => a * b,
        "/": (a, b) => Math.floor(a / b)
    };
    
    // Convertir les nombres romains en entiers.
    const nombre1 = parseInt(vers_entier(str1));
    const nombre2 = parseInt(vers_entier(str2));
    
    // Effectuer l'opération sur les 2 entiers.
    let resultat = ops[op](nombre1, nombre2);
    
    // Si demandé,
    if (nombre) {
        
        // Convertir le résultat en romain.
        resultat = vers_romain(resultat);
    }
    
    // Retourner le résultat de l'opération.
    return resultat;
}









//