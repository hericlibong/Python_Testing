from locust import HttpUser, task, between
import json
import random

class GudliftUser(HttpUser):
    # Temps d'attente entre 1 et 5 secondes entre chaque tâche
    wait_time = between(1, 5)

    # Charger les données des clubs disponibles (avec nom et email)
    with open('clubs.json', 'r') as clubs_file:
        clubs_data = json.load(clubs_file)
        clubs = [{"name": club['name'], "email": club['email']} for club in clubs_data['clubs']]

    # Charger les données des compétitions disponibles
    with open('competitions.json', 'r') as competitions_file:
        competitions_data = json.load(competitions_file)
        competitions = [competition['name'] for competition in competitions_data['competitions']]

    @task
    def load_points_board(self):
        # Récupérer la page des points disponibles
        self.client.get("/pointBoard")

    @task
    def load_competitions(self):
        # Sélectionner un club au hasard et utiliser son e-mail pour se connecter
        club = random.choice(self.clubs)
        self.client.post("/showSummary", data={"email": club["email"]})

    @task
    def book_places(self):
        # Choisir une compétition et un club au hasard
        competition = random.choice(self.competitions)
        club = random.choice(self.clubs)
        places = str(random.randint(1, 14))  

        # Effectuer la réservation
        response = self.client.post("/purchasePlaces", data={
            "competition": competition,
            "club": club["name"],
            "places": places
        })

        # Vérification d'un succès ou d'une erreur
        if "Successfully booked" in response.text:
            print(f"Successfully booked {places} places for {competition} by {club['name']}")
        elif "You don't have enough points" in response.text:
            print(f"{club['name']} tried to book {places} places but doesn't have enough points")
        elif "This competition has already taken place" in response.text:
            print(f"{club['name']} Attempt to book {places} places for past competition: {competition}")
            print ("Answer : 'This competition has already taken place. No reservations allowed'.")
        else:
            print(f"Booking failed for {club['name']} in {competition}")




