__author__ = 'Administrator'
from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080")
sleep(2)
# 使用xpath结合其他属性定位用户名输入框
browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
sleep(1)
# 使用xpath结合name属性定位用户名输入框
browser.find_element_by_xpath('//input[@name="loginId"]').clear()
sleep(1)
# 使用xpath结合tabindex属性定位用户名输入框
browser.find_element_by_xpath('//input[@tabindex="1"]').send_keys("sup")
sleep(1)
# 使用xpath结合type属性定位用户名输入框
browser.find_element_by_xpath('//input[@type="text"]').clear()
sleep(1)
# 使用xpath结合多个属性定位用户名输入框
browser.find_element_by_xpath('//input[@class="loginInput" and @name="loginId" and @tabindex="1" and @type="text"]').send_keys("sup")
sleep(2)

# 使用xpath结合多个属性定位密码输入框
browser.find_element_by_xpath('//input[@class="loginInput" and @name="password"]').send_keys("s1234567")
sleep(2)

# 使用xpath结合多个属性定位登录按钮
browser.find_element_by_xpath('//input[@id="button_submit"]').click()
sleep(2)

# 使用xpath结合text()定位新建事项
browser.find_element_by_xpath('//a[text()="新建事项"]').click()
sleep(2)

# 使用xpath结合contains方法来定位已发事项
browser.find_element_by_xpath('//a[contains(text(),"已发")]').click()
sleep(2)

# 使用xpath结合contains方法来定位已办事项上方的图片
browser.find_element_by_xpath('//img[contains(@src,"done.png")]').click()
sleep(2)

# 使用xpath结合其他属性定位密码修改
browser.find_element_by_xpath('//a[@class="black" and @title="密码修改" and text()="密码修改"]').click()
sleep(2)

browser.quit()
