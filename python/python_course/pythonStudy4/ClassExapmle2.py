class paixu:
    # 定义方法
    def suoyinpaixu(self, list1, a, b):
        list2 = list1[a:b]
        list2.sort()
        list1[a:b] = list2
        print(list1)
