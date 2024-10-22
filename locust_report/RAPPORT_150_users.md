Analyse du rapport Locust (150 utilisateurs)
# Aperçu

Ce rapport présente un test de performance effectué avec 150 utilisateurs sur un temps de montée en charge de 5 secondes. L’objectif du test était d’évaluer les temps de réponse du système sous une charge modérée pour trois types de requêtes :

- Accéder au tableau des points.
- Visualiser le résumé des compétitions (`/showSummary`).
- Réserver des places pour une compétition (`/purchasePlaces`).

## Principales métriques

| Type                  | # Requêtes | # Échecs | Moyenne (ms) | Min (ms) | Max (ms) | RPS   |
|-----------------------|------------|----------|--------------|----------|----------|-------|
| GET `/pointBoard`     | 4039       | 0        | 9.34         | 3        | 82       | 15.47 |
| POST `/purchasePlaces`| 4114       | 0        | 11.3         | 4        | 106      | 15.76 |
| POST `/showSummary`   | 4200       | 0        | 11.02        | 4        | 160      | 16.09 |
| **Total**             | **12353**  | **0**    | **10.56**    | **3**    | **160**  | **47.31** |

Aucun échec n’a été enregistré pendant le test, ce qui démontre la stabilité du système. Les temps de réponse moyens pour toutes les routes sont inférieurs à 11 ms, ce qui est bien en deçà des standards acceptables pour la plupart des applications web.

## Distribution des temps de réponse

| Méthode               | 50%ile (ms) | 80%ile (ms) | 90%ile (ms) | 99%ile (ms) | Max (ms) |
|-----------------------|-------------|-------------|-------------|-------------|----------|
| GET `/pointBoard`     | 7           | 12          | 18          | 36          | 82       |
| POST `/purchasePlaces`| 9           | 15          | 21          | 36          | 110      |
| POST `/showSummary`   | 8           | 15          | 20          | 39          | 160      |
| **Total**             | **8**       | **14**      | **20**      | **38**      | **160**  |

### GET `/pointBoard`

- 90 % des requêtes ont été traitées en 18 ms ou moins.
- Le temps de réponse maximum était de 82 ms, avec un 99e percentile à 36 ms.

### POST `/purchasePlaces`

- Le temps de réponse maximum pour cette action était de 110 ms, avec 90 % des requêtes traitées en 21 ms ou moins.
- 99 % des requêtes ont été complétées en 36 ms ou moins.

### POST `/showSummary`

- 90 % des requêtes ont été complétées en 20 ms, avec un temps maximum de 160 ms.
- Le temps médian pour cette route était de 8 ms, indiquant une bonne performance pour la majorité des utilisateurs.

## Comparaison avec les exigences

Selon les exigences du projet :

- **Récupérer une liste de compétitions ne doit pas prendre plus de 5 secondes.**
    - La route `/showSummary`, qui récupère les données des compétitions, avait un temps de réponse moyen de 11.02 ms, avec 99 % des requêtes traitées en 39 ms. Cela est largement inférieur à la limite de 5 secondes.

- **Mettre à jour le total de points ne doit pas prendre plus de 2 secondes.**
    - La route `/purchasePlaces`, qui met à jour les points, avait un temps de réponse moyen de 11.3 ms, avec 99 % des requêtes terminées en 36 ms. Cela est bien en dessous de la limite de 2 secondes.

## Performance du fichier `Locustfile.py`

Le script Locust charge dynamiquement les clubs et compétitions depuis des fichiers JSON et exécute trois tâches principales : visualiser le tableau des points, voir le résumé des compétitions et réserver des places. D'après les résultats du test :

- La tâche réservation de places a bien fonctionné avec 150 utilisateurs. Le temps de réponse moyen pour cette route étant de 11.3 ms, il n'y a pas d'indication de goulot d'étranglement pendant la réservation.
- Le tableau des points s’est chargé en moyenne en 9.34 ms, ce qui reflète la simplicité de cette route.
- La logique `random.choice()` dans le fichier Locustfile permet de tester différentes combinaisons de clubs et compétitions, simulant ainsi un comportement réaliste des utilisateurs.

## Conclusion

Le système a géré la charge de 150 utilisateurs de manière fluide, sans échec et avec des temps de réponse faibles. Les métriques de performance sont largement conformes aux exigences, démontrant que le système est bien optimisé pour la récupération des compétitions et la mise à jour des points. Pour des tests à plus grande échelle, il pourrait être intéressant d’augmenter encore la charge pour voir à quel moment la performance commence à se dégrader, mais pour l’instant, le système montre une excellente performance dans les conditions testées.