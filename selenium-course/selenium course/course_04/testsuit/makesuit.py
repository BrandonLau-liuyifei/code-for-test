__author__ = 'Administrator'
import unittest
from selenium_day4.testcase.login_testcase import UserLoginTestCase

def TestCase_to_suit_by_makesuit():
    # 调用unittest下的makesuit的方法将类中的用例打包
    class_testcase = unittest.makeSuite(UserLoginTestCase)
    # 调用unittest下的testsuit的方法获取套件并将打包好的用例添加到套件中
    test_suit = unittest.TestSuite(class_testcase)
    return test_suit

if __name__ == "__main__":
    test_runner = unittest.TextTestRunner()
    test_suit = TestCase_to_suit_by_makesuit()
    test_runner.run(test_suit)