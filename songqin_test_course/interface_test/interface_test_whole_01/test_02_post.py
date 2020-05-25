import requests
# 2种数据格式

# 1.数据格式form-data ，案例注册
# URL地址：url = "http://106.12.126.197:8000//register"
# 请求post
# 请求参数 username，password
# 2.json格式，登录接口
# 请求post
# 请求参数 username，password

import requests

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