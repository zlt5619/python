import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple




#显示日期时间
cellValue1 = 44435.4875
# cellValue2=xldate_as_tuple(cellValue1,0)
# cellValue3=datetime(*cellValue2).strftime('%Y/%m/%d %H:%M:%S')
# print("第2行第4列的内容为：",cellValue3)

def time_process(time):
    cell_value=time
    cell_value2=xldate_as_tuple(cell_value,0)
    cell_value3=datetime(*cell_value2).strftime('%Y/%m/%d %H:%M:%S')
    return cell_value3

a=time_process(cellValue1)
print(a)