# Calculer une factorielle

### Enoncé
Cette fonction calcule la factorielle d'un nombre donné.

### Etapes
* Initialiser le produit à 1.
* Calculer la factorielle en multipliant jusqu'au nombre donné.
* Retourner la factorielle calculée.

Note si le nombre est 0 ou 1; la valeur renvoyée sera 1.

### Pseudocode
```pseudode
Fonction factorielle (n)
    r <- 1
    Pour i de 1 jusqu'à n avec un pas de 1
        r <- r * i
    Fin pour
    Retourner r
Fin Fonction
```


### Exemples d'utilisation

Cet exemple va afficher
* "La factorielle de 6 est : 720"

En Python


```python
resultat = factorielle(6) 
print(f"La factorielle de 6 est : "{resultat})
```

En Javascript


```javascript
let resultat = factorielle(6)
console.log("La factorielle de 6 est :", resultat)
```

En Java


```java
public class Main {
    // Insérer ici la fonction factorielle

    public static void main(String[] args) {
        int resultat = factorielle(6);
        System.out.println("La factorielle de 6 est : " + resultat);
    }
}
```

En PHP

```PHP
<?php
$resultat = factorielle(6);
echo "La factorielle de 6 est : " . $resultat;
?>
```