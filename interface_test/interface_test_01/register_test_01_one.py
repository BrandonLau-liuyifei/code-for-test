#面向对象的思想设计正常注册接口测试
import requests

#定义测试类
class register_test():
    #定义属性，一般是定义在类的初始化防范中
    def __init__(self):
        self.url="ip address"
        self.userinfo={}
        self.userinfo={"username":"小明",
                       "password":"小明的密码",
                       "email":"xxx@outlook.com",
                       "phone":3838383,
                       "question":"小明妈妈的生日",
                       "answer":"1991.11.11"
                       }
    #定义测试方法
    def register_test_01(self):
        #发送接口请求
        s=requests.session()
        response=s.post(self.url,data=self.userinfo).json()
        print(response)

if __name__ == '__main__':
    registerobj=register_test()
    registerobj.register_test_01()

