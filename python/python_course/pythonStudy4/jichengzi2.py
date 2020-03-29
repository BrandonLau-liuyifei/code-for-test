from pythonStudy4.JichengFu import jcf
from pythonStudy4.jichengFu2 import jcf2

# 定义类jcz2同时继承自jcf和jcf2两个类
class jcz2(jcf, jcf2):
    def jisuan6(self):
        return self.d + self.a

# 定义jczz类继承自jcz2类，由于jcz2同时继承自jcf和jcf2两个类
# jczz会继承jcz2、jcf、jcf2三个类中的非私有的属性和方法
class jczz(jcz2):
    def jisuan7(self):
        return self.jisuan6() + self.a + self.d
