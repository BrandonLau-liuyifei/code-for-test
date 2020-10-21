#面向对象读取CSV文件中相关的接口测试数据数据，进行接口测试
import requests
import csv

#定义测试类
class check_test():
    def __init__(self):
        self.url="ip address"
    def checklist(self):
        #从CSV中获取测试数据
        checkinfo={}
        file=open("文件名.csv","r")
        table=csv.reader(file)
        for row in table:
            checkinfo["str"]=row[0]
            checkinfo["type"]=row[1]
            s=requests.session()
            response=requests.post(self.url,data=checkinfo).json()
            print(response)
            #加断言、加测试结果写入excel
            r=response.find(row[2])
            file2=open("文件名测试结果.csv","w")
            if r>0:
                print("接口测试通过")
                file2.write[row[0]+","+row[1]+","+row[2]+","+"测试通过"+"/n"]
            else:
                print("接口测试不通过")
                file2.write[row[0] + "," + row[1] + "," + row[2] + "," + "测试不通过" + "/n"]
        file2.close()
if __name__ == '__main__':
    checkobj=check_test()
    checkobj.checklist()
