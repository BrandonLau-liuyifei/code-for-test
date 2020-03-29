# 定义函数，实现往指定路径下txt文件写入内容的功能
def write_txt_by_add(txt_dir, content):
    f = open(txt_dir, "a")  # a 表示追加模块打开
    f.write(content)  # 写入内容
    f.close()

if __name__=="__main__":
    write_txt_by_add(r"D:\JNC\python\pythonstudy\pythonStudy4\testdata.txt", "\nyanzhengma=1234")

     f = open(r"D:\JNC\python\pythonstudy\pythonStudy4\testdata.txt", "a")  # a 表示追加模块打开
     f.write("\nyanzhengma=1234")
     f.close()
