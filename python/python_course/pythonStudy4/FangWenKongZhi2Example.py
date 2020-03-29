class paixu2:
    # 定义公共方法，在公共方法中调用私有属性，对私有属性的使用加以保护
    def set_value(self,list1, a, b):
        if type(list1) is list and type(a) is int and type(b) is int:
            self.__list1 = list1
            self.__a = a
            self.__b = b
        else:
            self.__list1 = [0]
            self.__a = 0
            self.__b = 0

    # 定义方法,在方法中使用了私有的属性
    def suoyinpaixu(self):
        list2 = self.__list1[self.__a:self.__b]
        list2.sort()
        self.__list1[self.__a:self.__b] = list2
        print(self.__list1)





    def __suoyinpaixu2(self, list1, a, b):
        list2 = list1[a:b]
        list2.sort()
        list1[a:b] = list2
        print(list1)
    # 定义公共方法，在公共方法中调用私有方法，对私有方法的使用加以保护
    def suoyinpaixu_public(self,list1, a, b):
        if type(list1)is list and type(a) is int and type(b) is int:
            self.__suoyinpaixu2(list1, a, b)