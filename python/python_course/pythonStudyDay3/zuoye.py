str1 = input("输入字符串：")
str2 = input("输入子串")
first_str_index = str1.find(str2)
if first_str_index != -1:
    last_str_index = first_str_index + len(str2) - 1
    print("%s的最后字符%s在整个字符串%s的索引为%d" % (str2,str2[-1],str1,last_str_index))
else:
    print("字符串%s没有子串%s" % (str1, str2))
