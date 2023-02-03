import art
import game_data
import random
from replit import clear

print(art.logo)

NAMES = []
for name in game_data.data:
    NAMES.append(name["name"])

FOLLOWERS = []
for follower_count in game_data.data:
    FOLLOWERS.append(follower_count["follower_count"])

DESCRIPTIONS = []
for description in game_data.data:
    DESCRIPTIONS.append(description["description"])

COUNTRYS = []
for country in game_data.data:
    COUNTRYS.append(country["country"])

NAME_A = random.choice(NAMES)
NAME_A_index = NAMES.index(NAME_A)
NAME_B = random.choice(NAMES)
NAME_B_index = NAMES.index(NAME_B)

SCORES = 0


def A_follower_count(NAME_A):
    followers_A = FOLLOWERS[NAME_A_index]
    return followers_A


def A_information(NAME_A):
    description_A = DESCRIPTIONS[NAME_A_index]
    country_A = COUNTRYS[NAME_A_index]
    print(f"Compare A: {NAME_A}, {description_A}, from {country_A}.")


def B_follower_count(NAME_B):
    followers_B = FOLLOWERS[NAME_B_index]
    return followers_B


def B_information(NAME_B):
    description_B = DESCRIPTIONS[NAME_B_index]
    country_B = COUNTRYS[NAME_B_index]
    print(f"Against B: {NAME_B}, {description_B}, from {country_B}.")


def compare(user_answer, SCORES):
    A_followers = A_follower_count(NAME_A_index)
    B_followers = B_follower_count(NAME_B_index)
    if user_answer == "A":
        if A_followers > B_followers:
            print(f"A > B\n{A_followers} > {B_followers}")
            return SCORES + 1
        else:
            print(f"A < B\n{A_followers} < {B_followers}")
            return SCORES * -1
    elif user_answer == "B":
        if A_followers > B_followers:
            print(f"A > B\n{A_followers} > {B_followers}")
            return SCORES * -1
        else:
            print(f"A < B\n{A_followers} < {B_followers}")
            return SCORES + 1


def game():
    global NAME_A, NAME_B, game_over, SCORES, NAME_A_index, NAME_B_index
    game_over = False
    while not game_over:
        A_information(NAME_A)
        print(art.vs)
        B_information(NAME_B)
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        SCORES = compare(answer, SCORES)
        if SCORES > 0:
            print(f"You're right! Current score: {SCORES}")
            clear()
            if answer == "A":
                NAME_B = random.choice(NAMES)
                NAME_B_index = NAMES.index(NAME_B)

            else:
                NAME_A = NAME_B
                NAME_A_index = NAMES.index(NAME_A)
                NAME_B = random.choice(NAMES)
                NAME_B_index = NAMES.index(NAME_B)
        else:
            clear()
            SCORES = SCORES * -1
            print(f"Sorry, that's wrong. Final score: {SCORES}")
            game_over = True


game()
