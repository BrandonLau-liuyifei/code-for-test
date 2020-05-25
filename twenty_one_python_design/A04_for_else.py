"""
for <循环变量> in <遍历对象>：
    <语句1>
else:
    <语句2>
"""

# for循环可以遍历字符串字符串、列表、元组、字典
for i in [1,2,3,4,5]:
    print(i,"的平方是：",i**2)
else:
    print("我不是遍历的值哦")

"""continue 跳过 & break 跳出"""

for i in (1,2,3,4,5):
    if i == 2:
        continue
    print(i,"的平方是：",i**2)
    if i ==4:
        break
else:
    print("循环结束了，么得值了")

dict_01 = {"apple":3,"banana":3.5,"pear":2.5}
for key,value in dict_01.items():   # items()
    print(key,":",value)
for key in dict_01.keys():          #key()
    print(key)
for i in dict_01.values():          #values()
    print(value)

# for_range
#range([start],stop[,step])
print("第一次循环输出：")
for i in range(4):
    print(i)
print("第二次循环输出：")
for i in range(0,8,2):
    print(i)

#复杂遍历  求输入两个数值之间的所有素数
x = (int(input("请输入开始值（int）：")),int(input("请输入结束值（int）：")))
x_max = max(x)
x_min = min(x)

for n in range(x_min,x_max+1):
    for i in range(2,n-1):
        if n % i == 0:
            break
    else:
        print(n,"：为素数")

# for语句与内置迭代函数
"""
enumerate(seq) 编号迭代
sorted(seq) 排序迭代
reversed(seq) 翻转迭代
zip(seq1,seq2,...) 并行迭代
"""
# 编号迭代 即返回编号，又返回值
for i,item in enumerate("dhfjgglrir"):
    print("第%d个值是%s" % (i,item))

#排序迭代 先遍历最小的值，在遍历最大的值
for i in sorted([3,1,4,6,2]):
    print(i)

#翻转迭代
for i in reversed([3,1,4,6,2]):
    print(i)

#并行迭代 多个遍历同时进行
aa = [1,2,3,4]
bb = [11,22,33,44]
cc = [111,222,333,444]
for a,b,c in zip(aa,bb,cc):
    print("aa的是%s,bb的是%s.cc的是%s:" % (a,b,c))
