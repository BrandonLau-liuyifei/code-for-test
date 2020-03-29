__author__ = 'Administrator'
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
# 使用css结合class属性定位用户名输入框
browser.find_element_by_css_selector(".loginInput").clear()
sleep(1)
# 使用css结合name属性定位用户名输入框
browser.find_element_by_css_selector('[name="loginId"]').send_keys("sup")
sleep(1)
# 使用css结合tabindex属性定位用户名输入框
browser.find_element_by_css_selector('[tabindex="1"]').clear()
sleep(1)
# 使用css结合type属性定位用户名输入框
browser.find_element_by_css_selector('[type="text"]').send_keys("sup")
sleep(1)
# 使用css结合多个属性定位用户名输入框
browser.find_element_by_css_selector('.loginInput[name="loginId"][tabindex="1"][type="text"]').clear()
browser.find_element_by_css_selector('.loginInput[name="loginId"][tabindex="1"][type="text"]').send_keys("sup")
sleep(2)

# 使用css结合多个属性定位密码输入框
browser.find_element_by_css_selector('.loginInput[name="password"][tabindex="2"][type="password"]').send_keys("s1234567")
sleep(2)

# 使用css结合多个属性定位登录按钮
browser.find_element_by_css_selector('#button_submit.loginbutton[type="button"]').click()
sleep(2)
browser.quit()

