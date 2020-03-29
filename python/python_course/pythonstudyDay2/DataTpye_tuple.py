# 定义元组
tup1 = ("huawei", "ali", 3, 4, ("meituan", "baidu"), ["zte", "oppe"])
tup2 = 3, 4, 5, 6, "nihao"  # 不加小括号定义元组，不是好习惯
print(type(tup2))
# 当元组内只有一个元素时，需要在元素的后面添加逗号，否则小括号会被当做运算符使用
tup3 = (3)  # 这不是定义元组
print(type(tup3))
tup4 = (3,)  # 这是定义元组
print(type(tup4))
tup5 = 3,  # 这是定义元组
print(type(tup5))

#使用索引获取元组内的值
tup6 = ("huawei", "ali", 3, 4, ("meituan", "baidu"), ["zte", "oppe"])
print('"%s"是tup6第二个元素'%tup6[1])
print("切片元组tup6[0：5]：", tup6[0:5])  # 元组切片
# in 和 not in 使用
r = "ali" in tup6
print(r)
r = "ali" not in tup6
print(r)

# + 和 * 使用
tup7 = (3, 5, 9)
tup8 = (1, 0, "i")
tup9 = tup7 + tup8
print(tup9)
tup10 = tup7 * 5
print(tup10)

#常用方法
#len(),获取元组长度
print("tup10长度为%d。"%len(tup10))
# tuple(),将列表转换为元组
list1 = ["nihao", "hello", 12]
tuple1 = tuple(list1)
print(tuple1)
# list(),将元组转换为列表
tup2 = (4, 5, 6, 7)
list2 = list(tup2)
print(list2)

#遍历元组
for t in tup2:
    print(t, end=" ")
print()
# 使用索引遍历
for i in range(0, len(tup2)):
    print(tup2[i], end=" ")
