import requests
from datatime import datetime
import smptlib
my_email = "usama.connexus@gmail.com"
password = "rzlb yrvo wcaj obmd"
MY_LAT=31.520370
MY_LNG=74.358749
def is_iss_overhead():
    iss_response=requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data=iss_response.json()
    print(data["iss_position"])
    Longitude=float(data["iss_position"]["longitude"])
    Latitude=float(data["iss_position"]["latitude"])
    diff_lat=MY_LAT-longitude
    diff_lng=MY_LNG-latitude
    # if((diff_lat <5 or diff_lat >-5) and (diff_lng>-5 or diff_lng<5) ):
    if MY_LAT-5 <= Longitude <= MY_LAT+5 and MY_LNG-5<=Latitude <= MY_LNG+5:
        print("iss satelited is really close to your location")
        return True

def Is_night():

    parameter={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }
    response=requests.get(url="http://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # splited=sunrise.split("T")
    # time_split= splited[1].split(":")
    # print(time_split)
    time_now=datatime.now().hour()
    if time_now >= sunset and time_now< sunrise:
        return True
    else:
        return False

if is_night()==True and is_iss_overhead()==True:
    random_message="Congratulation iss satelite is close to your location and it is night time"
    with smptblib.SMTP("smtp.gmail.com") as connection:
        conection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ossaama.shafiq@gmail.com",
                            msg=f"Subject:System generated Motivational Mail \n\n {random_message}")


