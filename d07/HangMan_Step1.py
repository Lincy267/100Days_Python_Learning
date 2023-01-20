#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please guess a letter\n").lower()
while len(guess) > 1:
    print(f"invalid input, please try again")
    guess = input("Please guess a letter\n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for chosen_letter in chosen_word:
    if chosen_letter == guess:
        print("True")
    else:
        print("False")