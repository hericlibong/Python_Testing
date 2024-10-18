import json
from flask import Flask,render_template,request,redirect,flash,url_for, session
from datetime import datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = next((club for club in clubs if club['email'] == request.form['email']), None)
    if club:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        flash("The entered email is unknown. Please try again with a valid email.")
        return redirect(url_for('index'))


@app.route('/book/<competition>/<club>')
def book(competition, club):
    # reconstruire les urls pour les espaces
    competition = competition.replace('-', ' ')
    club = club.replace('-', ' ')
    
    foundClub = next((c for c in clubs if c['name'] == club), None)
    foundCompetition = next((c for c in competitions if c['name'] == competition), None)
    
    if not foundClub or not foundCompetition:
        flash("Club or competition not found.")
        return redirect(url_for('index'))
    
    # Vérification de la date de la compétition
    competition_date = datetime.strptime(foundCompetition['date'], "%Y-%m-%d %H:%M:%S")
    if competition_date < datetime.now():
        flash("This competition has already taken place. No reservations allowed.")
        return render_template('welcome.html', club=foundClub, competitions=competitions)
    
    # Si la date est valide, afficher la page de réservation
    return render_template('booking.html', club=foundClub, competition=foundCompetition)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition_name = request.form['competition']
    club_name = request.form['club']
    places_requested = int(request.form['places'])

    competition = next((c for c in competitions if c['name'] == competition_name), None)
    club = next((c for c in clubs if c['name'] == club_name), None)

    if not competition or not club:
        flash("An error occurred. Please try again.")
        return redirect(url_for('index'))

    # Vérification des places et des points disponibles
    club_points = int(club['points'])
    available_places = int(competition['numberOfPlaces'])
    
    if places_requested > club_points:
        flash("You don't have enough points to complete this booking.")
    elif places_requested > available_places:
        flash("Not enough places available for this competition.")
    elif places_requested > 12:
        flash("You cannot book more than 12 places per competition.")
    else:
        # Mise à jour si les conditions sont remplies
        club['points'] = str(club_points - places_requested)
        competition['numberOfPlaces'] = str(available_places - places_requested)
        flash(f'Successfully booked {places_requested} places for {competition_name}!')
    
    return render_template('welcome.html', club=club, competitions=competitions)







# TODO: Add route for points display


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
