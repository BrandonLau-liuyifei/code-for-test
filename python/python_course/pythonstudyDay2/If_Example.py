
# 从键盘输入两个整数
a = int(input("请输入a："))
b = int(input("请输入b："))

# if语句判定a与b的大小
if a>b:
    print("%d>%d"%(a,b))
elif a==b:
    print("%d=%d" % (a, b))
elif a<b:
    print("%d<%d" % (a, b))

if a>b or a == b:
   print("%d>=%d" % (a, b))
else:
    print("%d<%d" % (a, b))

if a> b or a == b:
   print("%d>=%d" % (a, b))
   if a > b:
       print("%d>%d" % (a, b))
   else:
       print("%d=%d" % (a, b))
else:
    print("%d<%d" % (a, b))
    if b-a>5:
        print("%d-%d>5" % (b, a))
    elif b-a == 5:
        print("%d-%d=5" % (b, a))
    elif b-a < 5:
        print("%d-%d<5" % (b, a))


