from pythonStudyDay3.FunctionExample import jia  # 自定义函数导入时从工程目录下第一级目录开始导入
from pythonStudyDay3.FunctionExample2 import jiangxu_list

jia()
list1 = [2, 4, 2, 9, 10]
jiangxu_list(list1)

# for 循环打印排序后的列表
for l in  list1:
    print(l, end=" ")
