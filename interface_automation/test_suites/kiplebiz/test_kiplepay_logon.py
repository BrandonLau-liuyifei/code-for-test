#coding:utf-8
import unittest
import requests


class GetMerchantClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url_get_token= "https://extstaging.kiplepay.com:8088/api/account/internal/auth?"
        cls.url_get_merchant = "https://extstaging.kiplepay.com:8088/api/stores/terminal/profile/me?"
        cls.terminalId = {'terminalId':'1586923192937'}

    def gettoken(self):
        self.r = requests.get(url=self.url_get_token,params=self.terminalId)
        token = self.r.json()['AccessToken']
        return token

    def test_merchant_info_1(self):
        '''第一组测试用例：登录后，获取token'''
        self.r = requests.get(url=self.url_get_merchant,params=self.terminalId, headers={'Authorization':'Bearer'+self.gettoken()})
        self.assertIsNotNone(self.r.text,'AccessToken')
    def test_merchant_info_2(self):
        '''第二组测试用例：判断返回状态值是200'''
        self.r = requests.get(url=self.url_get_merchant,params=self.terminalId, headers={'Authorization':'Bearer'+self.gettoken()})
        self.assertEqual(self.r.status_code,200)
    def test_merchant_info_3(self):
        '''第三组测试用例：判断返回内容包含expire'''
        self.r = requests.get(url=self.url_get_merchant,params=self.terminalId, headers={'Authorization':'Bearer'+self.gettoken()})
        self.assertEqual(self.r.json()['MerchantId'],249)
    @classmethod
    def tearDownClass(cls):
        pass


# if __name__ == "__main__":
#     suite = unittest.suite.TestSuite()
#     tests = unittest.TestLoader().loadTestsFromTestCase(GetTokenClass)
#     suite.addTests(tests)
#     unittest.TextTestRunner().run(suite)


# if __name__ == '__main__':
#     unittest.main(verbosity=2)