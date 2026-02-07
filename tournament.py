class Tournament:
    def __init__(self, tournament_name, tournament_day, tournament_month, tournament_year, max_players, chosen_game):
        self.name = tournament_name
        self.day = tournament_day
        self.month = tournament_month
        self.year = tournament_year
        self.max_players = max_players
        self.players = []
        self.game = chosen_game

    def __repr__(self):
        return f"Nome torneo: {self.name}, Data inizio: {self.day}/{self.month}/{self.year}, Massimo di giocatori: {self.max_players} \nPartecipanti: {self.players}, Gioco: {self.game}"




def torunament_data(games):
    print("Adesso dovrai inserire i dati del torneo: ")
    tournament_name = input("Inserisci il nome del torneo: ")
    while True:
        tournament_day = input("Inserisci il giorno del torneo: ")
        try:
            tournament_day = int(tournament_day)
            print("Dato valido!")
            break
        except ValueError:
            print("Dato non valido!")
            continue
    while True:
        tournament_month = input("Inserisci il mese del torneo: ")
        if tournament_month.isalpha():
            print("Dato valido!")
            break
        else:
            print("Dato non valido!")
            continue
    while True:
        tournament_year = input("Inserisci il l'anno del torneo: ")
        try:
            tournament_year = int(tournament_year)
            print("Dato valido!")
            break
        except ValueError:
            print("Dato non valido!")
            continue

    while True:
        max_players = input("Inserisci il numero massimo di partecipanti: ")
        try:
            max_players = int(max_players)
            print("Dato valido!")
            break
        except ValueError:
            print("Dato non valido!")
            continue
    while True:
        for i,game in enumerate(games, start=1):
            print(f"{i}) {game}")
        print()
        choice = input("Inserisci il gioco del torneo inserendo il numero corrispondente: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Dato non valido!")
            continue
        if choice >= 1 and choice <= len(games):
            print(f"Il gioco del torneo sarà {games[choice - 1]}")
            chosen_game = games[choice - 1]
            break
        else:
            print("Dato non valido!")
            continue
    tournament = Tournament(tournament_name, tournament_day, tournament_month, tournament_year, max_players, chosen_game)
    return tournament

def add_players(users, tournaments):
    while True:
        print("Fornisci i dati per iscrivere un partecipante!")
        while True:
            user_id = input("Inserisci il numero di tessera del partecipante: ")
            try:
                user_id = int(user_id)
            except ValueError:
                print("Dato non valido!")
                continue
            for user in users:
                if user_id == user.id:
                    player = user
                    print(f"Utente trovato {player}")
                    break
                else:
                    player = False
            if player == False:
                print("Utente non trovato!")
                continue
            break
        
        while True:
            print("Ecco i tornei disponibili:")
            for i,tournament in enumerate(tournaments, start=1):
                print(f"{i}) Torneo di: {tournament.game}")
            chosen_game = input("Inserisci il numero corrispondente al torneo: ")
            try:
                chosen_game = int(chosen_game)
            except ValueError:
                print("Dato non valido!")
                continue
            if chosen_game >= 1 and chosen_game <= len(tournaments):
                selected_tournament = tournaments[chosen_game - 1]
                chosen_game = tournaments[chosen_game - 1].game
                print(f"Hai scelto il torneo di {chosen_game.title}")
            else:
                print("Dato non valido!")
                continue
            if len(player.purchases) == 0:
                print("Non possiedi nessun gioco!")
                return
            for game in player.purchases:
                if (game.purchase).title == chosen_game.title:
                    acquired = True
                else:
                    acquired = False
            if acquired == True:
                if len(selected_tournament.players) >= selected_tournament.max_players:
                    print("Il torneo è già al completo!")
                    return
                else:
                    selected_tournament.players.append(player)
                print("Sei stato iscritto al torneo con successo!")
            else:
                print("Non puoi iscriverti al torneo se non possiedi il gioco!")
            break
        break
    