import requests
import Tkinter

response=requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data=response.json()
print(data["iss_position"])
Longitude=data["iss_position"]["longitude"]
Latitude=data["iss_position"]["latitude"]

