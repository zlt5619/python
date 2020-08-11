from tkinter import *
from tkinter.filedialog import askopenfilenames
from pyautocad import Autocad, APoint
import xlrd

acad = Autocad(create_if_not_exists=True)

def draw_switch(position_X,positon_Y,load,switch):
    pp1=APoint(position_X,positon_Y)
    pp2=APoint(position_X,positon_Y+200)
    pp3=APoint(position_X+400,positon_Y+200)
    pp4=APoint(position_X+400,positon_Y)
    acad.model.AddLine(pp1, pp2)
    acad.model.AddLine(pp2, pp3)
    acad.model.AddLine(pp3, pp4)
    acad.model.AddLine(pp4, pp1)
    textString = load
    insertPnt = APoint(position_X+20, positon_Y+60)
    height =80
    acad.model.AddText(textString, insertPnt, height)
    textString = switch
    insertPnt = APoint(position_X+220, positon_Y+60)
    height = 70
    acad.model.AddText(textString, insertPnt, height)

def read_excel_file(filepath):
    workxls = xlrd.open_workbook(filepath)
    worksheet = workxls.sheet_by_name("Sheet1")
    row = worksheet.nrows  # 总行数
    file_related_list=[]
    for i in range(row):
        if i==0:
            pass
        else:
            rowdata = worksheet.row_values(i)  # i行的list
            file_related_list.append(rowdata)
    return file_related_list

def drawcad(mainpowersource,auxlirypowersoruce,filelist):
    global load_list, switch_file
    mainpowersource=mainpowersource.split(",")
    auxlirypowersoruce=auxlirypowersoruce.split(",")
    for f in filelist:
        filepath=f[0]
        if "负荷" in filepath:
            load_list=filepath
        elif "开关" in filepath:
            switch_file=filepath
        else:
            print("出错了")
    load_list=read_excel_file(load_list)
    switch_file=read_excel_file(switch_file)
    for row1 in load_list:
        current = round(row1[1] / row1[2], 2)
        for row2 in switch_file:
            if current < row2[1]:
                row1.append(row2[0])
                break

    p1 = APoint(0, 0)
    p2 = APoint(0, 2200)
    p3 = APoint(800, 2200)
    p4 = APoint(800, 0)
    acad.model.AddLine(p1, p2)
    acad.model.AddLine(p2, p3)
    acad.model.AddLine(p3, p4)
    acad.model.AddLine(p4, p1)
    start_X=[0,400]
    start_Y=1600
    for i in range(len(load_list)):
        a=i%2
        draw_switch(start_X[a],start_Y,load_list[i][0],load_list[i][3])
        if a==1:
            start_Y=start_Y-200
    print("完成绘图")
filelist=[]

def selectPath(path):
    path_ = askopenfilenames()
    path.set(path_)
    filelist.append(path_)

def generateFile():
    mainpowersource=path1.get()
    auxlirypowersoruce=path2.get()
    drawcad(mainpowersource,auxlirypowersoruce,filelist)



root = Tk(className="autocad生成器")
#geometry设置tk初始化大小
root.geometry("350x200")
path1 = StringVar()
path2 = StringVar()
path3 = StringVar()
path4 = StringVar()
L1=Label(root,text = "主电源:")
L1.place(x=10,y=20)
E1=Entry(root, textvariable = path1,width=10)
E1.place(x=80,y=20)
L2=Label(root,text = "辅助电源:")
L2.place(x=150,y=20)
E2=Entry(root, textvariable = path2,width=10)
E2.place(x=220,y=20)
L3=Label(root,text = "开关选择:")
L3.place(x=10,y=65)
E3=Entry(root, textvariable = path3,width=30)
E3.place(x=80,y=65)
B1=Button(root, text = "...", command = lambda :selectPath(path3),height=1)
B1.place(x=300,y=60)
L4=Label(root,text = "文件选择:")
L4.place(x=10,y=110)
E4=Entry(root, textvariable = path4,width=30)
E4.place(x=80,y=110)
B1=Button(root, text = "...", command = lambda :selectPath(path4),height=1)
B1.place(x=300,y=105)
B2=Button(root,text="输出CAD和EXCEL文件",command=generateFile)
B2.place(x=100,y=130)


root.mainloop()