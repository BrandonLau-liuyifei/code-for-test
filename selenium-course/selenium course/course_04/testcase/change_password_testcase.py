__author__ = 'Administrator'
import unittest
from selenium import webdriver
from time import sleep
from selenium_day3.user_login.def_user_login import login_by_different_username_password
from selenium_day3.shijianchuo.def_shijianchuo import jietu
from selenium_day3.change_password.def_change_password import change_password

class ChangePasswordTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        login_by_different_username_password(self.browser,"sup","s1234567")
        sleep(2)

    def tearDown(self):
        self.browser.quit()

    def test_01_wrong_old_password(self):
        try:
            change_password(self.browser,"s123123123","s1111111","s1111111")
            sleep(2)
            # 断言
            tips = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]').text
            self.assertEqual("旧密码输入错误！",tips)
        except Exception as e:
            jietu(self.browser,"修改密码报错")
            raise e

    def test_02_different_new_password(self):
        try:
            change_password(self.browser,"s1234567","s1111111","s2222222")
            sleep(2)
            # 断言
            tips_ele = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]')
            self.assertIsNotNone(tips_ele)
        except Exception as e:
            jietu(self.browser,"修改密码报错")
            raise e

unittest.TextTestRunner()