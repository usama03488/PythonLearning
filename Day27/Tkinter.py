from tkinter import *
#if we import like that then will no use tkinter things like "tkinter.label "

window=Tk()
window.title("My first gui")
window.minsize(width=1080,height=920)
# we can add padding arround the items like this
window.config(padx=100,pady=30)
my_label=Label(text="this is the label", font=("Arial",24,"bold"))
my_label.pack()

#for single item padding we do like this
my_label.config(padx=50,pady=50)

#pack is for fixed positions
#place manager is used to place item position by pixel
#my_label.place(10,10)
# prefer way is to use grid manager we will assign columns and rows for items
my_label.grid(column=0,row=0)
#we can not use grid with pack manager
# these are two types of line to change only label text like that
# my_label["text"]="new text"
# my_label.config(text="hello there")

#unlimited argument if we use asterik with name
#func(*args):
# for i in args:
#     print(i)
def button_click():
    print("demo button is clicked")
    enter_data=input.get()
    my_label["text"] = enter_data
button =Button(text="Click me", command= button_click)
#button.pack()
button.grid(column=1,row=1)
button2 =Button(text="button2", command= button_click)
button2.grid(column=3,row=0)
km=0
#Enter funtion for input field
input=Entry(width=50)
input.grid(column=4,row=4)
#text








window.mainloop()


