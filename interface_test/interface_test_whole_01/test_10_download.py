"""
参数stream，用于文件下载参数
举例：禅道下载用例的接口
"""
import requests
url=''
data={
    "num":10,
    'encode':'utf-8'
}
cookies={
    'cookies':''
}
r=requests.post(url=url,data=data,cookies=cookies,stream=False)
"""
stream--False时，一般下载大文件，文件保存在内存里
stream--True时，一般限制文件大小
"""
print(r.status_code)
print(r.content.decode('utf-8'))
"""
逻辑，需要把返回的请求信息，返回的字符串，把这些信息导入到文件中
"""
#写入文件
with open(r'E:\\cxy001.csv','wb') as f:  #打开文件进行写入操作，with的目的是去过文件不存在，也不会报错
    # 判断返回成功，把返回的信息写入到cxy001.csv中
    if r.status_code==200:  #状态码为200时，写入文件
        for chunk in r.iter_content(chunk_size=1):#iter_content 迭代器，循环去读取信息，chunk_size=1 设置文件大小
            f.write(chunk)

"""
思路总结：
1.发送接口请:
2.把返回值写入文件中，保存
3.stream--False针对大文件，内存不够时，把参数修改为True，默认为False
下载的文件校验：
1.期望值
2.读取文件里面的值，去对比，需要用python打开文件内容
"""
