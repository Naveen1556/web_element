from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
username = driver.find_elements(by=By.ID,value='login-input')
username[0].send_keys("naiknaveen155@gmail.com")
sleep(5)
