"""
对excel表格进行读取，然后根据matplotlib进行画图处理
1、读取excel表格
2、对对象进行赋值处理
将excel表格第一行的值，作为对象的属性值
根据内容行的值，生成新的对象，由多少行，生成多少个对象
3、选用特定对象进行画图处理
调用符合要求的对象，读取对象的属性值，进行画图
"""
from datetime import datetime
from tkinter import Tk, Frame, StringVar, Label, Entry, Button
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import xlrd


class generator_temperature_class(object):
    def __init__(self,id,time,before_bearing_tem,after_bearing_temp,huahua_temp,power):
        self.id=id
        self.time=time
        self.before_tem=before_bearing_tem
        self.after_tem=after_bearing_temp
        self.huahuan_tem=huahua_temp
        self.power=power


class Select_Frame(Frame):
    def __init__(self, root=None, generator_list=None,str=str):
        super().__init__(root)
        self.generator_list = generator_list
        self.str=str
        self.path1 = StringVar()
        self.path2 = StringVar()
        self.path3 = StringVar()
        self.path4 = StringVar()
        self.path5 = StringVar()
        self.path6 = StringVar()
        self.path7 = StringVar()
        self.path8 = StringVar()
        self.path9 = StringVar()
        self.path10 = StringVar()
        L1 = Label(self, text="输入起始时间")
        L1.grid(row=0, column=2)
        L2=Label(self,text="年")
        L2.grid(row=1, column=0,padx=5)
        L3 = Label(self, text="月")
        L3.grid(row=1, column=1,padx=5)
        L4 = Label(self, text="日")
        L4.grid(row=1, column=2,padx=5)
        L5 = Label(self, text="时")
        L5.grid(row=1, column=3,padx=5)
        L6 = Label(self, text="分")
        L6.grid(row=1, column=4,padx=5)
        E1 = Entry(self, textvariable=self.path1, width=4)
        E1.grid(row=2, column=0)
        E2 = Entry(self, textvariable=self.path2, width=4)
        E2.grid(row=2, column=1)
        E3 = Entry(self, textvariable=self.path3, width=4)
        E3.grid(row=2, column=2)
        E4 = Entry(self, textvariable=self.path4, width=4)
        E4.grid(row=2, column=3)
        E5 = Entry(self, textvariable=self.path5, width=4)
        E5.grid(row=2, column=4)

        L7 = Label(self, text="输入终止时间")
        L7.grid(row=3, column=2)
        L8 = Label(self, text="年")
        L8.grid(row=4, column=0, padx=5)
        L9 = Label(self, text="月")
        L9.grid(row=4, column=1, padx=5)
        L10 = Label(self, text="日")
        L10.grid(row=4, column=2, padx=5)
        L11 = Label(self, text="时")
        L11.grid(row=4, column=3, padx=5)
        L12 = Label(self, text="分")
        L12.grid(row=4, column=4, padx=5)
        E6 = Entry(self, textvariable=self.path6, width=4)
        E6.grid(row=5, column=0)
        E7 = Entry(self, textvariable=self.path7, width=4)
        E7.grid(row=5, column=1)
        E8 = Entry(self, textvariable=self.path8, width=4)
        E8.grid(row=5, column=2)
        E9 = Entry(self, textvariable=self.path9, width=4)
        E9.grid(row=5, column=3)
        E10 = Entry(self, textvariable=self.path10, width=4)
        E10.grid(row=5, column=4)
        B1 = Button(self, text="生成折线图", command=lambda: self.draw_picture(), height=1)
        B1.grid(row=6, column=2, padx=10, pady=30)

    def draw_picture(self):
        str1=int(self.children['!entry'].get())
        str2=int(self.children['!entry2'].get())
        str3=int(self.children['!entry3'].get())
        str4=int(self.children['!entry4'].get())
        str5=int(self.children['!entry5'].get())
        str6=int(self.children['!entry6'].get())
        str7=int(self.children['!entry7'].get())
        str8=int(self.children['!entry8'].get())
        str9=int(self.children['!entry9'].get())
        str10=int(self.children['!entry10'].get())
        start_time=datetime(str1,str2,str3,str4,str5)
        end_time=datetime(str6,str7,str8,str9,str10)
        if self.istimecorrect(start_time,end_time):
            x = list()
            y = list()
            for i in range(self.end_id,self.start_id):
                x.append(self.generator_list[i].time)
                if self.str=="发电机前轴承温度":
                    y.append(self.generator_list[i].before_tem)
                elif self.str=="发电机后轴承温度":
                    y.append(self.generator_list[i].after_tem)
                elif self.str=="发电机滑环室温度":
                    y.append(self.generator_list[i].huahuan_tem)
                else:
                    y.append(self.generator_list[i].power)
            plt.plot(x, y)
            plt.show()

        else:
            L13 = Label(self, text="输入时间有误，请重新输入")
            L13.grid(row=7, column=2)
    def istimecorrect(self,start_time,end_time):
        self.start_id=None
        self.end_id=None
        for i in self.generator_list:
            if start_time==i.time:
                self.start_id=i.id
            if end_time==i.time:
                self.end_id=i.id
        if self.start_id==None or self.end_id==None:
            return False
        else:
            return True

