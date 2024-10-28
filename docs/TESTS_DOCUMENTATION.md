Documentation des Tests
# Structure des Dossiers de Tests

Les tests sont répartis dans les dossiers suivants :

- **Unit Tests (tests/unit/)**: Ces tests valident des unités de code isolées, comme des fonctions spécifiques, pour s'assurer qu'elles fonctionnent correctement indépendamment des autres fonctionnalités.
- **Integration Tests (tests/integration/)**: Ils valident l'interaction entre plusieurs composants de l'application pour vérifier qu'ils fonctionnent ensemble comme prévu.
- **Functional Tests (tests/functional/)**: Ces tests reproduisent les actions de l'utilisateur final sur l'application et simulent des scénarios réels pour valider le comportement global de l'application.

## Détails des Tests

### Functional Tests

#### Test de Tentative de Réservation avec Compétition Passée

- **Emplacement**: `tests/functional/test_booking_past_competitions_functional.py`
- **Justification**: Vérifie que le système empêche la réservation pour une compétition déjà passée, en affichant un message d’erreur approprié.
- **Description**: Ce test simule une réservation sur une compétition dont la date est dépassée. Le test s'assure que le message "This competition has already taken place. No reservations allowed." est affiché. Ce test est fonctionnel car il vérifie le comportement de bout en bout.

#### Test de Réservation avec Compétition en Cours

- **Emplacement**: `tests/functional/test_booking_past_competitions_functional.py`
- **Justification**: Vérifie que les réservations pour des compétitions futures fonctionnent correctement.
- **Description**: Simule une réservation pour une compétition à venir et s'assure que le message "Successfully booked" apparaît, indiquant une réservation réussie.

#### Test d'Email Inconnu

- **Emplacement**: `tests/functional/test_unknown_email_functional.py`
- **Justification**: Vérifie le système d'identification par email pour s'assurer que les emails non enregistrés sont rejetés.
- **Description**: Simule la connexion avec un email inconnu et vérifie que le message approprié est affiché.

#### Test de Point Board

- **Emplacement**: `tests/functional/test_point_board.py`
- **Justification**: Assure l’accessibilité et le bon affichage du tableau de bord des points.
- **Description**: Vérifie que la route `/pointBoard` retourne une réponse correcte, affichant les points des clubs.

#### Test de Déconnexion (Logout)

- **Emplacement**: `tests/functional/test_logout.py`
- **Justification**: Vérifie que la déconnexion d'un utilisateur fonctionne correctement et supprime la session.
- **Description**: Simule la déconnexion d'un utilisateur et s'assure que l'utilisateur est redirigé vers l'index, et que la session est correctement vidée.

### Integration Tests

#### Test de Limite de 12 Places par Compétition

- **Emplacement**: `tests/integration/test_limit_of_12_places_integration.py`
- **Justification**: Assure que la limite de 12 places par compétition est appliquée, même en cas de réservations fractionnées.
- **Description**: Vérifie que toute tentative de réservation au-delà de 12 places est rejetée avec le message "You cannot book more than 12 places per competition.". Il s'agit d'un test d'intégration, car il combine plusieurs validations (compétition, club, places demandées).

#### Test de Points Insuffisants pour Réserver

- **Emplacement**: `tests/integration/test_points_exceeding_limit_integration.py`
- **Justification**: Vérifie que le club ne peut réserver que le nombre de places correspondant à ses points disponibles.
- **Description**: Simule une tentative de réservation de places avec des points insuffisants. Vérifie que le message "You don't have enough points to complete this booking." est affiché.

#### Test de Réservation de Valeurs Négatives pour les Places Demandées

- **Emplacement**: `tests/integration/test_negative_places_requested.py`
- **Justification**: Vérifie que le système n'accepte pas des valeurs négatives pour les places demandées.
- **Description**: Tente de réserver une valeur négative pour les places, et s'assure que le message "Please enter a positive number of places." est affiché.

#### Test de Réservation de Valeurs Non Numériques pour les Places Demandées

- **Emplacement**: `tests/integration/test_non_numeric_places_requested.py`
- **Justification**: Assure que seules des valeurs numériques sont acceptées pour la réservation des places.
- **Description**: Tente de réserver une valeur non numérique pour les places et vérifie que le message "Invalid number of places. Please enter a valid positive number in the field." est affiché.

### Unit Tests

#### Test de Tentative de Réservation avec Compétition Passée (Unitaire)

- **Emplacement**: `tests/unit/test_booking_past_competitions.py`
- **Justification**: Vérifie qu'une compétition passée ne peut pas être réservée.
- **Description**: Teste la fonction responsable de valider les dates et s'assure qu'aucune réservation n'est autorisée pour une date passée.

#### Test de Limite de 12 Places

- **Emplacement**: `tests/unit/test_limit_of_12_places.py`
- **Justification**: Vérifie que la limite de 12 places est appliquée dans la fonction qui gère la réservation.
- **Description**: Teste uniquement la logique de la limite de 12 places sans interaction avec la base de données ou d'autres composants.

#### Test de Points Insuffisants (Unitaire)

- **Emplacement**: `tests/unit/test_points_exceeding_limit.py`
- **Justification**: Vérifie la logique qui calcule si un club a assez de points pour réserver.
- **Description**: Teste la fonctionnalité isolée pour vérifier si un club possède les points nécessaires.

#### Test de Mise à Jour des Points après Réservation

- **Emplacement**: `tests/unit/test_points_update_after_booking.py`
- **Justification**: Vérifie que les points du club sont correctement mis à jour après une réservation.
- **Description**: Assure que les points sont soustraits correctement après une réservation réussie.

#### Test d’Email Inconnu (Unitaire)

- **Emplacement**: `tests/unit/test_unknown_email.py`
- **Justification**: Vérifie que l’email fourni correspond bien à un utilisateur existant.
- **Description**: Simule une tentative de connexion avec un email inconnu pour s'assurer que l'application répond correctement.

## Conclusion

La couverture de tests atteint 100% du fichier `server.py`, garantissant que toutes les branches importantes et les conditions de code sont couvertes. Les tests sont organisés pour maximiser la clarté et séparer les tests de bas niveau (unitaires) des scénarios d'intégration et des tests fonctionnels complets. Ces tests permettent de s'assurer que toutes les fonctionnalités de l'application sont correctement validées et que les utilisateurs finaux auront une expérience conforme aux spécifications.