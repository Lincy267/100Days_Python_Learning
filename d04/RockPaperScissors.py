rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = int(input("0=Rock, 1=Paper, 2=Scissors\n"))
ai_choice = random.randint(0,2)
game_image = [rock, paper, scissors]

if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])
else:
    print("INVAILID NUMBER!\n")

print(f"AI:\n{game_image[ai_choice]}")

if user_choice == ai_choice:
    print("DRAW")
elif user_choice == 0:
    if ai_choice == 1:
        print("YOU LOSE")
    elif ai_choice == 2:
            print("YOU WIN")
elif user_choice == 1:
    if ai_choice == 2:
        print("YOU LOSE")
    elif ai_choice == 0:
            print("YOU WIN")
elif user_choice == 2:
    if ai_choice == 0:
        print("YOU LOSE")
    elif ai_choice == 1:
            print("YOU WIN")