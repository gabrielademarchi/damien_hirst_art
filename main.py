from turtle import Screen, Turtle
import random

color_list = [(202, 164, 164), (150, 75, 75), (223, 201, 201), (52, 93, 93), (172, 154, 154), (140, 30, 30), (133, 163, 163), (198, 91, 91), (46, 122, 122), (72, 43, 43), (145, 178, 178), (13, 99, 99), (233,
                                                                                                                                                                                                           175, 175), (161, 142, 142), (105, 74, 74), (55, 46, 46), (183, 205, 205), (36, 60, 60), (18, 86, 86), (81, 148, 148), (148, 17, 17), (14, 70, 70), (30, 68, 68), (107, 127, 127), (174, 94, 94), (176, 192, 192)]

timmy = Turtle()
timmy.hideturtle()
timmy.speed('fastest')

screen = Screen()
screen.colormode(255)


def change_color(colors_list):
    return random.choice(colors_list)


def dot_pen(dot_size, gap):
    timmy.dot(dot_size)
    timmy.penup()
    timmy.forward(gap)  # dot doesnt need pendown


def t_position(x, y):
    timmy.penup()
    timmy.goto(x, y)
    timmy.pendown()


gap = 50
size = 20

y_coord = 0
for row in range(10):
    t_position(-200, -200 + y_coord)
    for column in range(10):
        timmy.color(change_color(color_list))
        dot_pen(size, gap)
    y_coord += gap


screen.exitonclick()
