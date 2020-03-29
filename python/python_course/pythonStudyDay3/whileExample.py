# while基本例子
i = 0
while i<9:
    print(i, end=" ")
    i += 1
print()
# 使用while语句实现乘法口诀表打印
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (j, i, j * i), end=" ")
        j += 1
    print()
    i += 1

# while...else语句
i = 0
while i < 9:
    print(i, end=" ")
    i += 1
else:  # 当while后的条件为False时else中的语句被执行
    print("我被执行")
print()
# continue关键字
i = 0
while i < 10:
    i += 1
    if i%2 == 0:
        continue  # 跳过本次循环
    print(i, end=" ")
print()
#break关键字
i = 0
while i < 10:
    i += 1
    if i%2 == 0:
        break  # 终止循环
    print(i, end=" ")

print()
i = 0
while i < 10:
    i += 1
    if i%2 == 0:
        break  # 终止循环
    print(i, end=" ")
else:
    print("我被执行")  # break终止的while语句，else后的语句是不执行的
