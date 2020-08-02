#coding:utf-8
from interface_automation.common.kiplebiz.operate_excel import *
from interface_automation.common.kiplebiz.request_api import *
import unittest

class GetMerchantClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        excel = readExcel(
            r"C:\Users\dan_li\PycharmProjects\untitled\interface_automation\data\kiplebiz\auto_testcases.xlsx")
        id = excel.getId
        name = excel.getName
        url = excel.getUrl
        scenario = excel.getScenario
        method = excel.getMethod
        headers = excel.getHeaders
        params = excel.getParams
        expect = excel.getCode
        code = excel.getCode
        row = excel.getRows
        cls.url = url
        cls.params = params
        cls.name = name
        cls.method = method
        cls.headers = headers
        cls.row = row
        cls.scenario = scenario
        cls.code = code

        cls.testcase_index = []
        for i in range(0, cls.row - 1):
            if cls.name[i] == 'get_token':
                cls.testcase_index.append(i)
        return cls.testcase_index

    def print_start_info(self,index):
        print("=========testAPI:", self.name[index], "======")
        print("=========start to test scenario-->", self.scenario[index], "======")
        print("method is:", self.method[index], '\n',
              "url is: ", self.url[index], '\n',
              "params is :", self.params[index], '\n',
              "headers is:", self.headers[index], '\n')

    def print_end_info(self,index):
        print("=========end to test scenario-->",self.scenario[index],"======")

    def test_gettoken_1(self):
        '''登录后，检查返回值是200'''
        for i in self.testcase_index:
            if self.scenario[i] =='检查返回值是200':
                self.print_start_info(i)
                api = testApi(self.method[i], self.url[i], self.params[i], self.headers[i])
                apiCode = api.getCode()
                self.assertEqual(apiCode,self.code[i])
                self.print_end_info(i)

    def test_gettoken_2(self):
        '''登录后，检查返回状态不为空'''
        for i in self.testcase_index:
            if self.scenario[i] =='检查返回状态不为空':
                self.print_start_info(i)
                api = testApi(self.method[i], self.url[i], self.params[i], self.headers[i])
                api_json = api.getJson()
                self.assertIsNotNone(api_json)
                self.print_end_info(i)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)