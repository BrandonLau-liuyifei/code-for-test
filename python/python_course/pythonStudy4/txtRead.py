import os   # 导入os 在os中有读取txt文件内容的方法

def get_testdata_to_dict(txtfile_dir):
    # 打开txt文件 ，获取文件对象赋值给变量f
    f = open(txtfile_dir)
    # 安行读取文件内容
    content = f.readlines()
    testdata_dict={}
    for c in content:
        # strip(),去除字符串中的某个子串
        testdata_list = c.strip("\n").split("=")
        testdata_dict[testdata_list[0]] = testdata_list[1]
    f.close()
    return testdata_dict

if __name__=="__main__":
    # # 使用os下getcwd()方法，获取当前脚本所在路径
    # dir = os.getcwd()
    # print(dir)
    # txtfile_dir = dir + "\TestData.txt"
    # print(txtfile_dir)
    # # 打开txt文件 ，获取文件对象赋值给变量f
    # f = open(txtfile_dir)
    # # 安行读取文件内容
    # content = f.readlines()
    # print(content)
    txt_dir = r"D:\JNC\python\pythonstudy\pythonStudy4\TestData.txt"
    testdata = get_testdata_to_dict(txt_dir)
    print(testdata)