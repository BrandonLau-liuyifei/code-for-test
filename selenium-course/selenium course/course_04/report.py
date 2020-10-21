__author__ = 'Administrator'
import sys
sys.path.append("D:\\zhaojia\\selenium\\selenium_105\\selenium_study")

import HTMLTestRunner
from selenium_day4.testsuit.discover import TestCase_to_suit_by_discover
from selenium_day3.shijianchuo.def_shijianchuo import shijianchuo

# 确定测试报告存放的路径、名字、格式
HTMLfile = "D:\\zhaojia\\selenium\\selenium_105\\selenium_study\\report\\HTMLreport" + shijianchuo() + ".html"

# 打开文件并准备写入
htmlreport_file = open(HTMLfile,"wb") # wb表示二进制的方式打开并写入

# 获取测试套件，获取执行的用例
test_suit = TestCase_to_suit_by_discover()

# 实例化HTMLTestRunner下的HTMLTestRunner对象，需要配置参数，写清楚报告的标题、描述内容
htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=htmlreport_file,title="OA测试报告",description="共计8条用例，执行结果如下：")

# 使用runner的对象来调用run的方法，执行测试套件
htmlrunner.run(test_suit)

# 关闭文件
htmlreport_file.close()