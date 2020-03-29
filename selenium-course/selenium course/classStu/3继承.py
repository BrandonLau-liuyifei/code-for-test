# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/2/5


class Animal:
    def __init__(self, weight):
        self.weight = weight

    def action(self):
        print("吃喝拉撒")


# 子类可以有自己的扩展
class Dog(Animal):  # Dog 类继承 Animal 类
    def __init__(self, name, weight):
        # super 关键字执行父类中的构造方法       子类可以继承父类的属性和方法
        super(Dog, self).__init__(weight)
        self.name = name

    # 子类可以有自己的特色行为
    def voice(self):
        print(self.name, "汪汪叫")


class Cat(Animal):  # Cat 类继承 Animal 类
    def __init__(self, name):
        self.name = name

    # 子类可以有自己的特色行为
    def voice(self):
        print(self.name, "喵喵叫")


wangCai = Dog("旺财", 60)
wangCai.action()  # 子类可以继承父类的方法和属性并直接调用
wangCai.voice()  # 子类可以有自己的特色，调用自己的方法
print(wangCai.weight)


jiaFei = Cat("加肥")
jiaFei.action()
jiaFei.voice()



# 子类没有构造方法，可以直接调用父类构造方法中封装的属性
class Pig(Animal):
    # 子类可以有自己的特色行为
    def voice(self):
        print("哼唧哼唧")

p = Pig(60)
print(p.weight)

