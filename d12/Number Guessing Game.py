# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

print(art.logo)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1, 100)

HARD_ATTEMPTS = 10
EASY_ATTEMPTS = 5

def select_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        print(f"You have {HARD_ATTEMPTS} attempts remaining to guess the number.")
        return HARD_ATTEMPTS
    elif difficulty == "hard":
        print(f"You have {EASY_ATTEMPTS} attempts remaining to guess the number.")
        return EASY_ATTEMPTS
    else:
        return 0


def player_guess():
    attempts_remain = select_difficulty()
    end_game = False
    while not end_game:
        if attempts_remain > 0:
            guess = int(input("Make a guess: "))
            if guess > number_to_guess:
                print("Too high")
                attempts_remain -= 1
                print("Guess again")
                print(f"You have {attempts_remain} attempts remaining to guess the number.\n")
            elif guess < number_to_guess:
                print("Too low")
                attempts_remain -= 1
                print("Guess again")
                print(f"You have {attempts_remain} attempts remaining to guess the number.\n")
            else:
                print(f"You got it! The answer was {number_to_guess}")
                end_game = True
        elif attempts_remain == 0:
            print(f"You've run out of guesses, you lose. The answer is {number_to_guess}.")
            end_game = True


player_guess()
