import random

def get_choice():
    player_choice = input("Enter a Choice (rock, paper, scissors) :")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose : {player}, computer chose : {computer}")
    if player == computer:
        return "Its a tie!"
    elif player == "rock" and computer == "scissors":
        return "Rock crushes Scissors — Player Wins!"
    elif player == "paper" and computer == "rock":
        return"Paper wraps Rock — Player Wins!"
    elif player == "scissors" and computer == "paper":
        return "Scissors cuts Paper — Player Wins!"
    elif player == "scissors" and computer == "rock":
        return "Rock crushes Scissors — Computer Wins!"
    elif player == "paper" and computer == "scissors":
        return "Scissors cuts Paper — Computer Won!"
    elif player == "rock" and computer == "paper":
        return "Paper wraps Rock — Computer Won!"
    
choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)