from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter.font as tkFont
import xlrd
from xlwt import *
#按钮Frame
from xlwt import Workbook


class b_Frame(Frame):
    def __init__(self,frame,input_Frame=None,row_Frame=None,input_file_frame=None):
        super().__init__(frame)
        self.iF=input_Frame
        self.info_list=[]
        self.row_Frame=row_Frame
        self.input_file_frame=input_file_frame
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
        input_signal=self.input_file_frame.input_signal
        output_signal=self.input_file_frame.output_signal
        #收集数据到self.info_list，
        for i in range(len(input_obj)):
            if i==0 or i==1:
                self.info_list.append(input_obj[i].cget("text"))
            else:
                self.info_list.append(input_obj[i].get())
        #info_list包含了前面两个label的值，需要去掉
        panduan_list=self.info_list[2:][::2]
        #判断收集到的数据，是否符合标准，是否在input和output信号
        #
        draw_label=self.panduan(panduan_list,input_signal,output_signal)
        if draw_label:
            l1=Label(self,text="输入信号有误",width=10)
            l1.grid(row=0, column=3, padx=3)
            self.info_list=[]
        else:
            l1 = Label(self, text="√", width=10)
            l1.grid(row=0, column=3, padx=3)
        print(self.info_list)
    def draw_another_row(self,value=None):
        f2 = basic_row_Frame(self.row_Frame, key=value)
        f2.grid()
    def panduan(self,panduan_list,input_signal,output_signal):
        #将值传回，决定后面的label值是哪个
        for i in panduan_list:
            if i in input_signal:
                pass
            elif i in output_signal:
                pass
            elif "信号" in i:
                self.draw_another_row(value=i)
            else:
                return 1
        return 0
#输入信号Frame
class input_Frame(Frame):
    def __init__(self,frame,key=None,value=None):
        super().__init__(frame)
        self.value=value
        if self.value==None:
            l1=Label(self,text=key)
            l1.grid(row=0,column=0)
            l2=Label(self,text="=",width=3)
            l2.grid(row=0,column=1)
            E1 = Entry(self, width=7)
            E1.grid(row=0, column=2,padx=3)
            E2 = ttk.Combobox(self, value=str1, width=3)
            E2.grid(row=0, column=3, padx=3)
            E3 = Entry(self, width=7)
            E3.grid(row=0, column=4, padx=3)
        else:
            l1 = Label(self, text=self.value[0])
            l1.grid(row=0, column=0)
            l2 = Label(self, text=self.value[1], width=3)
            l2.grid(row=0, column=1)
            output_data=self.value[2:]
            print(self.value)
            for i in range(len(output_data)):
                column=i+2
                if i%2==0:
                    E1 = Entry(self, width=7)
                    E1.grid(row=0, column=column, padx=3)
                else:
                    E2 = ttk.Combobox(self, value=str1,width=3)
                    E2.grid(row=0, column=column, padx=3)

#创建1行的输入Frame，由输入信号Frame和按钮Frame组成
class basic_row_Frame(Frame):
    def __init__(self,frame,key=None,value=None):
        super().__init__(frame)
        self.row_Frame=frame
        self.value=value
        i1=input_Frame(self,key=key,value=self.value)
        b1=b_Frame(self,input_Frame=i1,row_Frame=self.row_Frame,input_file_frame=if_frame)
        i1.grid(row=0,column=0)
        b1.grid(row=0,column=1)

#创建整体的输入Frame
class row_Frame(Frame):
    def __init__(self,frame, key=None, value=None):
        super().__init__(frame)
        self.key=key
        self.value=value
        #若value没有值，则输出基本输入行
        if value== {}:
            f1=basic_row_Frame(self, key= self.key)
            f1.grid()
        #若value有值，则先画若干行基本输入行，再改
        else:
            for i in range(len(value)):
                output=value[i]
                f1=basic_row_Frame(self,key=self.key,value=output)
                f1.grid()
#创建逻辑表达式输入
class input_signal_Frame(Frame):
    def __init__(self,root=None,key=None,value=None):
        super().__init__(root)
        str1 = key + "的逻辑输出表达式"
        self.key=key
        self.value=value
        r1=row_Frame(self,self.key,self.value,)
        r1.grid(row=0,column=0)
        b=Button(self,text="汇总信号",command=lambda r=r1:self.get_this_frame_data(r))
        b.grid(row=1,column=0)
    def get_this_frame_data(self,r1):
        self.output_data=dict()
        output_list=r1.grid_slaves()
        output_list.reverse()
        for i in range(len(output_list)):
            obj1=output_list[i].grid_slaves()[0]
            self.output_data[i]=obj1.info_list
        #打印输出
        print(self.output_data)
        if_frame.output_data[self.key]=self.output_data
        l1 = Label(self, text="√")
        l1.grid(row=1, column=1)
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
        print(if_frame.output_data)
        to_excel_data=if_frame.output_data
        return to_excel_data
    def to_excel(self,to_excel_data=None):
        ws = Workbook(encoding='utf-8')
        w_input = ws.add_sheet(sheetname="输入信号")
        w_output = ws.add_sheet(sheetname="输出信号")
        for i in range(len(if_frame.input_signal)):
            w_input.write(i, 0, if_frame.input_signal[i])
        for j in range(len(if_frame.output_signal)):
            w_output.write(j, 0, if_frame.output_signal[j])
        for k1, v1 in if_frame.output_data.items():
            w = ws.add_sheet(sheetname=k1)
            for k2, v2 in v1.items():
                i = k2
                for j in range(len(v2)):
                        w.write(i, j, v2[j])

        ws.save("输出文件.xls")
        L1 = Label(root, text="√", width=3)
        L1.pack()
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
            color=None
            if len(value)!=0:
                color="red"
            button = Button(self, text=key,bg=color,
                            command=lambda key=key, value=value: self.jump_to_signal_input_frame(key, value))
            button.grid(padx=2, pady=2, row=row, column=column)
            self.Buttons.append(button)
    def jump_to_signal_input_frame(self,key,value):
        str1=key+"的逻辑输出表达式"
        root1 = Tk(className=str1)
        root1.geometry("1000x400")
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
        self.output_data=dict()
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
                    data_list = {}
                    for j in range(row):
                        rowdata = worksheet.row_values(j)
                        data_list[j]=rowdata
                    self.data[i] = data_list
            #增加没有逻辑表达式的数据
            for shuchu in self.output_signal:
                if shuchu not in data.keys():
                    self.data[shuchu] = {}

            print("字典为", end="")
            print(data)
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

str1=["&&","||"]
if_frame=input_file_frame(root)
if_frame.pack()


root.mainloop()