import pandas

path="C:/Users/zlt/Desktop/刘梦/曲线图制作/附件1：大幕山风电场24号机组发电机温度数据.xls"
#获取全部的sheet
sheet_names=pandas.read_excel(path,sheet_name=None)
# print(sheet_names.keys())

#获取对应的sheet
target_sheet=pandas.read_excel(path,sheet_name="Sheet")
# print(target_sheet)

#获取开头行
header=target_sheet.head()
print(header)


