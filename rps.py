import random

def play_rps(choice):
    # 0 is rock
    # 1 is paper
    # 2 is scissors

    # calc computer choice
    computer_choice = random.randint(0,2)
    # compare computer choice vs user choice
    # determine win, lose or draw
    if computer_choice == choice:
        return "Draw"
    if computer_choice == 0:
        if choice == 1:
            return "You Win"
        elif choice == 2:
            return "You Lose"
    if computer_choice == 1:
        if choice == 0:
            return "You Lose"
        elif choice == 2:
            return "You Win"
    if computer_choice == 2:
        if choice == 0:
            return "You Win"
        elif choice == 1:
            return "You Lose"
    # return result


print(play_rps(2))