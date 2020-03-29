class people2:
    # 定义构造方法
    def __init__(self, n, a):
        self.name = n
        self.age = a
    # 定义方法
    def speak(self):  # self代表类的实例
        print("我叫%s，今年%d岁"%(self.name, self.age))
