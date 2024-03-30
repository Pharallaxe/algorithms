# Calculer la moyenne arithmétique

### Enoncé
Il s'agit d'écrire une fonction qui réaliser la moyenne arithmétique. Il existe plusieurs moyennes : celle-ci est couramment utilisée pour connaitre sa moyenne trimestrielle par exemple.

### Etapes
* Récupérer le nombre de termes.
* Effectuer la somme des termes.
* Diviser la somme par le nombre de termes.
* Retourner la moyenne arithmétique.

### Pseudocode
```pseudocode
fonction calculer_moyenne_arithmetique(liste_a_etudier)
    longueur_liste <- longueur de liste_a_etudier
    
    somme <- 0
    
    pour chaque nombre_etudie dans liste_a_etudier
        somme <- somme + nombre_etudie
    fin pour
    
    moyenne_arithmetique <- (1 / longueur_liste) * somme
    
    retourner moyenne_arithmetique
fin fonction
```


### Exemples d'utilisation

Cet exemple va afficher
* La moyenne arithmétique est : 12.33


En Python

```python
liste = [12, 14, 16, 8, 6, 18]
moyenne = arithmetique(liste)
print("La moyenne est", round(moyenne, 2))
```


En Javascript

```javascript
let tableau = [12, 14, 16, 8, 6, 18];
let moyenne = arithmetique(tableau);
moyenne = moyenne.toFixed(2)
console.log("La moyenne est", moyenne);
```


En Java

```java
public static void main(String[] args) {
    int[] tableau = { 12, 14, 16, 8, 6, 18 };
    double moyenne = arithmetique(tableau);
    System.out.println("La moyenne est  " +
        String.format("%.2f", moyenne));
}
```


En PHP

```PHP
<?php
$tableau = [12, 14, 16, 8, 6, 18];
$moyenne = arithmetique($tableau);
echo "La moyenne est " . round($moyenne, 2);
?>
```