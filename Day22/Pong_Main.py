# we are going to buold
from turtle import Turtle, Screen
import random
import time
from peddle import Peddle
from Ball import ball
my_screen = Screen()
my_screen.tracer(0)

# we creadted first peddle now we will try to move it up and down by getting user input
my_screen.setup(1000,800)
my_screen.bgcolor("black")
my_screen.title("Pong Game")

#this create the second peddle which we should use because it is comming form its own class and we can define its parameter there
R_paddle=Peddle((350,0))
L_paddle=Peddle((-350,0))
Ball=ball((0,0))
# peddle1=Turtle()
# peddle1.shape("square")
# peddle1.shapesize(5,1)
# peddle1.color("white")
# peddle1.penup()
# peddle1.goto(450,0)
my_screen.tracer(0)


my_screen.listen()
my_screen.onkey(R_paddle.goup,"Up")
my_screen.onkey(R_paddle.go_down,"Down")

# Update the screen so it shows the paddle
isgameon=True;
while(isgameon):
    time.sleep(0.2)
    my_screen.update()
    if(Ball.IsCollided== False):
        Ball.CheckPosition()
        Ball.move()
    if(Ball.Distance(R_paddle)< 5 and Ball.xcor()>340 or Ball.Distance(L_paddle)< 5 and Ball.xcor()< -340  ):
        Ball.Bounce_Xaxis()
        print("Ball collided with paddle")






my_screen.exitonclick()