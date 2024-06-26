//-----------------------------------------------
// Fonctions anagramme
/*-----------------------------------------------
/ Identifie si deux chaines sont anagrammes, donc
/ si elles sont composées des mêmes lettres exac-
/ tement.
//----------------------------------------------*/

import java.util.Arrays;

public class Anagramme {

//-----------------------------------------------
// Version courte
//-----------------------------------------------

    public static boolean anagramme(
            String str1, String str2) {
        String strA = str1.toUpperCase();
        String strB = str2.toUpperCase();

        char[] sortedA = strA.toCharArray();
        char[] sortedB = strB.toCharArray();
        
        Arrays.sort(sortedA);
        Arrays.sort(sortedB);

        String sortedStrA = new String(sortedA);
        String sortedStrB = new String(sortedB);

        return sortedStrA.equals(sortedStrB);
    }

//-----------------------------------------------
// Application
//-----------------------------------------------

    public static void main(String[] args) {
        String str1 = "listen";
        String str2 = "silent";

        boolean est_ana = anagramme(str1, str2);
        String chaine = est_ana ? "sont" :
            "ne sont pas";

        System.out.print("Les chaînes ");
        System.out.print(chaine);
        System.out.println(" des anagrammes.");
    }



//-----------------------------------------------
// Version golf
//-----------------------------------------------

static boolean A(String s1,String s2){char[] a=s1.
toUpperCase().toCharArray(),b=s2.toUpperCase()
.toCharArray();java.util.Arrays.sort(a);java.util
.Arrays.sort(b);return new String(a).equals(new
String(b));}


//-----------------------------------------------
// Version commentee
//-----------------------------------------------

    public static boolean anagramme_explication(
            String str1,
            String str2) {

        // Convertir les chaînes en majuscules.
        String strA = str1.toUpperCase();
        String strB = str2.toUpperCase();

        // Convertir les chaînes en tableaux.
        char[] sortedA = strA.toCharArray();
        char[] sortedB = strB.toCharArray();

        // Trier les tableaux.
        Arrays.sort(sortedA);
        Arrays.sort(sortedB);

        // Créer de nouvelles chaînes
        String sortedStrA = new String(sortedA);
        String sortedStrB = new String(sortedB);

        // Vérifier l'équivalence des chaînes.
        return sortedStrA.equals(sortedStrB);
    }
}









//