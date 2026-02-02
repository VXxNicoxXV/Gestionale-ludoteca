from show_menu import Menu

def main():
    card_number = 1
    users = []
    while True:
        Menu.show_menu()
        new_id_check = Menu.check_input(card_number,users)
        if new_id_check == True:
            card_number += 1
        print(users)


















if __name__ == "__main__":
    main()