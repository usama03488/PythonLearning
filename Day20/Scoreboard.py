from turtle import Turtle
import random

class scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        print("Initater called")
        self.color("yellow")
        self.penup()
        with open("data.txt") as file:
            self.high_score=int(file.read())

        self.score=score
        self.goto(0, 250)
        self.update_scoreboard(score=0)
        self.hideturtle()
        with open("data.txt", mode="w") as file:
            file.write("0")


    def update_scoreboard(self,score):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Arial",24,"normal"))
    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score=0
        self.update_scoreboard(self.score)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score +=1
        self.update_scoreboard(self.score)
        


