# Number Guessing Game - LLM_LAB1
# Generated using an AI model and then debugged and improved by me.
# The game lets the user guess a number until correct, and allows replay.

import random

def play_game():
    number = random.randint(1, 50)
    guess = 0

    while guess != number:
        guess = int(input("Enter your guess (1-50): "))

        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
        else:
            print("You guessed it!")

while True:
    play_game()
    repeat = input("Play again? (yes/no): ").lower()

    if repeat != "yes":
        print("Thanks for playing!")
        break
