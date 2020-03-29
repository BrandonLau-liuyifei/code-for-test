# lianxi-01 1、定义一个函数，定义一个字符串类型形参，实现传入任意一个字符串，返回去重升序排序后的字符串

"""str1=str(input("insert s: "))
set1=set(str1)
list1=list(set1)
list1.sort()
for i in list1:
    print(i,end="")"""

def lianxi_01(str1):
    # str1=str(input("insert s: "))
    set1=set(str1)
    list1=list(set1)
    list1.sort()
    for i in list1:
        print(i,end="")

# lianxi-02 2、定义一个函数，定义一个字符串类型形参，实现传入任意一个字符串，返回该字符串中个数最多的字符及个数例如传入：asdssdf   返回s 3

"""# str2=str(input("insert s: "))
    set1=set(str2)
    list2=list(set1)
    list1=[]
    for i in list2:
        n=str2.count(i,0,len(str2))
        list1.append(n)
    r=max(list1)
    for i in range(0,len(list1)):
        if list1[i]==r:
            print(list2[i],r)"""

def lianxi_02(str2):
    # str2=str(input("insert s: "))
    set1=set(str2)
    list2=list(set1)
    list1=[]
    for i in list2:
        n=str2.count(i,0,len(str2))
        list1.append(n)
    r=max(list1)
    for i in range(0,len(list1)):
        if list1[i]==r:
            print(list2[i],r)
# lianxi_03 3、定义一个函数，实现对一个列表按照指定索引范围排序paixu（list， a，b）：实现对列表list中索引范围a--b-1内的列表排序

"""list1=["1","3","2","8","x","m","b"]
a=1
b=6
for i in range(1,b-a):
    for j in range(a,b-i):
        if list1[j]<list1[j+1]:
            list1[j],list1[j+1]=list1[j],list1[j+1]
        else:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)"""

def lianxi_03(list1,a,b):
    # list1=["1","3","2","8","x","m","b"]
    # a=1
    # b=6
    for i in range(1,b-a):
        for j in range(a,b-i):
            if list1[j]<list1[j+1]:
                list1[j],list1[j+1]=list1[j],list1[j+1]
            else:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    print(list1)

if __name__=="__main__"


    

