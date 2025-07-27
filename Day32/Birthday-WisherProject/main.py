import pandas
import csv
import datetime as dt
import smtplib
import random
##################### Extra Hard Starting Project ######################

my_email = "usama.connexus@gmail.com"
password = "rzlb yrvo wcaj obmd"
def SendMail(to, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to,
                            msg= f"Subject:HAPPY BIRTHDAY!"
                                 f"\n\n {message}")



PLACEHOLDER="[NAME]"
time= dt.datetime.now()
current_day=time.day
current_month=time.month

data=pandas.read_csv("birthdays.csv")
dataframe=data.to_dict(orient="records")


for row in dataframe:
    print(f"current data: {current_day}")
    if int(row["day"]) == current_day and int(row["month"]==current_month):
        with open("Templates/letter_2.txt") as letter2:
            message = letter2.read()
            personalized = message.replace(PLACEHOLDER, row["name"])
            print("Now we will print this message:")
            print(personalized)
        x=random.randint(1, 3)
        if(x==1):
            file_path = "Templates/letter_1.txt"
        elif(x==2):

            file_path="Templates/letter_2.txt"
        elif (x == 3):
            file_path = "Templates/letter_3.txt"
        with open(file_path) as letter2:

            Message=letter2.read()
            Updated_message=Message.replace(PLACEHOLDER,row["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
            SendMail(row["email"], Updated_message)

        #print(f"today is {row["name"]} birthday ")


# 4. Send the letter generated in step 3 to that person's email address.




