from tkinter import *
from tkinter.filedialog import askopenfilenames
import xlrd

#电源选择
class power_select_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        L1 = Label(self, text="电源数量")
        L1.grid(row=0, column=0,padx=10)
        E1 = Entry(self, width=10)
        E1.grid(row=0, column=1)

#excel数据处理,待补充
class Excel_Reader():
    def __init__(self,filelists=None):
        self.filelists=filelists

    def print1(self):
        print(self.filelists)
#输入文件路径frame
class input_filepath_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.filelists=[]
        self.actual_path=None
        #用于在文本框显示已选择的文件
        self.text_path = StringVar()
        L1 = Label(self, text="输入文件:")
        L1.grid(row=0, column=0)
        E1 = Entry(self, textvariable=self.text_path, width=30)
        E1.grid(row=0, column=1)
        B1 = Button(self, text="...", command=lambda: self.selectPath(), height=1)
        B1.grid(row=0, column=2, padx=3)
        B2=Button(self, text="修改", command=lambda: self.clear(), height=1)
        B2.grid(row=0, column=3, padx=3)
        self.B3= Button(self, text="确认", command=lambda: self.confirm(), height=1)
        self.B3.grid(row=0, column=4, padx=3)
    #选择路径
    def selectPath(self):
        self.text_path.set(" ")
        self.filelists = []
        self.actual_path=askopenfilenames()
        self.text_path.set(self.actual_path)
        for i in self.actual_path:
            self.filelists.append(i)
    #清楚数据
    def clear(self):
        self.filelists = []
        self.text_path.set(" ")
        self.grid_slaves()[0].destroy()
        self.B3 = Button(self, text="确认", command=lambda: self.confirm(), height=1)
        self.B3.grid(row=0, column=4, padx=3)
    #确认数据
    def confirm(self):
        self.B3.destroy()
        self.L2=Label(self, text="√")
        self.L2.grid(row=0, column=4, padx=3)

#主输入程序frame
class input_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        #文件路径选择
        self.iff=input_filepath_frame(self)
        self.iff.pack()
        #电源路径选择
        self.psf=power_select_frame(self)
        self.psf.pack(pady=20)







#主程序
if __name__=="__main__":
    root=Tk(className="配电图绘制")
    root.geometry("600x600")
    i_f=input_frame(root)
    i_f.pack(pady=20)
    root.mainloop()