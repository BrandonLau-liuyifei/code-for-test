# 6.面向对象编程
#6.1 面向对象编程、类、对象，三大特点：封装、继承、包含
#6.2.1 定义类
"""
class <类名>(父类名):
    pass
"""

#空类 会继承内建类
class MyClass:
    pass
print(dir(MyClass))

#6.2.2 使用类
class MyClass1:
    "MyClass help."
myclass = MyClass1()
print("输出类说明：")
print(myclass.__doc__)
print("显示类帮助信息：")
help(myclass)

# 6.3类的属性和方法
"""
方法的第一个参数必须是self，而且不能省略
方法调用需要实例化类，并以实例名。方法名（参数列表）形式调用
整体进行一个单位的缩进，表示其属于类体中的内容
"""
# 6.3.1 类的方法
class SamplClass:
    def info(self):
        print("我定义的类！")
    def mycacl(self,x,y):
        return x+y
sc = SamplClass()
print("调用info方法的结果：")
sc.info()
print("调用mycacl方法的结果：")
print(sc.mycacl(3,4))

class DemoInit():
    def __init__(self,x,y=0):  #定义构造方法，具有两个初始化
        self.x = x
        self.y = y
    def mycacl1(self):  #定义应用初始化数据的方法
        return self.x+self.y
dia = DemoInit(3)
print("调用mycacl1方法结果1：")
print(dia.mycacl1())
dia = DemoInit(3,7)
print("调用mycacl1方法结果2：")
print(dia.mycacl1())

def coord_chng(x,y):    #定义一个全局函数，模拟坐标转换
    return(abs(x),abs(y))
class Ant:   #定义一个类Ant
    def __init__(self,x=0,y=0):  #定义一个构造方法
        self.x = x
        self.y = y
        self.disp_point()   #构造函数中调用类中的方法disp_point
    def move(self,x,y):   #定义一个方法move
        x,y = coord_chng(x,y)   #调用全局函数，坐标转换
        self.edit_point(x,y)
        self.disp_point(x,y)
    def edit_point(self,x,y):   #定义一个方法
        self.x +=x
        self.y +=y
    def disp_point(self):  #定义一个方法
        print("当前位置：(%d,%d)" % (self.x,self.y))
ant_a = Ant()
ant_a.move(2,4)
ant_a.move(-9,6)

#6.3.2 类的属性
"""
实例属性  self.属性名
类属性 类名.实例名
"""









