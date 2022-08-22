import turtle 
import random

tim = turtle.Turtle()
turtle.colormode(255)
# tim.shape("turtle")
tim.speed("fastest")
# tim.pensize(5)

# tim.color("red")
# colors = ["red", "green", "blue", "yellow", "orange", 
#           "purple", "pink", "aquamarine", "deep pink",
#           "peru", "lime", "firebrick", "cornflower blue",
#           "cyan", "chartreuse", "dark goldenrod", "coral"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_shape(num_sides):
    angle = 360 / num_sides
    # print(f"angle = {angle}")
    for i in range(num_sides):
        # print(f"Side {i}")
        tim.forward(100)
        tim.right(angle)

# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(i)
# draw_shape(3)

# for i in range(30):
#     if i % 2 == 0:
#         tim.pendown()
#     else: 
#         tim.penup()
#     tim.forward(10)



# for _ in range(300):
#     tim.setheading(random.choice([0, 90, 180, 270]))
#     tim.color(random_color())
#     tim.forward(20)

for i in range(0, 360, 10):
    tim.setheading(i)
    tim.color(random_color())    
    tim.circle(100)
    
window = turtle.Screen()
window.exitonclick()

