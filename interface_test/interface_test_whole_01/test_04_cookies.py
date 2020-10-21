#请求参数重添加cookies
"""cookie是一种辨明身份的token，sign签名
需要携带用户的cookies信息，都是为服务根据每个用户生成的每个人的临时身份的
"""
"""
接口信息：
url
请求参数
请求方式
返回结果
接口文档
"""

import requests

url = "http://106.12.126.197/fanwei/member.php?ctl=uc_consignee&fhash=fywffrgegrthrhw "
data = {
    "consignee":"cxy002",
    "address":"陕西省西安市蓝田县",
    "mobile":"18829788961",
    "ajax":1,
    "id":""
}
cookies = {
    "PHPSESSIONID":"huhsghdfgjdksfhgksdhfk"
}
r = requests.post(url = url,data = data,cookies = cookies)
print(r.encoding)
print(r.text.encode("utf-8").decode("unicode_escape"))

#没有加cookies前，结果提示"请先登录"，因此需要鉴权 cookies
#添加cookies后，结果提示"创建成功 "
