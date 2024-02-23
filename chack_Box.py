from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
class chack():
    def chakbox(self):
        driver = webdriver.Chrome()
        driver.get("https://artoftesting.com/samplesiteforselenium")
        driver.maximize_window()
        chack = driver.find_element(By.CLASS_NAME,"Performance").click()
        sleep(5)
        chack = driver.find_element(By.CLASS_NAME,"Automation").click()
        sleep(5)
chacking = chack()
chacking.chakbox()