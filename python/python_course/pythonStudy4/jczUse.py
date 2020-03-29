
from pythonStudy4.jichengZi import jcz
# 实例化jcz的对象
j1 = jcz()
j1.a = 10  # 子类对象j1可以直接使用父类的属性和方法
j1._b =12
# j1.__c =11
j1.d = 13
print(j1.jisuan())
print(j1.jisuan2())
print(j1.jisuan3())
print(j1.jisuan4())
print(j1.jisuan5())

