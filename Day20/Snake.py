from turtle import Turtle, Screen
import random
import time

MOVE_SPEED=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():


    def __init__(self):
        self.Snake_seg = []
        self.Create_Snake()
        self.head=self.Snake_seg[0]0


    def Create_Snake(self):
        X_offset = 0
        for _ in range(3):
            turtle_1 = Turtle()
            turtle_1.shape("square")
            turtle_1.color("white")
            turtle_1.penup()
            X_offset -= 10
            position = turtle_1.position()
            new_pos = [position[0] - X_offset, position[1]]
            turtle_1.goto(new_pos[0], new_pos[1])
            self.Snake_seg.append(turtle_1)
    #we have to extend a snake fro that we have to create and instance on snake and add it in to snake artrat
    def Extend_Snake(self):
        snake=Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        init_positon=self.Snake_seg[-1].position()
        offset = 10
        new_pos = [init_positon[0] - offset, init_positon[1]]
        snake.goto(new_pos[0], new_pos[1])
        self.Snake_seg.append(snake)
        print("Snake extended")


    def Move(self):

        for seg_num in range(len(self.Snake_seg) - 1, 0, -1):
            if (seg_num > 0):
                self.Snake_seg[seg_num].goto(self.Snake_seg[seg_num - 1].xcor(), self.Snake_seg[seg_num - 1].ycor())

        self.head.forward(MOVE_SPEED)
    def Move_up(self):
        if (self.head.heading()!=DOWN):
            self.head.setheading(UP)

    def Move_down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(DOWN)

    def Move_left(self):
        if(self.head.heading() !=RIGHT):
            self.head.setheading(LEFT)

    def Move_right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)


