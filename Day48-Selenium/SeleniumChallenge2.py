from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Credentials import cred
#keep chrome driver open we have to use chrome_options
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver=webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
firstname=driver.find_element(By.CLASS_NAME,value="top")
firstname.send_keys(cred.NAME,Keys.ENTER)
Lastname=driver.find_element(By.CLASS_NAME,value="middle")
Lastname.send_keys(cred.LAST_NAME,Keys.ENTER)
Mail=driver.find_element(By.CLASS_NAME,value="bottom")
Mail.send_keys(cred.EMAIL,Keys.ENTER)
BTN=driver.find_element(By.CLASS_NAME,value="btn")
BTN.click()


