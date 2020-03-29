# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/2/5

class Person:
    def __init__(self, name, age, sex, nationality):
        """
        self 是一个形式参数，默认等于根据类创建的对象
        构造方法，根据类创建对象的时候，会自动执行
        可以接受参数，
        创建对象的时候也要传参,
        类可以没有构造方法
        """
        self.name = name  # 将姓名封装进去
        self.age = age    # 将年龄封装进去
        self.sex = sex    # 将性别封装进去
        self.nationality = nationality   # 封装国籍属性

    def foo(self):
        # 类中的方法需要通过 self 间接调用被封装的内容
        print("对象的名称:", self.name)
        # print(name) # 报错

# 根据类创建对象会自动执行 __init__ 方法
# 将 "荀尘", 16, "男", "中华人民共和国"  依次封装到   obj 属性中
# 也就是说针对 Person 的构造函数进行传参，因为根据类创建对象的时候会自动执行构造方法
obj = Person("荀尘", 16, "男", "中华人民共和国")

# 我们上面是不是封装好了，接下来调用
print(obj.nationality)  # 通过对象.属性就可以调用
obj.foo()

