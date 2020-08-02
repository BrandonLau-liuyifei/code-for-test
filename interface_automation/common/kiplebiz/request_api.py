import requests


class testApi(object):
    def __init__(self,method,url,params,headers):
        self.method = method
        self.url = url
        self.params = params
        self.headers = headers

    @property
    def testingApi(self):
        # 根据不同的访问方式来访问接口
        try:
            if self.method == "post":
                print("开始执行post接口")
                if self.headers == "":
                    r = requests.post(self.url, data=eval(self.params))
                else:
                    r = requests.post(self.url, data=eval(self.params), headers=eval(self.headers))
                print("结束执行post接口")
            elif self.method == "get":
                print("开始执行get接口")
                if self.headers == "":
                    # print("headers is none")
                    r = requests.get(self.url, params=eval(self.params))
                else:
                    # print("headers is not none")
                    r = requests.get(self.url, params=eval(self.params),headers=eval(self.headers))
                print("结束执行get接口")
            return r
        except:
            return None
    def getCode(self):
        #获取访问接口的状态码
        code = self.testingApi.status_code
        return code

    def getJson(self):
        #获取返回信息的json数据
        json_data = self.testingApi.json()
        return json_data