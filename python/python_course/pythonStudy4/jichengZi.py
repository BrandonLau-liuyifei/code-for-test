
from pythonStudy4.JichengFu import jcf

# 定义类jcz继承jcf
class jcz(jcf):
    d = 0
    def jisuan2(self):
        return self.a + self.d

    def jisuan3(self):
        return  self.jisuan() + self.d

    def jisuan4(self):
        return self.jisuan() + self._b
    
    def jisuan5(self):
        return self.d + self.__c