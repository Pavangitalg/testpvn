
import random


def get_choices():
  player_choice = input("Enter a choice rock, paper, scissors:")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):
  print(f"You chose {player },computer chose {computer}")
  if player == computer:
    print("it is tie!")
  elif player == "rock":
    if computer == "scissors":
      return "Rock Smashes scissors! You WIN!."
    else:
      return "Paper Covers Rock, you lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper Covers Rock! You WIN!."
    else:
      return "Scissor cuts Paper, you lose."
  elif player == "scissors":
    if computer == "papers":
      return "Scissor cuts Paper! You WIN!."
    else:
      return "Rock Smashes scissors!, you lose."


choices=get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)


