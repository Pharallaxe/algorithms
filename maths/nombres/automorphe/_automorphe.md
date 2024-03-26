# Nombre automorphe

### Enoncé
Un nombre automorphe est un entier naturel dont
la suite des chiffres de son carré se termine par
celle du nombre lui-même.

### Etapes
* Récupérer la longueur du nombre donné.
* Elever le nombre à la puissance 2.
* Récupérer les derniers chiffres de ce carré.
* Comparer les chiffres du nombre donné et ceux
  de la puissance 2.

### Pseudocode

```pseudocode
fonction automorphe(nombre)
    longueur = longueur du nombre en chaine
    carré = nombre au carré
    carré_str <- convertir carré en chaîne de caractères
    carré_fin = extraire les derniers longueur chiffres de carré_str
    carré_fin_nombre = convertir carré_fin en entier
    retourner carré_fin_nombre == nombre
```

### Exemples d'utilisation

Cet exemple va afficher : 
* true (car 76² = 5776)


En Python

```python
print(automorphe(76))
```

En JavaScript

```javascript
console.log(automorphe(76));
```

