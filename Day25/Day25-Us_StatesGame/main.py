from turtle import Turtle,Screen
import csv
import pandas




screen=Screen()
turtle= Turtle()
screen.title("U.S states Game ")
image="blank_states_img.gif"
data=pandas.read_csv("50_states.csv")
screen.addshape(image)
turtle.shape(image)
data_dict=data.to_dict()
states=data["state"].to_list()


gussed_states=[]
missed=[]
while len(gussed_states) < 50:
    answere = screen.textinput(f"{len(gussed_states)}/50 Guessed", "What's another state name").title()
    print(answere)
    if(answere=="Exit"):
        # list comprehension
        missed=[state for state in states if state not in gussed_states]
# for dictionary comprehension
        #dict= {item_key:item_value for (item_key,value) in dict.item() }

        # for state in states:
        #     if state not in gussed_states:
        #         missed.append(state)
        print(missed)
        new_data=pandas.DataFrame(missed)
        new_data.to_csv("Gussed_states.csv")
        break
    if answere in states:
        gussed_states.append(answere)
        item = Turtle()
        item.hideturtle()
        item.penup()
        item.color("black")
        State_data = data[data.state == answere]
        item.goto(int(State_data.x.item()), int(State_data.y.item()))
        item.write(f"{State_data.state.item()}", align="center", font=("Arial", 14, "normal"))
        print(State_data.x)

# this is for getting cordinates on cliking mouse on screen but for now i don't need that

# def get_Mouse_Click(x,y):
#     print(x,y)
# screen.onscreenclick(get_Mouse_Click)
