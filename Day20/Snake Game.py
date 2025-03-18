from turtle import Turtle, Screen
import random
import time
from Snake import Snake


my_screen = Screen()
my_screen.tracer(0)
snake=Snake()
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.listen()
my_screen.onkey(snake.Move_up,"Up")
my_screen.onkey(snake.Move_down,"Down")
my_screen.onkey(snake.Move_left,"Left")
my_screen.onkey(snake.Move_right,"Right")

IsGameon=True
while IsGameon:
    my_screen.update()
    time.sleep(0.05)
    snake.Move()





my_screen.exitonclick()