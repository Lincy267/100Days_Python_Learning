from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()
screen.listen()
step = 20

def move_forwards():
    my_turtle.forward(step)

def move_backwards():
    my_turtle.backward(step)


def move_counter_clockwise():
    my_turtle.left(10)


def move_clockwise():
    my_turtle.right(10)


def clear_screen():
    my_turtle.reset()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
