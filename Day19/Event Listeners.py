from turtle import Turtle, Screen
import random



turtle = Turtle()

my_screen = Screen()

def move_forward():
    turtle.forward(100)

my_screen.listen()
my_screen.onkey(move_forward,"space")
my_screen.exitonclick()