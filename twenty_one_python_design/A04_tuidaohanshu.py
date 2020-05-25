#推到函数
# [<i相关表达式> for i in aiterator]
square = [i*i for i in range(1,11)]
print(square)

keys = ["name","age","weight"]
values = ["bob","23","68"]

# {key_exp:value_exp for key_exp,value_exp in aiterator}
dict_0 = {k:v for k,v in zip(keys,values)}
print(dict_0)

#推到函数-进阶
# [<i相关表达式> for i in aiterator if <条件>]
# {key_exp:value_exp for key_exp,value_exp in aiterator if <条件>}
square_odd = [i**2 for i in range(1,11) if i**2%2 != 1]
print(square_odd)

square_odd_01 = []
for i in range(1,11):
    if i**2%2 != 1:
        square_odd_01.append(i**2)
print(square_odd_01)



