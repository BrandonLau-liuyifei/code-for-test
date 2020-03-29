from DuoTaiExample import paixuzi1 as  p1, paixuzi2  as p2


class duotai:

    #定义一个方法，实现功能根据bool型的值返回不同子类paixuzi1和paixuzi2的对象
    def __get_object(self, bool_value):
        if bool_value == True:
            return p1()  #  将paixuzi1类的对象返回
        elif bool_value == False:
            return p2() #  将paixuzi2类的对象返回

    # 定义一个方法，实现功能根据bool型的值对列表实现升序或降序排序
    def sort_byvalue(self,list1, reverse=False):
        o = self.__get_object(reverse)
        o.sort_byself(list1)


if __name__ == "__main__":
    dt = duotai()
    list1 = [3, 2, 8, 1, 0, 9]
    dt.sort_byvalue(list1, True)
    print(list1)

