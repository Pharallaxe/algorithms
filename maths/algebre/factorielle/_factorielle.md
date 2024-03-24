# Calculer une factorielle

Cette fonction calcule la factorielle d'un nombre donné.

### Etapes :
* Initialiser le produit à 1.
* Calculer la factorielle en multipliant jusqu'au nombre donné.
* Retourner la factorielle calculée.

Note si le nombre est 0 ou 1; la valeur renvoyée sera 1.

### Pseudocode :
```pseudode
Fonction factorielle (n)
    r <- 1
    Pour i de 1 jusqu'à n avec un pas de 1
        r <- r * i
    Fin pour
    Retourner r
Fin Fonction
```


### Exemples d'utilisation :

En Python :

```python
resultat = calculer_factorielle(6) 
print(f"La factorielle de 6 est : "{resultat})
# Affiche "La factorielle de 6 est : 720
```

En Javascript

```javascript
let resultat = calculer_factorielle(6)
console.log("La factorielle de 6 est :", resultat)
// Affiche "La factorielle de 6 est : 720
```

En Java

```java
public class Main {
    // Insérer ici la fonction calculer_factorielle

    public static void main(String[] args) {
        int resultat = calculer_factorielle(6);
        System.out.println("La factorielle de 6 est : " + resultat);
        // Affiche "La factorielle de 6 est : 720
    }
}
```

En PHP

```PHP
<?php
$resultat = calculer_factorielle(6);
echo "La factorielle de 6 est : " . $resultat;
// Affiche "La factorielle de 6 est : 720
?>
```