from bs4 import BeautifulSoup
import requests
#-------Selenium-----------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep, time
#--------End--------------------

#-----------Selenium Start-------------------
class DataEntryBot:
    def __init__(self):
         self.driver = webdriver.Chrome()
    
    def EnterData(self, Address="",Price="",Link=""):
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd_FOY9kmETmStczqNDpKTrrsube-htdVevw1MKmjqT9BoP-g/viewform")
        sleep(2)
        addres =self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        addres.send_keys(Address,Keys.ENTER)
        price=self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price.send_keys(Price,Keys.ENTER)
       
        linkK=self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        linkK.send_keys(Link,Keys.ENTER)
        btn=self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        btn.click()
        sleep(5)
      
        #btn=self.driver.find_element(By.XPATH,'')

#------------BeautiFul Soup--------------
data= requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(data.text, 'html.parser')
Options_List=soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
Links_list=soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
Address_list=[]
LinkList=[]
for add in Links_list:
    Address=add.find("address")
    LinkList.append(add.get("href"))
    Address_list.append(Address.text.strip())
    print(Address.text)


for i in Options_List:
    cleaned = i.text.replace("+", "")
    print(cleaned)

#------------Beautiful Soup End-----------------
bot=DataEntryBot()
int=0
for int in range(0,len(Links_list)):
    bot.EnterData(Address_list[int],Options_List[int],LinkList[int])

