#作业1 从键盘输入任意一个字符串，再输入该字符串的任意一个子串，打印输出子串的最后一个字符在整个字符串中的索引可能用到函数find()。

# a=input("请输入字符串：")
# b=input("请输入子串：")
# c=a.find(b,0,len(a))
# if c != -1:
#     d = c+len(b)-1
#     print("%s在%s中的索引值为：%d"%(b[-1],a,d))
# else:
#     print("%s在%s中不存在" % (b, a))

#作业2 输入任意一个字符串，将字符串中的字符去重并按照升序排序打印出来。可能用到函数set(),str(),list()，sort(),切片

# e=input("请输入字符串：")
# set1=set(e)
# list1=list(set1)
# list1.sort()
# for i in list1:
#     print(i,end="")
# print()



#作业3 按照下列各式（XXXX-XX）从键盘输入年月，打印输出该年月有多少天 例如：输入：2019-08或2019-8 打印输出：31天

f=input("请输入年月（格式XXXX-XX或XXXX-X）：")
year=int(f[0:(f.find('-'))])
print(year)
g=f[(f.find('-'))+1:]
e=int(g)
if e in (1,3,5,7,8,10,12):
    print("31天")
elif e == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("29天") #闰年
    else:
        print("28天")
else:
    print("30天")
