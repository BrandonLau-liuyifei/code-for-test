##封装本次所有接口，需要调用的入参信息。
#coding:utf-8
from interface_automation.common.kiplebiz.request_api import *
from interface_automation.common.kiplebiz.operate_excel import *

class GetResponse(object):
    def __init__(self,interface_name,key):
        self.interface_name = interface_name
        self.key = key

    def get_response_value(self):
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
        testcase_index = []
        for i in range(0, row - 1):
            if name[i] == self.interface_name:
                testcase_index.append(i)
        j = testcase_index[0]
        api = testApi(method[j], url[j], params[j], headers[j])
        if self.key == 'AccessToken':
            # token = "{Bearer "+api.getJson()[self.key]+"}"
            # token = "{'Authorization': 'Bearer '" + api.getJson()[self.key]+"}"
            token = api.getJson()['AccessToken']
            token_dict = {'Authorization':'Bearer ' + token}
            # new_token = {'Authorization': 'Bearer ' + token}
            return str(token_dict)

if __name__ == '__main__':
    a = GetResponse('get_token','AccessToken')
    print(a.get_response_value())




