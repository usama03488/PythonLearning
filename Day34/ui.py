from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
age:int
name: str
class QuizInterface:
    #quiz: QuizBrain --> we can sepcify the data type like this It ensure that we send correct type of data as a parameter
    def __init__(self,quiz: QuizBrain):
        self.quizbrain = quiz
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=350,height=300,highlightthickness=0)
        self.canvas.config(bg="White")
        self.canvas.grid(row=1,column=1,columnspan=3,pady=20)
        self.questiontext=self.canvas.create_text(150,130,width=300,text="text comes here",font=("Arial",16,"bold"))
        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR,highlightthickness=0)
        self.score_label.grid(row=0,column=3)

        self.crossimg=PhotoImage(file="D:/Python Practice/DAY1-Practice/Day34/Images/false.png")
        self.trueimg=PhotoImage(file="D:/Python Practice/DAY1-Practice/Day34/Images/true.png")
        self.Crossbtn=Button(image=self.crossimg,highlightthickness=0,command=self.Cross_btn)
        self.Crossbtn.grid(row=2,column=1)
        self.truebtn=Button(image=self.trueimg,highlightthickness=0,command=self.True_btn)
        self.truebtn.grid(row=2, column=3)


        self.get_next_question()




        self.window.mainloop()
    def get_next_question(self):
        question_text=self.quizbrain.next_question()

        print(question_text)
        self.canvas.itemconfig(self.questiontext, text=question_text)
        self.canvas.config(bg="white")

    def True_btn(self):
        print("true button pressed")
        self.Give_feedback(self.quizbrain.check_answer("False"))

        self.get_new_question()
    def Cross_btn(self):
        print("cross btn pressed")

        self.Give_feedback(self.quizbrain.check_answer("False"))
        self.get_new_question()
    def Give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.reset_color)
    def reset_color(self):
        self.get_next_question()