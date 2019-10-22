# TP1 - Classification binaire : légitime / malicieux
© Tanguy Bridou & Valentin Urcun

Ce projet permet de détecter si un élément du jeu de données correspond à un logiciel légitime ou malicieux.

## Jeu de données
Fichier : antivirus_dataset.csv
Jeu de 30000 éléments composés du nom du software et d'un ensemble de métadonnées associées à ce dernier.

## Algorithmes utilisés et résultats

Nous avons comparé les résultats de trois algorithmes :
* **k plus proches voisins**
    * Précision : 0.9863
    * Recall : 0.9806
* **régression logique**
    * Précision : 0.3070
    * Recall : 0.9999
* **arbre décisionnel**
    * Précision : 0.9924
    * Recall : 0.9885

## Lancer le programme

Vous devez au préalable avoir installé sur votre machine tous les éléments du fichier Requirements.txt.

Placez-vous ensuite à la racine du projet, et exécutez la commande suivante :

```sh
$ python TP1.py
```
