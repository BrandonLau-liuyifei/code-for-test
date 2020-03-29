# 定义一个类
class people:
    # 定义属性
    name = ""
    age = 0
    # 定义方法
    def speak(self):  # self代表类的实例
        print("我叫%s，今年%d岁"%(self.name, self.age))
