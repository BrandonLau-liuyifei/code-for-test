import unittest2
from BeautifulReport import BeautifulReport
from tomorrow import threads

def get_test_suite():
    suite = unittest2.defaultTestLoader.discover("test_case","*Test.py")
    return suite

@threads(5)
def run_case(case):
    # unittest2.TextTestRunner().run(case)
    # 会生成一个html测试报告，需要事先指定存放位置
    BeautifulReport(case).report(description="测试报告", filename="51Testing测试报告", log_path="./report")

if __name__ == '__main__':
    suite = get_test_suite()
    # 每个线程单独执行一条测试用例
    for case in suite:
        run_case(case)
