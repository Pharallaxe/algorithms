//-----------------------------------------------
// geometrique 
/*-----------------------------------------------
/ Permet de realiser une moyenne geometrique qui
/ est plus insensible aux valeurs elevees que la
/ moyenne arithmetique. Elle permet donc une es-
/ timation meilleure des tendances centrales.

/ Cette moyenne de n nombres (x1, x2,..., xn) est
/ calculée en multipliant tous les nombres ensem-
/ ble, puis en prenant la racine enième de ce mê-
/ me produit.

/ Formule : MG = (x1 * x2 * ... * xn) ** (1/n)

/----------------------------------------------*/


public class Geometrique {

//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

public static double geometrique(int[] tableau) {
    int longueur = tableau.length;
    int produit = 1;
    for (int i = 0; i < longueur; i++) {
        produit *= tableau[i];
    }

    return Math.pow(produit, (1.0 / longueur));
}



//-----------------------------------------------
// Application
//-----------------------------------------------

public static void main(String[]args) {
    int[] tableau = {12, 14, 16, 8, 6, 18};
    double moyenne = geometrique(tableau);
    System.out.println("La moyenne est : " +
        String.format("%.2f", moyenne));
}

//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

public static double G(int[] t) {
    return Math.pow(java.util.stream.IntStream.of
    (t).reduce(1,(a,b)->a*b),1.0/t.length);
}

//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

public static double geometrique_detaillee(int[]
    tableau)
{
    int nombre_valeurs = tableau.length;
    int produit = 1;

    for (int i = 0; i < nombre_valeurs; i++) {
        int valeur_courante = tableau[i];

        produit *= valeur_courante;
    }

    double coefficient = 1.0 / nombre_valeurs;
    double res = Math.pow(produit, coefficient);

    return res;
}



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */

public static double geometrique_commentee(int[]
    tableau)
{
    // Identifier la longueur du tableau.
    int nombre_valeurs = tableau.length;

    // Initialiser le produit à 1.
    int produit = 1;

    // De 0 à la longueur du tableau,
    for (int i = 0; i < nombre_valeurs; i++) {

        // récupérer la valeur exacte dans le ta-
        // bleau, et
        int valeur_courante = tableau[i];

        // multiplier produit par cette valeur.
        produit *= valeur_courante;
    }

    // Calculer le facteur de la racine.
    double enieme = 1.0 / nombre_valeurs;

    // Calculer la racine enière de ce produit.
    double res = Math.pow(produit, enieme);

    // Retourner le résultat.
    return res;
}
}









//