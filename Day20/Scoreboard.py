from turtle import Turtle
import random

class scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        print("Initater called")
        self.color("yellow")
        self.penup()

        self.high_score=0
        self.goto(0, 250)
        self.update_scoreboard(score=0)
        self.hideturtle()


    def update_scoreboard(self,score):
        self.clear()
        self.high_score+=score
        self.write(f"Score: {self.high_score}", align="center", font=("Arial",24,"normal"))
    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))


