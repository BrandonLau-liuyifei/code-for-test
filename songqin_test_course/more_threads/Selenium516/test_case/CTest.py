import time

import unittest2
from selenium import webdriver


class CTest(unittest2.TestCase):
    def test_c(self):
        self.driver = webdriver.Chrome()
        print("开始执行C测试用例")
        self.driver.get("http://www.atstudy.com")
        time.sleep(15)
        self.assertTrue(False)
    def tearDown(self):
        self.driver.quit()
        print("测试用例C执行完成")