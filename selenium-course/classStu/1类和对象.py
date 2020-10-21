# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/2/5


# 声明一个类
class Foo:
    # 创建类中的的函数，也叫作方法
    def func(self, act_name):
        print("这是类里边的函数")
        print(act_name)


# 根据类 Foo 创建了对象 sunShangx，也叫类的实例化
sunShangx = Foo()
liuBei = Foo()


sunShangx.func("释放了一技能")
liuBei.func("释放了大招")




