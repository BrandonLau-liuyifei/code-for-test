__author__ = 'Administrator'
import unittest

def TestCase_to_suit_by_discover():
    # 确定用例存放的路径
    testcase_path = "D:\\zhaojia\\selenium\\selenium_105\\selenium_study\\selenium_day4\\testcase\\"
    # 调用unittest下的defaultTestLoader方法下的discover方法，来获取测试用例并添加到测试套件中
    test_suit = unittest.defaultTestLoader.discover(testcase_path,pattern="*.py")
    return test_suit

if __name__=="__main__":
    test_runner = unittest.TextTestRunner()
    test_suit = TestCase_to_suit_by_discover()
    test_runner.run(test_suit)
