from tkinter import *
import random
root = Tk()
root.title("Play Rock Paper Scissors!")

def play_rps(choice):
    # 0 is rock, 1 is paper, 2 is scissors

    # clear display
    display.delete(0, END)
    
    # answer to return
    answer = ""
    # calc computer choice
    computer_choice = random.randint(0,2)
    # compare computer choice vs user choice
    # determine win, lose or draw
    if computer_choice == choice:
        answer = "Draw"
    if computer_choice == 0:
        if choice == 1:
            answer = "You Win"
        elif choice == 2:
            answer = "You Lose"
    if computer_choice == 1:
        if choice == 0:
            answer = "You Lose"
        elif choice == 2:
            answer = "You Win"
    if computer_choice == 2:
        if choice == 0:
            answer = "You Win"
        elif choice == 1:
            answer = "You Lose"
    
    display.insert(0, answer)

# Entry field to display result
display = Entry(root, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=3)

# Button for RPS choices
rock = Button(root, text="Rock", command=lambda: play_rps(0))
rock.grid(row=1, column=0)
paper = Button(root, text="Paper", command=lambda: play_rps(1))
paper.grid(row=1, column=1)
scissors = Button(root, text="Scissors", command=lambda: play_rps(2))
scissors.grid(row=1, column=2)

root.mainloop()