from tkinter import *
from tkinter.filedialog import askopenfilenames
from first_edtion.cad_function import drawCAD




"""
建立自定义的Frame
第一行，有输入文件label，文件框，选择文件按钮   选择文件后，所选文件路径会赋值到自身frame的参数中
第二行，一个生成CAD文件的按钮，产生一个新的窗口，并将自身frame收集到的文件路径作为参数，传到新的窗口
"""
class input_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.path1 = StringVar()
        self.filelist = []
        L1 = Label(self, text="输入文件:")
        L1.grid(row=0, column=0)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=0, column=1)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath(self.path1), height=1)
        B1.grid(row=0, column=2, padx=3)
        B2 = Button(self, text="完成文件输入", command=lambda: self.checkInput(), height=1)
        B2.grid(row=0, column=3, padx=3)
        B3=Button(self,text="生成CAD文件",command=lambda :self.createNewWindow(self.filelist),height=1)
        B3.grid(row=1, column=1, padx=3)

    def selectPath(self, path1):
        path_ = askopenfilenames()
        path1.set(path_)
        self.filelist=[]
        self.filelist.append(path_)

    def checkInput(self):
        L2=Label(self,text="√")
        L2.grid(row=0, column=4, padx=3)

    def createNewWindow(self,filelist):
        root1 = Tk(className="CAD文件生成")
        root1.geometry("200x100")
        if filelist==[]:
            L1=Label(root1,text="请输入文件路径")
            L1.pack(pady=10)
        else:
            r_frame=result_frame(root1,filelist)
            r_frame.pack()
        root1.mainloop()
"""
创立一个新frame
第一行，label 请确认CAD软件已打开
第二行，按钮，在桌面生成CAD文件
"""
class result_frame(Frame):
    def __init__(self,root=None,filelist=None):
        super().__init__(root)
        self.filelist=filelist
        L1=Label(self, text="请确认CAD软件已打开")
        B1=Button(self, text="生成CAD文件", command=lambda: self.draw(self.filelist), height=1)
        L1.pack(pady=10)
        B1.pack()
    def draw(self,filelsit):
        filelsit=filelsit
        drawCAD(filelsit)



if __name__=="__main__":
    # 建立基础框架
    root = Tk(className="二次图制作")
    root.geometry("500x100")
    if_frame = input_frame(root)
    if_frame.pack(pady=10)

    root.mainloop()