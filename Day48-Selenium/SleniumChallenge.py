from selenium import webdriver
from selenium.webdriver.common.by import By
import random
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
Listdata=driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
TitleList=driver.find_elements(By.CSS_SELECTOR, value=".event-widget a")
events={}
for i in range(0,len(Listdata)):
    events[i]={
        "time":Listdata[i].text,
        "name":TitleList[i].text
    }

print(events)
driver.quit()