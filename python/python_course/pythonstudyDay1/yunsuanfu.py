# 数学运算符
a = 10
b = 12

c = a + b  # 加法
print(c)

c = c - a  # 减法
print(c)
c = c * b  # 乘法
print(c)
d = c/a  # 除法
print(d)
e = c//a  # 整除
print(e)
f = c % a  # 求余数
print(f)
j = e ** f # e的f次方
print(j)

# 比较运算符
a = 8
b = 9
c = a == b  # 等于
print(c)
print(a != b)  # 不等于

print(a >= b)  # 大于等于
print(a <= b)  # 小于等于

# 赋值运算符
b //= a
print(b)

a **= b
print(a)

# 逻辑运算符
print(a > b and b > a)
print(a > b or b > a)
print(not a>b)  # not 将真的变成假的，将假的变成真的


# 成员运算符
a = 4
b = 9
list1 = [2, 3, 4, 5]

r = a in list1
print(r)
r = a not in list1
print(r)

r = b in list1
print(r)
r = b not in list1
print(r)

# 使用成员运算符遍历list1
for s in list1:
    print(s)

# 定义变量i 表示列表list1的索引，使用索引遍历列表
for i in range(0, len(list1)):   # 相当于c语言中：for(int i =0; i<len(list1);i++){printf(list1[i])}
    print(list1[i])











