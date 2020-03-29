import keyword  # 导入整个keyword模块
from time import sleep # 从time模块导入sleep函数
from pythonstudyDay1.basegrammer2 import fu

fu()
print(keyword.kwlist)
sleep(5)

# 这是一行注释
"""
第一行注释
第二行注释
第三行注释

"""
# 第一行注释
# 第二行注释
# 第三行注释
print("hello world")

a = 0
a = 1.1
a = 12
b = 13
c = 20
d = 30
print(a +
      b)

if a < b:
    print(a)
if b-a > 0:
        print(b)



e = a + b\
    + c +\
    d
print("e的值为：", e)