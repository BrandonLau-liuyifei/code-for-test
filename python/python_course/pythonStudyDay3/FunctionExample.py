# 定义函数
def jia():
    print(1+1)

def jia2(a, b):  # 定义函数jia2，设置两个参数
    print(a + b)

def jia3(a,b): # 定义函数jia2，设置两个参数
    return a+b  # 返回a+b的值

def jia4():
    return (1+1)
# 任何模块都有一个属性__name__，当在本模块内执行代码时，该属性的值为__main__
#当模块被导入引用，在引用的模块内执行代码时，被导入模块的__name__属性值变为了被导入模块名称
if __name__ == "__main__":
    jia()  #调用jia函数
    jia2(3, 4)
    jia2(100, 20)
    r = jia3(5, 9)
    print(r)
    c=jia4()
    print(c)
