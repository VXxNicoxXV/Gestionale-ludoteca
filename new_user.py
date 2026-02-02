class User:
    def __init__(self, name, surname, card_number):
        self.name = name
        self.surname = surname
        self.id = card_number

    def __repr__(self):
        return f"Cliente {self.name} {self.surname}, id: {self.id}"





def user_data(card_number):
    while True:
        name = input("Inserisci il tuo nome: ")
        if name.isalpha():
            print("Dato valido!")
            break
        else:
            print("Dato non valido!")
            continue
    while True:
        surname = input("Inserisci il tuo cognome: ")
        if surname.isalpha():
            print("Dato valido!")
            break
        else:
            print("Dato non valido!")
            continue
    Customer = User(name, surname, card_number)
    return Customer
    

