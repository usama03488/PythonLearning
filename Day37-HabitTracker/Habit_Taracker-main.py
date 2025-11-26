import requests
from datetime import datetime, timedelta
Endpoint="https://pixe.la/v1/users"

TOKEN="j321k4bnbk2h3j4bhsd"
USERNAME="osamashafiq"
GraphId="graph1"
user_parameter={
    "Token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# this is for creating a user on pixela but i have created it already so no need to call it againss
# response=requests.post(url=Endpoint,json=user_parameter)
# print(response.text)
 #////creating graph
Graph_Endpoint=f"{Endpoint}/{USERNAME}/graphs"
graph_parameter={

    "id":"graph1",
    "name":"Practice Graph",
    "unit":"commit",
    "type":"int",
    "color":"shibafu"
}
Header={
    "X-USER-TOKEN":TOKEN
}
# response1=requests.post(url=Graph_Endpoint,json=graph_parameter,headers=Header)
# print(response1.text)
#----------------------------------
PixelEndpoint=f"{Graph_Endpoint}/{GraphId}"
date=datetime.today().date()
formatted = date.strftime("%Y%m%d")

Pixel_parameter={
    "date":formatted,
    "quantity":"20"
}
# pixel_response=requests.post(url=PixelEndpoint,json=Pixel_parameter,headers=Header)
# print(pixel_response.text)
#-----------------------Update request (PUT)--------------------
Update_Endpoint=f"{PixelEndpoint}/20250813"
pixel_update_parameter={
    "quantity": "199"
}
# updated_response=requests.put(url=Update_Endpoint,json=pixel_update_parameter,headers=Header)
# print(updated_response.text)
#------------------------Delete Request--------------------------------------/
Delete_Response=requests.delete(url=Update_Endpoint,headers=Header)
print(Delete_Response.text)