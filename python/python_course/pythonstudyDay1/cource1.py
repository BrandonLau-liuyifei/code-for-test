# python开始
print('hello world')

# 注释这样用 # 注释语句 或者ctrl+/，一次选中多个注释，取消也可用ctrl+/

# 模块导入
# 导入模块方式1
import time  # 导入整个模块
time.sleep(5)
from time import *  # 这样表达也可以
sleep(5)

# 导入模块方式2
from time import sleep  # 导入time模块的sleep函数，也可多个函数
sleep(5)

# 导入模块方式3
sleep(5)  # alt+enter 选择导入time模块

# 多语句执行
#   a 加括号，一行完
a, b, c, d = 1, 2, 3, 4
e1 = (a + b + c + d)
print("输出的e1值：",e1)

# b 加\ 分句写
e2 = a + b \
    + c + \
    d
print("输出的e2值为：",e2)

# 数学运算符与运算
f1=c+d
f2=c-d
f3=c*d
f4=c/d
f5=c//d  
f6=c**d
print("f数学运算值为：",f1,f2,f3,f4,f5,f6)

# 关系运算符和运算
print(a>b)
print(a<b)
print(a!=b)
print(a==b)
print(a>=b)
print(a<=b)

if a < b:
    print("我是小的那个：",a)
if c > b:
    print("我是大的那个：",c)

# 赋值运算
a+=b
print(a)
a*=b
print(a)

# 逻辑运算
print(a>b and a<b)
print(a>b or a<b)
print(not a>b)
print(not a<b)

# 成员运算符
list = [1,2,3,4,5,6,7,8,9,0]
h=a in list
print(h)
h=a not in list
print(h)
i=2 in list
print(i)
i=2 not in list
print(i)

for j in  list:  # 使用成员运算符遍历list1
    print(j)

for k in range(0,len(list)): # 定义变量k 表示列表list1的索引，使用索引遍历列表
    print(list[k])
    # 相当于c语言中：for(int i =0; i<len(list1);i++){printf(list1[i])}

# 赋bool值运算
l = True
print(l+l)
m=False
print(m==0)

if 100:
    print("100在python中为真")
if 'abc':
    print("abc在python中为真")
if 0:
    print("输不出来0")

# 数字类型转换
n=3.14159
o=int(n) # 浮点数转整数
p=3
q=float(p) # 整数转浮点数
r='123.456789'
s=float(r) #  字符串转浮点数
print(o,q,s)
t=complex(3,5) # 数字转复数
print(t)

# 字符串定义
aa='我是一个字符串'
bb="我是一个字符串"
cc='我也是"一个"字符串'
dd="我依然是'一个'字符串"
ee="我呢依然是\"一个\'字符串"

ff=aa[0] # 通过索引获取字符串中的字符
gg=aa[1:6] # str[a:b]获取的是索引范围a--b-1的字符
hh=aa[1:] # str[a:]获取的是索引a以后的所有字符
ii=aa[:6] # str[:b]获取的是索引0--b-1范围内字符
print(ff,gg,hh,ii)
jj=aa[1:6:3]
print(jj) # str[a:b:c]在索引范围a--b-1内，从开始按照步长c增加索引值获取字符，到b-1结束
print(aa[-1],aa[-5:-1])

kk='abc'
ll='def'
print(kk+ll) # 字符拼接
print(kk*3) # 字符复制

mm='是'in aa
print(mm)
nn='是'not in aa
print(nn)

# 字符串中转义字符
print('あ\nいしてる') # 换行
print('あ\\nいしてる') # \\转义为\
print(r"あ\nいしてる") # r 不转义作用
print("あ\tいしてる") # \t 空格作用

# 字符串格式化
name = "ねこ"
print("我是%s猫" % name)  # 字符串格式化

# name=input("name:")
# age=int(input("age:"))
# weight=float(input("weight:"))
# print("i'm %s,%d years old,my weight is %fKg" %(name,age,weight))

# 常用函数
# len(),   获取字符串长度，并返回
str2="わたしはりゅうです"
print("the length of str2:",len(str2))

# replace(),将字符串中某个子串替换为另一个字符串,并返回替换后、
new_str2=str2.replace("わたし","これ")
print(new_str2)

# split(),使用字符串中的某个字符，分隔字符串，返回一个列表
new_str3=str2.split("は")
print(new_str3)

# count(),在指定索引范围内统计某个子串出现的次数
ll=str2.count("わ",0,9)
print(ll)

# find(),检测子串是否存在于字符串中，存在则返回子串第一个字符在整个字符串中的索引，不存在返回-1
mm=str2.find("は",0,9)
print(mm)















