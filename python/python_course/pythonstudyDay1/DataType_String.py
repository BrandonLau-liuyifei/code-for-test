# 使用""定义字符串
a = "tom and jerry"
# 使用单引号定义字符串
b = '中华人民共和国万岁'
# 定义包含双引号的字符串
c = '香港的"港独"去死'
# 定义包含单引号的字符串
d = "香港的'港独'去死第二次"
# 在字符串中转义双引号和单引号
e = '香港的\"港独\'去死第二次'
# 通过索引获取字符串中字符
# 获取索引为0的字符
r = e[0]
print("字符串e的第一个字符是：", r)
# 对字符串切片
# 获取字符串e中的第2-6个字符
r = e[1:6]  # str[a:b]获取的是索引范围a--b-1的字符
print("aaaa",r)

r = e[1:]  # # str[a:]获取的是索引a以后的所有字符
print(r)

r = e[:6]  # # str[a:]获取的是索引a以后的所有字符
print(r)   # str[:b]获取的是索引0--b-1范围内字符

r = e[1:6:3]  # str[a:b:c]在索引范围a--b-1内，从a还是按照步长c增加索引值获取字符，到b-1结束
print(r)
# 在python中字符串的索引从右向左的值从-1开始一次递减
a = "tom and jerry"
print(a[-1])
print("***", a[-5:-1])

# 使用+拼接字符串
b = "tom"
c = "jerry"
d = b + c
print(d)
# 使用*复制字符串
d = d*3
print(d)

# 成员运算符在字符串中的应用
e = "tomandjerry"
r = "tom" in e
print(r)
r = "tom" not in e
print(r)

# 字符串中转义字符
print("d:\nc\python")  # \n 转义为换行
print("d:\\nc\python")  # \\ 转义为\
print(r"d:\nc\python")  # 字符串前加r防止转义
str1 = r"d:\nc\python"  # 字符串前加r防止转义
print("d:\tc\python")  # \t 转义tab

# 字符串格式化
name = "tom"
print("我是%s猫" % name)  # 字符串格式化

#从键盘输入人名，年龄，体重
# username = input("请输入姓名：")
# age = int(input("请输入年龄："))
# weight = float(input("请输入体重："))
# print("我叫%s，%d岁，%f公斤" %(username, age, weight))  # 在一个字符串中多次格式化

# 常用函数
# len(),   获取字符串长度，并返回
str2 = "中华人民共和国万岁"
print("str2长度：", len(str2))
# replace(),将字符串中某个子串替换为另一个字符串,并返回替换后字符串
new_str2 = str2.replace("人民", "renmin")
print(new_str2)
# split(),使用字符串中的某个字符，分隔字符串，返回一个列表
str3 = "wdewdruidet"
str_list = str3.split("d")
print(str_list)
# count(),在指定索引范围内统计某个子串出现的次数
str4 = 'wrwrddwruier'
r = str4.count("wr", 0, 8)  # count("s", a,b),在索引范围a--b-1范围内统计子串s的次数
print(r)
# find(),检测子串是否存在于字符串中，存在则返回子串第一个字符在整个字符串中的索引，不存在返回-1
str5 = 'wrwrddwruier'
r = str5.find("wr", 3, 9)  # find("s", a, b)  在索引a--b-1范围内查找子串s，找到则返回子串第一个字符在整个字符串中的索引
print(r)


str6 = "sdgwetr"
for s in str6:
    print(s)








