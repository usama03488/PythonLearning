#draw triangle,square,pentagon,hexagon,heptagon,octagon,nonagon,decagon
from turtle import Turtle, Screen
import random
def draw_Shape(player,sides,colors):
    player.color(colors)
    Turnangle=360/sides
    for _ in range(sides):
        player.forward(100)
        player.right(Turnangle)
tri=Turtle()
draw_Shape(tri,3,"green")
draw_Shape(tri,4,"red")
draw_Shape(tri,5,"black")
draw_Shape(tri,6,"blue")
draw_Shape(tri,7,"yellow")
my_screen=Screen()
my_screen.exitonclick()
