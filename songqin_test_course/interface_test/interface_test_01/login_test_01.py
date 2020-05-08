"""针对登陆接口进行测试
    接口请求地址
    接口请求参数
    预期结果"""
# import requests
# # 1。掉用接口
# # 2。传入接口参数
# # 3。获取相应结果
# url1="http://localhost:8080/jwshoploh=gin/user/login"
# userinfo = {"username":"张张",
#             "password":"zhangmoumoudemima"
#             }
# response = requests.post(url1,data=userinfo).text()
# print(response)
# # 4。进行对比，得出结论
# msg=response.find("用户名不通过")
# if msg>0:
#     print("登陆接口不传入任何参数，测试通过")
# else:
#     print("登陆接口不传入任何参数，测试失败")

#从CSV文件中调用参数
# import csv
# file = open("userinfo.csv","r")  #和py防止在一起可以免写路径
# table = csv.reader(file)  #table指所有列
# userinfo={}
# for row in table:
#     userinfo["username"]=row[0]
#     userinfo["password"]=row[1]
#     userinfo["result"]=row[2]
#     print(userinfo)

# #测试结果写入excel，统一文件不支持即读又写的状态
# import csv
# file2=open("测试结果.csv","w")
# file2.write("xiaoliu"+","+"xiaoliudemima"+","+"测试结果")
# file2.close()


#代码汇总
import requests
import csv

url1="http://localhost:8080/jwshoploh=gin/user/login"
userinfo={}
file=open("userinfo","r")
table=csv.reader(file)
for row in table:
    userinfo["uesrname"]=row[0]
    userinfo["password"]=row[1]
    response=requests.get(url1,data=userinfo).text()
    print(response)
#加断言  测试结果写入excel
    res=response.find(row[2])
    file2=open("测试结果.csv","w")
    if res>0:
        print("接口测试通过")
        file2.write[row[0]+","+row[1]+","+row[2]+","+"测试通过"+"/n"]
    else:
        print("接口测试不通过")
        file2.write[row[0] + "," + row[1] + "," + row[2] + "," + "测试不通过"+"/n"]
file2.close()



