"""
从键盘输入3个整数，判定可以组成什么三角形？
任意两边之和大于第三边组成三角形
a == b 且 b==c  等边
a == b 且 b!=c  或  a == c 且 b!=c   或 b == c 且 b!=a  等腰
a*a + b*b == c*c 或 b*b + c*c ==a*a 或  a*a + c*c == b*b 直角
a*a + b*b < c*c 或 b*b + c*c <a*a 或  a*a + c*c < b*b 钝角
a*a + b*b > c*c 且 b*b + c*c >a*a 且  a*a + c*c > b*b 锐角

要求要能判断出是等腰的直角还是等腰的锐角还是等腰的钝角还是等边还是一般直角还是一般锐角还是一般钝角
"""
# the first method
"""a=int(input("input a:"))
b=int(input("input b:"))
c=int(input("input c:"))
if a+b>c and b+c>a and a+c>b:
    if a==b & b==c:
        print("dengbianruijiaoxing")
    elif a == b and b!=c or b == c and a!=c or a == c and b!=c:
        if a*a + b*b == c*c or b*b + c*c ==a*a or  a*a + c*c == b*b:
            print("dengyaozhijiaosanjiaoxing")
        elif a*a + b*b < c*c or b*b + c*c <a*a or  a*a + c*c < b*b:
            print("dengyaoruijiaosanjiaoxing")
        elif a*a + b*b > c*c or b*b + c*c >a*a or  a*a + c*c > b*b:
            print("dengyaodunjiaosanjiaoxing")
    else:
        if a*a + b*b == c*c or b*b + c*c ==a*a or  a*a + c*c == b*b:
            print("yibanzhijiaosanjiaoxing")
        elif a*a + b*b < c*c or b*b + c*c <a*a or  a*a + c*c < b*b:
            print("yibanruijiaosanjiaoxing")
        elif a*a + b*b > c*c or b*b + c*c >a*a or  a*a + c*c > b*b:
            print("yibandunjiaosanjiaoxing")
else:
    print("bunengzuchengsanjiaoxing")"""

# the second method
a=int(input("input a:"))
b=int(input("input b:"))
c=int(input("input c:"))
if a+b>c and b+c>a and a+c>b:
        if a*a + b*b == c*c or b*b + c*c ==a*a or  a*a + c*c == b*b:
            if a == b and b!=c or b == c and a!=c or a == c and b!=c:
                print("dengyaozhijiaojiaosanjiaoxing")
            else:
                print("yibanzhijiaojiaosanjiaoxing")
        elif a*a + b*b < c*c or b*b + c*c <a*a or  a*a + c*c < b*b:
            if a == b and b!=c or b == c and a!=c or a == c and b!=c:
                print("dengyaodunjiaojiaosanjiaoxing")
            else:
                print("yibandunjiaojiaosanjiaoxing")
        elif a*a + b*b > c*c or b*b + c*c >a*a or  a*a + c*c > b*b:
            if a == b and b!=c or b == c and a!=c or a == c and b!=c:
                print("dengyaoruijiaojiaosanjiaoxing")
            elif a==b & b==c:
                print("dengbianruijiaosanjiaoxing")
            else:
                print("yibanruijiaojiaosanjiaoxing")      
else:
    print("bunengzuchengsanjiaoxing")
