//-----------------------------------------------
// harmonique 
/*-----------------------------------------------
/ Permet de realiser une moyenne harmonique. Elle
/ permet d'etablir une moyenne plus significative
/ dans certains domaines, comme celui du calcul
/ des vitesses?

/ Cette moyenne de n nombres (x1, x2,..., xn) est
/ calculee en divisant le nomùbre de valeurs par
/ la somme des inverses de chaque valeur.

/                           N
/ Formule : MH = --------------------------
                 (1/x1 + 1/x2 + ... + 1/xn)

/----------------------------------------------*/

public class Harmonique {
    
//-----------------------------------------------
// Version courte
//-----------------------------------------------

public static double harmonique(int[] tableau) {

    double somme = 0;
    
    for (double valeur : tableau) {
        somme += 1 / valeur;
    }

    return tableau.length / somme;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

public static void main(String[]args) {
    int[] tableau = {50, 90};
    double moyenne = harmonique(tableau);
    System.out.println("La moyenne est : " +
        String.format("%.2f", moyenne));
}


//-----------------------------------------------
// Version golf
//-----------------------------------------------

public static double H(int[] T) {
   return T.length/java.util.Arrays.stream(T)
   .mapToDouble(n->1.0/n).sum();
}



//-----------------------------------------------
// Version detaillee
//-----------------------------------------------


public static double harmonique_detaillee(
        int[] tableau)
{

    int nbr_valeurs = tableau.length;
    double somme = 0;
    
    for (int i = 0; i < nbr_valeurs; i++) {
        int valeur = tableau[i];
        somme += 1.0 / valeur;
    }

    double res = nbr_valeurs / somme;

    return res;
}



//-----------------------------------------------
// Version commentee
//-----------------------------------------------


public static double harmonique_commentee(
        int[] tableau)
{
    // Identifier la longueur du tableau.
    int nbr_valeurs = tableau.length;

    // Initialiser un double nommé "somme" a 0.
    double somme = 0;
    
    // De 0 a la longueur de la tableau,
    for (int i = 0; i < nbr_valeurs; i++) {

        // Recuperer la valeur a l'index i.
        int valeur = tableau[i];

        // Ajouter l'inverse de cette valeur a la
        // somme.
        somme += 1.0 / valeur;
    }

    // Calculer la moyenne.
    double res = nbr_valeurs / somme;
    
    // Retourner la moyenne.
    return res;
}
}









//