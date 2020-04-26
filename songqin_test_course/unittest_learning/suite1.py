import unittest
# testsuite过程
#创建一个测试加载器
loader = unittest.TestLoader()
# 创建测试套件
suite = unittest.TestSuite
#从测试类中加载测试庸碌
tests = loader.loadTestsFromTestCase(case1.userTestCase.testUser())
#将测试用例加载到测试组
suite.addTests(tests)

# 创建测试运器 verbosity 0-简单报告 1-一般报告 2-详细报告
# 输出至屏幕
# runner = unittest.TextTestRunner(verbosity=2)
# 输出至文件
# with open ("./test_report.txt","w") as m:
#     runner = unittest.TextTestRunner(verbosity=2,stream=m)
#     runner.run(suite)
#输出至html文件
with open ("./http_test_report.html","w") as f:
    runner = HTMLTestRunner(verbosity=2
                            stream=f,
                            title="unittest练习",
                            discription="用例执行报告描述")
    runner.run(suite)