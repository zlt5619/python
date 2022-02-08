# 引入库
from openpyxl import Workbook,load_workbook
from openpyxl.styles import *
import warnings
warnings.filterwarnings('ignore')

path="C:/Users/zlt/Desktop/胡志伟/01 故障记录汇总表-2021年10月（湖北分公司）-V2.1）.xlsx"
# 加载已存在的工作簿
# openpyxl只能处理 .xlsx 合适的表格
wb = load_workbook(path)
#打开大文件时，根据需求使用只读或只写模式减少内存消耗。
# wb = load_workbook(filename='large_file.xlsx', read_only=True)

#获取sheet的名称
sheetnames=wb.sheetnames
# print(wb.sheetnames)
#使用for循环遍历所有的工作表：
# for sheet in wb:
#     print(sheet.title)

# 使用工作表名字获取工作表：
ws= wb["故障填报主表"]
# print(ws)

# 可以单独指定行、列、或者行列的范围
col=ws['C']
for i in col:
    print(i.value)





