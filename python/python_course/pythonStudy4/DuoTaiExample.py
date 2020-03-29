# 定义类paixu
class paixu:
    def sort_byself(self, list1):
        return None


# 定义类paixuzi1继承类paixu，在子类paixuzi1中重写父类peixu中的sort_byself()
class paixuzi1(paixu):
    def sort_byself(self, list1):  # 重写父类peixu中的sort_byself()实现降序排序
        if type(list1) is list:
            for i in range(1, len(list1)):  # 变量i表示排序轮数
                # 嵌套for循环遍历列表，获取元素两两对比，变量j表示索引，每一轮对比元素都是从第一个开始，所以j必须从0开始.
                for j in range(0, len(list1) - i):  # len(list1)-i可以控制每一轮对比元素个数随轮数增加递减
                    if list1[j] < list1[j + 1]:  # 如果list1[j]<list1[j+1]成立，倒换list1[j]和list1[j+1]的值
                        list1[j], list1[j + 1] = list1[j + 1], list1[j]  # 倒换list1[j]和list1[j+1]的值
        else:
            return None


# 定义类paixuzi2继承类paixu，在子类paixuzi2中重写父类peixu中的sort_byself()
class paixuzi2(paixu):
    def sort_byself(self, list1):  # 重写父类peixu中的sort_byself()实现升序排序
        if type(list1) is list:
            for i in range(1, len(list1)):  # 变量i表示排序轮数
                # 嵌套for循环遍历列表，获取元素两两对比，变量j表示索引，每一轮对比元素都是从第一个开始，所以j必须从0开始.
                for j in range(0, len(list1) - i):  # len(list1)-i可以控制每一轮对比元素个数随轮数增加递减
                    if list1[j] > list1[j + 1]:  # 如果list1[j]>list1[j+1]成立，倒换list1[j]和list1[j+1]的值
                        list1[j], list1[j + 1] = list1[j + 1], list1[j]  # 倒换list1[j]和list1[j+1]的值
        else:
            return None