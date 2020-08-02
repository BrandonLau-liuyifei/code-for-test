#coding:utf-8
import unittest
import requests


class GetOrderClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url_get_token= "https://extstaging.kiplepay.com:8088/api/account/internal/auth?"
        cls.url_get_order = "https://extstaging.kiplepay.com:8088/api/terminal/orders/pendingorders?"
        cls.terminalId = {'terminalId':'1586923192937'}

    def gettoken(self):
        self.r = requests.get(url=self.url_get_token,params=self.terminalId)
        token = self.r.json()['AccessToken']
        return token

    def test_order_info_1(self):
        '''第一组测试用例：登录后，检查状态码是否是200'''
        self.r = requests.get(url=self.url_get_order,params=self.terminalId, headers={'Authorization':'Bearer'+self.gettoken()})
        self.assertEqual(self.r.status_code,200)
    def test_order_info_2(self):
        '''第二组测试用例：登录后，检查是否获取orderid'''
        self.r = requests.get(url=self.url_get_order,params=self.terminalId, headers={'Authorization':'Bearer'+self.gettoken()})
        self.assertEqual(self.r.json()[0]['OrderId'],4277)

    @classmethod
    def tearDownClass(cls):
        pass


# if __name__ == "__main__":
#     suite = unittest.suite.TestSuite()
#     tests = unittest.TestLoader().loadTestsFromTestCase(GetTokenClass)
#     suite.addTests(tests)
#     unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main(verbosity=2)