#测试产品查询接口，按照产品ID来进行
#面向对象编程思想
import requests
#定义测试类
class test_search():
    def test_case1(self):
        response=requests.get("http://localhost:8080/SSM/product/10").text
        print(response)
        r = response.find("\"prodId\":10")
        print(r)
        if r > -1:
            print("查询接口测试通过")
        else:
            print("查询接口测试失败")
    def test_case2(self):
        id=10
        response=requests.get("http://localhost:8080/SSM/product/"+str(id)).text
        print(response)
    def test_case3(self):
        idlist = [10, 15, 25]
        # print(idlist[2])
        for i in range(0, 3):
            response = requests.get("http://localhost:8080/SSM/product/" + str(idlist[i])).text
            print(response)

if __name__ == '__main__':
    #实例化对象
    testobj=test_search()
    #调用测试方法
    testobj.test_case1()
    testobj.test_case2()
    testobj.test_case3()