# 5.1函数使用
# 5.1.1 声明函数
"""
def <函数名> (参数列表)：
    <函数语句>
    return <返回值>
"""
# 5.1.2 调用函数
def hello():
    print("hello world")
hello()

def tpl_sum(T):
    result = 1
    for i in T:
        result = result+i
    return result
ll = tpl_sum([1,2,3,4])
print(ll)

# 5.2.1 默认值参数
"""
def <函数名> (参数=默认值):
    <语句>
"""
def hello1(name="python"):
    print("您好，%s!" % name)
hello1()
hello1("liuyifei")

# 先声明无默认值参数，再声明有默认值参数
def test(a,b = 3):
    pass
test(3)

#5.2.2 参数传递
def hello3(hi = "您好",name = "Python"):
    print("%s,%s" % (hi,name))
hello3("jonson")
hello3("hi","Json")
#参数传递
hello3(name = "周杰伦")
hello3(name = "林俊杰",hi= "周杰伦")

#5.2.3 可变数量参数传递
# *变量，该参数就是一个可变长参数，在调用该函数时，依次序赋值后，剩下的参数将收集到该带*号的元祖中，参数不能为关键字参数为
def change_para_num(*tpl):
    print(type(tpl))
    print(tpl)
change_para_num(1,2,3)

def change_para_num1(*tpl,a,b = 0):
    print("tpl:",tpl)
    print("a:",a)
    print("b:",b)
change_para_num1(1,2,3,a=5)

# **变量，自定义参数时的参数前加**，多余的关键字以字典的方式收集到变量中，该变量放在所有参数之后
def change_para_dic(a,b = 0,**adict):
    print("adict:",adict)
    print("a",a)
    print("b",b)
change_para_dic(1,k=3,b=2,c=3)

def cube(name,**nature):
    all_nature = {
        "x":1,
        "y":1,
        "z":1,
        "color":"white",
        "weight":1
    }
    all_nature.update(nature)
    print(name,"立方的属性")
    print("体积",all_nature["x"]*all_nature["y"]*all_nature["z"])
    print("颜色",all_nature["color"])
    print("重量",all_nature["weight"])
cube("first")
cube("second",y=3,color="red")
cube("third",z=2,color="green",weight=10)

#5.2.4 拆解序列的函数调用
def mysum(a,b):
    return a+b
print("拆解元祖调用：")
print(mysum(*(5,9)))
print("拆解元祖调用：")
print(mysum(**{'a':5,'b':9}))

#   5.2.5函数调用时参数的传递的方法
# 可变   不可变
def change(aint,alist):
    aint=0
    alist[0]=0
    alist.append(4)
    print("函数中的aint：",aint)
    print("函数中的alist：",alist)
aint=3
alist=[1,2,3]
# 调用前
print("函数前的aint：",aint)
print("函数前的alist：",alist)
#调用后
change(aint,alist)
print("函数后的aint：",aint)
print("函数后的alist：",alist)

def myfun(list1=[]):
    list1.append("abc")
    print(list1)
myfun(list1=[])
myfun()
myfun()


def myfun1(list2=None):
    list2 = [] if list2 is None else list2
    list2.append("abc")
    print(list2)
myfun1(list2=None)
myfun1(list2=[])
myfun1()

# 5.3 变量的作用域
"""
内置作用域：Python预先定义的
全局作用域：所编写的整个程序
局部作用域：某个函数局部范围
"""
def myfun3():
    a=0
    a+=3
    print("函数内a：",a)
a="external"
print("全局作用域a：",a)
myfun3()
print("全局作用域a：",a)

def myfun4():
    global a
    a=0
    a+=3
    print("函数内a:",a)
a="external"
print("全局作用域a:",a)
myfun4()
print("全局作用域a:",a)

a=3
def myprint():
    print(a)
myprint()

# 5.4 python内建函数
# 使用匿名函数lambda
# lambda paras:expr
import math
s=lambda x1,y1,x2,y2:math.sqrt((x1-x2)**2+(y1-y2)**2)
x=s(1,2,3,4)
print(x)

aa=bin(20) #10进制转2进制
bb=hex(20) #10进制转16进制
cc=oct(20) #10进制转8进制
dd=callable(a) #测试对象是否可调用
ddd=chr(97) #97ascii码转字符
ee=ord("x") #字符转ascii码
ff=isinstance("abc",str)
list_01=[1,2,3,4,5,6,7,8,9]
list_02=list(filter(lambda x:x%2 and x%3,list_01)) #对序列中的函数进行过滤
list_03=list(map(lambda x:x*2,list_01))
print(aa,bb,cc,ddd,ee,list_02,list_03,ff)

















