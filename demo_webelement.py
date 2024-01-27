from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
class webelment():
    def element(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        user = driver.find_elements(By.XPATH,"//input[@id='user_name']")
        user[0].send_keys("naveennaik")
        password = driver.find_element(By.XPATH,"(//input[@id='user_pass'])[1]")
        password.send_keys("naveen")
        username = driver.find_element(By.XPATH, "//input[@id='login_button']")
        username.is_enabled()
        print(username)
        button = driver.find_elements(By.XPATH,"//input[@id='login_button']")
        button[0].click()
        select = driver.find_element(By.XPATH,"//select[@id='productType']")
        select.click()
        viwe = driver.find_element(By.XPATH,"//input[@id='viewButton']")
        viwe.is_enabled()
        sleep(10)

find = webelment()
find.element()