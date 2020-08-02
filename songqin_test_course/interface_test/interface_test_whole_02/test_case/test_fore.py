import requests

from interface_test.interface_test_whole_02.common.get_excel import get_excel_row
from interface_test.interface_test_whole_02.config.conf import server_ip


""""
# 注册接口
url = "http://106.12.126.197:8000//register"
#表单数据格式，参数data，数据是字典格式
data = {
    "username":"cxy201",
    "password":"cxy123456"
}
#发送请求格式，表单形式的数据，使用data
r_reg= requests.post(url = url,data = data)
print(r_reg.text)
print(r_reg.status_code)

#登录接口
url = "http://106.12.126.197:8000//login"
#数据格式为json格式，字典形式
json = {
    "username":"cxy201",
    "password":"cxy123456"
}
#发送请求格式，使用json格式
r_reg= requests.post(url = url,json = json)
print(r_reg.text)
print(r_reg.status_code)
"""
# 注册接口
url = server_ip()+":8000//register"#带括号表示引入函数而非方法
#表单数据格式，参数data，数据是字典格式
# username,password = get_excel_row(1)
# data = {
#     "username":username,
#     "password":password
# }
# 字典格式{
#     "username":"cxy201",
#     "password":"cxy123456"
# }
usermassage = get_excel_row(4)[1]
json_tarns = eval(usermassage)
data = json_tarns
#发送请求格式，表单形式的数据，使用data
r_reg= requests.post(url = url,data = data)
print(r_reg.text)
print(r_reg.status_code)

#登录接口
url = server_ip()+":8000//login"
#数据格式为json格式，字典形式
json = {
    "username":"cxy201",
    "password":"cxy123456"
}
#发送请求格式，使用json格式
r_reg= requests.post(url = url,json = json)
print(r_reg.text)
print(r_reg.status_code)

"""
切换环境时只需切换server_ip函数的返回值
"""