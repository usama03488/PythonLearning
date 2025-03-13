from turtle import Turtle, Screen
import random

screen=Screen()
tim=Turtle()

screen.colormode(255)

Colors=[(254, 225, 6), (16, 254, 5), (252, 4, 145), (188, 3, 254), (9, 254, 243)]
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(350)
tim.setheading(0)
Number_of_dots=100
for _ in range(1,Number_of_dots+1):
    tim.dot(20, random.choice(Colors))
    tim.forward(50)
    if(_%10==0):
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)








screen.exitonclick()