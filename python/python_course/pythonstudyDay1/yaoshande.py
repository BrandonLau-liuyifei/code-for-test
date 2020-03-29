list1=[1,2,3]
for i in list1:
    print(i)
for k in range(0,len(list1)):
    print(list1[k])
m=False
print(m*100)
if 100:
    print("100在python中为真")
if 'abc':
    print("abc在python中为真")
if 0:
    print("输不出来0")

aa='我是一个字符串'
bb="我是一个字符串"
cc='我也是"一个"字符串'
dd="我依然是'一个'字符串"
ee="我呢依然是\"一个\'字符串"

ff=aa[0] # 通过索引获取字符串中的字符
gg=aa[1:6] # str[a:b]获取的是索引范围a--b-1的字符
hh=aa[1:] # str[a:]获取的是索引a以后的所有字符
ii=aa[:6] # str[:b]获取的是索引0--b-1范围内字符
print(ff,gg,hh,ii)
jj=aa[1:6:3]
print(jj) # str[a:b:c]在索引范围a--b-1内，从开始按照步长c增加索引值获取字符，到b-1结束
print(aa[-1],aa[-5:-1])

print('あ\nいしてる') # 换行
print('あ\\nいしてる') # \\转义为\
print(r"あ\nいしてる") # r 不转义作用
print("あ\tいしてる") # \t 空格作用

