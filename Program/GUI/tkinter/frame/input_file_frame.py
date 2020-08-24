from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.font as tkFont
import xlrd


class input_file_frame(Frame):
    def __init__(self,filelist=None,data=None,input_signal=None,output_signal=None):
        Frame.__init__(self,filelist=None,data=None,input_signal=None,output_signal=None)
        self.path1=StringVar()
        self.filelist=filelist
        self.data=data
        self.input_signal=input_signal
        self.output_signal=output_signal
        L1 = Label(self, text="输入文件:")
        L1.grid(row=0, column=0)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=0, column=1)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath(self.path1), height=1)
        B1.grid(row=0, column=2, padx=3)
        B2 = Button(self, text="完成信号输入", command=lambda: self.read_file(self.filelist, self.data), height=1)
        B2.grid(row=0, column=3, padx=3)

    def selectPath(self,path1):
        path_ = askopenfilename()
        path1.set(path_)
        self.filelist.append(path_)

    def read_file(self,filelist, data1):
        data = data1
        fontStyle = tkFont.Font(size=20)
        L = Label(self, text="信号输入完成", font=fontStyle)
        L.grid(row=1, column=0)
        workxls = xlrd.open_workbook(filelist[0])
        worksheet_input = workxls.sheet_by_name("输入信号")
        row = worksheet_input.nrows
        for i in range(row):
            rowdata = worksheet_input.row_values(i)[0]  # i行的list
            self.input_signal.append(rowdata)

        worksheet_output = workxls.sheet_by_name("输出信号")
        row = worksheet_output.nrows
        for i in range(row):
            rowdata = worksheet_output.row_values(i)[0]  # i行的list
            self.output_signal.append(rowdata)

        # 读取输入文件写好的信号相关内容，并将内容赋给字典data
        excel_list = workxls.sheet_names()[2:]
        if len(excel_list) == 0:
            pass
        else:
            for i in excel_list:
                worksheet = workxls.sheet_by_name(i)
                row = worksheet.nrows
                data_list = []
                for j in range(row):
                    rowdata = worksheet.row_values(j)
                    data_list.append(rowdata)
                self.data[i] = data_list
        for shuchu in self.output_signal:
            if shuchu not in data.keys():
                self.data[shuchu] = [[]]

        print("字典为", end=None)
        print(data)

root=Tk(className="仪表逻辑图")
root.geometry("900x400")
filelist=[]
input_signal=[]
output_signal=[]
data=dict()
if_frame=input_file_frame(data=data,input_signal=input_signal,output_signal=output_signal,filelist=filelist)
if_frame.pack()
root.mainloop()