__author__ = 'Administrator'
import unittest
from selenium import webdriver
from time import sleep
from selenium_day3.user_login.def_user_login import login_by_different_username_password
from selenium_day3.shijianchuo.def_shijianchuo import jietu

# 定义一个类，这个类必须继承自unittest.TestCase这个类
class UserLoginTestCase(unittest.TestCase):
    # 定义setUp这个前置方法，执行用例之前的公共操作
    def setUp(self):
        # 驱动浏览器，设置最大化
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()

    # 定义tearDown这个后置方法，执行用例之后的公共操作
    def tearDown(self):
        # 关闭浏览器
        self.browser.quit()

    # 定义方法，方法名字以test_开头，实现正常场景登录，登录完成后使用assertEqual进行断言
    def test_01_login_by_correct_username_password(self):
        try:
            login_by_different_username_password(self.browser,"sup","s1234567")
            sleep(2)
            # 使用登录后的用户名进行断言
            username_ele = self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[1]/label')
            username = username_ele.text
            self.assertEqual(username,"苏鹏")
        except Exception as e:
            jietu(self.browser,"登录异常")
            raise e

    # 定义方法，使用正确的用户名和错误的密码登录，登录完成后提示错误信息使用assertEqual进行断言
    def test_02_login_by_correct_username_wrong_password(self):
        try:
            login_by_different_username_password(self.browser,"sup","s1234567888")
            sleep(2)
            # 使用错误提示信息的内容进行断言
            tips_ele = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]')
            tips = tips_ele.text
            self.assertEqual("登录名或密码错误，请重试！",tips)
        except Exception as e:
            jietu(self.browser,"登录异常")
            raise e

    # 定义方法，使用错误的用户名和正确的密码登录，登录完成后提示错误信息使用assertEqual进行断言
    def test_03_login_by_wrong_username_correct_password(self):
        try:
            login_by_different_username_password(self.browser,"supppp","s1234567")
            sleep(2)
            # 使用错误提示信息的内容进行断言
            tips_ele = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]')
            tips = tips_ele.text
            self.assertEqual("登录名或密码错误，请重试！",tips)
        except Exception as e:
            jietu(self.browser,"登录异常")
            raise e

    # 定义方法，使用正确的用户名空的密码进行登录，完成后使用是否存在提示信息assertIsNotNone进行断言
    def test_04_login_by_correct_username_null_password(self):
        try:
            login_by_different_username_password(self.browser,"sup","")
            sleep(2)
            tips_ele = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]')
            self.assertIsNotNone(tips_ele)
        except Exception as e:
            jietu(self.browser,"登录异常")
            raise e

    # 定义方法，使用空的用户名正确的密码进行登录，完成后使用是否存在提示信息assertIsNotNone进行断言
    def test_05_login_by_null_username_correct_password(self):
        try:
            login_by_different_username_password(self.browser,"","s1234567")
            sleep(2)
            tips_ele = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]')
            self.assertIsNotNone(tips_ele)
        except Exception as e:
            jietu(self.browser,"登录异常")
            raise e

    # 定义方法，假定登录按钮不可点击，输入用户名密码后获取登录按钮的点击状态，使用assertTrue进行断言
    def test_06_login_button_clickable(self):
        try:
            self.browser.get("http://172.21.5.51:8080/oa")
            sleep(2)
            # 输入用户名
            self.browser.find_element_by_xpath('//input[@class="loginInput"]').clear()
            self.browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
            # 输入密码
            self.browser.find_element_by_xpath('//input[@name="password"]').send_keys("s1234567")
            # 获取登录按钮的状态
            button_status = self.browser.find_element_by_xpath('//input[@id="button_submit"]').is_enabled()
            self.assertTrue(button_status)
        except Exception as e:
            jietu(self.browser,"登录异常")
            raise e

if __name__=="__main__":
    unittest.TextTestRunner()