__author__ = 'Administrator'
import unittest
from selenium_day4.testcase.login_testcase import UserLoginTestCase

def TestCase_to_suit_by_addtest():
    # 实例化unittest下的testsuit类的对象
    testcasesuit = unittest.TestSuite()
    # 使用testcasesuit对象调用addtest的方法，将类中的用例一个一个添加到套件中
    testcasesuit.addTest(UserLoginTestCase("test_01_login_by_correct_username_password"))
    testcasesuit.addTest(UserLoginTestCase("test_02_login_by_correct_username_wrong_password"))
    testcasesuit.addTest(UserLoginTestCase("test_03_login_by_wrong_username_correct_password"))
    testcasesuit.addTest(UserLoginTestCase("test_04_login_by_correct_username_null_password"))
    testcasesuit.addTest(UserLoginTestCase("test_05_login_by_null_username_correct_password"))
    testcasesuit.addTest(UserLoginTestCase("test_06_login_button_clickable"))
    return testcasesuit

if __name__=="__main__":
    # 实例化unittest下的TextTestRunner类的对象
    test_runner = unittest.TextTestRunner()
    # 获取测试套件
    test_suit = TestCase_to_suit_by_addtest()
    # 通过test_runner调用run的方法来执行套件
    test_runner.run(test_suit)