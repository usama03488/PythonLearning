import requests
from twilio.rest import Client
KEY="key"
Lat=31.520370
Lon=74.358749
URL="https://api.openweathermap.org/data/2.5/weather"
#---Twilio credentials---
#Account_id="your acc id"
#Auth_token="Auth-token"
     #lat={Lat}&lon={Lon}&appid={KEY}"
parameter={
    "lat":Lat,
    "lon":Lon,
    "appid":KEY
}
response=request.get(URL,params=parameters)
response.raise_for_status()
print(response.json())
data=response.json()
is_Rain=False
for Hour_data in data["List"]:
    if(Hour_data["weather"][0]["id"])<700):
        is_Rain=True;
if(is_Rainn):
    client=Client(Account_id,Auth_token)
    message=client.message\.create(
        body="Getting from from osama app",
        from="sender-number here",
            to="send  number"
    )


