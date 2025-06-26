from tkinter import *
MILE_ONE=1.60


window=Tk()
window.title("Mile to km Converter")
window.config(padx=20,pady=20)
window.minsize(width=600,height=600)
"""jk"""
my_label=Label(text="My first converter", font=("Arial",26,"bold") )

my_label.config(padx=5,pady=5)
my_label.grid(column=2,row=0)

"""add input field"""
input=Entry(width=30)
input.grid(column=2,row=2)


"""add texts"""
text1= Label(text="miles")
text1.grid(column=3,row=2)


text2= Label(text=" is equal to")
text2.grid(column=0,row=3)


text3= Label(text="km")
text3.grid(column=3,row=3)

result_label = Label(text="0")
result_label.grid(column=2, row=3)
def convert():
    """WE WILL CONVERT MILES TO KILOMERTER here and then assign this add this into text"""
    km=MILE_ONE*float(input.get())
    """this is a multi string in our gui"""
    result_label.config(text=f"miles is equal to {km:.2f} kilometers")
   # text.grid(column=2,row=3)

#add ur items here

btn=Button(text="Calculate", command=convert)
btn.grid(column=2,row=4)
















window.mainloop()