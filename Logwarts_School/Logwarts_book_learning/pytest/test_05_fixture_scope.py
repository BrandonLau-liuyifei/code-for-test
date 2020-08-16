"""
指定范围内共享
fixture 中的参数scope，可以控制fixture的控制范围（session>module>class>function）
function    函数或者方法级别都会被调用
class       类级别调用1次
module      模块级别调用1次
session     多个文件调用1次（可跨.py文件调用，每个py文件就是module）
setup和teardown加装饰器函数@classmethod也可以实现，但这里通过设置模块级别的fixture装饰器@pytest.fixture(scope="module")
"""
import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("执行teardown")
    print("最后关闭浏览器")

@pytest.mark.usefixtures("open") #可选则使用，作为将前置函数作为参数传入
def test_search1():
    print("test_search1")
    raise NameError
    pass

def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_search3")
    pass

if __name__ == "__main__":
    pytest.main(['-v','-s','test_05_fixture_scope.py'])

"""

============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/mac/PycharmProjects/untitled/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.7.4', 'Platform': 'Darwin-19.6.0-x86_64-i386-64bit', 'Packages': {'pytest': '5.3.5', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.0.1', 'allure-pytest': '2.8.10', 'ordering': '0.6', 'metadata': '1.8.0'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk-11.0.5.jdk/Contents/Home'}
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning/Logwarts_book_learning
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collecting ... collected 3 items

test_05_fixture_scope.py::test_search1 test_search1
FAILED
test_05_fixture_scope.py::test_search2 打开浏览器
test_search2
PASSED
test_05_fixture_scope.py::test_search3 test_search3
PASSED执行teardown
最后关闭浏览器


=================================== FAILURES ===================================
_________________________________ test_search1 _________________________________

    def test_search1():
        print("test_search1")
>       raise NameError
E       NameError

test_05_fixture_scope.py:21: NameError
========================= 1 failed, 2 passed in 0.10s ==========================
"""

