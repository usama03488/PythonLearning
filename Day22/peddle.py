from turtle import Turtle, Screen
import random
import time


class Peddle(Turtle):
    def __init__(self,position):

        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def goup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    def create_Peddle(self):
        Y_offset=0
        for _ in range(4):

            peddle.shape("square")
            peddle.color("white")
            peddle.penup()
            Y_offset -=10
            position = peddle.position()
            new_pos = [position[0], position[1] - Y_offset]
            peddle.goto(new_pos[0],new_pos[1])
            self.pedle_seg.append(peddle)
    def move_up(self):
        if self.head.ycor() < 250:
            for seg in self.pedle_seg:
                new_y = self.head.ycor() + 20
                self.head.goto(self.head.xcor(), new_y)




