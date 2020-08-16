"""
多次使用paramtrize
同一个测试用例还可以同时添加多个@pytest.mark.parametrize，多个parametrize的所有元素相互组合(笛卡尔积)，
生成大量的测试用例。
"""
import pytest

@pytest.mark.parametrize("x" ,[1 ,2])
@pytest.mark.parametrize("y" ,[8 ,10 ,11])
def test_foo(x ,y):
    print(f"测试数据组合x:{x},y:{y}")

if __name__=="__main__":
    pytest.main(['-v','-s','test_12_02_params.py'])

"""
测试结果结果：
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/mac/PycharmProjects/untitled/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.7.4', 'Platform': 'Darwin-19.6.0-x86_64-i386-64bit', 'Packages': {'pytest': '5.3.5', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.0.1', 'allure-pytest': '2.8.10', 'ordering': '0.6', 'metadata': '1.8.0'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk-11.0.5.jdk/Contents/Home'}
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning/pytest
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collecting ... collected 6 items

test_12_02_params.py::test_foo[8-1] 测试数据组合x:1,y:8
PASSED
test_12_02_params.py::test_foo[8-2] 测试数据组合x:2,y:8
PASSED
test_12_02_params.py::test_foo[10-1] 测试数据组合x:1,y:10
PASSED
test_12_02_params.py::test_foo[10-2] 测试数据组合x:2,y:10
PASSED
test_12_02_params.py::test_foo[11-1] 测试数据组合x:1,y:11
PASSED
test_12_02_params.py::test_foo[11-2] 测试数据组合x:2,y:11
PASSED

============================== 6 passed in 0.03s ===============================
"""