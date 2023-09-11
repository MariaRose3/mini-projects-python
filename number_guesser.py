# number guesser game
# generate a random number and find out how many
# attempts it takes the user to make the right guess

import random

max_limit = input("Type a number: ")

if max_limit.isdigit():
    max_limit = int(max_limit) 
    if max_limit <= 0:
        print("Please type a number greater than 0.")
        quit()
else:
    print("Please type a number.")
    quit()

random_number = random.randint(0,max_limit)
# print(max_limit)
guesses = 0
correct_guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        continue
    if user_guess == random_number:
        print("You got it!")
        correct_guesses += 1
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You are below the number.")

print("You got it in", guesses,"guesses.")
print(f"Your rate of success is {(correct_guesses/guesses) * 100}%")
    