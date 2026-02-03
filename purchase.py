from functions import Function

class Purchase:
    def __init__(self):
        pass





def purchasing(games):
    counter = 1
    print("Quale gioco vuoi acquistare?")
    while True:
        searched = Function.search_game(games)
        if searched == False:
            continue
        elif searched == 1:
            pass
        else:
            for game in searched:
                print(f"{counter}) {game}")
                counter += 1
            while True:
                choise = input("Inserisci il numero del gioco che vuoi acquistare: ")
                if choise > len(searched) or choise < len(searched):
                    print("va bene!")
                    break
                else:
                    print("nono!")
                    continue
