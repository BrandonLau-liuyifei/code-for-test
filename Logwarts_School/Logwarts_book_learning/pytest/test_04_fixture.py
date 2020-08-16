"""
pytest fixture
pytest fixture 可以使用@pytest.fixture来装饰方法
作用：1  被装饰的方法可以作为1个参数传入到方法中
     2  完成测试之前的初始化
     3  返回数据给测试函数
"""
"""
1.将fixture作为函数参数
    通常setup和teardown可以完成初始化，但是不够灵活，如果遇到测试用例不需要setup和teardown，可以使用fixture方法，
将初始化方法作为参数传入需要用到的用例。
"""
import pytest

@pytest.fixture()
def login():
    print("这是个登录的方法")
    return("tom","123")

@pytest.fixture()
def operate():
    print("登录后的操作")

def test_case1(login,operate):
    print(login,operate)
    print("test_case1,需要登录")

def test_case2():
    print()
    print("test_case2,不需要登录")

def test_case3(login):
    print(login)
    print("test_case3,需要登录")

if __name__ == "__main__":
    pytest.main(['-v','-s','test_04_fixture.py'])

"""
执行结果：
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/mac/PycharmProjects/untitled/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.7.4', 'Platform': 'Darwin-19.6.0-x86_64-i386-64bit', 'Packages': {'pytest': '5.3.5', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.0.1', 'allure-pytest': '2.8.10', 'ordering': '0.6', 'metadata': '1.8.0'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk-11.0.5.jdk/Contents/Home'}
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning/Logwarts_book_learning
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collecting ... collected 3 items

test_04_fixture.py::test_case1 这是个登录的方法
登录后的操作
('tom', '123') None
test_case1,需要登录
PASSED
test_04_fixture.py::test_case2 
test_case2,不需要登录
PASSED
test_04_fixture.py::test_case3 这是个登录的方法
('tom', '123')
test_case3,需要登录
PASSED

============================== 3 passed in 0.02s ===============================
"""