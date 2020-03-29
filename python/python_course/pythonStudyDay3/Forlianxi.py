# 打印乘法口诀表
for i in range(1, 10):
    for j in  range(1, i+1):
        print("%d*%d=%d"%(j,i,j*i),end=" ")
    print()

"""
   *
  ***
 *****  
*******
"""
for i in range(1,5):
    print(" "*(4-i),end="")
    print("*"*(2*i-1),end="")
    print()

#for循环嵌套实现三角形打印
for i in range(1,5):
    # 定义for循环打印空格
    for j in range(4, i, -1):
        print(" ",end="")
    #定义for循环打印*
    for k in range(0,2*i-1):
        print("*",end="")
    print()

#  指定三角形行数
n = int(input("请输入行数："))
for i in range(1, n+1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
    print()