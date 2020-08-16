"""
控制测试用例运行顺序
    pytest加载测试用例为乱序，指定顺序，需要安装pytest-order插件pip install pytest-ordering。
测试用例上加上装饰器函数@pytest.mark.run(order=[num]),测试用例按照num的大小执行顺序。
适用于流程业务的测试
"""
import pytest

class TestPytest(object):

    @pytest.mark.run(order=-1)
    def test_two(self):
        print("\ntest_two,测试用例")

    @pytest.mark.run(order=3)
    def test_one(self):
        print("\ntest_one,测试用例")

    @pytest.mark.run(order=-1)
    def test_three(self):
        print("\ntest_three,测试用例")

if __name__ == "__main__":
    pytest.main(['-v','-s','test_03_order.py'])

"""
运行结果：
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/mac/PycharmProjects/untitled/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.7.4', 'Platform': 'Darwin-19.6.0-x86_64-i386-64bit', 'Packages': {'pytest': '5.3.5', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.0.1', 'allure-pytest': '2.8.10', 'ordering': '0.6', 'metadata': '1.8.0'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk-11.0.5.jdk/Contents/Home'}
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning/Logwarts_book_learning
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collecting ... collected 3 items

test_03_order.py::TestPytest::test_one 
test_one,测试用例
PASSED
test_03_order.py::TestPytest::test_two 
test_two,测试用例
PASSED
test_03_order.py::TestPytest::test_three 
test_three,测试用例
PASSED

============================== 3 passed in 0.02s ===============================
"""