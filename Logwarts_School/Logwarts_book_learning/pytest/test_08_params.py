"""
fixture 传递参数
在fixture方法上加上装饰器@pytest.fixture(params=[1,2,3])（列表形式）,会传入这3个不同的参数到测试用例中。
传入的数据需要使用固定的参数名request来接收。
"""
import pytest

@pytest.fixture(params=[1,2,3])
def data(request):
    return request.param

def test_not_2(data):
    print(f"测试数据：{data}")
    assert data < 5

if __name__=="__main__":
    pytest.main(['-v','-s','test_08_params.py'])

"""
执行结果：
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/mac/PycharmProjects/untitled/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.7.4', 'Platform': 'Darwin-19.6.0-x86_64-i386-64bit', 'Packages': {'pytest': '5.3.5', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.0.1', 'allure-pytest': '2.8.10', 'ordering': '0.6', 'metadata': '1.8.0'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk-11.0.5.jdk/Contents/Home'}
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collecting ... collected 3 items

test_08_params.py::test_not_2[1] 测试数据：1
PASSED
test_08_params.py::test_not_2[2] 测试数据：2
PASSED
test_08_params.py::test_not_2[3] 测试数据：3
PASSED

============================== 3 passed in 0.02s ===============================
"""