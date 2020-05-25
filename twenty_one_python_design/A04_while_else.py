"""
while <条件1>
    <语句1>
else:
    <语句2>
"""

list_01 = [1,2,3,4,5]
total = len(list_01)
i = 0
while i <= total-1:
    print(i,list_01[i]**2)
    i = i+1
else:
    print("循环结束")







