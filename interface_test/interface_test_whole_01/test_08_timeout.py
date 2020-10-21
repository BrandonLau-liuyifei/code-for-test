import requests
"""
timeout参数
1.接口返回请求时间要求在范围内
2.接口请求时间不固定的时候，在要求内是否成功，要求内成功，不再要求内成功
"""

# 1.淘宝手机号码查询
url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18319011906"
r = requests.get(url = url,timeout=0.01,verify=False)
print(r.text)

"""
1.循环10次，接口请求
2.当时间超过2s，认为是失败，我们需要把结果上报
"""
# 1.防伪系统上传查询
for i in range(10):
    try:
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
        cookies_02 = {
            "PHPSESSID":"   "
        }
        r_02 = requests.post(url=url_02,data=data_02,files=files_02,cookies=cookies_02,timeout=0.01)
        print(r_02.text)
    except:
        print("运行报错")