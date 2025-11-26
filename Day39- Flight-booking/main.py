#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
#-- first i have to send token request by including they secrect and key
ORIGIN_CITY_IATA = "LON"
Flight_search=FlightSearch()

# print(Flight_search.Setup_Connection())
#2 get IATA CODE OF CITY

#////this is a data sheet object which will help to add and get data from sheet
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
def update_Iatacode():
    for item in SheetData:
        code = Flight_search.get_Code(item["city"])
        item["iataCode"] = code
        sheet_Data.update_row(item["city"], item["iataCode"], item["lowestPrice"], item["id"])

update_Iatacode()
sheet_Data=DataManager()
SheetData=sheet_Data.Get_data()["prices"]
print(SheetData)
for destination in SheetData:
    print(f"Getting flights for {destination['city']}...")
    flight=Flight_search.CheckFlights(ORIGIN_CITY_IATA,destination["iataCode"]
                                      ,tomorrow,six_month_from_today)
    print(flight)





