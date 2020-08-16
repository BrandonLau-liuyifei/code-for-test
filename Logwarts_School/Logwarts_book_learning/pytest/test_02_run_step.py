"""
pytest框架结构
同unittest，执行用例前后会执行setup和teardown，但pytest更加灵活。
模块级 setup_module/tearndown_module       在模块始末调用
函数级 setup_function/teardown_function    在函数始末调用      在类外部
类级   setup_class/teardown_class          在类始末调用        在类中
方法级 setup_method/teardown_method        在方法始末调用       在类中
方法级 setup/teardown                       在方法的始末调用    在类中
执行顺序：setup_module>setup_class>setup_method>setup>teardown>teardown_method>teardown_class>teardown_module
"""
import pytest

def setup_module():
    print("\nsetup_module,只执行1次，当多个测试类是使用")

def teardown_module():
    print("\nteardown_module,只执行1次，当多个测试类是使用")

class TestPytest1(object):

    @classmethod
    def setup_class(cls):
        print("\nsetup_class1,只执行1次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class1,只执行1次")

    def setup_method(self):
        print("\nsetup_method1,只执行1次")

    def teardown_method(self):
        print("\nteardown_method1,只执行1次")

    def test_three(self):
        print("test_three,测试用例")

    def test_four(self):
        print("test_four,测试用例")


class TestPytest2(object):

    @classmethod
    def setup_class(cls):
        print("\nsetup_class2,只执行1次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class2,只执行1次")

    def setup_method(self):
        print("\nsetup_method2,只执行1次")

    def teardown_method(self):
        print("\nteardown_method2,只执行1次")

    def test_three(self):
        print("test_three,测试用例")

    def test_four(self):
        print("test_four,测试用例")

if __name__=="__main__":
    pytest.main(['-v','-s','test_02_run_step.py'])

"""
运行结果：
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/mac/PycharmProjects/untitled/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.7.4', 'Platform': 'Darwin-19.6.0-x86_64-i386-64bit', 'Packages': {'pytest': '5.3.5', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.0.1', 'allure-pytest': '2.8.10', 'ordering': '0.6', 'metadata': '1.8.0'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk-11.0.5.jdk/Contents/Home'}
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning/Logwarts_book_learning
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collecting ... collected 4 items

test_02_run_step.py::TestPytest1::test_three 
setup_module,只执行1次，当多个测试类是使用

setup_class1,只执行1次

setup_method1,只执行1次
test_three,测试用例
PASSED
teardown_method1,只执行1次

test_02_run_step.py::TestPytest1::test_four 
setup_method1,只执行1次
test_four,测试用例
PASSED
teardown_method1,只执行1次

teardown_class1,只执行1次

test_02_run_step.py::TestPytest2::test_three 
setup_class2,只执行1次

setup_method2,只执行1次
test_three,测试用例
PASSED
teardown_method2,只执行1次

test_02_run_step.py::TestPytest2::test_four 
setup_method2,只执行1次
test_four,测试用例
PASSED
teardown_method2,只执行1次

teardown_class2,只执行1次

teardown_module,只执行1次，当多个测试类是使用


============================== 4 passed in 0.03s ===============================
"""