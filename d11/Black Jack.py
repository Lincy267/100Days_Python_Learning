############### Blackjack Project #####################
import random
from replit import clear
import art

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_score = 0
ai_score = 0
ai_hands_list = []

def player_first_draw():
    global player_hands, player_score
    player_hands = random.choices(cards, k=2)
    player_score = sum(player_hands)
    print(f"Your cards: {player_hands}, current score: {player_score}")


def ai_first_draw():
    global ai_hands, ai_score, ai_hands_list
    ai_hands = random.choice(cards)
    ai_hands_list.append(ai_hands)
    ai_score = int(ai_hands)
    print(f"Computer's first card: {ai_hands}")


def player_next_draw():
    global player_hands, player_score
    player_hands.append(random.choice(cards))
    player_score = sum(player_hands)
    if player_score > 21 and 11 in player_hands:
        player_ace_index = player_hands.index(11)
        player_hands[player_ace_index] = 1
        player_score = sum(player_hands)
    print(f"Your cards: {player_hands}, current score: {player_score}")


def ai_next_draw():
    global ai_hands_list, ai_score
    ai_next_hand = random.choice(cards)
    ai_hands_list.append(ai_next_hand)
    ai_score = sum(ai_hands_list)
    if ai_score > 21 and 11 in ai_hands_list:
        ai_ace_index = ai_hands_list.index(11)
        ai_hands_list[ai_ace_index] = 1
        ai_score = sum(ai_hands_list)
        ai_next_hand = 1
    print(f"Computer's next card: {ai_next_hand}")


def game_result(player_score, ai_score):
    if player_score > ai_score:
        print(f"Your final hand: {player_hands}, your final score: {player_score}, \nAI's final hand: {ai_hands_list}, AI's final score: {ai_score}. \nYOU WIN!")
    elif ai_score > 21:
        print(f"{ai_hands_list}, AI score: {ai_score}. AI WENT OVER, YOU WIN!!")
    elif player_score < ai_score:
        print((f"Your final hand: {player_hands}, your final score: {player_score}, \nAI's final hand: {ai_hands_list}, AI's final score: {ai_score}. \nAI WIN!"))
    else:
        print(f"Your final hand: {player_hands}, your final score: {player_score}, \nAI's final hand: {ai_hands_list}, AI's final score: {ai_score}. \nDRAW!")



def black_jack():
    end_game = False
    while not end_game:
        if input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "n":
            end_game = True
        else:
            pass_drawing = False
            clear()
            print(art.logo)
            ai_hands_list.clear()
            player_first_draw()
            ai_first_draw()
            while not pass_drawing:
                if_draw = input(f"Type 'y' to get another card, type 'n' to pass: ")
                if if_draw == "y":
                    player_next_draw()
                    if player_score > 21 or ai_score > 21:
                        if player_score > 21:
                            print(f"Your score: {player_score}. YOU WENT OVER, YOU LOSE!")
                        else:
                            print(f"AI score: {ai_score}. AI WENT OVER, YOU WIN!")
                        end_game = True
                        black_jack()
                        break
                elif if_draw == "n":
                    while ai_score < 17:
                        ai_next_draw()
                    game_result(player_score, ai_score)
                    pass_drawing = True




black_jack()
##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
