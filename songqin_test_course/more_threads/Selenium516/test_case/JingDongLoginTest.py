import time

from selenium import webdriver
import unittest


class JingDongLoginTest(unittest.TestCase):
    def test_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.jd.com/")
        driver.find_element_by_css_selector("#ttbar-login > a:nth-child(1)").click()
        driver.find_element_by_link_text("账户登录").click()
        driver.find_element_by_id("loginname").clear()
        driver.find_element_by_id("loginname").send_keys("13922358271")
        driver.find_element_by_id("nloginpwd").send_keys("")
        time.sleep(15)
        driver.find_element_by_id("loginsubmit").click()
        time.sleep(15)
        cookies = driver.get_cookies()
        print(cookies)