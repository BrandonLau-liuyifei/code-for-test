#coding=utf8
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
first_url = "https://www.baidu.com/"
second_url = "http://news.baidu.com/"

print("now access to %s" % first_url)
driver.get(first_url)
sleep(2)

print("now acess to %s" % second_url)
driver.get(second_url)
sleep(2)

print("now back to %s" % first_url)
driver.back()
sleep(2)

print("now forword to %s" % second_url)
driver.forward()
sleep(2)

driver.quit()