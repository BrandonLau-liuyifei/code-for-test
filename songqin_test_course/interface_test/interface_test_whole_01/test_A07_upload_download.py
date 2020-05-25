#文件上传
# 携程中上传图片接口

import requests
url = "https://sinfo.ctrip.com/MyInfo/Ajax/UploadPhoto.ashx"
cookies = {
    "cookies":"   "
}
# 文件参数名 uploadFiles_852
# 文件名 cxy123.jpg
# 文件目录 "E:\\cxy123.jpg","rb"
# 文件格式 image/jpeg
files = {
    "uploadFile_852":("cxy123.jpg",open("E:\\cxy123.jpg","rb"),"image/jpeg")
}
r = requests.post(url=url,files=files,verify=False,cookies=cookies)
print(r.text)

# 蝉道-测试用例上传-csv文件
"""
url：
请求参数：
请求方式：
文件：
返回结果：
"""
url_01 = "http://106.12.126.197/zentaopms/www/index.php"
data = {
    "m":"testcase",
    "f":"import",
    "productID":5,
    "branch":0
}
files = {
    "file":("template.csv",open("E:\\template.csv","rb"),"application/vnd.ms-excel")
}
cookies = {
    "cookies":"   "
}
r_01 = requests.post(url=url,data=data,files=files,cookies=cookies)
print(r_01.text)

#fangwei系统
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
r_02 = requests.post(url=url_02,data=data_02,files=files_02,cookies=cookies)
print(r_02.text)
