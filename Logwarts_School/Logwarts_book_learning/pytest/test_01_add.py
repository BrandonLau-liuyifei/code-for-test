"""
pytest测试框架
pytest install:
pip install -U pytest
pytest --version
测试用例识别与运行
测试用例规范：
    测试文件以test开头，或以test结尾也可以
    测试类以test开头，且不能带有init方法
    测试函数以test开头
    断言基本使用assert即可
"""
import pytest

def add(x,y):
    return x+y

def test_add():
    assert add(1,10) == 11
    assert add(1,1) == 2
    assert add(1,99) ==100

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x
    def test_two(self):
        x = "hello"
        assert hasattr(x,"check")

if __name__=="__main__":
    pytest.main()

"""
执行方式：
方式1：
    命令行执行以下脚本：
        cd 进入用例所在的目录
        执行pytest -参数 指定的test*.py的文件  或   pytest -参数（可执行目录下所有的test*.py文件）
方式2：
    在导入pytest的test*.py文件中，执行pytest.main(['-参数','指定test*.py文件']) 或
    pytest.main(['-参数']) （执行当前目录中的所有test*.py文件）

pytest 运行参数：
    pytest --help查看帮助文档
    pytest 无参数 读取路径下符合规则的文件，类，方法，函数并全部执行
    pytest -v   打印详细日志，方便定位问题
    pytest -s   打印print输出的语句
    pytest -k   跳过指定测试类、测试方法、某个测试类中的某个测试方法的运行
        pytest -k '类名'
        pytest -k '方法名'
        pytest -k '类名 and not 方法名'
    pytest -x   遇到用例失败立即停止
    pytest --maxfail=[num]  失败用例量到阀值立即停止
    pytest -m [标记名]  运行@pytest.mark.[标记名]的测试用例
    如  @pytest.mark.login
        def test_add():
            assert add(1,10) == 11
            assert add(1,1) == 2
            assert add(1,99) ==100 
    pytest运行模式
        pytest 文件名.py   #运行文件
        pytest 文件名.py::类名   #运行文件中的类
        pytest 文件名.py::类名::方法名  #运行文件中的类的方法   
"""

"""
执行结果：
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning/Logwarts_book_learning
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collected 10 items

test_03_order.py .                                                       [ 10%]
test_01_add.py ..F                                                       [ 40%]
test_02_run_step.py ....                                                 [ 80%]
test_03_order.py ..                                                      [100%]

=================================== FAILURES ===================================
______________________________ TestClass.test_two ______________________________

self = <Logwarts_book_learning.Logwarts_book_learning.test_01_add.TestClass object at 0x7fe18b3fae50>

    def test_two(self):
        x = "hello"
>       assert hasattr(x,"check")
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_01_add.py:29: AssertionError
========================= 1 failed, 9 passed in 0.11s ==========================
"""