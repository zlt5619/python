from tkinter import *
from tkinter.filedialog import askopenfilenames

class GUI():
    def selectPath(self,path):
        path_ = askopenfilenames()
        path.set(path_)
        self.filelist.append(path_)

    def generateFile(self):
        self.mainpowersource = self.path1.get()
        self.auxlirypowersoruce = self.path2.get()


    def __init__(self):
        self.filelist=[]
        self.mainpowersource=None
        self.auxlirypowersoruce=None
        self.root=Tk(className="autocad生成器")
        self.root.geometry("350x200")
        self.path1 = StringVar()
        self.path2 = StringVar()
        self.path3 = StringVar()
        self.path4 = StringVar()
        L1 = Label(self.root, text="主电源:")
        L1.place(x=10, y=20)
        E1 = Entry(self.root, textvariable=self.path1, width=10)
        E1.place(x=80, y=20)
        L2 = Label(self.root, text="辅助电源:")
        L2.place(x=150, y=20)
        E2 = Entry(self.root, textvariable=self.path2, width=10)
        E2.place(x=220, y=20)
        L3 = Label(self.root, text="开关选择:")
        L3.place(x=10, y=65)
        E3 = Entry(self.root, textvariable=self.path3, width=30)
        E3.place(x=80, y=65)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self.root, text="...", command=lambda :self.selectPath(self.path3), height=1)
        B1.place(x=300, y=60)
        L4 = Label(self.root, text="文件选择:")
        L4.place(x=10, y=110)
        E4 = Entry(self.root, textvariable=self.path4, width=30)
        E4.place(x=80, y=110)
        B1 = Button(self.root, text="...", command=lambda :self.selectPath(self.path4), height=1)
        B1.place(x=300, y=105)
        B2 = Button(self.root, text="输出CAD和EXCEL文件", command=self.generateFile)
        B2.place(x=100, y=130)
        self.root.mainloop()


