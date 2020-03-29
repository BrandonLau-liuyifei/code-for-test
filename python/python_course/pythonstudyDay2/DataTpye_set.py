# 定义集合
set1 = {2, 3, "nihao", 4,2,"nihao"}  # 集合中有重复内容会去重
print(set1)
set2 = {3,5,9}
# 使用set定义集合
set3 = set("asdasdqw")
print(set3)
set3 = set([1,2,3])
print(set3)
set3 = set((7,8,9))
print(set3)
set3 = set({1:"one", 2:"twe"})  # 把字典中的键转换为集合
print(set3)
# 定义空集合
set4 = set()
print(set4)
#集合运算
seta = {"a", "b", "c","d", "e","f"}
setb = {"c","d", "e","f","g","h"}
r = seta - setb  # 结果为集合seta中包含的而在集合setb中不包含的元素
print(r)
r = seta | setb # 结果为集合seta或setb中包含的所有元素
print(r)
r = seta & setb # 结果为同时在集合seta和setb中包含的元素
print(r)
r = seta ^ setb # 结果为不同时在集合seta和setb中包含的元素
print(r)

# 成员运算符in的使用
setc = {"c","d", "e","f","g","h"}
r = "d" in setc
print(r)
r = "d" not in setc
print(r)
# 使用成员运算符遍历集合
for s in setc:
    print(s, end=" ")

