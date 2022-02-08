"""
1、读取excel表格
2、生成相应对象
3、数据分析
"""
from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib
import matplotlib.pyplot as plt

import xlrd
class Fault(object):
    def __init__(self,id,company,station,generator_num,generator_no,
                 generator_factory,generator_model,fault_name,info,
                 fault_code,fault_description,fault_kind,
                 fault_start_time,maintanence_start_time,recover_time,
                 fault_first_location,fault_second_location,fault_third_location,
                 check_list,fault_reason,maintantence_level,maintanence_kind,
                 work_ticket_num,maintanence_movement,maintanence_object,
                 object_name,object_kind,object_num,object_danwei,object_factory,
                 test_method,fault_analysis_report_num,lost_power,
                 maintanence_cost,total,people_name,people_num):
        self.id=id
        self.company=company
        self.station=station
        self.generator_num=generator_num
        self.generator_factory=generator_factory
        self.generator_no=generator_no
        self.generator_model=generator_model
        self.fault_name=fault_name
        self.info=info
        self.fault_code=fault_code
        self.fault_description=fault_description
        self.fault_kind=fault_kind
        self.fault_start_time=fault_start_time
        self.maintanence_start_time=maintanence_start_time
        self.recover_time=recover_time
        self.fault_first_location=fault_first_location
        self.fault_second_location=fault_second_location
        self.fault_third_location=fault_third_location
        self.check_list=check_list
        self.fault_reason=fault_reason
        self.maintanence_level=maintantence_level
        self.maintanence_kind=maintanence_kind
        self.work_ticket_num=work_ticket_num
        self.maintanence_movement=maintanence_movement
        self.maintanence_object=maintanence_object
        self.object_name=object_name
        self.object_kind=object_kind
        self.object_num=object_num
        self.object_danwei=object_danwei
        self.object_factory=object_factory
        self.test_method=test_method
        self.fault_analysis_report_num=fault_analysis_report_num
        self.lost_power=lost_power
        self.maintanence_cost=maintanence_cost
        self.total=self.get_total(total)
        self.people_name=people_name
        self.people_num=people_num

    def get_total(self, total):
        if total=="":
            num=0.0
        elif total=="0":
            num=0.0
        else:
            num=float(total)
        return num
class StationInfo(object):
    def __init__(self,id,station_name,station_capacity,station_generator_num):
        self.id=id
        self.station_name=station_name
        self.station_capacity=station_capacity
        self.station_generator_num=station_generator_num
        self.total_fault_count=0
        self.total_fault_time=0.0
        self.total_lost=0.0
def getTime(start_time,end_time):
    start_time=xlrd.xldate.xldate_as_datetime(start_time, 0)
    end_time=xlrd.xldate.xldate_as_datetime(end_time, 0)
    time=end_time-start_time
    return time

class Draw_Picture_Frame(Frame):
    def __init__(self,root=None,fault_list=None,station_list=None):
        super().__init__(root)
        self.faulr_list=fault_list
        self.station_list=station_list
        B1 = Button(self, text="MTBF", command=lambda: self.draw_picture("MTBF"), height=1)
        B1.grid(row=0, column=1, padx=10, pady=30)
        B2 = Button(self, text="MTTR", command=lambda: self.draw_picture("MTTR"), height=1)
        B2.grid(row=1, column=1, padx=10, pady=30)
        B3 = Button(self, text="TBA", command=lambda: self.draw_picture("TBA"), height=1)
        B3.grid(row=2, column=1, padx=10, pady=30)
        B4 = Button(self, text="单位容量故障次数", command=lambda: self.draw_picture("单位容量故障次数"), height=1)
        B4.grid(row=3, column=1, padx=10, pady=30)
        B5 = Button(self, text="单位容量经济损失", command=lambda: self.draw_picture("单位容量经济损失"), height=1)
        B5.grid(row=4, column=1, padx=10, pady=30)
    def draw_picture(self, param):
        font = {'family': 'Microsoft YaHei', 'weight': 'bold', 'size': '14'}
        matplotlib.rc("font", family="Microsoft YaHei", weight="bold", size="14")
        x = list()
        y = list()
        for i in self.station_list:
            x.append(i.station_name.strip("风电场"))
            if param=="MTBF":
                y.append(i.MTBF)
            elif param=="MTTR":
                y.append(i.MTTR)
            elif param=="TBA":
                y.append(i.TBA)
            elif param=="单位容量故障次数":
                y.append(i.fault_count_per_capacity)
            else:
                y.append(i.lost_per_capacity)
        plt.figure(figsize=(20, 8))
        plt.bar(x, y, width=0.5, label=param)
        for a, b, i in zip(x, y, range(len(x))):  # zip 函数
            plt.text(a, b + 0.01, "%.2f" % y[i], ha='center', fontsize=10)  # plt.text 函数
        plt.show()

