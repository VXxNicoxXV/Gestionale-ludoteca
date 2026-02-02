class Tournament:
    def __init__(self, tournament_name, tournament_day, tournament_month, tournament_year, max_players):
        self.name = tournament_name
        self.day = tournament_day
        self.month = tournament_month
        self.year = tournament_year
        self.max_players = max_players
        self.players = []

    def __repr__(self):
        return f"Nome torneo: {self.name}, Data inizio: {self.day}/{self.month}/{self.year}, Massimo di giocatori: {self.max_players} \nPartecipanti: {self.players}"




def torunament_data():
    print("Adesso dovrai inserire i dati del torneo: ")
    tournament_name = input("Inserisci il nome del torneo: ")
    while True:
        tournament_day = input("Inserisci il giorno del torneo: ")
        if tournament_day.isdigit():
            print("Dato valido!")
            break
        else:
            print("Dato non valido!")
            continue
    while True:
        tournament_month = input("Inserisci il giorno del torneo: ")
        if tournament_month.isalpha():
            print("Dato valido!")
            break
        else:
            print("Dato non valido!")
            continue
    while True:
        tournament_year = input("Inserisci il giorno del torneo: ")
        if tournament_year.isdigit():
            print("Dato valido!")
            break
        else:
            print("Dato non valido!")
            continue

    while True:
        max_players = input("Inserisci il numero massimo di partecipanti: ")
        if max_players.isdigit():
            print("Dato valido!")
            break
        else:
            print("Dato non valido!")
            continue
    tournament = Tournament(tournament_name, tournament_day, tournament_month, tournament_year, max_players)
    return tournament


    