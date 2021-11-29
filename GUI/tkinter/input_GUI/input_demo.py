from tkinter import *
from tkinter.filedialog import askopenfilenames

def selectPath():
    path_ = askopenfilenames()
    path.set(path_)

def generateFile():
    pass

root = Tk(className="autocad生成器")
#geometry设置tk初始化大小
root.geometry("400x100")
path = StringVar()

Label(root,text = "文件选择:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "...", command = selectPath).grid(row = 0, column = 2)

Button(root,text="输出CAD和EXCEL文件",command=generateFile).grid(row=1,column=1)

root.mainloop()