class input_file_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.path1 = StringVar()
        self.path2 = StringVar()
        self.filepath=None
        L1 = Label(self, text="输入故障数据文件:")
        L1.grid(row=0, column=0,pady=30,padx=20)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=0, column=1,pady=30)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath01(self.path1), height=1)
        B1.grid(row=0, column=2, padx=10,pady=30)
        L2 = Label(self, text="输入场站基本文件:")
        L2.grid(row=1, column=0, pady=30, padx=20)
        E2 = Entry(self, textvariable=self.path2, width=30)
        E2.grid(row=1, column=1, pady=30)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath02(self.path2), height=1)
        B1.grid(row=1, column=2, padx=10, pady=30)
        B2=Button(self,text="分析数据",command=lambda :self.read_excel(),height=1)
        B2.grid(row=2,column=1,padx=10)


    def selectPath01(self,path1):
        path_ = askopenfilename()
        path1.set(path_)
        self.filepath01=path_
    def selectPath02(self,path2):
        path_ = askopenfilename()
        path2.set(path_)
        self.filepath02=path_

    def read_excel(self):
        work_book = xlrd.open_workbook(self.filepath01)
        sheet = work_book.sheet_by_name("故障填报主表")
        row_num = sheet.nrows
        fault_list = []
        for i in range(4, row_num):
            id, company, station, generator_num, generator_no, generator_factory, generator_model, fault_name, info, fault_code, fault_description, fault_kind, fault_start_time, maintanence_start_time, recover_time, fault_first_location, fault_second_location, fault_third_location, check_list, fault_reason, maintantence_level, maintanence_kind, work_ticket_num, maintanence_movement, maintanence_object, object_name, object_kind, object_num, object_danwei, object_factory, test_method, fault_analysis_report_num, lost_power, maintanence_cost, total, people_name, people_num = sheet.row_values(
                i, 0, 37)
            f = Fault(id, company, station, generator_num, generator_no, generator_factory, generator_model, fault_name,
                      info, fault_code, fault_description, fault_kind, fault_start_time, maintanence_start_time,
                      recover_time, fault_first_location, fault_second_location, fault_third_location, check_list,
                      fault_reason, maintantence_level, maintanence_kind, work_ticket_num, maintanence_movement,
                      maintanence_object, object_name, object_kind, object_num, object_danwei, object_factory,
                      test_method, fault_analysis_report_num, lost_power, maintanence_cost, total, people_name,
                      people_num)
            fault_list.append(f)
        work_book02 = xlrd.open_workbook(self.filepath02)
        sheet02 = work_book02.sheet_by_name("Sheet1")
        row_num02 = sheet02.nrows
        station_list = []
        for i in range(1, row_num02):
            id, station_name, station_capacity, station_generator_num = sheet02.row_values(i, 0, 4)
            station_capacity = int(station_capacity)
            station_generator_num = int(station_generator_num)
            s = StationInfo(id, station_name, station_capacity, station_generator_num)
            station_list.append(s)
        # 获取故障总次数，故障修复时间，经济损失
        for i in fault_list:
            if (i.info == "非计划停机"):
                for j in station_list:
                    if i.station == j.station_name:
                        j.total_fault_count += 1
                        j.total_fault_time += getTime(i.fault_start_time, i.recover_time).total_seconds()
                        j.total_lost += i.total
        # 开始计算MTBF，MTTR，TBA，单位容量故障次数，单位容量经济损失
        for i in station_list:
            if i.total_fault_count == 0:
                i.MTBF = round(30 * 24 * i.station_generator_num, 2)
                i.MTTR = round(i.total_fault_time / 3600, 2)
            else:
                i.MTBF = round(30 * 24 * i.station_generator_num / i.total_fault_count, 2)
                i.MTTR = round((i.total_fault_time / 3600) / i.total_fault_count, 2)
            i.TBA = round(
                (30 * 24 * i.station_generator_num - i.total_fault_time / 3600) / (30 * 24 * i.station_generator_num),
                4)
            i.fault_count_per_capacity = i.total_fault_count / i.station_capacity
            i.lost_per_capacity = i.total_lost / i.station_capacity

        root1=Tk(className="绘图")
        root1.geometry("200x500")
        draw_picture_frame=Draw_Picture_Frame(root1,fault_list,station_list)
        draw_picture_frame.pack()


root=Tk(className="Excel文件处理")
root.geometry("500x300")

if_frame=input_file_frame(root)
if_frame.pack()

root.mainloop()