def list_sort(T):
    T.sort()
    print(T)
list_sort([4,6,3,2,9,0])

def str_none(str_01):
    j=0
    for i in str_01:
        if i==" ":
            j=j+1
    print(j)
str_none("ab cd ef gh im no")

user=[
    {"name":"john","password":"123","usertype":"1"},
    {"name":"john1","password":"123d","usertype":"2"},
]
name=[]
password=[]
usertype=[]
for i in user:
    name.append(i.get("name"))
    password.append(i.get("password"))
    usertype.append(i.get("usertype"))
def logcheck():
    name_input=input("请输入用户名：")
    if name_input in name:
        for nn in range(len(name)):
            if name[nn]==name_input:
                password_input=input("请输入密码：")
                if password_input == password[nn]:
                    print(usertype[nn])
                else:
                    print("密码错误:",0)
    else:
        print("账户错误：",0)
logcheck()




