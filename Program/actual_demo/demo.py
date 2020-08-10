from tkinter import *
from tkinter.filedialog import askopenfilenames
from pyautocad import Autocad, APoint
import pandas as pd

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
    load_list=pd.read_excel(load_list)
    switch_file=pd.read_excel(switch_file)
    acad = Autocad(create_if_not_exists=True)


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
B1=Button(root, text = "...", command = selectPath(path3),height=1)
B1.place(x=300,y=60)
L4=Label(root,text = "文件选择:")
L4.place(x=10,y=110)
E4=Entry(root, textvariable = path4,width=30)
E4.place(x=80,y=110)
B1=Button(root, text = "...", command = selectPath(path4),height=1)
B1.place(x=300,y=105)
B2=Button(root,text="输出CAD和EXCEL文件",command=generateFile)
B2.place(x=100,y=130)


root.mainloop()