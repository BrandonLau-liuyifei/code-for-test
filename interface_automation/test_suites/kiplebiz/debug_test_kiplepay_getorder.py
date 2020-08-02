#coding:utf-8
from interface_automation.common.kiplebiz.operate_excel import *
from interface_automation.common.kiplebiz.request_api import *
from interface_automation.common.kiplebiz.initialization import *
import unittest
import requests
class GetOrderClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        excel = readExcel(
            r"C:\Users\dan_li\PycharmProjects\untitled\interface_automation\data\kiplebiz\auto_testcases.xlsx")
        id = excel.getId
        name = excel.getName
        url = excel.getUrl
        scenario = excel.getScenario
        method = excel.getMethod
        # headers = excel.getHeaders
        params = excel.getParams
        expect = excel.getExpect
        code = excel.getCode
        row = excel.getRows

        cls.url = url
        cls.params = params
        cls.name = name
        cls.method = method
        # cls.headers = headers
        cls.row = row
        cls.scenario = scenario
        cls.code = code
        cls.key = "AccessToken"
        cls.get_token = "get_token"
        cls.expect = expect
        cls.testcase_index = []
        response = GetResponse(cls.get_token, cls.key)
        cls.headers = response.get_response_value()
        for i in range(0, cls.row - 1):
            if cls.name[i] == 'get_order':
                cls.testcase_index.append(i)
        return cls.testcase_index

    def print_start_info(self,index,headers):
        print("=========testAPI:", self.name[index], "======")
        print("=========start to test scenario-->", self.scenario[index], "======")
        print("method is:", self.method[index], '\n',
              "url is: ", self.url[index], '\n',
              "params is :", self.params[index], '\n',
              "headers is:", headers, '\n')

    def print_end_info(self,index):
        print("=========end to test scenario-->",self.scenario[index],"======")

    def test_getorder_1(self):
        '''检查返回值是200'''
        for i in self.testcase_index:
            if self.scenario[i] =='检查返回值是200':
                # print (self.name[i],self.key)
                self.print_start_info(i, self.headers)
                api = testApi(self.method[i], self.url[i], self.params[i], self.headers)
                apiCode = api.getCode()
                self.assertEqual(apiCode,self.code[i])
                print(api.getJson())
                self.print_end_info(i)

    def test_getorder_2(self):
        '''检查orderid不为空'''
        for i in self.testcase_index:
            if self.scenario[i] =='检查orderid不为空':
                self.print_start_info(i, self.headers)
                api = testApi(self.method[i], self.url[i], self.params[i], self.headers)
                api_json = api.getJson()
                self.assertIsNotNone(api_json[0]['OrderId'])
                self.print_end_info(i)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)