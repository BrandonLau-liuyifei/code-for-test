
# 导入random模块
# 使用random模块下的randrange()函数随机生成一个数字
# n = random.randrange(0, 100)
# 从键盘输入数字猜n的值，如果猜大了给出猜大了的提升，如果猜小了给出猜小了的提升
# 猜错了一直猜下去，猜对了结束程序

import random
from random import randrange
n = randrange(0, 100)
m = int(input("猜："))
while m != n:
    if m>n:
        print("猜大了")
    else:
        print("猜小了")
    m = int(input("继续猜："))
print("猜对了")