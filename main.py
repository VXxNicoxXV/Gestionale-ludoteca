from show_menu import Menu

def main():
    card_number = 1
    users = []
    games = []
    tournaments = []
    while True:
        Menu.show_menu()
        new_id_check = Menu.check_input(card_number,users, games, tournaments)
        if new_id_check == True:
            card_number += 1
        print(users)
        print(games)
        print(tournaments)


















if __name__ == "__main__":
    main()