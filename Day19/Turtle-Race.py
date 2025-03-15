from turtle import Turtle, Screen
import random

colors=["light cyan", "dark green","dark orange","dark red","salmon","bisque"]

Is_race_on=False


my_screen = Screen()
my_screen.colormode(255)
my_screen.setup(500,500)
User_bet=my_screen.textinput(title="Make your bet" , prompt="what do you think who will win the race")
turtles_list=[]
# print(User_bet)
y_axis=150
for i in range(0,6):
    turtle_1 = Turtle(shape="turtle")
    turtle_1.color(colors[i])
    turtle_1.penup()
    turtle_1.goto(-230, y_axis)
    y_axis -=50
    turtles_list.append(turtle_1)
if User_bet:
    Is_race_on=True
while(Is_race_on):
    for turtle in turtles_list:
        turtle.forward(random.randint(0,50))
        if turtle.xcor() > 230:
            Is_race_on=False
            winner=turtle.pencolor()
            if(winner==User_bet):
                print(f"You won the bet. The winner is {winner}")
            else:
                print(f"You loose the bet.The winner is {winner}")

            break
# turtle_1.backward(100)
# turtle_2.backward(100)
# turtle_3.backward(100)
# turtle_4.backward(100)
# turtle_5.backward(100)




my_screen.exitonclick()