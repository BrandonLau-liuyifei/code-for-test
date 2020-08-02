import requests

#抓取用户参数信息
from interface_test.interface_test_whole_02.common.get_db import get_sql

url = 'http://172.12.126.197/fanwei/m.php'
user_id=get_sql("select id from user where user='hahahaha'")[0][0]
data={
    "user":"hahahaha",
    "id":"dfjhgjndfjdfl"
}
cookies={
    "PHPSESSION":"sdfsdfsdfsdf"
}
r=requests.post(url=url,data=data,cookies=cookies)
print(r.text)
