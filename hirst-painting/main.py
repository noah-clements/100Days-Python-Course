# import colorgram
import random
import turtle 


# rgb_colors = []
# rgb_tuples = []
# colors = colorgram.extract('hirst.webp', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append(color.rgb)
#     new_color = (r, g, b)
#     rgb_tuples.append(new_color)

# print(rgb_colors)
# print(rgb_tuples)
color_list = [(238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), 
                (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), 
                (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), 
                (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), 
                (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), 
                (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), 
                (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

turtle.colormode(255)
turtle.bgcolor(249, 248, 248)

turtle.setup(660, 660)

tim = turtle.Turtle()
tim.speed("fastest")
# tim.pensize(10)
# tim.home()
tim.penup()
tim.hideturtle()
# tim.setpos(-300.0, -300.0)
for i in range(10):
    tim.setpos(-270.0, (-270.0 + (i * 60)))
    for _ in range (10):
        tim.dot(20, random.choice(color_list))
        tim.forward(60)
    
# tim.dot(20)

window = turtle.Screen()
window.exitonclick()