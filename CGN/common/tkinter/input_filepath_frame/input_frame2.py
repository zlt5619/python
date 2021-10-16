from tkinter import *
from tkinter.filedialog import askopenfilenames
"""
新增功能
增加修改和确认按钮
修改按钮：清除所有数据
确认按钮，按了以后，变成1个勾
"""
"""
用于接收文件路径，可以得到多个文件路径，也可得到一个文件路径
通过input_frame的filelists属性，将得到的文件路径传递出去
传递出去的filelists为列表，列表的每个元素，就是路径，形式是字符串str，不是元组
展示为  
label  文字：输入文件
entry  文本框：起初为空，选择后，有值
button 按钮：显示选择文件的路径   每次点击，会清空上次的选择

这个frame不会对选择的文件进行判断，任何文件类型都能输入，包括路径和文件

"""

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