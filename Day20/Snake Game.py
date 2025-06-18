from turtle import Turtle, Screen
import random
import time
from Snake import Snake
from Food import Food
from Scoreboard import scoreboard
#file=open("D:\Python Practice\DAY1-Practice\Day20\my_file.txt") there are two wayd to open file
#by default file open in read mode but we can change it to write by writing mode=w: "a" stand for append
with open("new_file.txt", mode="a") as file:
    file.write("no is not the best time")

    # by this technique we no longer have to close the file

#file.close()
my_screen = Screen()
my_screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=scoreboard(0)
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")

my_screen.listen()
my_screen.onkey(snake.Move_up,"Up")
my_screen.onkey(snake.Move_down,"Down")
my_screen.onkey(snake.Move_left,"Left")
my_screen.onkey(snake.Move_right,"Right")
score=0
IsGameon=True

while IsGameon:
    my_screen.update()
    time.sleep(0.05)
    snake.Move()


    if(snake.head.distance(food)<15):
        print("nom nom nom")
        snake.Extend_Snake()
        scoreboard.increase_score()
        food.New_Food()
    if(snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280):

        scoreboard.reset_score()
        snake.reset()
        #this is the collision dectection code without using slicing
    # for segments in snake.Snake_seg:
    #     if( snake.head!= segments and  snake.head.distance(segments)<10):
    #         print("Game Over")
    #         IsGameon=False
    #         scoreboard.game_over()

    #Now I will use slicing to find collision of snake with its tale
    #In Slicing usually we can skip some indexex of array or tuples or we can just get a specific chunk of data from a large data set of arrays
    #foe example slicing_1[1:2], this is the syntax of slicing and first value is the starting index and after colon we give the last index of array
    #However we can also provide the increment amount like how much increment we want between indexes manipulation
    #for example sliving_1[1:5:-1] in this third value is the increment amount in the current example slicing will be done with an increment of 1 but its direction will be from end to start
    for segments in snake.Snake_seg[1:]:
        if(  snake.head.distance(segments)<10):
            scoreboard.reset_score()
            snake.reset()




my_screen.exitonclick()