import requests
#淘宝查询手机和归属地接口
"""
接口的url地址 --url
接口的请求参数 --tel
接口的请求方式 --get
"""

#定义一个变量
# url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.html"
#get 请求的两种方式
#方式1：请求方式参数保存在url里面
url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.html?tel=13922358271"
r = requests.get(url = url)
print(r.text)
print(r.url)
print(r.status_code)
print(r.cookies)
print(r.content)
# 方式2：请求方式参数保存在params里面，字典方式保存
