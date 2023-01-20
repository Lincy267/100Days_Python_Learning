#Step 4

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6
print(stages[lives])
#Create blanks
display =[]
for letter in chosen_word:
    display.append("_")
print(' '.join(display))

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    n = 0
    if guess not in chosen_word:
        lives -= 1
    # Check guessed letter
    for letter in chosen_word:
        n += 1
        if letter == guess:
            display[n-1] = letter
    print(stages[lives])
    print(' '.join(display))

#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    # Check if user has got all letters.

    if lives == 0:
        end_of_game = True
        print("YOU LOSE!")
    elif "_" not in display:
        end_of_game = True
        print("YOU WIN!")



#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.