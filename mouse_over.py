from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
class morebutton():
    def more(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebutton = driver.find_element(By.XPATH,"//span[@class='more-arr']")
        sleep(2)
        achain = ActionChains(driver)
        achain.move_to_element(morebutton).perform()
        sleep(2)
        user = driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']")
        user.click()
        sleep(10)

find = morebutton()
find.more()