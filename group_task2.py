# Make a rock paper scissors app that you can play against computer

# The program should keep track of:

### Number of Rounds Played
### Number of Rounds Won by User
### Number of Round Won by Computer

# After each round, the program should display the results and ask if they want another round
# You should use functions, loops, conditionals, random number generation to achieve this

# random.randit() method for random number
# random.randint(1,4)

import random, sys

options = {1: "rock", 2: "paper", 3: "scissors"}

def rock_paper_scissors_game():

    global rounds_played # bad practice, but fixes logic
    global human_wins # bad practice, but fixes logic
    global computer_wins # bad practice, but fixes logic

    print(f"{options}\n")
    user_chosen = int(input("What do you wanna choose?"))
    print(f"The user has chosen: {options[user_chosen]}")

    computer_chosen = random.randint(1,3)
    print(f"The computer has chosen {options[computer_chosen]}")

    if user_chosen == 1:
        if computer_chosen == 3:
            human_wins += 1
            print("user")
        else:
            computer_chosen == 2
            computer_wins += 1
            print("computer")
        
    elif user_chosen == 2:
        if computer_chosen == 1:
            human_wins += 1
            print("user")
        else:
            computer_chosen == 3
            computer_wins += 1
            print("computer")

    elif user_chosen == 3:
        if computer_chosen == 2:
            human_wins += 1
            print("user")
        else: 
            computer_chosen == 1
            computer_wins += 1
            print("computer")

    else:
        user_chosen == computer_chosen
        print("draw")

rounds_played = 0
human_wins = 0
computer_wins = 0
while True:
    print(f"Rounds played: {rounds_played}")
    print(f"Human wins: {human_wins}")
    print(f"Computer wins: {computer_wins}")
    play_answer = input("Do you want to play? \n")
    if play_answer == "yes":
        rounds_played += 1
        rock_paper_scissors_game()
    else:
        sys.exit()