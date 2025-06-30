from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
rep=1
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
import math
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    if(IsTimer_ACTIVE):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if(count_sec== 0):
            count_sec="00"
        elif count_sec<10:
            count_sec= f"0{count_sec} "
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if (count > 0):
            window.after(1000, counter, count - 1)
        else:
            Increase_stage()

def Increase_stage():
    global rep
    rep +=1
    start_time()

def start_time():
    global IsTimer_ACTIVE
    global rep
    work_Sec=WORK_MIN *60
    Shortbreak_sec=SHORT_BREAK_MIN *60
    Longbreak_Sec=LONG_BREAK_MIN *60
    IsTimer_ACTIVE=True
    if(rep%2==1):
        counter(work_Sec)
        Title_label.config(text="Work", fg= GREEN)

    elif(rep<7 and rep%2==0):
        counter(Shortbreak_sec)
        Title_label.config(text="Break", fg=PINK)

    else:
        counter(Longbreak_Sec)
        Title_label.config(text="Break", fg=RED)



def Reset_Time():
    global IsTimer_ACTIVE
    global rep
    rep=0
    IsTimer_ACTIVE = False
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro-Day28")
window.config(width=40,height=40,bg= YELLOW)







count=120
canvas=Canvas(width=200,height=224, bg=YELLOW,highlightthickness=0 )
Title_label=Label(text="Timer", font=(FONT_NAME,25,"bold"), fg=GREEN, bg=YELLOW)
Title_label.grid(row=0,column=1)
#===this is the fucntion which get image from files and load it into out project
tomato_image =PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100,116,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))

canvas.grid(row=1,column=1)
#
start_btn=Button(text="Start" ,highlightthickness=0,command=start_time  )
start_btn.grid(row=3,column=0)
reset_btn=Button(text="Reset",highlightthickness=0, command=Reset_Time )
reset_btn.grid(row=3,column=2)


check_mark=Label(text="✓" ,fg=GREEN, bg=YELLOW   )
check_mark.grid(row=3,column=1)

IsTimer_ACTIVE=False






window.mainloop()