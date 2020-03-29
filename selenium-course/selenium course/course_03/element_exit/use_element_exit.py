__author__ = 'Administrator'
from selenium import webdriver
from time import sleep

from selenium_day3.element_exit import def_element_exit

browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
# 调用函数，判断用户名输入框是否存在
username_ele = def_element_exit.element_exit_by_xpath(browser,'//input[@class="loginInput"]')
if username_ele == True:
    browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
else:
    print("用户名输入框未找到。")

# 调用函数，判断密码输入框是否存在
password_ele = def_element_exit.element_exit_by_xpath(browser,'//input[@name="password"]')
if password_ele==True:
    browser.find_element_by_xpath('//input[@name="password"]').send_keys("s1234567")
else:
    print("密码输入框未找到。。。。")

# 调用函数，判断登录按钮是否存在
login_button = def_element_exit.element_exit_by_xpath(browser,'//input[@id="button_submit"]')
if login_button == True:
    browser.find_element_by_xpath('//input[@id="button_submit"]').click()
else:
    print("登录按钮未找到。。。。")

sleep(2)

# def_element_exit.text_click_jietu(browser,"新建事项")
# def_element_exit.text_click_jietu(browser,"已发事项")
# def_element_exit.text_click_jietu(browser,"已办事项")
# def_element_exit.text_click_jietu(browser,"待发事项")
# def_element_exit.text_click_jietu(browser,"待办事项")
# def_element_exit.text_click_jietu(browser,"综合查询")
# def_element_exit.text_click_jietu(browser,"退出登录")

list1 = ["新建事","已发事项","已办事项","待发事项","待办事项","综合查询","退出登录"]
for i in list1:
    def_element_exit.text_click_jietu(browser,i)
    sleep(2)

browser.quit()