import requests
import os
from dotenv import load_dotenv

class FlightSearch:

    def __init__(self,code="TESTING",target_price=0):
        load_dotenv()
        self.Amadeus_key = os.getenv("Amadeus_key")
        self.Amadeus_secret = os.getenv("Amadeus_secret")
        self.Iata_code=code
        self.max_price=target_price
        self.token=self.Setup_Connection()
        self.get_IATA_code("PARIS")

        print(self.token)

    #This class is responsible for talking to the Flight Search API.
    def get_Code(self,cityname):
        print(f"city name:{cityname} ")
        return ""
    def Setup_Connection(self):
        # This function will give us the access_token which we have to attach in every api call
        api_header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        Data = {
            "grant_type": "client_credentials",
            "client_id": self.Amadeus_key,
            "client_secret": self.Amadeus_secret
        }
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        response = requests.post(url=url, data=Data, headers=api_header)
        access_token = response.json()["access_token"]

        return access_token
    def get_IATA_code(self,city_name):
        headers = {
            "Authorization": f"Bearer {self.token}",
        }
        data={
            "countryCode": "FR",
            "keyword":city_name,


        }
        Url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        code_data=requests.get(url=Url,params=data,headers=headers)
        print(f"iata code: { code_data.json()["data"][0]}")

    def CheckFlights(self,DestinationCode,OriginCode,from_time,to_time):

        url = "https://test.api.amadeus.com/v1/shopping/flight-offers"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        parameters={
            "originLocationCode":OriginCode,
            "destinationLocationCode":DestinationCode,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate":to_time.strftime("%Y-%m-%d"),
            "adults":1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }
        response=requests.get(url=url,headers=headers,params=parameters)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()

    def Getoffers(self):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {
            "data": {
                "type": "flight-offer-pricing",
                "flightOffers": [
                    {
                        # insert your flight-offer object you got earlier from search API
                        "id": "1",
                        "source": "GDS",
                        "price": {
                            "currency": "USD",
                            "total": "500.00"
                        }
                    }
                ],
                "payments": [
                    {
                        "brand": "VISA",
                        "binNumber": "4111111111111111",
                        "flightOfferIds": ["1"]
                    }
                ],
                "travelers": [
                    {
                        "id": "1",
                        "dateOfBirth": "1990-01-01"
                    }
                ]
            }
        }
        response = requests.post(url, headers=headers, json=body)

        print(response.json())
