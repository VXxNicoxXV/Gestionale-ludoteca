from new_user import user_data
from new_game import game_data

class Menu:
    def show_menu():
        print("Inserisci la tua scelta: ")
        print("1) Registra cliente")
        print("2) Aggiungi un gioco al catalogo")
        print("3) Vendi un gico")
        print("4) Cerca un gioco")
        print("5) Visualizza giochi disponibili")
        print("6) Crea torneo")
        print("7) Iscrivi un utente al torneo")
        print("8) Visualizza partecipanti di un torneo")
        print("9) Visualizza punti fedeltà")

    def check_input(card_number, users, games):
        choose = input("Inserisci la tua scelta: ")
        match choose:
            case "1":
                new_user = user_data(card_number)
                users.append(new_user)
                return True
            case "2":
                new_game = game_data()
                games.append(new_game)
            case _:
                print("mah")