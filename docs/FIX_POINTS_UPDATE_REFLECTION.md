# Documentation : Fixation anticipée du bug "Points Update Not Reflected"

## Contexte

Le bug "Points update not reflected" devait être corrigé dans l'issue dédiée, mais a été résolu par anticipation lors de la résolution de l'issue `bug/points-exceeding-limit`.

## Issue corrigée : "Points Update Not Reflected"

Le problème initial était que les points d'un club ne se mettaient pas à jour après une réservation de places. Les utilisateurs ne pouvaient pas voir le décompte des points après la réservation, ce qui créait de la confusion.

## Fixation anticipée lors de l'issue `bug/points-exceeding-limit`

### Résumé des modifications apportées

Lors de la résolution du bug `bug/points-exceeding-limit`, la mise à jour des points a été implémentée correctement dans la fonction `purchasePlaces`, avec la validation des points et la mise à jour des données après la réservation.

Les points sont mis à jour avec la logique suivante :

```python
club['points'] = str(club_points - placesRequested)
competition['numberOfPlaces'] = str(available_places - placesRequested)
```

### Modification dans le fichier welcome.html

Pour que la mise à jour des points soit bien reflétée dans l'interface utilisateur, la valeur mise à jour des points est renvoyée dans le fichier welcome.html après chaque réservation.

La balise suivante a été ajoutée dans le fichier welcome.html pour afficher correctement les points restants d'un club après la réservation :

```html
<!-- Reste du contenu des compétitions -->
<h3>Points available: {{club['points']}}</h3>
```
Cette ligne assure que les points disponibles pour le club sont correctement mis à jour et affichés chaque fois que la page welcome.html est rendue après une réservation réussie.



### Test automatique pour vérifier la mise à jour des points

Un test unitaire a été ajouté pour vérifier que la mise à jour des points se fait correctement après chaque réservation. Voici un extrait de ce test :

```python
def test_points_update_after_booking(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Winter Games',
        'club': 'Simply Lift',
        'places': '5'
    }, follow_redirects=True)

    assert b"Points available: 8" in response.data  # 13 - 5 = 8
    assert b"Successfully booked 5 places for Winter Games!" in response.data
```

## Conclusion

La correction du bug "Points Update Not Reflected" a donc été effectuée lors de l'issue `bug/points-exceeding-limit`. Les points sont désormais correctement mis à jour et affichés après chaque réservation, et des tests unitaires ont été ajoutés pour garantir que le comportement est conforme aux attentes.