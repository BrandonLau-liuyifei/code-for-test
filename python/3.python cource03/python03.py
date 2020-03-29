for i in "abcde":
    print(i,end="")
print()

list1=[1,2,3,4,5]
for i in range(0,len(list1)):
    print(list1[i])

for i in  range(0,10):
    i+=3
    print(i,end="")
print()

for i in range(0,10,3):
    print(i,end="")
print()

for i in range(9,0,-1):
    print(i,end="")
print()

for i in range(10):
    print(i,end="")
print()

for i in range(0,):
    print(i,end="")
print()

for i in range(0,10):
    print(i,end="")
else:
    print("it's me")
    
for i in range(0,10):
    if i%2==0:
        continue
    print(i,end=" ")

for i in 'abcvhdjf':
    if i=="w":
        break
    print(i,end=" ")
else:
    print("it's me") # 只结束for循环， 不结束else

list2=[1,2,3,4,5,[3,4,2],"we",["s","e"]]
for i in list2:
    if type(i) is list: 
        for l in i:
            print(l,end="")
    else:
        print(i,end="")
print()

j=1
for i in range(1,6):
    j=j*i
print(j)


for i in range(1,10):
     for j in range(1,i+1):
         print("%d*%d=%d" %(j,i,i*j),end="  ")
     print()

print()
     
for i in range(1,5):
    for m in range(4,i,-1):
        print(" ",end="")
    for n in range(0,2*i-1):
        print("*",end="")
    print()
#----------------------------------------------------------------
# for 以上循环控制语句练习


i=1
while i<=9:
    j=1
    while j<=i:
        print("%d*%d=%d" %(j,i,j*i),end=" ")
        j+=1
    print()
    i+=1

"""导入random模块
使用random模块下的randrange()函数随机生                成一个数字
n = random.randrange(0, 100)
从键盘输入数字猜n的值，如果猜大了给出猜大了的提升，如果猜小了给出猜小了的提升
猜错了一直猜下去，猜对了结束程序"""



import random
n = random.randrange(0,100)
d=int(input("insert int: "))
while d!=n:
      if d>n:
          print("it's too big")                
      elif d<n:
          print("it's too small")
      d=int(input("insert int: "))
else: 
    print("it's over")

