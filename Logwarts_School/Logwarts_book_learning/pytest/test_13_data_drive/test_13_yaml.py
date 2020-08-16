"""
数据驱动
数据存放在外部文件，方便数据的读取，测试数据测用例分开管理，常用的数据源有yaml、csv、json、excel等。
pip install PyYAML

YAML是一种容易阅读和适合表示程序的数据结构，可用于不同程序间交换数据、丰富表达能力和可扩展性、易用于使用的语言。
通过缩进或符号来表示数据类型。
pyyaml文件模块在python处理yaml格式，主要使用yaml.safe_dump()和yaml.safe_load()将python值和yanl格式数据相互转换。
"""
import pytest,yaml

@pytest.mark.parametrize("a,b",yaml.safe_load(open("testdata.yml",encoding='utf-8')))
def test_foo(a,b):
    print(f"a+b = {a+b}")

if __name__ == "__main__":
    pytest.main(['-v','-s','test_13_yaml.py'])
"""
yaml文件中定义了列表数据，通过open()获取特testdata.yml文件对象，使用yaml.safe_load()加载这个文件的对象，将yaml
格式文件转换为python值，分别传到用例中生成多条用例分别执行
"""

"""
测试结果：
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/mac/PycharmProjects/untitled/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.7.4', 'Platform': 'Darwin-19.6.0-x86_64-i386-64bit', 'Packages': {'pytest': '5.3.5', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.0.1', 'allure-pytest': '2.8.10', 'ordering': '0.6', 'metadata': '1.8.0'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk-11.0.5.jdk/Contents/Home'}
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning/pytest/test_13_data_drive
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collecting ... collected 2 items

test_13_yaml.py::test_foo[1-2] a+b = 3
PASSED
test_13_yaml.py::test_foo[20-30] a+b = 50
PASSED

============================== 2 passed in 0.02s ===============================
"""