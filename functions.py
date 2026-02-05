class Function:
    def search_game(games):
        searching = input("Scrivi il titolo del gioco: ")
        searched = []
        for game in games:
            if searching.lower() in game.title.lower():
                searched.append(game)
        if len(searched) > 0:
            print("Sono stati trovati i seguenti giochi :", searched)
            return searched
        else:
            print("Nessun risultato corrispondente alla ricerca!")
            return False
    def available_games(games):
        for game in games:
            if game.quantity == 0:
                continue
            print(f"- {game} Disponibili: {game.quantity}")
            print()