USERNAME="lubnahnyar"
PASSWORD="Usama.03488shafiq"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep, time
class InstagramBot:
    def __init__(self):
        
        self.driver = webdriver.Chrome()
    def LoginAcc(self):
        self.driver.get("https://www.instagram.com/?flo=true")
        sleep(2)
        username=self.driver.find_element(By.XPATH,  '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        username.send_keys(USERNAME,Keys.ENTER)
        password=self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(PASSWORD,Keys.ENTER)
        sleep(150)
        #Check If save info panel appear
        save_login_prompt=self.driver.find_elements(By.XPATH,"//div[contains(text(),'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()
        sleep(5)
         # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
 
user=InstagramBot()
user.LoginAcc()