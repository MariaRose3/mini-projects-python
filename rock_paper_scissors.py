import random

player_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    player_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if player_input =="q":
        break

    if player_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock=0, paper=1, scissors=2

    computer_choice = options[random_number]
    print("Computer chose",computer_choice +".")

    if player_input == "rock" and computer_choice == "scissors":
        print("You won!")
        player_wins += 1
    elif player_input == "paper" and computer_choice == "rock":
        print("You won!")
        player_wins += 1
    elif player_input == "scissors" and computer_choice == "paper":
        print("You won!")
        player_wins += 1
    elif player_input == computer_choice:
        continue
    else:
        print("Oops, you lost!")
        computer_wins += 1

print(f"You won {player_wins} times!")
# print(f"Your rate of success is {(player_wins/(player_wins+computer_wins)) * 100}%")
print("Goodbye!")