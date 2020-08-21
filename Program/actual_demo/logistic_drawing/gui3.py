from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
import xlrd
import pandas as pd

root=Tk(className="仪表逻辑图")
root_X="800"
root_Y="200"
root.geometry(root_X+"x"+root_Y)
"""
Python中的locals 方法

1 createVar = locals()
2 listTemp = range(1,10)
3 for i,s in enumerate(listTemp):
4     createVar['a'+i] = s
批量生成变量
"""
# for i in range(50):
#     locals()["path"+str(i+1)]=StringVar()
path1=StringVar()
path2=StringVar()
filelist=[]
input_signal=[]
output_signal=[]
X=80
Y=75
N=[1,1,1,1]
str1=["&&","||"]
zhongjianxinhao=[]




for i in range(100):
    zhongjianxinhao.append("中间信号"+str(i))

def selectPath(path1):
    path_ = askopenfilenames()
    path1.set(path_)
    filelist.append(path_)
def read_file(filelist):
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

def addEntry(Button1,Button2,N):
    x1=int(Button1.place_info()['x'])
    x2=int(Button2.place_info()['x'])
    Y=int(Button2.place_info()['y'])
    i=len(N)
    e1 =ttk.Combobox(root,values=str1,width=3)
    e1.place(x=x1, y=Y+5)
    e2 = Entry(root, width=7)
    e2.place(x=x1+60, y=Y+5)
    x1+=120
    x2+=120
    Button1.place(x=x1,y=Y)
    Button2.place(x=x2,y=Y)
    N.append(1)
    N.append(1)
    E.append(e1)
    E.append(e2)


def compare_in_list(print_info, input_signal, output_signal):
    a=1
    # print(print_info)
    # print(output_signal)
    # print(input_signal)
    for i in range(len(print_info)):
        # if i==0:
        #     if print_info[i] not in output_signal:
        #         a=0
        #         print("erroe1")
        # elif i%2==1:
        #     if print_info[i] not in input_signal :
        #         a=0
        #         print("erroe2")
        # else:
        #     pass
        if i==0:
            if print_info[i] not in output_signal:
                a=0
                print("erroe1")
        elif i%2==1:
            if print_info[i] not in input_signal and print_info[i] not in output_signal :
                a=0
                print("erroe2")
    return a

def getinfo():
    print_info=[]
    print_str_1=None
    print_str_2=None
    for e in E:
        if int(e.place_info()['y'])==Y:
            print_info.append(e.get())
    a=compare_in_list(print_info,input_signal,output_signal)
    if a:
        for i in range(len(print_info)):
            if i==0:
                print_str_1=print_info[i]+"="
            elif i==2:
                print_str_2="("+print_info[1]+print_info[2]+print_info[3]+")"
            elif i%2==0:
                print_str_2="("+print_str_2+print_info[i]+print_info[i+1]+")"
            else:
                pass
        print(print_str_1+print_str_2)
        demo_excel=print_str_1+print_str_2
        df = pd.DataFrame([demo_excel], columns=['1'], index=['a'])
        df.to_excel('excel_output.xls')
    else:
        print("error")
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

B3 = Button(root, text="完成信号输入", command=lambda :read_file(filelist), height=1)
B3.place(x=650, y=15)

E3=Entry(root, width=10)
E3.place(x=X, y=Y)
L3=Label(root, text="=",width=5)
L3.place(x=X+80,y=Y)
E4=Entry(root,width=7)
E4.place(x=X+120,y=Y)
E5=ttk.Combobox(root,values=str1,width=3)
E5.place(x=X+180,y=Y)
E6=Entry(root,width=7)
E6.place(x=X+240,y=Y)

B4=Button(root,text="+",command=lambda :addEntry(B4,B5,N))
B4.place(x=X+300,y=Y-5)
B5=Button(root,text="完成",command=lambda :getinfo())
B5.place(x=X+330,y=Y-5)


E=[E1,E2,E3,E4,E5,E6]
L=[L1]


root.mainloop()