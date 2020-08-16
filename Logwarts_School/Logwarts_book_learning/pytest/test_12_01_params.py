"""
参数化用例
pytest中使用@pytest.mark.parametrize参数化
"""
"""
使用parametrize参数化
def parametrize(self,argnames,argcalues,indrect=False,ids=Nones，scope=None)
参数说明：
    argsnames  参数名
    argsvalues 参数值，参数组成的列表，列表中的元素数量，对应生成该数量的测试用例
使用方法：
    使用@pytest.mark.paramtrize()装饰测试方法
    parametrize('data'，param)，data为参数名，param是引入的参数列表
    将自定义的参数名data作为参数传递给测试用例test_func,在测试用例内部使用data参数    
"""
import pytest

@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("5*7",30)])
def test_eval(test_input,expected):
    # eval 将字符串str当成有效的表达方式来求值，并返回结果
    assert eval(test_input) == expected

if __name__ == "__main__":
    pytest.main(['-v','-s','test_12_01_params.py'])

"""
测试结果：
=================================== FAILURES ===================================
______________________________ test_eval[7*5-30] _______________________________

test_input = '7*5', expected = 30

    @pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
    def test_eval(test_input,expected):
        # eval 将字符传str当成有效设为表达式来求值，并返回结果
>       assert eval(test_input) == expected
E       assert 35 == 30
E         -35
E         +30

test_12_params.py:21: AssertionError
========================= 1 failed, 2 passed in 0.07s ==========================
"""


