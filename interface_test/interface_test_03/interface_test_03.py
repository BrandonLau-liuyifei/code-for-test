import unittest
import requests,json

class api_test(unittest.TestCase):

    def test_api_01(self):
        #手机归属地查询  基于get请求
        url = "http://apis.juhe.cn/mobile/get"
        param = {"phone":"19186956812","key":"ffe950dd3e85ee36de34b33575d1e177"}
        res_01 = requests.get(url,param)
        print(res_01.text)
        dict_01 = json.loads(res_01.text)
        self.assertEqual(dict_01["reason"],"Return Successd!")
    def test_api_02(self):
        # 天气预报查询，基于post请求
        url = "http://apis.juhe.cn/simpleWeather/query"
        data = {"city":"长沙", "key": "371e78e1c2d2eeabb361294723857e8d"}
        res_02 = requests.post(url,data)
        print(res_02.text)
        dict_02 = json.loads(res_02.text)
        self.assertIn("查询成功",dict_02["reason"])

if __name__ == '__main__':
    unittest.main()