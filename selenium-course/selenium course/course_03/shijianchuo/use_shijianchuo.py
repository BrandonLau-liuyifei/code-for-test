__author__ = 'Administrator'
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By

# from selenium_day3.shijianchuo import def_shijianchuo
from selenium_day3.shijianchuo.def_shijianchuo import jietu

browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8080/oa")

WebDriverWait(browser,10).until(ec.presence_of_all_elements_located((By.CLASS_NAME,"loginInput")))
# 输入用户名
browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
# 输入密码
browser.find_element_by_xpath('//input[@name="password"]').send_keys("s1234567")

# 设置动态等待，判断登录按钮的value值是否出现预期的登录两个字
# 用到的方法：text_to_be_present_in_element_value
WebDriverWait(browser,10).until(ec.text_to_be_present_in_element_value((By.ID,"button_submit"),"登录"))
# 点击登录按钮
browser.find_element_by_xpath('//input[@id="button_submit"]').click()

# 点击新建事项之前，设置动态等待，判断新建事项是否可以点击
# 用到的方法：element_to_be_clickable
WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.LINK_TEXT,"新建事项")))
# def_shijianchuo.jietu(browser,"首页截图")
jietu(browser,"首页截图")
browser.quit()