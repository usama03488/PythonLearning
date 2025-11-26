import requests
import os
from dotenv import load_dotenv

class DataManager:
    def __init__(self):
        load_dotenv()
        self.Sheety_Endpoint = "https://api.sheety.co/e5fab00e413cee4da934884801a3ca4b/flightDeals/prices"
        self.data_list=[]
        self.sheety_token = os.getenv("AUTHORIZATION")


    def Add_row(self,city,Iata,price):
        header_data={
            "Content-Type": "application/json",
            "Authorization": self.sheety_token
        }
        body={
            "prices":{
                "city":city,
                "iata code":Iata,
                "lowest price":price
            }
        }
        response=requests.post(url=self.Sheety_Endpoint, json=body,headers=header_data)
        print(response.json())
    def update_row(self,city,Iata,price,id):
        print(f"iata code: {Iata} ")
        header_data = {
            "Content-Type": "application/json",
            "Authorization": self.sheety_token
        }
        body = {
            "price": {
                "iataCode": Iata,
            }
        }
        response = requests.put(url=self.Sheety_Endpoint+f"/{id}", json=body, headers=header_data)
        print(response.json())
    def Get_data(self):
        print(self.sheety_token)
        header_data = {
            "Content-Type": "application/json",
            "Authorization": self.sheety_token
        }
        data=requests.get(url=self.Sheety_Endpoint,headers=header_data)
        # print(data.json())
        self.data_list=data.json()
        return self.data_list
    #this delete function will delete entire row
    def Delete_data(self, city, Iata, price, id):

        header_data = {
            "Content-Type": "application/json",
            "Authorization": self.sheety_token
        }

        response = requests.put(url=self.Sheety_Endpoint + f"/{id}", json=body, headers=header_data)
        print(response.json())


    #This class is responsible for talking to the Google Sheet.
