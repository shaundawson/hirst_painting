from turtle import Turtle, Screen

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


for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)




screen = Screen()
screen.exitonclick()