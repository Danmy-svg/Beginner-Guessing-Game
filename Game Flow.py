import random

print("Welcome to my number guessing game")
print(
    'The rules of the game are that you guess a number between 1 - 100 and I will tell you whether you guessed the right number')

Secret_number = random.randint(1, 100)

max_tries = 11
counter = max_tries - 0

while counter > 0:
    counter -= 1
    Guess = int(input(f"You have {counter} tries left. Guess a number "))

    if Guess == Secret_number:
        print("Correct 😊")
        break

    elif Guess < Secret_number:
        print("Too low! Ya numpty go again 🤣")

    else:
        print("Too high your wrapping it! 🤮")

    if counter == 0:
        print("GAME OVER 💀")
        break