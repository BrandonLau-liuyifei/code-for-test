# 加载第三方库urillib、requests
#开发接口测试步骤：1.根据测试用例构建相应点http请求get、post等，发送给服务端
#               2.接收并检查响应信息
import requests
from pprint import pprint
#get请求
res = requests.get("http://ip:port/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
print(res.status_code)
retOBJ = res.json()
pprint(retOBJ,width=30)
list1 = res.json()['retlist']

#加检查点1
if retOBJ['retcode'] == 0:
    print("检查点==>返回结果retcode为0，检查通过")
else:
    print("检查点==>返回结果retcode不为0，检查不通过")

#post请求
res1 = requests.post('http://ip:port/api/mgr/',
                     data={
                         'action':'add_course',
                         'data':'''{
                         'name':'猴哥',
                         'desc':'初中化学课程'，
                         'display_idx':'4'
                         }'''
                      })
retOBJ = res.json()
pprint(retOBJ,width=30)
list2 = res.json()['retlist']

#加检查点2
#取出，多了一门课程对象
newcourse = None
for one in list2:
    if one not in list1:
        newcourse = one
        break
#检查点
assert newcourse!=None
assert newcourse['name']=="猴哥"






