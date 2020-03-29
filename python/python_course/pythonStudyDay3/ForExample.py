# 在for语句中使用成员运算符遍历序列
for l in 'wsxqwe':
    print(l, end=" ")
print()  # 换行
# 使用索引遍历序列
list1 = [1,3,45,8,2,0]
for l in range(0, len(list1)):  # 变量l表示索引
    print(list1[l], end=" ")
print()
# range() 函数的使用
for i in range(0, 10):  # 相当于for(int i=0;i<10;i++){ printf(i);}
    print(i, end=" ")
print()
for i in range(0, 10):
    i += 3            # i += 3 语句执行后i的变化不影响for i in range(0, 10)中i的变化
    print(i, end=" ")
print()
for i in range(0, 10, 3):  # 3为i变化的步长，相当于c语言中for(int i=0;i<10;i=i+3){ printf(i);}
    print(i, end=" ")
print()
for i in range(9, 0, -1):  #-1位i变化的步长，相当于c语言中for(int i=9;i>0;i--){ printf(i);}
    print(i, end=" ")
print()
for i in range(9, 0, -2):  #-1位i变化的步长，相当于c语言中for(int i=9;i>0;i=i-2){ printf(i);}
    print(i, end=" ")
print()
for i in range(10):  # 相当于for i in range(0, 10):
    print(i, end=" ")
print()
for i in range(0,):  # 相当于for i in range(0, 0):
    print(i, end=" ")
# for else语句
for i in range(0, 10):
    print(i, end=" ")
else:
    print("我被执行")
print()
# continue关键字
for i in range(0, 10):
    if i%2 == 0:
        continue  # 跳过当前循环
    print(i, end=" ")
print()
# break关键字
for i in "asdwerfd":
    if i == "w":
        break  # 终止循环
    print(i, end=" ")
print()
# break关键字终止的循环else语句不执行
for i in "asdwerfd":
    if i == "w":
        break  # 终止循环
    print(i, end=" ")
else:
    print("我被执行")
