__author__ = 'Administrator'
# coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

DesiredCapabilities.INTERNETEXPLORER["ignoreProtectedModeSettings"] = True
browser = webdriver.Ie()
browser.get("http://127.0.0.1:8080/oa")
browser.find_element_by_name("loginId").clear()
browser.find_element_by_name("loginId").send_keys("sup")
browser.find_element_by_name("password").send_keys("s1234567")
browser.find_element_by_id("button_submit").click()
time.sleep(5)
browser.quit()


