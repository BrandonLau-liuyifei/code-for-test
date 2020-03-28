#接口测试用例批量进行
#实现方案 python+requests库+excel操作
"""1.excel测试用例读取
   2.接口请求代码构建
   3.测试结果写入excel
   4.后续一些辅助性工作"""

# 1。excel测试用例读取
import xlrd
#读取测试用例文件
excel_dir =r"/Users/mac/PycharmProjects/songqin_test_course/port_test/物流查询接口用例的副本.xlsx"
# 打开excel
workbook = xlrd.open_workbook(excel_dir)
# 查看所有子表名
print(workbook.sheet_names())  #返回list
#或者如下
worksheet=workbook.sheet_by_name('Sheet1')
# # 读取1行
# rows=worksheet.row_values(1)
# # 读取1列
# clos=worksheet.cell_value(2)
# print(rows)

# 读取指定单元格
celldata=worksheet.cell(1,3).value
print(celldata)
# 或
# print(worksheet.cell(1,6).ctype)  ctype查看单元格数据类型，如返回1，代表字符串

# 2。构建接口对应请求
#请求头有token，获取token
import requests
import json
# 2-1获取token
token_url1='http://ip:port/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'
token_data={"userName":"liumoumou",
            "password":"liumoumoudemima"
            }
headers={"Content-Type":"application/json"}
resp=requests.post(token_url1,data=json.dumps("token_data"),headers="headers")
token=resp.json()['token']
print(token)
# 2-2新增用户
adduser_url1="http://ip:port/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"
#请求参数为字符串，字符串转json格式
adduser_data=json.loads(celldata)
print(type(adduser_data))
adduser_headers={"Content-y=type":"application/json","X-AUTO_TOKEN":token}
adduser_resp=requests.post(adduser_url1,data=json.dumps(adduser_data),headers="adduser_headers")
print(adduser_resp.text)
  #加检查点
res=adduser_resp.json()["message"]
if res=="success":
    print("新增用户测试成功----成功，耗时为",adduser_resp.elapsed.total_seconds())
    excel_res="pass"
else:
    print("新增用户测试成功----失败，")
    excel_res = "fail"

#3.测试结果写入excel
import xlutils
# 首先打开文件
# workbooknew=xlrd.open_workbook(excel_dir)
# 复制
workbookWr= xlutils.copy(workbook)
wrsheet=workbook.get_sheet(0)
wrsheet.write(1,9,excel_res)
workbookWr.save(r"/Users/mac/PycharmProjects/songqin_test_course/port_test/物流查询接口用例的副本testresult.xlsx")













