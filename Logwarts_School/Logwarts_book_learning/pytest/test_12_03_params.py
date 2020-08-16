"""
@pytest.fixture 与 @pytest.mark.parametrize结合实现参数化
测试数据在fiture方法中使用，同时也需要在测试用例中使用，可以在使用parametrize的时候添加一个参数indirect=True，
pytest实现将参数传入到fixtrue方法中，也可以在测试用例中使用。
paramtrize源码：
    def parametrize(self,argnames,argvalues,indirect=False,ids=None,scope=none)
"""
"""
indirect参数配置为True，pytest会把argnames当作函数去执行，将argvalues作为参数传入到argnames这个函数里。
"""
import pytest
#方法名作为参数
test_user_data = ['tom','jerry']
@pytest.fixture(scope="module")
def login_r(request):
    #通过request。param获取参数
    user = request.param
    print(f"\n 登录用户：{user}")
    return user

@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值:{a}")
    assert a !=""

if __name__ == "__main__":
    pytest.main(['-v','-s','test_12_03_params.py'])

"""
测试结果：
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/mac/PycharmProjects/untitled/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.7.4', 'Platform': 'Darwin-19.6.0-x86_64-i386-64bit', 'Packages': {'pytest': '5.3.5', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.0.1', 'allure-pytest': '2.8.10', 'ordering': '0.6', 'metadata': '1.8.0'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk-11.0.5.jdk/Contents/Home'}
rootdir: /Users/mac/PycharmProjects/Logwarts_School/Logwarts_book_learning/pytest
plugins: html-2.0.1, allure-pytest-2.8.10, ordering-0.6, metadata-1.8.0
collecting ... collected 2 items

test_12_03_params.py::test_login[tom] 
 登录用户：tom
测试用例中login的返回值:tom
PASSED
test_12_03_params.py::test_login[jerry] 
 登录用户：jerry
测试用例中login的返回值:jerry
PASSED

============================== 2 passed in 0.02s ===============================
"""