class Draw_Picture_Frame(Frame):
    def __init__(self,root=None,generator_list=None):
        super().__init__(root)
        self.generator_list=generator_list
        B1 = Button(self, text="发电机前轴承温度",command=lambda: self.draw_picture("发电机前轴承温度"), height=1)
        B1.grid(row=0, column=1, padx=10, pady=30)
        B2 = Button(self, text="发电机后轴承温度", command=lambda: self.draw_picture("发电机后轴承温度"),height=1)
        B2.grid(row=1, column=1, padx=10, pady=30)
        B3 = Button(self, text="发电机滑环室温度",command=lambda: self.draw_picture("发电机滑环室温度"), height=1)
        B3.grid(row=2, column=1, padx=10, pady=30)
        B4 = Button(self, text="有功功率", command=lambda: self.draw_picture("有功功率"),height=1)
        B4.grid(row=3, column=1, padx=10, pady=30)

    def draw_picture(self,str):
        root2 = Tk(className="画图参数选择")
        root2.geometry("300x400")
        select_frame=Select_Frame(root2,generator_list=self.generator_list,str=str)
        select_frame.pack()


class input_file_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.path1 = StringVar()
        self.filepath=None
        L1 = Label(self, text="输入文件:")
        L1.grid(row=0, column=0,pady=30,padx=20)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=0, column=1,pady=30)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath(self.path1), height=1)
        B1.grid(row=0, column=2, padx=10,pady=30)
        B2=Button(self,text="生成图像",command=lambda :self.read_excel(),height=1)
        B2.grid(row=1,column=1,padx=10)


    def selectPath(self,path1):
        path_ = askopenfilename()
        path1.set(path_)
        self.filepath=path_

    def read_excel(self):
        work_book = xlrd.open_workbook(self.filepath)
        sheet = work_book.sheet_by_name("Sheet")
        row_num = sheet.nrows
        # 创建generator温度对象的列表
        generator_list = []
        for i in range(row_num):
            if i == 0:
                pass
            else:
                id = i
                time, before_bearing_tem, after_bearing_temp, huahua_temp, power = sheet.row_values(i)
                time = xlrd.xldate.xldate_as_datetime(time, 0)
                before_bearing_tem = round(before_bearing_tem, 2)
                after_bearing_temp = round(after_bearing_temp, 2)
                huahua_temp = round(huahua_temp, 2)
                power = round(power, 2)
                g = generator_temperature_class(id, time, before_bearing_tem, after_bearing_temp, huahua_temp, power)
                generator_list.append(g)
        root1=Tk(className="图像处理")
        root1.geometry("300x400")
        draw_picture_frame=Draw_Picture_Frame(root1,generator_list=generator_list)
        draw_picture_frame.pack()




root=Tk(className="Excel文件处理")
root.geometry("500x200")

if_frame=input_file_frame(root)
if_frame.pack()

root.mainloop()

