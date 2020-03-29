import os
dir=os.getcwd()
print(dir)
txt1_dir=dir+"/txt1.txt"
print(txt1_dir)
# f=open(txt1_dir)
# content=f.readlines()
# print(content)

def transfer_txt_to_dict(txt1_dir):
    f = open(txt1_dir)
    content=f.readlines()
    txt_dict={}
    for c in content:
        txt_list=c.strip("\n").split("=")
        txt_dict[txt_list[0]]=txt_list[1]
    f.closed
    return(txt_dict)

if __name__=="__main__":
    txt1_dir="/Users/mac/Desktop/ 软件测试学习/9.python/4.python course04/pythonStudy4/txt1.txt"
    txtdata=transfer_txt_to_dict(txt1_dir)
    print(txtdata)
