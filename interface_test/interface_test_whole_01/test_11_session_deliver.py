#session 参数
#有很多接口需要一些公共的参数，比如cookies
"""
fw系统中都有公共的参数cookies，通过登录生成
"""
import requests
# 登录接口
url_login="   "
data_login={

}
s=requests.session()
# r_login=requests.post(url=url_login,data=data_login)
r_login=s.post(url=url_login,data=data_login)
print(r_login.content.decode('unicode_escape'))

#添加地址接口
url = "http://106.12.126.197/fanwei/member.php?ctl=uc_consignee&fhash=fywffrgegrthrhw "
data = {
    "consignee":"cxy002",
    "address":"陕西省西安市蓝田县",
    "mobile":"18829788961",
    "ajax":1,
    "id":""
}
# cookies = {
#     "PHPSESSIONID":"huhsghdfgjdksfhgksdhfk"
# }
# r = requests.post(url = url,data = data,cookies = cookies)
r = s.post(url = url,data = data)
print(r.encoding)
print(r.text.encode("utf-8").decode("unicode_escape"))

#文件上传接口
url_02= "http://106.12.126.197/fangwei/file.php"
data_02 = {
    "upload_type":0,
    "localUrl":"E:\\cxy.jpg",
    "m":"file",
    "a":"do_ipload"
}
files_02 = {
    "imageFile":("cxy.jpg",open("E:\\cxy.jpg","rb"),"image/jpeg")
}
# cookies_02 = {
#     "PHPSESSID":"   "
# }
# r_02 = requests.post(url=url_02,data=data_02,files=files_02,cookies=cookies,timeout=5)
r_02 = s.post(url=url_02,data=data_02,files=files_02)
print(r_02.text)

"""
如何将公共参数保存在session中 
操作步骤：
登录方式请求之前，建立session s, s=requests.session
建立的后续请求，直接用s发送请求，把requests替换为s
公共参数已经保存在s中，添加地址接口与上传文件接口中去掉cookies条件

"""
