from turtle import Turtle, Screen
import random

def Generate_Color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
# Create a new turtle object
direction=[0,90,180,45,270]
Line_Color=["light cyan", "dark green","dark orange","dark red","salmon","bisque","dark orchid"]
turtle = Turtle()
turtle.pensize(5)
turtle.speed("fastest")
my_screen = Screen()
my_screen.colormode(255)



angle=10

for _ in range(int(360/10)):

    my_tuple = Generate_Color()
    turtle.pencolor(my_tuple)
    turtle.circle(100)
    turtle.setheading(turtle.heading()+10)

# we wil try to create a circle with a specific radius
# while(True):
#     current_dir=random.randint(0,len(direction)-1)
#     my_tuple=Generate_Color()
#     turtle.pencolor(my_tuple)
#     #turtle.pencolor(my_tuple[0], my_tuple[1], my_tuple[2])
#     turtle.right(direction[current_dir])
#     turtle.forward(20)
my_screen.exitonclick()