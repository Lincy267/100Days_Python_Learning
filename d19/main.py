from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

starting_x = -230
starting_y = -120
stoping_x = 230
step = 50
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=starting_x, y=starting_y + turtle_index * step)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > stoping_x:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print("you won!")
            else:
                print(f"you lose! the winner is the {winning_color} turtle")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()



