from locust import HttpUser, task, between
import random

class GudliftUser(HttpUser):
    # Temps d'attente entre 1 et 5 secondes entre chaque tâche, pour simuler un utilisateur réaliste
    wait_time = between(1, 5)

    # Clubs et compétitions disponibles
    clubs = [ "Simply Lift", "Iron Temple", "She Lifts", "Muscle League", "Power Pushers"]
    competitions = ["Spring Festival", "Fall Classic", "Winter Games", "Summer Bash", "Strength Showdown"]

    @task
    def load_points_board(self):
        # Récupérer la page des points disponibles
        self.client.get("/pointBoard")

    @task
    def load_competitions(self):
        # Charger les compétitions après connexion
        self.client.post("/showSummary", data={"email":"john@simplylift.co"})

    @task
    def book_places(self):
        # Choisir une compétition et un club au hasard
        competition = random.choice(self.competitions)
        club = random.choice(self.clubs)
        places = str(random.randint(1, 18))  # Random entre 1 et 18 places

        # Effectuer la réservation
        response = self.client.post("/purchasePlaces", data={
            "competition": competition,
            "club": club,
            "places": places
        })

        # Vérification d'un succès ou d'une erreur
        if "Successfully booked" in response.text:
            print(f"Successfully booked {places} places for {competition} by {club}")
        elif "You don't have enough points" in response.text:
            print(f"{club} tried to book {places} places but doesn't have enough points")
        elif "This competition has already taken place" in response.text:
            print(f"Attempt to book {places} places for past competition: {competition}")
        else:
            print(f"Booking failed for {club} in {competition}")





