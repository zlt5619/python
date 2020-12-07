from tkinter import *
from tkinter.filedialog import askopenfilenames
from CAD.draw_seconary_drawing.cad_function import drawCAD


#建立基础框架
root= Tk(className="二次图制作")
root.geometry("400x100")

#输入模块包含 请输入文件，文件框，文件选择按钮
path = StringVar()
input_frame=Frame(root, height=20, width=400)
Label(input_frame, text="文件选择:").grid(row=0, column=0)
Entry(input_frame, textvariable=path).grid(row=0, column=1)
def selectPath():
    path_ = askopenfilenames()
    path.set(path_)
    input_frame.info=path_
Button(input_frame, text = "...", command = selectPath).grid(row = 0, column = 2)

#生成CAD按钮，按一下，先弹出窗口，确认CAD是否打开，再按一次，生成CAD文件
def createNewWindow():
    root2=Tk(className="CAD文件")
    root2.geometry("200x100")
    root2.info=input_frame.info
    Label(root2,text="请确认CAD软件已打开").pack()
    Button(root2,text="生成CAD",command=drawCAD).pack()

b1=Button(root,text="生成CAD文件",command=createNewWindow)


input_frame.pack()
b1.pack()
root.mainloop()