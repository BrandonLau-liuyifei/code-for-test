# __author__ ：Nathaniel
# -*- coding: UTF-8 -*-

import unittest



# 测试类集合
from unittest_learning_01.HTMLTestRunner import HTMLTestRunner
from unittest_learning_01.test_02 import CalculateTestCase, StringTestCase

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


if __name__ == '__main__':
    # 将测试结果输出到测试报告html中
    with open("HTMLReport.html", "w", encoding="utf8") as f:
        runner = HTMLTestRunner(stream=f,
                                title="测试报告",
                                description="用例执行详细信息",
                                verbosity=2
                                )
        runner.run(whole_suite())

# if __name__ == '__main__':
#     # 测试结果输出到文本文件
#     with open('test_report.txt', 'a') as f:
#         # 创建测试运行器（TestRunner），将测试报告输出到文件中
#         runner = unittest.TextTestRunner(verbosity=2, stream=f)
#         runner.run(whole_suite())

# if __name__ == '__main__':
#     # 创建测试运行器（TestRunner）
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(whole_suite())
