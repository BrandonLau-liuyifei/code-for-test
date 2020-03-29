import xlwt
import os

# 创建一个excel文件对象,声明该文件以utf-8编码
e = xlwt.Workbook(encoding='utf-8')
#创建excel文件的sheet页对象
s = e.add_sheet("test", cell_overwrite_ok=True)  #  test为创建的sheet页的名字，cell_overwrite_ok表示是否可以覆盖单元格内容
# 向sheet页对象s添加数据
s.write(0, 0, "重启是个好发明")  #  向第一行第一列单元格写入数据
# 使用for循环控制单元格坐标的变化，向excel中写入数据
for i in range(1, 10):
    for j in range(1, i+1):
        s.write(i, j, "%d*%d=%d"%(j,i,(j*i)))
excelfilepath = os.getcwd() + r"\testdata2.xls"
e.save(excelfilepath)  # 将内容保存到excelfilepath文件中


