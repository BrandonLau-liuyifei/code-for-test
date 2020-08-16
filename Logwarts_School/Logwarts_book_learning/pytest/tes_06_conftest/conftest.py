"""
    ·fixture scope 为session级别，可以跨.py模块调用，有多个.py文件的用例时，如果多个测试用例只需1次fixture，
将scopoe="session"写入conftest文件中。
使用规则：
1.conftest.py名称固定，不可更改。
2.conftest.py同测试用例在同一包中，且包中包含__init__。
3.confest.py不需要导入，pytest可识别到这个文件。
4.confest.py文件放入的位置，在这个位置中作用于全局。
"""
import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("执行teardown")
    print("最后关闭浏览器")