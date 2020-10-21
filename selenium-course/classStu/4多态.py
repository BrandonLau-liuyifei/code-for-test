# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/2/5


# # 在 JAVA 中创建变量必须指定数据类型
# public static viod main(String[] args){};
# # 上述一行定义了一个方法，指定了变量类型 String 类，如果赋值不是 String 类 就会报错

# public static viod main(Foo[] args){};
# # 自己实现一个 Foo 类，赋值类型就可以是Foo类或其子类中的任意一个


# 但是 python 原生多态，所以没有这种限制
def foo(num):
    print(num)


foo("你好")

foo(100)

