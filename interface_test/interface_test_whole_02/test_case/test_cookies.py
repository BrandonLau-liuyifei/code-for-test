import requests

# 动态关联关联-1 返回结果中cookies关联
# 登录接口
url_login="   "
data_login={

}
s=requests.session()
# r_login=requests.post(url=url_login,data=data_login)
r_login=s.post(url=url_login,data=data_login)
print(r_login.content.decode('unicode_escape'))
print(r_login.cookies)


#添加地址接口
url = "http://106.12.126.197/fanwei/member.php?ctl=uc_consignee&fhash=fywffrgegrthrhw "
data = {
    "consignee":"cxy002",
    "address":"陕西省西安市蓝田县",
    "mobile":"18829788961",
    "ajax":1,
    "id":""
}
r = s.post(url = url,data = data,cookies=r_login.cookies)
print(r.encoding)
print(r.text.encode("utf-8").decode("unicode_escape"))



