import smtplib
import datetime as dt
import random
time= dt.datetime.now()
current_day=time.weekday()

my_email = "usama.connexus@gmail.com"
password = "rzlb yrvo wcaj obmd"
if(current_day==6):
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        random_message=random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ossaama.shafiq@gmail.com",
                            msg= f"Subject:System generated Motivational Mail \n\n {random_message}")



