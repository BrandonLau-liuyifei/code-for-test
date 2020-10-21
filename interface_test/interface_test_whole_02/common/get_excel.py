import xlrd
# 验证登录  正确账户密码、错误的账号密码
# 读取excel数据
# 打开文件，文件的地址，使用相对路径
excel = xlrd.open_workbook("../testdata/excel.xlsx")
# 按照索引读取撕一页信息
table = excel.sheets()[0]
print(table.nrows,table.ncols)  #获取总行数,总列数
print(table.row_values(0)) #获取第一行数据
print(table.col_values(0)) #获取第一列数据
# print(table.cell_value(0,1)) #获取第一行第一列的数据

for i in range(1,table.nrows):
    print(table.cell_value(i,1),table.cell_value(i,2))

def get_excel_row(row):
    excel = xlrd.open_workbook("../testdata/excel.xlsx")
    table=excel.sheets()[0]
    return table.cell_value(row,1),table.cell_value(row,2)
