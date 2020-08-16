"""
自动执行fixture
如果每天测试用例都需要添加fixture功能，需在每一条用例方法中传入fixture的名字，
在装饰器函数中添加参数@pytest.fixture("autouse='ture")，autouse为true，会自动应用到每条测试用例中，
只是没有办法传返回值给测试用例。
"""
import pytest

@pytest.fixture(autouse="true")
def myfixtrue():
    print("this is my fixtrue")

class TestAutouse():
    def test_one(self):
        print("执行test_one")
        assert 1+1 == 2

    def test_two(self):
        print("执行test_two")
        assert 1 == 1

if __name__=="__main__":
    pytest.main(['-v','-s','test_07_autouse.py'])

"""
执行结果：
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/mac/PycharmProjects/untitled/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.7.4', 'Platform': 'Darwin-19.6.0-x86_64-i386-64bit', 'Packages': {'pytest': '5.3.5', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.0.1', 'allure-pytest': '2.8.10', 'ordering': '0.6', 'metadata': '1.8.0'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk-11.0.5.jdk/Contents/Home'}
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collecting ... collected 2 items

test_07_autouse.py::TestAutouse::test_one this is my fixtrue
执行test_one
PASSED
test_07_autouse.py::TestAutouse::test_two this is my fixtrue
执行test_two
PASSED

============================== 2 passed in 0.04s ===============================
"""