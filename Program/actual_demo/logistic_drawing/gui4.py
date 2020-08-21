"""
    #设置文本字体大小
    fontStyle = tkFont.Font(size=20)
    L1 = Label(root, text="信号输入完成",font=fontStyle)
"""
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
import xlrd
import pandas as pd

root=Tk(className="仪表逻辑图")
root_X="800"
root_Y="200"
root.geometry("1000x200")

path1=StringVar()
path2=StringVar()
filelist=[]
input_signal=[]
output_signal=[]
str1=["&&","||"]
X=10
Y=90
N=[1,1,1,1]
d=dict()
def addEntry(Button1,Button2,N):
    x1 = int(Button1.place_info()['x'])
    x2 = int(Button2.place_info()['x'])
    Y = int(Button2.place_info()['y'])
    i = len(N)
    e1 = ttk.Combobox(root, values=str1, width=3)
    e1.place(x=x1, y=Y + 5)
    e2 = Entry(root, width=7)
    e2.place(x=x1 + 60, y=Y + 5)
    x1 += 120
    x2 += 120
    Button1.place(x=x1, y=Y)
    Button2.place(x=x2, y=Y)
    N.append(1)
    N.append(1)
    Y+=5
    d[Y].append(e1)
    d[Y].append(e2)
def getinfo():
    pass
def draw_Frame(output,X,Y):
    L1 = Label(root,text=output, width=10)
    L1.place(x=X, y=Y)
    L2 = Label(root, text="=", width=5)
    L2.place(x=X + 80, y=Y)
    E2 = Entry(root, width=7)
    E2.place(x=X + 120, y=Y)
    E3 = ttk.Combobox(root, values=str1, width=3)
    E3.place(x=X + 180, y=Y)
    E4 = Entry(root, width=7)
    E4.place(x=X + 240, y=Y)
    B4 = Button(root, text="+", command=lambda: addEntry(B4, B5, N))
    B4.place(x=X + 300, y=Y - 5)
    B5 = Button(root, text="完成", command=lambda: getinfo())
    B5.place(x=X + 330, y=Y - 5)
    d[Y]=[L1,L2,E2,E3,E4]


def selectPath(path1):
    path_ = askopenfilenames()
    path1.set(path_)
    filelist.append(path_)
def read_file(filelist,X,Y):
    workxls = xlrd.open_workbook(filelist[0][0])
    worksheet = workxls.sheet_by_name("Sheet1")
    row = worksheet.nrows
    for i in range(row):
        rowdata = worksheet.row_values(i)[0]  # i行的list
        input_signal.append(rowdata)
    workxls = xlrd.open_workbook(filelist[1][0])
    worksheet = workxls.sheet_by_name("Sheet1")
    row = worksheet.nrows
    for i in range(row):
        rowdata = worksheet.row_values(i)[0] # i行的list
        output_signal.append(rowdata)
    #设置文本字体大小
    fontStyle = tkFont.Font(size=20)
    L1 = Label(root, text="信号输入完成",font=fontStyle)
    L1.place(x=10, y=50)
    for i in output_signal:
        draw_Frame(i,X,Y)
        Y+=40
L1 = Label(root, text="输入信号:")
L1.place(x=10, y=20)
E1 = Entry(root, textvariable=path1, width=30)
E1.place(x=80, y=20)
 # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
B1 = Button(root, text="...", command=lambda :selectPath(path1), height=1)
B1.place(x=300, y=15)

L2 = Label(root, text="输出信号:")
L2.place(x=330, y=20)
E2 = Entry(root, textvariable=path2, width=30)
E2.place(x=400, y=20)
 # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
B2 = Button(root, text="...", command=lambda :selectPath(path2), height=1)
B2.place(x=620, y=15)
B3 = Button(root, text="完成信号输入", command=lambda :read_file(filelist,X,Y), height=1)
B3.place(x=650, y=15)

root.mainloop()