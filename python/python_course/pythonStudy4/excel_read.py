import os
import xlrd
# 获取当前.py文件所在路径
filepath = os.getcwd()
print(filepath)
excelfilepath = filepath + r"\testdata.xlsx"  # 组织excel文件完整路径为一个字符串
print(excelfilepath)
e = xlrd.open_workbook(excelfilepath)  # 打开excel文件，得到excel文件的对象
sheet0 = e.sheet_by_index(0) # 通过sheet页的索引获取sheet页的对象，sheet索引从左往右从0开始依次递增
nrows_number = sheet0.nrows # 获取数据的行数
print(nrows_number)
ncols_number = sheet0.ncols  # 获取数据的列数
print(ncols_number)
# 使用for循环读取每一行的内容
for i in range(nrows_number):
    values = sheet0.row_values(i)  #读取第i行的数据，i从0开始
    print(values)
print("***************************************************")
# 使用for循环读取每一列的内容
for i in range(ncols_number):
    values = sheet0.col_values(i)  #读取的是第i列的数据，i从0开始
    print(values)
print("***************************************************")
# 按照单元格坐标读取
# 读取第一行第一列交叉单元格内容
values = sheet0.cell_value(0, 0)
print(values)
# 读取第三行第二列交叉单元格内容
values = sheet0.cell_value(2, 1)
print(values)