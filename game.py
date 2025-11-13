# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com/)
# to assist in creating this code.

import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 10)
    guess = None
    attempts = 0

    while guess != number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 You guessed it in {attempts} tries!")
        except ValueError:
            print("Please enter a valid number.")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
