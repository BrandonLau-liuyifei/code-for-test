#实例化fwkz类的对象
from pythonStudy4.FangWenKongZhiExample import fwkz

f1 = fwkz()
f1.a = 5
f1.b = 6
print(f1.jisuan())

f1.a = 5
f1._c= 7
print(f1.jisuan2())

f1.b = 6
f1.__d = 10
print(f1.jisuan3())