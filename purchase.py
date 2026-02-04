from functions import Function

class Purchase:
    def __init__(self):
        pass





def purchasing(games):
    counter = 0
    print("Quale gioco vuoi acquistare?")
    while True:
        searched = Function.search_game(games)
        if searched == False:
            continue
        elif searched == 1:
            pass
        else:
            for game in searched:
                counter += 1
                print(f"{counter}) {game}")
            counter = 0
        
        while True:
            choise = int(input("Inserisci il numero del gioco che vuoi acquistare: "))
            if choise > len(searched) or choise < len(searched):
                print("Non va bene!")
                for game in searched:
                    counter += 1
                    print(f"{counter}) {game}")
                counter = 0
                continue
            else:
                print("SIIIIII!", searched(choise - 1))
                break
