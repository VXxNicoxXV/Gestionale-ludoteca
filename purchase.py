import math
import datetime
from functions import Function

class Purchase:
    def __init__(self, customer, chosen_product):
        current_time = datetime.datetime.now()
        self.date = current_time.date()
        self.hour = current_time.time()
        self.customer = customer
        self.purchase = chosen_product

    def __repr__(self):
        return f"Cliente: {self.customer}\nAcquisto: {self.purchase}\nData: {self.date} alle ore {self.hour}"

def loyalty_points_add(customer, chosen_product):
    if chosen_product.price >= 10:
        points = float(chosen_product.price / 10)
        customer.loyalty_points += math.floor(points)
        return math.floor(points)
    else:
        return False


def purchasing(games, users, movements):
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
        not_available = []
        if searched == False:
            continue
        elif len(searched) >= 1:
            for game in searched[:]:
                if game.quantity == 0:
                    not_available.append(game)
                    searched.remove(game)
        print("Giochi non disponibili: ")
        print()
        for i, game in enumerate(not_available, start = 1):
            print(f"{i}) {game}")
        print()
        print("Giochi Disponibili: ")
        print()
        for i, game in enumerate(searched, start = 1):
            print(f"{i}) {game}")
        break
        
    while True:
        choice = input("Inserisci il numero del gioco che vuoi acquistare (tra i giochi disponibili): ")
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
                    movements.append(purchased)
                    customer.purchases.append(purchased)
                    chosen_product.quantity -= 1
                    points_check = loyalty_points_add(customer, chosen_product)
                    if points_check >= 1:
                        print(f"Sono stati aggiunti {points_check} al tuo account!")
                    print("Acquisto effettuato con successo!")
                    break
                case "no":
                    print("Acquisto annullato!")
                    return
                case "_":
                    print("Input non valido!")
                    continue
        break
        



