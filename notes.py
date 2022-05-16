import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

tim.shape("turtle")
tim.color("OliveDrab")
tim.color("OliveDrab")

# def draw_square():
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.right(90)

# draw_square()

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)




#Draw Dashed Line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()




#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

# taking input for the no of the sides of the polygon
# n = int(input("Enter the no of the sides of the polygon : "))
  
# taking input for the length of the sides of the polygon
# l = int(input("Enter the length of the sides of the polygon : "))
  

# for _ in range(n):
#     tim.forward(l)
#     tim.right(360 / n)

# colours = ["CornflowerBlue","DarkOrchid", "IndianRed", "wheat","DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()