import random

win = 0
draw = 0
loss = 0

def play_game():
    global win, draw, loss
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()[0]
        if user_choice not in ["r", "p", "s", "q"]:
            print("Invalid choice. Please try again.")
            continue
        if user_choice == "q":
            break
        else:
            print(f"You chose {user_choice}.")

        computer_choice = random.choice(["r", "p", "s"])
        print(f"Computer chose {computer_choice}.")
        
        if user_choice == computer_choice:
            draw += 1
            print("It's a draw!")
        elif (user_choice == "r" and computer_choice == "s") or \
             (user_choice == "p" and computer_choice == "r") or \
             (user_choice == "s" and computer_choice == "p"):
            win += 1
            print("You win!")
        else:
            loss += 1
            print("You lose!")


print("Welcome to Rock, Paper, Scissors! ", end="")
response = input("Do you wish to play the game? (Y/N): ").lower()[0]

if response == "y":
    print("Great! Let's play!")
    play_game()
elif response == "n":
    print("Okay, maybe next time!")
else:
    print("Invalid input. Exiting the game.")
    exit(1)

print(f"Final Score: Wins: {win}, Draws: {draw}, Losses: {loss}")