import xlrd
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
from xlrd import xldate_as_tuple
import xlwt
import matplotlib
import matplotlib.pyplot as plt

#横坐标显示中文
font = {'family': 'Microsoft YaHei', 'weight': 'bold', 'size': '14'}
matplotlib.rc("font", family="Microsoft YaHei", weight="bold", size="14")

#定义时间处理函数，读取excel表格的时间格式数据
#输入一个excel时间格式数据，返回XXXX/XX/XX XX：XX：XX
def time_process(time):
    cell_value=time
    cell_value2=xldate_as_tuple(cell_value,0)
    cell_value3=datetime(*cell_value2).strftime('%Y/%m/%d %H:%M:%S')
    return cell_value3

#通过对话框，获取相关的文件路径
root=tk.Tk()
root.withdraw()
Filepath=filedialog.askopenfile()

#获取文件路径
#print(Filepath.name)

#导入文件，开始读取excel文件
excel_path=Filepath.name
excel=xlrd.open_workbook(excel_path,encoding_override="utf-8")

all_sheets=excel.sheets()
#print(all_sheets)

#找到对应的sheet
for each_sheet in all_sheets:
    #print(each_sheet.name)
    if each_sheet.name=="9月份故障汇总表":
        chosen_sheet=each_sheet

#打印相应sheet的行数
#print(chosen_sheet.nrows)

#读取开头行
First_row_value=chosen_sheet.row_values(0)
print(First_row_value)

#获取  信息类型  所在的列数
for i in range(len(First_row_value)):
    if First_row_value[i]=="信息类型":
        Xinxileixing_col_num=i
# print(Xinxileixing_col_num)

#获取   风电场  所在列
for i in range(len(First_row_value)):
    if First_row_value[i]=="风电场":
        Fengdianchang_col_num=i
# print(Fengdianchang_col_num)

#获取 机组总数 所在列
for i in range(len(First_row_value)):
    if First_row_value[i]=="机组总数":
        Jizuzongshu_col_num=i
# print(Jizuzongshu_col_num)


#获取所有行数
TotalNumberOfRows =chosen_sheet.nrows
# print(TotalNumberOfRows)

#读取第一行数据
# data_first_row_value=chosen_sheet.row_values(1)
# print(data_first_row_value)

#读取第一行第八列数据
# data_first_row_value=chosen_sheet.row_values(1)
# print(data_first_row_value[Xinxileixing_col_num])

#定义新的列表，列表元素，信息类型为故障停机的行
#确定风电场列表
Chosen_rows=[]
Fengdianchang_list=[]
for i in range(1,TotalNumberOfRows):
    if chosen_sheet.row_values(i)[Xinxileixing_col_num]=="故障停机":
        Chosen_rows.append(chosen_sheet.row_values(i))
    if chosen_sheet.row_values(i)[Fengdianchang_col_num] not in Fengdianchang_list:
        Fengdianchang_list.append(chosen_sheet.row_values(i)[Fengdianchang_col_num])
#确认选定故障停机的数量
# print(len(Chosen_rows))
#确定风电场列表
# print(Fengdianchang_list)

#定义故障次数，词典{xx风电场：xx次}，确定风电场风机数量，定义风机数，词典{xx风电场：xx台风机}
Fault_num=dict()
for i in Fengdianchang_list:
    Fault_num[i]=0
# print(Fault_num)
Fengji_num=dict()
for i in Fengdianchang_list:
    Fengji_num[i]=0

#统计故障次数,先生成总的故障次数列表，再依次统计
Fault_list=[]
for each_row in Chosen_rows:
    Fault_list.append(each_row[Fengdianchang_col_num])
for k in Fault_num.keys():
    Fault_num[k]=Fault_list.count(k)
print(Fault_num)

#根据风电场，确定各风电场风机数
for i in range(1,TotalNumberOfRows):
    for k in Fengji_num.keys():
        if chosen_sheet.row_values(i)[Fengdianchang_col_num]==k:
            Fengji_num[k]=chosen_sheet.row_values(i)[Jizuzongshu_col_num]

# print(Fengji_num)

MTBF=dict()

for k in Fengji_num.keys():
    if Fault_num[k]==0:
        MTBF[k]=30*24*Fengji_num[k]
    else:
        MTBF[k]=30*24*Fengji_num[k]/Fault_num[k]

# print(MTBF)

workbook=xlwt.Workbook()
worksheet=workbook.add_sheet('demo')

n1=[]
n2=[]
# for k,v in MTBF.items():
#     if type(v)==str:
#         pass
#     else:
#         n1.append(k)
#         n2.append(v)
#
#
# plt.scatter(n1,n2)
# plt.xticks(rotation=300)
# plt.xlabel("风电场",rotation="horizontal")
# plt.show()



MTBF=list(MTBF)
worksheet.write(0,0,MTBF[0])
worksheet.write(0,1,MTBF[1])

workbook.save('demo.xls')







