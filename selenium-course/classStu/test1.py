# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/4/12

class Animal:
    def __init__(self, name):
        self.name = name

    def action(self):
        print("吃喝拉撒")


class Pig(Animal):
    def __init__(self, activity, name):
        super(Pig, self).__init__(name)
        # super.__init__(self, name)
        self.activity = activity


    # 方法的重载
    # def action(self):
    #     print("变成年货")
    def foo(self):
        print(self.name)
        self.action()


p = Pig("出演动画片", "花花")
print(p.name)  # 子类可以直接调用父类中的属性
p.action()    # 子类可以直接调用父类的方法


