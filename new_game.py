class Game:
    def __init__(self, game_type, title, editor, price, players, average_game_time, quantity):
        self.game_type = game_type
        self.title = title
        self.editor = editor
        self.price = price
        self.players = players
        self.average_game_time = average_game_time
        self.quantity = quantity
    
    def __repr__(self):
        currency = "€"
        return f"\nTipo di gioco: {self.game_type} Nome: {self.title} di {self.editor[0]}({self.editor[1]}), Prezzo: {self.price}{currency}, \nGiocatori: da un minimo di {self.players[0]} ad un massimo di {self.players[1]}, \nDurata media della partita: {self.average_game_time}"

def game_data():
    editor = []
    players = []
    print("Adesso dovrai inserire i dati del gioco: ")
    while True:
        game_type = input("Inserisci il tipo di gioco (carte, dadi, tavolo): ")
        if game_type.lower() == "carte" or game_type.lower() == "dadi" or game_type.lower() == "tavolo":
            print("Dato valido!")
            break
        else:
            print("Dato non valido!")
            continue
    while True:
        title = input("Inserisci il nome del gioco: ")
        if title.isdigit():
            print("Dato non valido!")
            continue
        else:
            print("Dato valido!")
            break

    while True:
        name = input("Inserisci il nome dell'editore: ")
        if title.isdigit():
            print("Dato non valido!")
            continue
        else:
            print("Dato valido!")
            break
    while True:
        country = input("Inserisci il paese: ")
        if country.isdigit():
            print("Dato non valido!")
            continue
        else:
            print("Dato valido!")
            break
    editor.append(name)
    editor.append(country)
    while True:
        price = input("Inserisci il prezzo: ")
        try:
            price = float(price)
        except ValueError:
            print("Dato non valido!")
            continue
        print("Dato valido!")
        break
    while True:
        min_players = input("Inserisci il numero minimo di giocatori: ")
        try:
            min_players = int(min_players)
        except ValueError:
            print("Dato non valido!")
            continue
        print("Dato valido!")
        break
    while True:
        max_players = input("Inserisci il numero massimo di giocatori: ")
        try:
            max_players = int(max_players)
        except ValueError:
            print("Dato non valido!")
            continue
        print("Dato valido!")
        break
    players.append(min_players)
    players.append(max_players)
    while True:
        average_game_time = input("Inserisci la durata media di una parita (in minuti): ")
        if average_game_time.isdigit():
            print("Dato valido!")
            break
        else:
            print("Dato non valido!")
            continue
    while True:
        quantity = input("Inserisci la quantità disponibile: ")
        try:
            quantity = int(quantity)
        except ValueError:
            print("Dato non valido")
            continue
        print("Dato valido!")
        break
    game = Game(game_type, title, editor, price, players, average_game_time, quantity)
    return game
    

        

        
        
        