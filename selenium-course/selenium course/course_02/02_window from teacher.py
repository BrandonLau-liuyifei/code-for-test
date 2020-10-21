__author__ = 'Administrator'
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
# 打开万年历和计算器
browser.find_element_by_xpath('//a[text()="万年历"]').click()
sleep(2)
browser.find_element_by_xpath('//a[text()="计算器"]').click()
sleep(2)
# 获取打开网页的句柄
windows = browser.window_handles
print(type(windows),len(windows))

# 切换到万年历的页面中，点击下一月和上一年
browser.switch_to.window(windows[1])
browser.find_element_by_xpath('//a[@id="yuejia"]').click()
sleep(2)
browser.find_element_by_xpath('//a[@id="nianjian"]').click()
sleep(2)

# 切换到计算器的页面中，计算4+9=
browser.switch_to.window(windows[2])
# 点击4的按钮
browser.find_element_by_xpath('//input[@name="k4"]').click()
sleep(2)
# 点击+的按钮
browser.find_element_by_xpath('//input[@value=" + "]').click()
sleep(2)
# 点击9的按钮
browser.find_element_by_xpath('//input[@name="k9"]').click()
sleep(2)
# 点击=的按钮
browser.find_element_by_xpath('//input[@value=" ＝ "]').click()
sleep(2)

# 关闭计算器的窗口
browser.close()
sleep(2)

# 关闭万年历的窗口，还需要切换到万年历的窗口中再关闭
browser.switch_to.window(windows[1])
browser.close()
sleep(2)

# 登录OA，需要切换到登录的页面中
browser.switch_to.window(windows[0])
# 使用sup的账号登录
browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
sleep(2)
browser.find_element_by_xpath('//input[@name="password"]').send_keys("s1234567")
sleep(2)
browser.find_element_by_xpath('//input[@id="button_submit"]').click()
sleep(2)

browser.quit()