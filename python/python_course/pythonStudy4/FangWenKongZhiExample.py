class fwkz:
    a = 0
    b = 0
    _c = 0  # 定义受保护的属性
    __d = 0 # 定义私有的属性


    def jisuan(self):
        return self.a + self.b

    def jisuan2(self):
        return  self.a + self._c

    def jisuan3(self):
        return self.b + self.__d