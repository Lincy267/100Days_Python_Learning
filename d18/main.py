# import colorgram
# colors = colorgram.extract('1280px-Gay_Pride_Flag.svg.jpg', 6)
#
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_list.append(rgb_tuple)
# print(rgb_list)
color_list = [(227, 0, 0), (117, 0, 136), (0, 77, 253), (253, 141, 0), (0, 128, 32), (254, 238, 0)]

import random
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.hideturtle()
my_turtle.speed(0)
screen = Screen()
screen.colormode(255)
my_turtle.penup()



for i in range(10):
    my_turtle.setposition(-250.0, i * 50 - 200)
    for i in range(10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.forward(50)





screen.exitonclick()
