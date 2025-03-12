from turtle import Turtle, Screen
import random

# Create a new turtle object
direction=[0,90,180,45,270]
Line_Color=["light cyan", "dark green","dark orange","dark red","salmon","bisque","dark orchid"]
turtle = Turtle()
turtle.pensize(10)
turtle.speed("fastest")
my_screen = Screen()
# we wil try to create a random walking pattern of tutle
while(True):
    current_dir=random.randint(0,len(direction)-1)
    turtle.color(random.choice(Line_Color))
    turtle.right(direction[current_dir])
    turtle.forward(20)
my_screen.exitonclick()