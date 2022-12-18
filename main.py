# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("download.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random


color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
              (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71),
              (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164),
              (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]

AJ = t.Turtle()
t.colormode(255)
AJ = t.Turtle()
AJ.speed("fastest")
AJ.penup()
AJ.hideturtle()
AJ.setheading(225)
AJ.forward(300)
AJ.setheading(0)


number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    AJ.dot(20, random.choice(color_list))
    AJ.forward(50)

    if dot_count % 10 == 0:
        AJ.setheading(90)
        AJ.forward(50)
        AJ.setheading(180)
        AJ.forward(500)
        AJ.setheading(0)

screen = t.Screen()
screen.exitonclick()