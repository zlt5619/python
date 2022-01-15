import xlrd

path="C:/Users/zlt/Desktop/刘梦/曲线图制作/附件1：大幕山风电场24号机组发电机温度数据.xls"

#读取excel表格
work_book = xlrd.open_workbook(path)

#获取excel中sheet的数量
# work_book.nsheets
print(work_book.nsheets)

#获取excel中sheet的名称列表
print(work_book.sheet_names())

# 获取excel中sheet的所有列表
print(work_book.sheets())

#获取excel中指定的sheet
#通过索引获取
print("index")
print(work_book.sheet_by_index(0))
#通过sheet的名称去获得sheet
print("Name")
print(work_book.sheet_by_name("Sheet"))

#获得sheet
sheet=work_book.sheet_by_name("Sheet")
#获得sheet的所有行数
print("总行数")
print(sheet.nrows)
#获得总列数
print("总列数")
print(sheet.ncols)

'''
单元格类型索引：
XL_CELL_EMPTY: 'empty',
XL_CELL_TEXT: 'text',
XL_CELL_NUMBER: 'number',
XL_CELL_DATE: 'xldate',
XL_CELL_BOOLEAN: 'bool',
XL_CELL_ERROR: 'error',
XL_CELL_BLANK: 'blank',
'''
print("-----------------------")
print("单元格相关数据")
# 获取sheet表单元格对象，单元格数据类型：单元格值
cell_0 = sheet.cell(0,0)
print(cell_0)
# 获取sheet表单元格值
cell_0_value = sheet.cell_value(0,0)
print(cell_0_value)
# 获取单元格类型
cell_0_type = sheet.cell_type(0,0)
print(cell_0_type)

print("-----------------------")
print("行相关数据")
#获取某一行所有数据类型及值
# [text:'采样时间', text:'334024_发电机前轴承温度', text:'334024_发电机后轴承温度', text:'334024_发电机滑环室温度', text:'334024_有功功率']
row_0=sheet.row(0)
print(row_0)
#获取某一行的值
row_value=sheet.row_values(0)
print(row_value)
#获取某一行的长度
row_length=sheet.row_len(0)
print(row_length)
## 获取某一行对象数据类型、值，可指定开始结束列
row_0_slice = sheet.row_slice(0,1,3)
"def row_slice(self, rowx, start_colx=0, end_colx=None):"
print(row_0_slice)
# 获取sheet表对象某一行数据类型,返回一个数组对象
row_0_type = sheet.row_types(0)
"def row_types(self, rowx, start_colx=0, end_colx=None):"
print(row_0_type)
# 获得sheet对象所有行对象生成器
rows = sheet.get_rows()
print(rows)
#可以循环rows生成器

print("-----------------------")
print("列相关数据")
# 获取sheet表有效列数
col_sum = sheet.ncols
print(col_sum)
# 获取某一列的全部值
col_0_value = sheet.col_values(0)
"def col_values(self, colx, start_rowx=0, end_rowx=None):"
# print(col_0_value)
# 获取列对象的切片
col_0 = sheet.col_slice(1,0,5)
"def col_slice(self, colx, start_rowx=0, end_rowx=None):"
print(col_0)
#获取列对象数据类型和值
col=sheet.col(0)
# print(col)

# 处理时间格式

date01=xlrd.xldate.xldate_as_datetime(sheet.cell_value(1,0),0)
date02=xlrd.xldate.xldate_as_datetime(sheet.cell_value(10,0),0)
date03=xlrd.xldate.xldate_as_datetime(sheet.cell_value(8877,0),0)
print(date01)
print(date02)
print(date03)
print((date01-date02).seconds)
print((date01-date03).days)





