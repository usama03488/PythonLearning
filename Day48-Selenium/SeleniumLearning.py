from selenium import webdriver
from selenium.webdriver.common.by import By
#keep chrome driver open we have to use chrome_options
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")
price= driver.find_element(By.CLASS_NAME, value="a-button-text").text
print(price)
DocumentationLink=driver.find_element(By.CSS_SELECTOR, value="#.className #tag here") #we will use a class tag and we
# can also pass any tag element which is inside that class without any name or id or class
#----------xpath----------
#WE CAN also use xpath to reah to any tag
# like this //*[@id="navFooter"]/div[4]/div/ul[1]/li[7]/a/h5

#driver.close() # this close function will only close the tab
#driver.quit() # this quit function will close the whole browser no matter how many tabs are there

