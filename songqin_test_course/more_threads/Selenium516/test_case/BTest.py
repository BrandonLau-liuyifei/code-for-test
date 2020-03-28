import time

import unittest2
from selenium import webdriver


class BTest(unittest2.TestCase):
    def test_b(self):
        self.driver = webdriver.Chrome()
        print("开始执行B测试用例")
        self.driver.get("http://www.atstudy.com")
        time.sleep(15)
        self.assertTrue(True)
    def tearDown(self):
        self.driver.quit()
        print("测试用例B执行完成")