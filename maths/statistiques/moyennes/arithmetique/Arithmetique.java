//-----------------------------------------------
// arithmetique 
/*-----------------------------------------------
/ Permet de realiser une moyenne a partir d'une 
/ liste de plusieurs valeurs.
/----------------------------------------------*/

// A NE PAS OUBLIER!
import java.util.Arrays;


public class Arithmetique {

//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contexte
// de la fonction et sa logique.

public static double arithmetique(
        int[] tableau) {

    int somme = Arrays.stream(tableau).sum();

    return somme / (tableau.length * 1.0);
}



//-----------------------------------------------
// Application
//-----------------------------------------------
public static void main(String[] args) {
    int[] tableau = { 12, 14, 16, 8, 6, 18 };
    double moyenne = arithmetique(tableau);
    System.out.println("La moyenne est  " +
        String.format("%.2f", moyenne));
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !

public static double A(int[] t) {
    return Arrays.stream(t).average().orElse(0);
}



//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

public static double arithmetique_detaillee(
        int[] tableau) {

    int nbr_valeurs = tableau.length;
    int somme = 0;

    for (int i = 0; i < nbr_valeurs; i++) {
        int valeur = tableau[i];
        somme += valeur;
    }

    double moyenne = somme / (nbr_valeurs * 1.0);

    return moyenne;
}



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */


public static double arithmetique_commentee(
        int[] tableau) {

    // Recuperer la longueur du tableau.
    int nbr_valeurs = tableau.length;

    // Initialiser un int nommé "somme" a 0.
    int somme = 0;

    // De 0 a la longueur du tableau,
    for (int i = 0; i < nbr_valeurs; i++) {
        
        // Récupérer la valeur à l'index i.
        int valeur = tableau[i];

        // Ajouter ce nombre a la somme.        
        somme += valeur;
    }

    // Diviser la somme par la nombre de valeurs
    // en s'assurant de renvoyer un double en
    // faisant "* 1.0".
    double moyenne = somme / (nbr_valeurs * 1.0);

    // Retourner la moyenne calculee.
    return moyenne;
}
}









//