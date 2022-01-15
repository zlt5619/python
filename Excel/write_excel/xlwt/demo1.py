# 创建只能读取的excel表格

import xlwt
from xlwt import easyxf

path="C:/Users/zlt/Desktop/demo.xlsx"
book = xlwt.Workbook()
# 新建工作簿
table = book.add_sheet('sheet_name',cell_overwrite_ok=True)
 # 如果对同一单元格重复操作会发生overwrite Exception，cell_overwrite_ok为可覆盖
# sheet = book.add_sheet('sheet_name')
read_only = easyxf("")
table.write(0,0,"protected",read_only)
book.save(path)
