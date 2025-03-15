from turtle import Turtle, Screen
import random



turtle = Turtle()

my_screen = Screen()

"""W- to move forward
S- to move backwards
A- to turn left
D- to turn right"""

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)
def move_left():
    turtle.left(10)
def move_right():
    turtle.right(10)


my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="d", fun=move_right)
my_screen.onkey(key="a", fun=move_left)



my_screen.exitonclick()