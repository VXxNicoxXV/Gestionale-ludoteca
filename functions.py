class Function:
    def search_game(games):
        searching = input("Scrivi il titolo del gioco: ")
        searched = []
        for game in games:
            if searching.lower() in game.title.lower():
                searched.append(game)
        if len(searched) == 0:
            print("Sono stati trovati i seguenti giochi :", searched)
        else:
            print("Nessun risultato corrispondente alla ricerca!")