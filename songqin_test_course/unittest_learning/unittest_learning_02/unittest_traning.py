"""
UnitTest应用：
1. 类对象必须继承于UnitTest.TestCase模块
2. 四大组件：
case：测试用例，基于test_开头的都是测试用例，测试用例会自行排序，默认排序规则A-Z，a-z，0-9
fixture：设置有前置条件（setup）与后置条件（teardown）
suite % runner：测试套件，套件运行需要结合运行器（htmltestrunner / texttestrunner）
assert：断言

"""
#导入测试框架
import unittest

class unittoday(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("this is setupclass")
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("this is teardownclass")
    #前置条件
    def setUp(self) -> None:
        print("this is setup")
    #后置条件
    def tearDown(self) -> None:
        print("this is teardown")
    #创建测试用例
    def test_01(self):
        print("this is tastcase_01")
    def test_03(self):
        print("this is tastcase_03")
    def test_02(self):
        print("this is tastcase_02")
    def test_04(self):
        c=self.plus()
        print("this is tastcase_04")
    def plus(self):
        a=1
        b=2
        print(a+b)

if __name__=="__main__":
     unittest.main()