#技术试验
#发送请求
import requests

#发送请求，并接受接口返回结果
# V1.0 version 传入接口测试数据为常量
# response=requests.get("http://localhost:8080/SSM/product/4").text
# print(response)

# V2.0 version 传入变量数据
# id=10
# response=requests.get("http://localhost:8080/SSM/product/"+str(id)).text
# print(response)

#V3.0 version 传入多个测试数据
# idlist=[10,15,25]
# # print(idlist[2])
# for i in range(0,3):
#     response=requests.get("http://localhost:8080/SSM/product/"+str(idlist[i])).text
#     print(response)

#V5.0 version 如何测试接口响应结果是否正确
# r=response.find("\"prodId\":4")
# print(r)
# if r>-1:
#     print("查询接口测试通过")
# else:
#     print("查询接口测试失败")
# response.count()


#unittest测试框架的运行机理
#导入框架类库
# import unittest
# #继承unittest框架
# class test_s(unittest.TestCase):
#     #定义测试方法
#     def test_case1(self):
#         response = requests.get("http://localhost:8080/SSM/product/10").text
#         print(response)
#         r = response.find("\"prodId\":10")
#         print(r)
#         if r > -1:
#             print("查询接口测试通过")
#         else:
#             print("查询接口测试失败")
# if __name__ == '__main__':
#     unittest.main()


#V4.0 version 从数据库中获取实时的数据作为测试参数传入
#进行数据库的连接
# import pymysql
# #服务器地址，用户名，密码,数据库名,字符集
# db=pymysql.connect(host="localhost",user="root",password="",
#                   database="bwfshop",charset="utf8")
# #创建数据库游标
# cur=db.cursor()
# #执行SQL命令
# cur.execute("select prodId from product where prodId=10")
# #获取记录集
# record=cur.fetchall()
# # print(record)
# # for id in record:
# # print(id[0])
# response = requests.get("http://localhost:8080/SSM/product/10").json()
# print(response)

#V6.0 version 如何通过脚本进行数据库的验证
#1、如何把返回结果中实际的prodSn取出来
# for sn in response:
#     print("接口实际返回值",sn["prodSn"])
#     r1=sn["prodSn"]
# #2、获取数据库中sn对应的值
# cur.execute("select prodSn from product where prodId=10")
# result=cur.fetchall()
# print("数据库获取的值",result[0][0])
# r2=result[0][0]
# if r1==r2:
#     print("Sn的值相同")
# else:
#     print("Sn测试值不相等")


import MySQLdb
#服务器地址，用户名，密码,数据库名,字符集
db=MySQLdb.connect(host="localhost",user="root",password="",
                  database="bwfshop",charset="utf8")
#创建数据库游标
cur=db.cursor()
#执行SQL命令
cur.execute("select prodId from product ")
#获取记录集
record=cur.fetchall()
# print(record)
for id in record:
    print(id[0])
    response = requests.get("http://localhost:8080/SSM/product/"+str(id[0])).json()
    # response = requests.get("http://localhost:8080/SSM/product/10").json()
    # print(response)
    #获取实际接口响应结果的sn的值
    for sn in response:
        print("接口返回结果中的sn",sn["prodSn"])
        #实际接口返回结果的SN
        r1=sn["prodSn"]
        #获取数据库中对应的SN
        cur.execute("select prodSn from product where prodId="+str(id[0]))
        # cur.execute("select prodSn from product where prodId=10" )
        result=cur.fetchall()
        for sn in result:
            print("数据库中对应的sn",sn[0])
            r2=sn[0]
            if r1==r2:
                print("获取的sn的值相等")
            else:
                print("获取的sn的值不同")

