#Step 5

import random
import hangman_words
import hangman_art

# word_list = ["aardvark", "baboon", "camel"]
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)


print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

lives = 6
print(hangman_art.stages[lives])

display =[]
for letter in chosen_word:
    display.append("_")
print(' '.join(display))

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    n = 0
    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word, you lose a life, lives remains: {lives}")


    if guess in display:
        print(f"letter already guessed, please try again")
        guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for letter in chosen_word:
        n += 1
        if letter == guess:
            display[n-1] = letter

    print(hangman_art.stages[lives])
    print(' '.join(display))

    if lives == 0:
        end_of_game = True
        print("YOU LOSE!")
    elif "_" not in display:
        end_of_game = True
        print("YOU WIN!")

