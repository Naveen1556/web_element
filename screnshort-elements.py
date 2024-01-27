from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
driver.maximize_window()
sleep(2)

countinu_button = driver.find_elements(By.XPATH,"//button[@id='login-continue-btn']")
countinu_button[0].screenshot(".C:\\test.png")
countinu_button[0].click()
driver.get_screenshot_as_file("\\test1.png")
sleep(1)