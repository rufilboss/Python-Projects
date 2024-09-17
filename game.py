import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def win_checker(player, computer):
    print(f"You choose {player}, computer choose {computer}")
    if player == computer:
        return "It's a tie!"
    
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock, you win!"
        
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock, you win!"
        else:
            return "Scissors cut paper, you lose!"
        
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You Win!"
        else:
            return "Rock crushes scissors, you lose!"
    
choices = get_choices()
results = win_checker(choices["player"], choices["computer"])
print(results)