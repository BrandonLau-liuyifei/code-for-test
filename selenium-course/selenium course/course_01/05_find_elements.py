__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
Elements=browser.find_elements_by_class_name("loginInput")
print(type(Elements),len(Elements))
for i in Elements:
    i.clear()
Elements[0].send_keys("sup")
sleep(2)
Elements[1].send_keys("s1234567")
sleep(2)
Elements1=browser.find_elements_by_id("button_submit")
print(type(Elements1),len(Elements1))
Elements1[0].click()
sleep(2)

browser.quit()