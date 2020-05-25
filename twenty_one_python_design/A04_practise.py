# 二-1

# course_01 = int(input("first_score："))
# if course_01 >= 60:
#     course_02 = int(input("second_score："))
#     if course_02 >= 60:
#         print(" 通过")
#     else:
#         print("补考")
# else:
#     print("不通过")

haha_01 = "你很乖啦"
haha_02 = "那还不赶紧补偿一下"
haha_03 = "冯楠怎么不听话"

call_liu = input("不是给我打电话吗？打了 or 没打：")
if call_liu == "打了":
    xiang_qing_chu = input("想清楚哦！打了 or 没打：")
    if xiang_qing_chu == "打了":
        print(haha_01)
    else:
        print(haha_02)
else:
    print(haha_03)