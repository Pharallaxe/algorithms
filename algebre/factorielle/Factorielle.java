// -----------------------------------------------
// Fonction factorielle
// -----------------------------------------------
// Calcul du produit des entiers de 1 a n, où n un
// entier positif est passe en argument.
// -----------------------------------------------

public class Factorielle {

// -----------------------------------------------
// Version courte
// -----------------------------------------------

public static int factorielle(int nombre) {
    int produit = 1;
    
    for (int i = 1; i <= nombre; i++) {
        produit *= i;
    }
    
    return produit;
}

//-----------------------------------------------
// Application
//-----------------------------------------------

public static void main(String[] args) {

    int res = factorielle(6);
    System.out.print("La factorielle de 6");
    System.out.println("est " + res);
}

// -----------------------------------------------
// Version golf
// -----------------------------------------------

public static int F(int n){
int p=1;for(int i=1;i<=n;i++)p*=i;return p;}

//-----------------------------------------------
// Version commentee
//-----------------------------------------------

public static int factorielle_commentee(
    int nombre) {

    // Initialiser le produit a 1
    int produit = 1;
    
    // De 1 a nombre,
    for (int i = 1; i <= nombre; i++) {

        // multiplier par le nombre courant.
        produit *= i;
    
    }
    
    // Retourner la factorielle calculee.
    return produit;
}
}









//