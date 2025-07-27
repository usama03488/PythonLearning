BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import pandas
import csv
import time
global English_trans
current_card={}
to_learn= {}
#we read data at the start at the start
try :
    data=pandas.read_csv("Data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("D:/Python Practice/DAY1-Practice/Day31 Capstone Project/Data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")





print(to_learn)


def getword():
    global  current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_card, text=current_card["French"], fill= "black")
    canvas.itemconfig(canvas_img, image=frontimg)
    flip_timer=window.after(3000, flip_side)
def flip_side():
    print("card flipped")
    canvas.itemconfig(canvas_title, text="English", fill= "white")
    canvas.itemconfig(canvas_card, text=current_card["English"], fill= "white")

    canvas.itemconfig(canvas_img, image=backimg)
    #window.after(3000, turn_back)
def turn_back():
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_card, text=current_card["French"], fill= "black")
    canvas.itemconfig(canvas_img, image=frontimg)
def known_word():
    to_learn.remove(current_card)
    new_data=pandas.DataFrame(to_learn)
    #when we set index to false it means that while saving document file do not add a columns of index
    #there was an issue that mutiple column are creadted of index at every game end
    new_data.to_csv("Data/words_to_learn.csv ", index=False)



    getword()


    #return current_card["French"]






window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR )
flip_timer= window.after(3000, flip_side)
canvas=Canvas(width=800,height=526,highlightthickness=0 )
frontimg=PhotoImage(file="D:/Python Practice/DAY1-Practice/Day31 Capstone Project/Image/card_front.png")
backimg = PhotoImage(file="D:/Python Practice/DAY1-Practice/Day31 Capstone Project/Image/card_back.png")
canvas_img=canvas.create_image(400,263,image=frontimg)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0 )
canvas_title=canvas.create_text(400,150,text="French", font=("Ariel", 40, "italic"))
#I get random word from csv file and display that word on screen

canvas_card=canvas.create_text(400,263,text="card", font=("Ariel", 60, "bold"))

canvas.grid(row=0,column=0,columnspan=2)
#cross image
crossimg=PhotoImage(file= "D:/Python Practice/DAY1-Practice/Day31 Capstone Project/Image/wrong.png")
Crossbtn = Button(image=crossimg, highlightthickness=0,command=getword)
Crossbtn.grid(row=1,column=0)

correctimg=PhotoImage(file= "D:/Python Practice/DAY1-Practice/Day31 Capstone Project/Image/tick.png")
Correctbtn=Button(image=correctimg, highlightthickness=0, command=known_word )
Correctbtn.grid(row=1,column=1)
getword()




window.mainloop()