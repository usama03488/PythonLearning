import os
import requests
from datetime import datetime, timedelta
Nutrient_Endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
sheetyEndpoint=os.getenv("Sheety_Endpoint")
API_KEY = os.getenv("Api_key")
APP_ID = os.getenv("AppID")
print(APP_ID )
AUTH_CODE = os.getenv("Authentication_code")
Header_rep={
    "Content-Type": "application/json",
    "x-app-id":APP_ID ,
    "x-app-key":API_KEY
}
def get_filtered_Data():
    parameter = {
        "query": user_detail
    }
    response = requests.post(url=Nutrient_Endpoint, json=parameter, headers=Header_rep)

    print(response.json())
    exercise_data = response.json()["exercises"][0]
    exercise = exercise_data["user_input"]
    duration = exercise_data["duration_min"]
    calories = exercise_data["nf_calories"]
    return exercise, duration, calories
    # return Excercise_Data
Date=datetime.now().strftime("%d/%m/%y")
Time_now=datetime.now().strftime("%X")

def Add_Row():
    Header = {
        "Content-Type": "application/json",
        # If authentication is enabled in Sheety:
        "Authorization":AUTH_CODE
    }
    exercise, duration, calories =get_filtered_Data()
    Row_data={
        "sheet1":{
            "date": Date,
            "time": Time_now,
            "exercise":  exercise,
            "duration": duration,
            "calories": calories,
        }
    }
    row_add_response=requests.post(url=sheetyEndpoint,json=Row_data,headers=Header)
    row_add_response.raise_for_status()
    print(row_add_response.text)

#----Sheety Endpoint




user_detail=input("Tell me which Excercise you did: " )
Add_Row()

