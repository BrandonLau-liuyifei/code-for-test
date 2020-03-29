# 给多个变量同时赋值
a, b = 3, 4 # 3被赋值给a，4被赋值给b
print("b和a的值分别是", b, a)
# 给变量c 赋值为bool型值Ture
c = True
print(c + c)
# 给变量d 赋值为bool型值False
d = False
print(d == 0)
# 在python中除了0和None以外，一切为真
if 100:
    print("100在python中为True")


if "der":
    print("der在python中为True")
# 给变量e 赋值为复数
e = 3 + 4j
print(e+e)

# 给变量f赋值为浮点型数据
f = 3.9
print(a * f)

# 数字类型转换
# 将浮点数f转换为整数,小数部分被舍掉
r = int(f)
print(r)
s = "123"  # 定义字符串s,纯数字组成的字符串可以转换为数字
print(type(s))
r = int(s)
print(type(r))
print(r)
# 将整数转为浮点数
g = 3
r = float(g)
print(r)

s = "12.7"
r = float(s)  # float可以将由数字组成的字符串或由数字+点组成的字符串转换为小数
print(r)

#将整数转换为复数
r = complex(3, 4)
print(r)







