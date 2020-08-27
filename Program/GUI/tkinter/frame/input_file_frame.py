from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter.font as tkFont
import xlrd
import xlwt
#按钮Frame
class b_Frame(Frame):
    def __init__(self,frame,input_Frame=None,row_Frame=None):
        super().__init__(frame)
        self.iF=input_Frame
        self.info_list=[]
        self.row_Frame=row_Frame
        B1 = Button(self, text="+", command=lambda: self.addBox())
        B1.grid(row=0, column=0, padx=3)
        B2 = Button(self, text="-", command=lambda: self.subBox())
        B2.grid(row=0, column=1, padx=3)
        B3 = Button(self, text="完成",
                    command=lambda: self.collect_info_and_draw_another_row())
        B3.grid(row=0, column=2, padx=3)
    def addBox(self):
        column=self.iF.grid_size()[0]
        E1 = ttk.Combobox(self.iF, value=str1, width=3)
        E1.grid(row=0, column=column, padx=3)
        E2 = Entry(self.iF, width=7)
        E2.grid(row=0, column=column+1, padx=3)

    def subBox(self):
        column=self.iF.grid_size()[0]
        if column==3:
            pass
        else:
            obj1=self.iF.grid_slaves().pop(0)
            obj1.destroy()
            obj2 = self.iF.grid_slaves().pop(0)
            obj2.destroy()

    def collect_info_and_draw_another_row(self):

        input_obj=self.iF.grid_slaves()
        input_obj.reverse()
        #收集数据到self.info_list，
        for i in range(len(input_obj)):
            if i==0 or i==1:
                self.info_list.append(input_obj[i].cget("text"))
            else:
                self.info_list.append(input_obj[i].get())
        #再判断是否需要生成新的row
        for i in self.info_list:
            if "信号" in i:
                self.draw_another_row(i)


    def draw_another_row(self,value=None):
        f2 = basic_row_Frame(self.row_Frame, key=value)
        f2.pack()

#输入信号Frame
class input_Frame(Frame):
    def __init__(self,frame,key=None):
        super().__init__(frame)
        l1=Label(self,text=key,width=8)
        l1.grid(row=0,column=0)
        l2=Label(self,text="=",width=3)
        l2.grid(row=0,column=1)
        E1 = Entry(self, width=7)
        E1.grid(row=0, column=2,padx=3)
        E2 = ttk.Combobox(self, value=str1, width=3)
        E2.grid(row=0, column=3, padx=3)
        E3 = Entry(self, width=7)
        E3.grid(row=0, column=4, padx=3)

#创建1行的输入Frame，由输入信号Frame和按钮Frame组成
class basic_row_Frame(Frame):
    def __init__(self,frame,key=None):
        super().__init__(frame)
        self.row_Frame=frame
        i1=input_Frame(self,key=key)
        b1=b_Frame(self,input_Frame=i1,row_Frame=self.row_Frame)
        i1.grid(row=0,column=0)
        b1.grid(row=0,column=1)
#创建多行输入
class rows_Frame(Frame):
    def __init__(self,frame,key=None,value=None):
        super().__init__(frame)
#创建整体的输入Frame
class row_Frame(Frame):
    def __init__(self, frame, key=None, value=None):
        super().__init__(frame)
        self.key=key
        self.value=value
        if value==[[]]:
            f1=basic_row_Frame(self, key= self.key)
            f1.pack()
        else:
            f1=rows_Frame(self,key=self.key,value=self.value)
            f1.pack()
#创建逻辑表达式输入
class input_signal_Frame(Frame):
    def __init__(self,root=None,key=None,value=None):
        super().__init__(root)
        str1 = key + "的逻辑输出表达式"
        self.key=key
        self.value=value
        r1=row_Frame(self,self.key,self.value)
        r1.grid(row=0,column=0)
        b=Button(self,text="汇总信号",command=lambda :self.get_this_frame_data())
        b.grid(row=1,column=0)
    def get_this_frame_data(self):
        output_data[self.key]=10
#创建收集所有汇总信息的Frame
class get_all_info_Frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.root=root
        b1=Button(self,text="汇总生成Excel文件",command=lambda :self.get_info_and_to_excel())
        b1.grid(row=0,column=0)
    def get_info_and_to_excel(self):
        to_excel_data=self.get_info()
        self.to_excel(to_excel_data=to_excel_data)
    def get_info(self):
        print(output_data)
        to_excel_data=None
        return to_excel_data
    def to_excel(self,to_excel_data=None):
        pass
#创建Button生成Frame
class Button_Frame(Frame):
    def __init__(self,root=None,data=None):
        super().__init__(root)
        self.data=data
        self.Buttons=[]
        self.keys=list(data.keys())
        self.values=list(data.values())
        for index in range(len(self.keys)):
            row = int(index / 6)
            column = index % 6
            key = self.keys[index]
            value = self.values[index]
            button = Button(self, text=key,
                            command=lambda key=key, value=value: self.jump_to_signal_input_frame(key, value))
            button.grid(padx=2, pady=2, row=row, column=column)
            self.Buttons.append(button)
    def jump_to_signal_input_frame(self,key,value):
        str1=key+"的逻辑输出表达式"
        root1 = Tk(className=str1)
        root1.geometry("600x600")
        isr=input_signal_Frame(root1,key=key,value=value)
        isr.pack()
        root1.mainloop()
#创建文件输入Frame
class input_file_frame(Frame):
    def __init__(self,root=None):
        #继承了Frame（root）的安排
        super().__init__(root)
        self.path1=StringVar()
        self.filelist=[]
        self.data=dict()
        self.input_signal=[]
        self.output_signal=[]
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
        if len(self.grid_slaves())==5:
            self.grid_slaves(1,0)[0].destroy()
        if filelist[0].endswith("xls") or filelist[0].endswith("xlsx"):
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

            print("字典为", end="")
            print(data)
            output_data=data
            b=Button_Frame(root,data)
            gaiF = get_all_info_Frame(root)
            b.pack()
            gaiF.pack()

        else:
            L = Label(self, text="输入有误，请再次输入", font=fontStyle)
            L.grid(row=1, column=0)
            # print(filelist)
            self.filelist=[]

root=Tk(className="仪表逻辑图")
root.geometry("900x400")
output_data=dict()
str1=["&&","||"]
if_frame=input_file_frame(root)
if_frame.pack()


root.mainloop()