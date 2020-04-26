# _*_ coding:utf-8 _*_

import unittest

#继承来自unittest。TestCase的类
class calculateTestCase(unittest.TestCase):
# 定义以test开头的测试用例，测试用例可以有N个
    def testAdd(self):
        self.assertEqual(1+1,2,msg="断言1+1=2")
    def testSubtraction(self):
        self.assertEqual(1-1,2,msg="断言1-1=0")

class userTestCase(unittest.TestCase):
    def testUser(self):
        self.assertEqual("zhangsan","zhangsan",msg="断言1+1=2")

# if __name__=="__main__":
#     unittest.main()


