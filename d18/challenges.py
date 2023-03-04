import random
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")

screen = Screen()
screen.colormode(255)


# challenge 1: draw a square
def square():
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)


# square()

# challenge 2: draw a dashed line
def dashed_line():
    for i in range(15):
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)
        my_turtle.pendown()


# dashed_line()

# challenge 3: draw a triangle, square, pentagon, hexagon, heptagon.....
def multi_shapes():
    for i in range(3, 11):
        angle = 360 / i
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        my_turtle.pencolor(r, g, b)
        for move in range(i):
            my_turtle.forward(100)
            my_turtle.right(angle)
            my_turtle.forward(100)


# multi_shapes()

# challenge 4&5: random walk with random color
def random_walk():
    my_turtle.hideturtle()
    my_turtle.width(10)
    my_turtle.speed(0)

    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        return random_color

    for i in range(100):
        directions = [0, 90, 180, 270]
        random_direction = float(random.choice(directions))
        my_turtle.pencolor(random_color())
        my_turtle.setheading(random_direction)
        my_turtle.forward(20)

# random_walk()

# challenge 6: make a spirograph
def spirograph():
    my_turtle.speed(0)
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    for i in range(0, 360, 5):
        my_turtle.pencolor(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(i)

spirograph()

screen.exitonclick()
