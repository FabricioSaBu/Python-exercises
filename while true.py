import random

secret_number = random.randint(1, 100)
guess_count = 0

while True:
    guess_count += 1
    user_guess = int(input("Guess the number: "))
    if user_guess < secret_number:
        print("Too low")
    elif user_guess > secret_number:
        print("Too high")
    else:
        print("Your number of guesses was: " + str(guess_count))
        break