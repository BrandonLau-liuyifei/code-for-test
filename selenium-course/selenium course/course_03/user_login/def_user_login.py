__author__ = 'Administrator'
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium_day3.shijianchuo.def_shijianchuo import jietu
# 定义函数，实现用户登录的过程
def login_sup(browser):
    try:
        browser.get("http://127.0.0.1:8080/oa")
        # 设置动态等待，判断所有符合class属性为logininput的元素全部加载完成，然后再执行后续脚本
        # 用到的方法：presence_of_all_elements_located
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
    except Exception as e:
        jietu(browser,"登录报错")
        raise e

# 定义函数，实现使用不同的用户名密码登录的过程
def login_by_different_username_password(browser,username,password):
    try:
        browser.get("http://127.0.0.1:8080/oa")
        # 设置动态等待，判断所有符合class属性为logininput的元素全部加载完成，然后再执行后续脚本
        # 用到的方法：presence_of_all_elements_located
        WebDriverWait(browser,10).until(ec.presence_of_all_elements_located((By.CLASS_NAME,"loginInput")))
        # 输入用户名
        browser.find_element_by_xpath('//input[@class="loginInput"]').clear()
        browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys(username)
        # 输入密码
        browser.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        # 设置动态等待，判断登录按钮的value值是否出现预期的登录两个字
        # 用到的方法：text_to_be_present_in_element_value
        WebDriverWait(browser,10).until(ec.text_to_be_present_in_element_value((By.ID,"button_submit"),"登录"))
        # 点击登录按钮
        browser.find_element_by_xpath('//input[@id="button_submit"]').click()
    except Exception as e:
        jietu(browser,"登录报错")
        raise e