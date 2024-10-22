# Analyse du Rapport de Performance Locust pour 75 Utilisateurs

## Rapport de Test de Performance

## Période du test
20/10/2024 04:52:29 - 20/10/2024 05:00:35

## Hôte ciblé
http://127.0.0.1:5000/

## Nombre d’utilisateurs simulés
75

## Ramp-up
5 utilisateurs/secondes

## Script utilisé
locustfile.py

## 1. Objectif du test
L’objectif de ce test était d’évaluer la performance de l’application avec 75 utilisateurs simultanés en s’assurant que :
- Le temps de récupération de la liste des compétitions ne dépasse pas 5 secondes.
- Le temps de mise à jour des points ne dépasse pas 2 secondes.

## 2. Statistiques globales
| Type  | Nom               | # Requêtes | # Fails | Moyenne (ms) | Min (ms) | Max (ms) | Taille moyenne (bytes) | RPS  | Échecs/s |
|-------|-------------------|------------|---------|--------------|----------|----------|------------------------|------|----------|
| GET   | //pointBoard      | 3938       | 0       | 8.38         | 3        | 131      | 1148.01                | 8.1  | 0        |
| POST  | //purchasePlaces  | 3988       | 0       | 9.54         | 4        | 105      | 1197.38                | 8.2  | 0        |
| POST  | //showSummary     | 4005       | 0       | 8.93         | 4        | 79       | 1049                   | 8.23 | 0        |
| Agrégé| Tous les Endpoints| 11931      | 0       | 8.95         | 3        | 131      | 1131.28                | 24.53| 0        |

### Interprétation
- Le nombre total de requêtes effectuées était de 11 931 pour l’ensemble des endpoints.
- Le temps moyen de réponse agrégé était de 8.95 ms, ce qui est bien inférieur aux exigences de performance.
- Aucune erreur (0 échec) n’a été relevée pendant le test, montrant la robustesse de l’application sous cette charge.
- Le RPS (Requests Per Second) total était de 24.53, ce qui montre que l’application a traité en moyenne près de 25 requêtes par seconde sans échec.

## 3. Statistiques spécifiques par endpoint
### a. GET /pointBoard (Tableau des points)
- Nombre de requêtes : 3938
- Temps moyen de réponse : 8.38 ms
- Min : 3 ms
- Max : 131 ms
- Le temps de réponse 50 %ile (médiane) est de 6 ms.
- Le temps maximum observé de 131 ms est largement en dessous des 5 secondes exigées pour la récupération des données.

### b. POST /purchasePlaces (Réservation de places)
- Nombre de requêtes : 3988
- Temps moyen de réponse : 9.54 ms
- Min : 4 ms
- Max : 105 ms
- Le temps maximum de 105 ms est très inférieur à l’exigence de 2 secondes pour la mise à jour des points, ce qui montre une très bonne optimisation.

### c. POST /showSummary (Résumé de la compétition)
- Nombre de requêtes : 4005
- Temps moyen de réponse : 8.93 ms
- Min : 4 ms
- Max : 79 ms
- Le temps moyen pour afficher la liste des compétitions est également très en dessous des 5 secondes exigées, même avec une charge de 75 utilisateurs simultanés.

## 4. Distribution des Temps de Réponse (Percentiles)
Les statistiques de percentile permettent de mieux comprendre les performances pour la majorité des utilisateurs.

| Endpoint            | 50%ile | 60%ile | 70%ile | 80%ile | 90%ile | 95%ile | 99%ile | 100%ile |
|---------------------|--------|--------|--------|--------|--------|--------|--------|---------|
| GET /pointBoard     | 6 ms   | 7 ms   | 9 ms   | 11 ms  | 14 ms  | 18 ms  | 33 ms  | 130 ms  |
| POST /purchasePlaces| 7 ms   | 9 ms   | 11 ms  | 13 ms  | 16 ms  | 21 ms  | 33 ms  | 110 ms  |
| POST /showSummary   | 7 ms   | 8 ms   | 10 ms  | 12 ms  | 15 ms  | 19 ms  | 31 ms  | 79 ms   |

Pour 99 % des requêtes, le temps de réponse pour toutes les routes était de moins de 110 ms.
Même dans les 100 % des cas les plus lents, aucun des endpoints n’a dépassé 130 ms, ce qui est très loin des 5 secondes exigées.

## 5. Analyse par rapport aux consignes
Les consignes indiquaient que le temps de récupération des compétitions devait être inférieur à 5 secondes et la mise à jour des points en moins de 2 secondes. Voici les résultats par rapport à ces attentes :
- **Affichage du tableau des points (GET /pointBoard)** : Le temps moyen de réponse est de 8.38 ms, bien inférieur à la limite de 5 secondes.
- **Réservation de places (POST /purchasePlaces)** : Le temps moyen de mise à jour est de 9.54 ms, très en dessous de la limite de 2 secondes.
- **Affichage des compétitions (POST /showSummary)** : Le temps moyen est de 8.93 ms, bien en dessous de l’exigence de 5 secondes.

## 6. Impact des données de test et du code (locustfile.py)
Le code de test simule des utilisateurs effectuant des actions réalistes telles que :
- Consulter le tableau des points.
- Réserver des places pour des compétitions avec des clubs choisis aléatoirement.
- Afficher la liste des compétitions.

Ces actions ont été bien réparties et représentent un bon scénario de test pour évaluer l’application sous charge. Le choix aléatoire des compétitions et des clubs permet également de simuler une utilisation variée de l’application.

## 7. Conclusion
Le test avec 75 utilisateurs a montré que l’application répond très bien sous une charge modérée. Les temps de réponse sont largement en dessous des limites fixées par les consignes de performance. L'application peut traiter les requêtes rapidement et sans erreur. Elle semble donc prête pour une utilisation plus intensive, avec la possibilité d’augmenter la charge pour de futurs tests.

### Recommandations
- **Poursuivre l’optimisation** : Bien que les résultats soient très satisfaisants, il peut être intéressant de pousser les tests à 100 ou 150 utilisateurs pour voir si l’application reste performante à grande échelle.
- **Documenter les résultats** : Intégrer ce rapport et ses conclusions dans la documentation du projet pour démontrer les performances de l’application.

Cette analyse pourrait être documentée dans un fichier `performance_report.md` dans la branche dédiée.