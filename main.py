from show_menu import Menu

def main():
    card_number = 1
    users = []
    games = []
    tournaments = []
    movements = []
    while True:
        Menu.show_menu()
        new_id_check = Menu.check_input(card_number,users, games, tournaments, movements)
        if new_id_check == True:
            card_number += 1
        print(users)
        print(games)
        print(tournaments)
        print(movements)


















if __name__ == "__main__":
    main()