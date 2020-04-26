# __author__ ：Nathaniel
# -*- coding: UTF-8 -*-

import unittest


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return a / b


class CalculateTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("哈哈")

    def testAdd(self):
        print("加法")
        self.assertEqual(1 + 1, 2)


class StringTestCase(unittest.TestCase):
    def testHello(self):
        print("哈喽")
        self.assertTrue("hello world".endswith("d"))


if __name__ == '__main__':
    # 测试类集合
    testCaseSli = [CalculateTestCase, StringTestCase]


    def whole_suite():
        # 创建测试加载器
        loader = unittest.TestLoader()
        # 创建测试组
        suite = unittest.TestSuite()
        # 遍历所有测试类
        for test_class in testCaseSli:
            # 从测试类中加载测试用例
            tests = loader.loadTestsFromTestCase(test_class)
            # 将测试用例添加到测试组中
            suite.addTests(tests)
        return suite


    # 创建测试运行器（TestRunner）
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(whole_suite())
