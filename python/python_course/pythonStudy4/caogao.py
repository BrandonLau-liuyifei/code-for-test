#去重升序排序
# def shengxu(a):
#     b=set(a)
#     b=list(b)
#     b.sort()
#     for i in b:
#         print(i,end="")
#
# x=input("请输入一个字符串：")
# shengxu(x)

#查询出现次数最多的字符
def chaxun(a):
    seta=set(a)
    list2=list(seta)
    list1=[]
    for i in list2:
        list1.append(a.count(i,0,len(a)))
    r=max(list1)
    for i in range(0,len(list1)):
        if list1[i]==r:
            print(list2[i],r)
#
x=input("请输入一个字符串：")
chaxun(x)

# 定义一个函数，实现对一个列表按照指定索引范围排序
#                 paixu（list， a，b）：实现对列表list中索引范围a--b-1内的列表排序
def suoyinpaixu(list1,a,b):
    list2=list1[a:b]
    list2.sort()
    list1[a:b]=list2
    print(list1)

a=[1,4,7,3,3,4,9,0,3]
suoyinpaixu(a,2,7)





