# 定义列表
list1 = ['google', '51testing', 2019, ['facebook', 'microsoft']]
list2 = [1, 2, 3, 4, 5, 6]
#使用索引获取列表内数据
print(list1[0])
print(list1[0][0])
#对列表切片
print(list2[1:5])
# 使用索引对列表内元素赋值
list1[0] = 'huawei'
print(list1)
# 使用索引删除列表内的数据
del list1[3][0]  # 删除list1中的facebook
print("删除后list1为：", list1)
# 打印数据类型
print(type(list1[3]))
# +号拼接列表
list3 = [3, 4]
list4 = ['www', 'it']
list5 = list3+list4
print(list5)
# *复制列表
list6 = list3*3
print(list6)

# in和not in
list7 = ['huawei', 'ali', 'mi', 9 , ['eleme', 'meituan']]
r = 'huawei' in list7
print(r)
r = 9 in list7
print(r)
r = ['eleme', 'meituan'] not in list7
print(r)
r = 'eleme' not in list7
print(r)

#常用函数
#len(),获取列表长度
l = len(list7)
print("list7长度为：", l)
#append(),给列表后面添加元素
list7.append('oppo')
print(list7)
# extend(),在列表末尾一次性追加另一个序列中的多个值
list8 = [1, 2, 3]
list9 = [7, 8, 9]
list9.extend(list8)
print(list9)
# sort(),给列表排序
list10 = [3, 5, 1, 10, 7]
list10.sort() # 默认升序
print(list10)
list11 = [3, 5, 1, 10, 7]
list11.sort(reverse=True)  # 降序排序 、
print(list11)
reverse()#  反向列表中的元素
list12 = [3, 5, 1, 10, 7]
list12.reverse()
print(list12)

# 遍历列表
# 使用成员运算符in遍历列表，变量l表示列表内的元素
for l in list12:
    print(l, end=",")  #  print() 中加end=""起到不换行的作用
print()  # 起到换行作用
# 定义变量i表示列表索引，使用索引遍历列表
for i in range(0, len(list12)):  # for（int i=0;i<5;i++）
    print(list12[i], end=" ")