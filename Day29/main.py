from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def Generate_pass():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password = []
    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    # for letter in range(0,nr_letters):
    #     password =password + random.choice(letters)

    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    # for let in range(0, nr_numbers):
    #     password+= random.choice(numbers)
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    # for let in range(0, nr_symbols) :
    #     password += random.choice(symbols).
    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)
    password = "".join(password_list)
    Password_input.insert(0,password)
    #pyper is used to automatically copy text which will be needed to paste somewhere
    pyperclip.copy(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# Hard_pass=""
# total_iteration = nr_letters+ nr_symbols+ nr_numbers
# for i in range(0, total_iteration):
#     pick=random.randrange(0,3)
#     if pick==0:
#         Hard_pass+=random.choice(letters)
#     elif pick==1:
#         Hard_pass +=random.choice(numbers)
#     elif pick==2:
#         Hard_pass +=random.choice(symbols)
# print(f"Hard password is {Hard_pass}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data(**kwargs):
    email=kwargs['email']
    website=kwargs['website']
    password=kwargs['password']
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }

    if(len(email ) >0 and len(website)>0 and len(password)>0):
        is_ok = messagebox.askokcancel(title="this is the enters data",
                                       message=f"email: {kwargs['email']} \n website: {kwargs['website']} \n password: {kwargs['password']} ")

        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file,  indent=4)
                # now we use load to load it
                # read ->
                # data=json.load(data_file)
                # --jason update---
                # step 1 load data/read data
                data = json.load(data_file)
            # step2 replace data with new data
        except (FileNotFoundError, json.JSONDecodeError):
            print("data is not there")
            with open("data.json", "w") as data_file:

                json.dump(new_data, data_file, indent=4)
        else:

            data.update(new_data)
            # step3 write updated data into file
            with open("data.json", "w") as data_file:

                json.dump(data, data_file, indent=4)
    else:
        is_ok=False
        messagebox.showinfo(title="Error", message="You have some blank fields ")



    if is_ok == True:




# in day 30 we will make a jason file now and try to read and write in it
        # with open("data.txt", "a") as data:
        #     data.write(f"\n")
        for key, value in kwargs.items():
            print(f"{key} = {value}")
            #data.write(f"{value} |")
            website_input.delete(0, END)
            Password_input.delete(0, END)























def search_Credentials():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except:
        print("we have a empty storage")
    else:
        web=website_input.get()
        if web in data:
            values = data[web]
            email = values["email"]
            password = values["password"]
            messagebox.showinfo(title="Credentials", message=f"Your data\n"
                                                             f"Email: {email} \n"
                                                             f"Password: {password} ")
        else:
            messagebox.showinfo(title="Erroe", message=f"No such website data exits in data base" )








# ---------------------------- UI SETUP ------------------------------- #
def save():
    save_data(email=Email_input.get(),website=website_input.get(),password=Password_input.get())
def generatepass():
    string=""
    for i in range(7):
        string= random.randint

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas=Canvas(height=400, width=400 )

logo=PhotoImage(file= "logo.png")
canvas.create_image(200,200,image=logo)
canvas.grid(row=1, column=2)

website=Label(text= "website")
website.grid(row=2,column=1)
website_input=Entry(width=35)
website_input.grid(column=2,row=2,columnspan=2)
website_input.focus()

search_btn=Button(text="Search",highlightthickness=0,command=search_Credentials)
search_btn.grid(row=2,column=3)

Email=Label(text= "Email/username")
Email.grid(row=3,column=1)
Email_input=Entry(width=35)
Email_input.grid(column=2,row=3,columnspan=2)


password_label=Label(text= "Password")
password_label.grid(row=4,column=1)
Password_input=Entry(width=20)
Password_input.grid(column=2,row=4,columnspan=1)

# insert used to insert some prefilled string o means the index where we want to add that text

Gen_btn=Button(text="Generate password",highlightthickness=0, command= Generate_pass)
Gen_btn.grid(column=3,row=4)


Addbtn=Button(text="Add", width=25,highlightthickness=0,command=save )
Addbtn.grid(column=2,row=5,columnspan=2)









window.mainloop()