# auth鉴权问题，发生接口请求时，添加auth鉴权参数
import requests
url='http://106.12.126.197:3000'
r=requests.get(url=url,auth=('account','password'))
print(r.text)