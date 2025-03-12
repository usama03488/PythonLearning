from turtle import Turtle, Screen

My_turtle= Turtle()
My_turtle.shape("turtle")
My_turtle.color("red")
for _ in range(120):
    if(_%2==0):
        My_turtle.penup()
        My_turtle.forward(2)
    else:
        My_turtle.pendown()
        My_turtle.forward(4)





   # My_turtle.right(90)


my_screen=Screen()
my_screen.exitonclick()


