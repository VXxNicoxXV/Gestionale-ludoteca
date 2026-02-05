import datetime
from functions import Function

class Purchase:
    def __init__(self, customer, chosen_product):
        current_time = datetime.now()
        self.date = current_time.date()
        self.hour = current_time.time()
        self.customer = customer
        self.purchase = chosen_product

    def __repr__(self):
        return f"Cliente: {self.customer}\nAcquisto: {self.purchase}\nData: {self.date} alle ore {self.hour}"


def purchasing(games, users):
    while True:
        user_id = input("Inserisci il numero di tessera del cliente: ")
        try:
            user_id = int(user_id)
            print("Ricerca dell'utente...")
        except ValueError:
            print("Input non valido!")
            continue
        for user in users:
            if user.id == user_id:
                customer = user
                print(f"Utente trovato: {user}")
                break
            else:
                customer = False
        if customer == False:
            print("Utente inesistente!")
            continue
        else:
            break

    print("Quale gioco vuoi acquistare?")
    while True:
        searched = Function.search_game(games)
        for game in searched:
            if game.quantity == 0:
                
        if searched == False:
            continue
        else:
            print("Giochi trovati: ")
            print()
            for i, game in enumerate(searched, start = 1):
                print(f"{i}) {game}")
        break
        
    while True:
        choice = input("Inserisci il numero del gioco che vuoi acquistare: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Input non valido!")
            continue
        
        if choice < 1 or choice > len(searched):
            print("Selezione non valida!")
            for i, game in enumerate(searched, start = 1):
                print(f"{i}) {game}")
            continue
        else:
            chosen_product = searched[(choice - 1)]
            print("Riepilogo dell'ordine:")
            print(f"Cliente: {customer}")
            print(f"Gioco in acquisto: {chosen_product}")

        while True:
            confirmation = input("Scrivi 'SI' per confermare l'acquisto oppure 'NO' per annullare: ")
            match confirmation.lower():
                case "si":
                    purchased = Purchase(customer, chosen_product)
                    break
                case "no":
                    return "Acquisto annullato!"
                case "_":
                    print("Input non valido!")
                    continue
        break
        



