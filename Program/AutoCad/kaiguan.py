from pyautocad import Autocad,APoint

acad = Autocad(create_if_not_exists=True)
# acad.prompt() 用来在cad控制台中打印文字
acad.prompt("Hello, Autocad from Python")
# p1=APoint(0,0)
# p2=APoint(100,0)
# p3=APoint(140,30)
# p4=APoint(140,0)
# p5=APoint(240,0)
#
# acad.model.AddLine(p1, p2)
# acad.model.AddLine(p2, p3)
# acad.model.AddLine(p4, p5)

import xlrd
workxls = xlrd.open_workbook("D:\负荷定义.xlsx")
worksheet = workxls.sheet_by_name("Sheet1")
row = worksheet.nrows  # 总行数
file_related_list=[]
for i in range(row):
    if i==0:
        pass
    else:
        rowdata = worksheet.row_values(i)  # i行的list
        file_related_list.append(rowdata)
for i in file_related_list:
    i.append(round(i[2]/i[1], 2))
    if i[3]<1:
        i.append(1)
    elif i[3]<2:
        i.append(2)
    elif i[3]<5:
        i.append(5)
    elif i[3]<10:
        i.append(10)
    else:
        i.append(20)
def kaiguan_drawing(current,position,text):
    position_x=position[0]
    position_y=position[1]
    p1=APoint(position_x+0,position_y+0)
    p2=APoint(position_x+100,position_y+0)
    p3=APoint(position_x+140,position_y+30)
    p4=APoint(position_x+140,position_y+0)
    p5=APoint(position_x+240,position_y+0)
    acad.model.AddLine(p1, p2)
    acad.model.AddLine(p2, p3)
    acad.model.AddLine(p4, p5)
    p6=APoint(position_x+0,position_y+0)
    height = 30
    acad.model.AddText(text, p6, height)
for i in range(len(file_related_list)):
    if i==0:
        kaiguan_drawing(file_related_list[i][3],[0,0],file_related_list[i][4])
    kaiguan_drawing(file_related_list[i][3],[280,120-(i-1)*60],file_related_list[i][4])
