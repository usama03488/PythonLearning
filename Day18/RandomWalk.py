from turtle import Turtle, Screen
import random

# Create a new turtle object
direction=[90,-90,-180,180,45,-45]
turtle = Turtle()
my_screen = Screen()
# we wil try to create a random walking pattern of tutle
while(True):
    current_dir=random.randint(0,len(direction)-1)
    turtle.right(direction[current_dir])
    turtle.forward(20)
my_screen.exitonclick()