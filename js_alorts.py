from selenium import webdriver
from time import sleep
class demoja():
    def javascript(self):
        driver = webdriver.Chrome()
        #driver.get("https://training.rcvacademy.com/")
        driver.maximize_window()
        driver.execute_script("window.open('https://training.rcvacademy.com/','_self')")
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[3];")
        driver.execute_script("arguments[0].click",demo_element)
        sleep(5)

demo = demoja()
demo.javascript()