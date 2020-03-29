# for循环嵌套
list1 = [1, 3, 4, 2, [3, 4, 2], "we", ["s", "z"]]
#
for i in list1:  # 变量i表示list1中的元素
    if type(i) is list:  # 判断i的类型是否为列表
        for l in i:   # 变量l表示list1嵌套的列表内的元素
            print(l, end=" ")
    else:
        print(i, end=" ")
print()
# for 语句计算一个数的阶乘
#以5的阶乘为例：5！=5*4！=5*4*3！=5*4*3*2！=5*4*3*2*1！=5*4*3*2*1*1
j = 1
for i in range(1, 6):
    j = j*i
print(j)

# 冒泡排序
#   1、 对于给定的序列，排序的轮数为序列长度-1轮
#   2、每一轮对比的元素个数随轮数增加递减
#   3、在两两对比元素时，符合条件则倒换两个元素，不符合则不到换

#定义for循环控制排序的轮数，排序的轮数为序列长度-1轮
list2 = [7, 4, 1, 3, 9]
for i in range(1,len(list2)):  # 变量i表示排序轮数
    # 嵌套for循环遍历列表，获取元素两两对比，变量j表示索引，每一轮对比元素都是从第一个开始，所以j必须从0开始.
    for j in range(0, len(list2)-i):  # len(list2)-i可以控制每一轮对比元素个数随轮数增加递减
        if list2[j] < list2[j+1]:  # 如果list2[j]<list2[j+1]成立，倒换list2[j]和list2[j+1]的值
            list2[j], list2[j+1] = list2[j+1], list2[j]  # 倒换list2[j]和list2[j+1]的值


# 使用for 语句遍历排序后的list2
for i in list2:  # 变量i表示列表list2中的元素
    print(i, end=" ")


r=len(list2)
print(r)
