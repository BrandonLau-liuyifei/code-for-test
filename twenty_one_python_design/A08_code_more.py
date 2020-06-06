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
# 文件名:a8_2.py
import module_test
module_test.m_t_pr()
print("使用导入模块中的变量",module_test.name)

# 8.1.3 模块位置
import sys    #导入sys模块
print(sys.path)  #输出当前模块查找的路径
# sys.path.append(path) #添加Apath为路径查找路径

#8.1.4 __pycache__目录




