 # 定义字典
dict1 = {1: "one", 2: "two", "ali": "4200多亿美刀", (1, 2, 3): ("one", "two", "three")}
# "ali": "4200多亿美刀"会被"ali": ("one", "two", "three")覆盖
dict2 = {1: "one", 2: "two", "ali": "4200多亿美刀", "ali": ("one", "two", "three")}
print(dict2)
#通过键获取字典中的值
print(dict1[1])
print(dict1[(1, 2, 3)])
#通过键更改字典中的值
dict1[1] = "一"
print(dict1)


dict3 = {1: "one", 2: "two", "ali": "4200多亿美刀", (1, 2, 3): ("one", "two", "three")}
# 使用in判断键是否包含在某个字典中
r = 1 in dict3
print(r)
# 字典中键的值可以相同
dict4 = {1:"one", "一":"one"}
print(dict4)

#函数
# len(),获取键的长度
dict5 = {1: "one", 2: "two", "ali": "4200多亿美刀", (1, 2, 3): ("one", "two", "three")}
r = len(dict5)
print("dict5是长度为%d的字典"%r)
#dict6长度为3
dict6 = {1: "one", 2: "two", "ali": "4200多亿美刀", "ali": ("one", "two", "three")}
r = len(dict6)
print("dict6是长度为%d的字典"%r)

# update(),把某个字典中的键值对更新到另一字典中
dict7 = {1:"one"}
dict8 = {2:"two"}
dict7.update(dict8)
print(dict7)
# values()方法会返回一个迭代器，结合list()将字典中的所有值转换为列表
list1 = list(dict7.values())
print(list1)
# keys()方法会返回一个迭代器，结合list()将字典中的所有键转换为列表
list2 = list(dict7.keys())
print(list2)

#遍历字典
dict8 = {1: "one", 2: "two", "ali": "4200多亿美刀", (1, 2, 3): ("one", "two", "three")}
#遍历字典值可以先将字典中的值转为列表再遍历
list3 = list(dict8.values())
for l in list3:
    print(l, end=" ")
print()
#遍历字典值可以先将字典中的键转为列表在使用键遍历字典中的值
list4 = list(dict8.keys())
for l in list4:
    print(dict8[l], end=" ")
print()

#以上两个for可以按照下面来写
for val in dict8.values():
    print(val, end=" ")
print()
for key in dict8.keys():
    print(dict8[key], end=" ")