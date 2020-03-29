
def cheng(a, b):
    return a*b
def get_str_by_index(str, i):
    return str[i]
# 设置默认参数
def cheng2(a=3, b=5):
    return a*b

# 定义不定长参数的函数
def fun(*args):
    print(args)
    for i in args:
        print(i, end=" ")

def fun2(**kwargs):
    print(kwargs)

def fun3(a, b, c=54, *args,**kwargs):
    print("a=",a,"b=",b, "c=",c, "args=",args, "kwargs=",kwargs)

if __name__ == "__main__":
    r = cheng(3,3)
    print(r)
    r = get_str_by_index("wer", 1)
    print(r)
    #在传实参时，声明某个实参赋值给某个形参，可以不用按照形参的顺序传参
    r = get_str_by_index(i=1, str="wert")
    print(r)
    r = get_str_by_index(str = "wert", i=1)
    print(r)
    r = cheng2()  # 按照默认值计算
    print(r)
    r = cheng2(4, 6)  # 按照传入的值计算
    print(r)
    r = cheng2(7)  # 第一个参数按照传入的值计算
    print(r)
    r = cheng2(b=7)  # 声明传入的实参赋值给形参b
    print(r)
    # 调用不定长参数的函数，传入不定长参数
    fun(4, 8,"eee", [3,4,5])  # 传入的参数会形成为元组
    print()
    fun2(num = 4, num2=8, sdsf="333")
    fun3(3,4,5,6,7,e=8,n=9,m=10)
