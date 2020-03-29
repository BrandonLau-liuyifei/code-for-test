
d = input("是否开始判断？ yes or no")
while d == "yes":
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    if a+b > c and a+c > b and b+c > a:
        print("构成三角形")
    else:
        print("不构成三角形")
    d = input("是否继续判断？ yes or no")
else:
    print("判断结束")