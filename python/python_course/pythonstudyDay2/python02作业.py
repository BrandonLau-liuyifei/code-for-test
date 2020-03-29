# 字符串位置查询
str1=str(input("请输入父字符串："))
str2=str(input("请输入子字符串："))
if str2 not in str1:
    print("警告：不在该父符串内")
else:
    l=str1.find(str2,0,len(str1))+len(str2)-1
    print(l)

# 字符串排序
str1=str(input("请输入任意一个字符串："))
set1=set(str1)
list1=list(set1)
list1.sort()
print(list1)

# 输入年月得天数
time=str(input("inputxxxx-xx格式:"))
year=int(time[0:4])
month=int(time[6:7])
list1=[1,3,5,7,8,10,12]
list2=[4,6,9,11]
if month>=1 and month<=12:
    if month in list1:
        print("%d月的天数：31天" %month)
    elif month in list2:
        print("%d月的天数：30天" %month)
    else:
        if year%4==0:
            print("%d月分数:28天" %month)
        else:
            print("%d月分数:29天" %month)
else:
    print("输错啦")

