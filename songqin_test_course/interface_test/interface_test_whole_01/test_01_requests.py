#安装requests包
# pip install requests
import requests
r = requests.get(url = "http://www.baidu.com")
print(r.text)
print(r.encoding)
print(r.url)
print(r.cookies)
print(r.headers)
print(r.content)
#requests 原理
"""
前端发送请求参数--
    --requests请求
      --发送后端
        --返回结果
步骤：
    1.参数输入
    2.发送请求
    3.检查返回结果
"""