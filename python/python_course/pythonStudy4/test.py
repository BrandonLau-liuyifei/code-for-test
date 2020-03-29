# 作业：1、定义一个函数，定义一个字符串类型形参，实现传入任意一个字符串，返回去重升序排序后的字符串
# def resort(str1):
#     set1=set(str1)
#     list1=list(set1)
#     list1.sort()
#     return ''.join(list1)
# if __name__== "__main__":
#     str0=input("请输入一个字符串：")
#     str2= resort(str0)
#     print (str2)
from time import sleep

print("-----------------------------------------------------------")
#2、定义一个函数，定义一个字符串类型形参，实现传入任意一个字符串，返回该字符串中个数最多的字符及个数
#   例如传入：asdssdf   返回s 3
# def maxcout(str0):
#     a=[]
#     c=[]
#     for i in range(0,len(str0)):
#         a.append(len(str0.split(str0[i])))
#     for i in range(0,len(str0)):
#         if len(str0.split(str0[i]))==max(a):
#             c.append(str0[i])
#     set1=set(c)
#     return set1,max(a)-1
# if __name__=="__main__":
#     F=True
#     while F:
#         str0 = input("please input a non-empty string:")
#         b=maxcout(str0)
#         print(b)
#         sleep(0.5)
#         Num=ord(input("Press the key Q to quit the function."
#                       "\nOnly a single key from A to Z is valid."))
#         if Num==81 or Num==113:
#             F=False
print("-----------------------------------------------------------")


# 3、定义一个函数，实现对一个列表按照指定索引范围排序
#   paixu（list， a，b）：实现对列表list中索引范围a--b-1内的列表排序
def paixu(list1,a,b):
    list2=list1[:a]
    list3=list1[a:b]
    list3.sort()
    list4=list1[b:]
    list5=list2+list3+list4
    return list5
if __name__== "__main__":
    str0=input("请输入一个字符串：")
    list1=list(str0)
    print(list1)
    q= paixu(list1,4,8)
    print (q)
print('----------------------------------------------------------')
"""

def register(username,password):
    a=[]
    b=[]
    if username not in a:
        a.append(username)
        if password!="":
            b.append(password)
        else:
            print("Password can not be none.")
    else:
        print("Username was registered.")
    return a,b
def login(username,password):
    c=register.a
    d=register.b
    for i in c:
        if username==c[i]:
            e=i
            if d[e]==password:
                print("Successful login.")
            else:
                print("Wrong password.")
                f=input("please input the right password:")
        else:
            print("No such user")
"""



