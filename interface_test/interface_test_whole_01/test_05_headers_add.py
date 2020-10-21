 # requests中的headers请求参数
# "headers发送请求，参数不是每个接口读必须要添加，开发可以定义"
"""
二个例子
一种是不需要headers，前程无忧搜索职位接口
二种是需要headers，12306查询车票接口
"""
"""
第一个是前程无忧，查询职位接口，不需要添加headers
需要测试接口，需要请求url地址，参数，请求方式
"""
"""
步骤：
1.打开前程无忧的网站
2.打开F12-选择network，进行抓包，获取信息
3.搜索职位，点击查询
"""
import requests
# url = 'https://search.51job.com/list/200200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# r_51job = requests.get(url=url)
# print(r_51job.text)
# # 打印返回中文乱码
# print(r_51job.encoding) #打印返回信息为html界面的编码信息，html默认编码方式iso-8859-1
# r_51job.encoding = "GB2312"
# print(r_51job.text)

#发送请求需要cookies参数
url_12306 = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-05-20&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=FZS&purpose_codes=ADULT"
# 需要添加headers信息
cookies  = {
    "cookies":"JSESSIONID=28FA2CE745DA376CE292BB29F833E9A8; BIGipServerotn=1139802634.24610.0000; BIGipServerpool_passport=351076874.50215.0000; RAIL_EXPIRATION=1590147807485; RAIL_DEVICEID=MyO44gUrZnBRPoL2unLbgo0VA-LyUdzuCAA88liqhb1L3dPgn_kL8T8vkoWZ9Ssew017dvLogQFxdqbpaixa5o7fONpvE1aPlqSM9pNAw0QpyJAMQGieQl7zIgIqL1DCNSYG4YAfbav4qm36DuEw-7s7t1xFDqwz; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u798F%u5DDE%2CFZS; _jc_save_toDate=2020-05-18; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2020-05-20"
}
r_12306 = requests.get(url = url_12306,cookies = cookies)
print(r_12306.text)