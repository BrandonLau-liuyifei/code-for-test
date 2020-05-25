# 页面请求需要添加整数解决方式
import requests
url = "https://www.ctrip.com"

# r = requests.get(url=url)
# print(r.text)

# 解决方法1
# #verify参数默认为True，False默认忽略证书
# r = requests.get(url=url,verify=False)
# print(r.text)

# 解决方法2
#verify参数默认为True，False默认忽略证书
r = requests.get(url=url,verify="证书路径")
print(r.text)