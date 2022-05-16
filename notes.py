from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("OliveDrab")
timmy_the_turtle.color("OliveDrab")

# def draw_square():
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# draw_square()

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)




#Draw Dashed Line
# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()




#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

# taking input for the no of the sides of the polygon
# n = int(input("Enter the no of the sides of the polygon : "))
  
# taking input for the length of the sides of the polygon
# l = int(input("Enter the length of the sides of the polygon : "))
  

# for _ in range(n):
#     timmy_the_turtle.forward(l)
#     timmy_the_turtle.right(360 / n)

colours = ["CornflowerBlue","DarkOrchid", "IndianRed", "wheat","DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# for shape_side_n in range(3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)

directions = [0, 90, 180, 270]

for _ in range(200):
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()