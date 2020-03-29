# a=input("请输入字符串：")
# b=input("请输入子串：")
# c=a.find(b,0,len(a))
# if c != -1:
#     d = c+len(b)-1
#     print("%s在%s中的索引值为：%d"%(b[-1],a,d))
# else:
#     print("%s在%s中不存在" % (b, a))

# 定义一个函数实现判断一个字符串的子串最后一个字符在整个字符串中的索引并返回，如果子串不存在返回-1

def get_last_char_index(str, substr):
    c = str.find(substr,0,len(str))
    if c != -1:
        d = c+len(substr)-1
        return d
    else:
        return -1

# 定义函数，实现对列表的降序排序
def jiangxu_list(list2):
    if type(list2) is list:
        for i in range(1, len(list2)):  # 变量i表示排序轮数
            # 嵌套for循环遍历列表，获取元素两两对比，变量j表示索引，每一轮对比元素都是从第一个开始，所以j必须从0开始.
            for j in range(0, len(list2) - i):  # len(list2)-i可以控制每一轮对比元素个数随轮数增加递减
                if list2[j] < list2[j + 1]:  # 如果list2[j]<list2[j+1]成立，倒换list2[j]和list2[j+1]的值
                    list2[j], list2[j + 1] = list2[j + 1], list2[j]  # 倒换list2[j]和list2[j+1]的值
    else:
        return None


if __name__ == "__main__":
    r = get_last_char_index("wsxedc", "sxxe")  # 调用get_last_char_index函数
    print(r)





