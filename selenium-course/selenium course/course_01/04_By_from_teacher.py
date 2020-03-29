__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
browser.find_element(By.CLASS_NAME,"loginInput").send_keys("sup")
sleep(2)
browser.find_element(By.NAME,"password").send_keys("s1234567")
sleep(2)
browser.find_element(By.ID,"button_submit").click()
sleep(2)
browser.find_element(By.LINK_TEXT,"新建事项").click()
sleep(2)
browser.find_element(By.PARTIAL_LINK_TEXT,"已发").click()
sleep(2)
browser.find_element(By.CSS_SELECTOR,'[src="/oa/common/images/leftmenu/collaborate/done.png"]').click()
sleep(2)
browser.find_element(By.XPATH,'//a[text()="待发事项"]').click()
sleep(2)
browser.find_element(By.TAG_NAME,"a").click()
sleep(2)
browser.quit()

