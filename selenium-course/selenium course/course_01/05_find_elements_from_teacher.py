__author__ = 'Administrator'
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
elements = browser.find_elements_by_class_name('loginInput')
print(type(elements),len(elements))

for i in elements:
    i.clear()

elements[0].send_keys("sup")
sleep(2)

elements[1].send_keys("s1234567")
sleep(2)

elements1 = browser.find_elements(By.ID,"button_submit")
print(type(elements1),len(elements1))
elements1[0].click()
sleep(2)

browser.quit()