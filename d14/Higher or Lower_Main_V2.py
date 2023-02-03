import art
import game_data
import random
from replit import clear

print(art.logo)


def extract_data():
    """Extract data from game_data.py and store it to separate list."""
    names = []
    followers = []
    descriptions = []
    countries = []

    for data in game_data.data:
        names.append(data["name"])
        followers.append(data["follower_count"])
        descriptions.append(data["description"])
        countries.append(data["country"])

    return names, followers, descriptions, countries


def info(name, description, country):
    """Retrieve and display the attributes of 'name', 'description', 'country' using the given name."""
    print(f"{name}, {description}, {country}")


def compare(follower_count_a, follower_count_b, answer, score):
    """Compare follower counts of a and b then evaluate answers. Return player score and correct answer."""
    if answer == "A":
        if follower_count_a > follower_count_b:
            print(f"A > B\n{follower_count_a} > {follower_count_b}")
            return score + 1, "A"
        else:
            print(f"A < B\n{follower_count_a} < {follower_count_b}")
            return score * -1, "B"
    elif answer == "B":
        if follower_count_a > follower_count_b:
            print(f"A > B\n{follower_count_a} > {follower_count_b}")
            return score * -1, "A"
        else:
            print(f"A < B\n{follower_count_a} < {follower_count_b}")
            return score + 1, "B"
    return 0


def game(names, followers, descriptions, countries):
    """Main function."""
    score = 0
    game_over = False
    name_a = random.choice(names)
    name_a_index = names.index(name_a)
    name_b = random.choice(names)
    name_b_index = names.index(name_b)
    while not game_over:
        info(name_a, descriptions[name_a_index], countries[name_a_index])
        print(art.vs)
        info(name_b, descriptions[name_b_index], countries[name_b_index])

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        score, correct_answer = compare(followers[name_a_index], followers[name_b_index], answer, score)

        if score > 0:
            print(f"You're right! Current score: {score}")
            clear()
            if correct_answer == "A":
                name_b = random.choice(names)
                name_b_index = names.index(name_b)

            if correct_answer == "B":
                name_a = name_b
                name_a_index = names.index(name_a)
                name_b = random.choice(names)
                name_b_index = names.index(name_b)
        else:
            clear()
            score = score * -1
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


names, followers, descriptions, countries = extract_data()
game(names, followers, descriptions, countries)
