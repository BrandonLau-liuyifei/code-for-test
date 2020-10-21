import requests,re,json
# 动态关联2-response body中的数据关联
"""
接口返回数据格式：
1.text/html格式的数据提取
前程无忧-查询接口
查询对应公司的url地址，需要查询返回地址
下一个查询接口的请求参数url地址
"""
# url_51='https://search.51job.com/list/200200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare'
# r_51 = requests.get(url=url_51)
# r_51.encoding="gb2312"
# print(r_51.text)
# url_yun=re.findall('title="中国移动通信有限公司研究院" href="(.+?)">中国移动通信有限公司研究院')
# # 如何提取text/html中的信息，用re模块，正则表达式
# # <span class="t2"><a target="_blank" </a></span>title="中国移动通信有限公司研究院" href="https://jobs.51job.com/all/co2752144.html">中国移动通信有限公司研究院r
# r_51_yun = requests.get(url=url_yun[0]) #获取匹配第一个数值
# r_51_yun.encoding="gb2312" #设置编码
# print(r_51_yun.text)  #打印公司信息

"""
2.json格式的数据提取
"""

url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-07-31&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=FZS&purpose_codes=ADULT'
headers={
    'Cookie':'JSESSIONID=C7D1C7170C0C87972C92F7EE2D4F9964;_uab_collina=159603177499194833607613; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u798F%u5DDE%2CFZS; _jc_save_wfdc_flag=dc; BIGipServerotn=49283594.24610.0000; BIGipServerpool_passport=334299658.50215.0000; route=495c805987d0f5c8c84b14f60212447d; RAIL_EXPIRATION=1596347251534; RAIL_DEVICEID=pk5P1EDoDTZmn31CpG7tjB5238GEummodRp1exsVOJiawLtq665qvLOiK3Lijhgb8ZkbKWuTsHH-XJTlrmIBs7kwxJaz2RK9EODuTu3uWpOMqcpHkOFnfXqWNOIhdoP__e09NFEWpN3ERQ22mvXKy3PZeSNVOBaK; _jc_save_toDate=2020-07-29; _jc_save_fromDate=2020-07-31'
}
r_12306=requests.get(url=url,headers=headers)
print(r_12306.text)
# 返回为json格式，r.json()读取返回信息
print(r_12306.json())
#提取返回码200
print(r_12306.json()["httpstatus"])