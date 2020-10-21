"""
token鉴权方式，令牌
业务规则：登录以后，返回一个token参数，拿token进行后面的操作请求
"""
import requests
# 登录接口
url = "http://106.12.126.197:8000/login"
#数据格式为json格式，字典形式
json = {
    "username":"cxy201",
    "password":"cxy123456"
}
#发送请求格式，使用json格式
r_reg= requests.post(url = url,json = json)
print(r_reg.text)
print(r_reg.status_code)

#充值接口
"""
参数：金额、流水号、token
"""
url_01="http://106.12.126.197:8000/recharge"
data={
    "momney":"123456",
    "serial":"112232424",
    "token":"hvfiagfkasbkjsdfahsfvjhasbdfbdsjb"
}
r_recharge=requests.post(url=url_01,data=data)
print(r_recharge.text)

"""
总结：
请求登录接口后，生成一个token返回值，用于后续请求中的鉴权问题
"""