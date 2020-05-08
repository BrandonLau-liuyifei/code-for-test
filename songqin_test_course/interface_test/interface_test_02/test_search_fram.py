#导入框架类库
import unittest
import requests
import MySQLdb
#继承unittest框架
class test_s(unittest.TestCase):
    def setUp(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="",
                             database="bwfshop", charset="utf8")
        # 创建数据库游标
        self.cur = self.db.cursor()
    #定义测试方法
    def test_case1(self):
        response = requests.get("http://localhost:8080/SSM/product/10").text
        print(response)
        r = response.find("\"prodId\":10")
        print(r)
        self.assertEquals()
        if r > -1:
            print("查询接口测试通过")
        else:
            print("查询接口测试失败")
    def test_case2(self):
        id = 10
        response = requests.get("http://localhost:8080/SSM/product/" + str(id)).text
        print(response)
    def tearDown(self):
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    unittest.main()