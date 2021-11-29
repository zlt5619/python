from tkinter import *
from tkinter.filedialog import askopenfilenames

filelist=[]

def selectPath():
    path_ = askopenfilenames()
    path.set(path_)
    for p in path_:
        filelist.append(p)

def generateFile():
    print(filelist)
root = Tk(className="autocad生成器")
#geometry设置tk初始化大小
root.geometry("400x100")
path = StringVar()

L=Label(root,text = "文件选择:")
L.place(x=10,y=40)
E=Entry(root, textvariable = path,width=30)
E.place(x=80,y=40)
B1=Button(root, text = "...", command = selectPath,height=1)
B1.place(x=300,y=35)
B2=Button(root,text="输出CAD和EXCEL文件",command=generateFile)
B2.place(x=100,y=60)

root.mainloop()