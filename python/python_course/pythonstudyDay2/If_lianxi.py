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
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if a+b > c and b+c > a and a+c > b:
    if a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
        if a == b and b != c or a == c and b != c or b == c and b != a:
            print("等腰直角")
        else:
            print("一般直角")
    elif a*a + b*b < c*c or b*b + c*c < a*a or a*a + c*c < b*b:
        if a == b and b != c or a == c and b != c or b == c and b != a:
            print("等腰钝角")
        else:
            print("一般钝角")
    elif a*a + b*b > c*c and b*b + c*c > a*a and a*a + c*c > b*b:
        if a == b and b != c or a == c and b != c or b == c and b != a:
            print("等腰锐角")
        elif a == b and b == c:
            print("等边")
        else:
            print("一般锐角")
else:
    print("输入三边不能组成三角形")