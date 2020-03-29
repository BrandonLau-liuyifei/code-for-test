__author__ = 'Administrator'
from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080")
sleep(2)
browser.find_element_by_xpath('//input[@class="loginInput"]').clear()
sleep(2)
browser.find_element_by_xpath('//input[@name="loginId"]').send_keys("sup")
sleep(2)
browser.find_element_by_xpath('//input[@tabindex="1"]').clear()
sleep(2)
browser.find_element_by_xpath('//input[@type="text"]').clear()
sleep(2)
browser.find_element_by_xpath('//input[@name="loginId" and @name="loginId" and @tabindex="1" and @type="text"]').send_keys("sup")
sleep(2)
browser.find_element_by_xpath('//input[@class="loginInput" and @type="password" and @tabindex="2" and @name="password"]').send_keys("s1234567")
sleep(2)
browser.find_element_by_xpath('//input[@id="button_submit"]').click()
sleep(2)
browser.find_element_by_xpath('//a[text()="新建事项"]').click()
sleep(2)
browser.find_element_by_xpath('//a[contains(text(),"已发")]').click()
sleep(2)
browser.find_element_by_xpath('//img[contains(@src,"done.png")]').click()
sleep(2)
browser.find_element_by_xpath('//a[@class="black" and @title="密码修改" and text()="密码修改"]').click()
sleep(2)


