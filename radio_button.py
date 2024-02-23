from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
class radio():
    def radiobutton(self):
        driver = webdriver.Chrome()
        driver.get("https://artoftesting.com/samplesiteforselenium")
        driver.maximize_window()
        driver.find_element(By.NAME,value="gender").click()
        print(driver)
        sleep(2)
        driver.find_element(By.ID,value="female").click()
        print(driver)
        sleep(2)

find = radio()
find.radiobutton()