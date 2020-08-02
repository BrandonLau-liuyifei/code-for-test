"""
复杂度低的项目使用模块来管理
复杂度高的项目使用包来管理
"""
# 8.1.1 模块
"""
模块导入：
import 模块名
import 模块名 as 新名字
from 模块名 import 函数名
"""
import math
from math import sqrt
import math as shuxue
print("调用math.sqrt:\t",math.sqrt(2))
print("直接调用sqrt:\t",sqrt(5))
print("调用shuxue.sqrt:\t",shuxue.sqrt(3))

# 8.1.2 自己编写的模块
# 模块文件
# 文件名称:module_test.py
# print("导入的测试模块的输出")
#
# name = 'module_test'
# def m_t_pr():
#     print("模块module_test中的m_t_pr的函数")

# 调用自己编写的模块
# 文件名:a8_2.py  从模块中直接调取
# import module_test
# module_test.m_t_pr()
# print("使用导入模块中的变量",module_test.name)

# 8.1.3 模块位置
import sys    #导入sys模块
print(sys.path)  #输出当前模块查找的路径
sys.path.append("..") #添加path为路径查找路径
from module import module_test
module_test.m_t_pr()
print("使用导入模块中的变量",module_test.name)

#8.1.4 __pycache__目录
'''
调用别的模块的的py文件进行编译,产生编译文件
调用没有用到的py文件，可以可以执行编译脚本
命令行python -O compile.py 进行脚本优化编译
'''
import py_compile
py_compile.compile('A07_practice.py','A07_practice.pyc')

# 8.1.5具有独立运行能力的模块
"""
每个程序都有1个__name__属性，程序中通过__name__属性值判断。
程序作为模块导入，__name__属性被设置为模块名。
程序独立运行，__name__属性被设置为__main__。
__name__加入可以导入模块，也能独立运行
模块见 module--module_test.py
"""

# 8.2包

# 8.2.1 包的导入
"""
handle/
    __init__    #有这个证明是一个包
    index.py
    info.py
导入 handle模块中index中的hdl()函数
import handle.index             handle.index.hdl()
from handle import index        index.hdl()
from handle.index from hdl      hdl()
"""

# 8.2.2 包详解
"""
__init__.py文件是一个空文件。
__init__.py文件如不是一个空文件，其中的函数和参数在导入包时会被执行
"""
"""
模块调用
grnd/
    __init__.py
    prnta
        __init__.py
        suba.py
        sub/
            __init__.py
            sona.py
    prntb
        __init__.py
        subb.py
        subc.py
        
包模块中引用同一目录下的模块，直接引用
import subc
包模块中引用同一级别的目录中的另一模块，必须从父包上级开始导入。
from grnd.prnta import subc
包模块引用其目录下的子包中的某个模块，可以使用相对导入的方式。
from .sub import sona
"""
# 8.3 python常用标准库
# 8.3.1 数学类模块
"""
库1：math 常见的数学函数
三角函数 sin()、cos()、tan()
反三角函数 asin()、acos()、atn()
对数函数log()、log100()、log2()
库2：random 中包含了常见的随机数生成函数,如random、randint。
    按概率生成随机数的函数如gauss等，还有shuffle乱序列表、choice()从序列中随机取元素等随机函数。
"""
import random
print(random.random())  #生成0-1之间的随机数
print(random.randint(0,10))   #生成0-10之间的随机整数
print(random.choice((1,3,4,6,7,8,9)))   #从元祖中随机返回一个值
list_01 = [1,2,3,4,5,6,7]
print(random.shuffle(list_01))
print(list_01)

# 8.3.2 日期时间类
"""
库:calendar、datetime、time
"""
import time,datetime,calendar
print(datetime.datetime.now())  #获取本地的日期和时间
print(datetime.datetime.utcnow())  #获取本地的日期和时间
print(time.time())  #获取自初始时间至现在的秒数







