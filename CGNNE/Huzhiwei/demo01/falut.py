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

path01="C:/Users/zlt/Desktop/胡志伟/01 故障记录汇总表-2021年10月（湖北分公司）-V2.1）.xlsx"
#读取excel表格
work_book = xlrd.open_workbook(path01)
sheet=work_book.sheet_by_name("故障填报主表")
row_num=sheet.nrows

fault_list=[]
for i in range(4,row_num):
    id, company, station, generator_num, generator_no,generator_factory, generator_model, fault_name, info,fault_code, fault_description, fault_kind,fault_start_time, maintanence_start_time, recover_time,fault_first_location, fault_second_location, fault_third_location,check_list, fault_reason, maintantence_level, maintanence_kind,work_ticket_num, maintanence_movement, maintanence_object,object_name, object_kind, object_num, object_danwei, object_factory,test_method, fault_analysis_report_num, lost_power,maintanence_cost, total, people_name, people_num=sheet.row_values(i,0,37)
    f=Fault(id, company, station, generator_num, generator_no,generator_factory, generator_model, fault_name, info,fault_code, fault_description, fault_kind,fault_start_time, maintanence_start_time, recover_time,fault_first_location, fault_second_location, fault_third_location,check_list, fault_reason, maintantence_level, maintanence_kind,work_ticket_num, maintanence_movement, maintanence_object,object_name, object_kind, object_num, object_danwei, object_factory,test_method, fault_analysis_report_num, lost_power,maintanence_cost, total, people_name, people_num)
    fault_list.append(f)

# print(type(sheet.cell_value(5,12)))
# print(sheet.cell_type(5,12))
# print(xlrd.xldate.xldate_as_datetime(sheet.cell_value(5,12),0))

#获取每个对象的时间差
def getTime(start_time,end_time):
    start_time=xlrd.xldate.xldate_as_datetime(start_time, 0)
    end_time=xlrd.xldate.xldate_as_datetime(end_time, 0)
    time=end_time-start_time
    return time

#
# print(fault_list[1].id)
# print(fault_list[1].generator_factory)
# print(fault_list[1].fault_start_time)
# print(fault_list[1].recover_time)
# time=getTime(fault_list[1].fault_start_time,fault_list[1].recover_time)
# print(time.total_seconds())
# print(fault_list[14].id)
# print(fault_list[14].generator_factory)
# print(xlrd.xldate.xldate_as_datetime(fault_list[14].fault_start_time,0))


class StationInfo(object):
    def __init__(self,id,station_name,station_capacity,station_generator_num):
        self.id=id
        self.station_name=station_name
        self.station_capacity=station_capacity
        self.station_generator_num=station_generator_num
        self.total_fault_count=0
        self.total_fault_time=0.0
        self.total_lost=0.0

path02="C:/Users/zlt/Desktop/胡志伟/湖北分公司风电场基础数据.xlsx"
#读取excel表格
work_book02 = xlrd.open_workbook(path02)
sheet02=work_book02.sheet_by_name("Sheet1")
row_num02=sheet02.nrows
station_list=[]
for i in range(1,row_num02):
    id,station_name,station_capacity,station_generator_num=sheet02.row_values(i,0,4)
    station_capacity=int(station_capacity)
    station_generator_num=int(station_generator_num)
    s=StationInfo(id,station_name,station_capacity,station_generator_num)
    station_list.append(s)
# print(station_list[0].station_name)
# print(station_list[0].station_capacity)
# print(station_list[0].station_generator_num)

#获取故障总次数，故障修复时间，经济损失
count=0
for i in fault_list:
    if(i.info=="非计划停机"):
        for j in station_list:
            if i.station==j.station_name:
                j.total_fault_count+=1
                j.total_fault_time+=getTime(i.fault_start_time,i.recover_time).total_seconds()
                j.total_lost+=i.total

# for i in station_list:
#     print(i.station_name)
#     print(i.total_fault_count)
#     print(i.total_fault_time)
#     print(i.total_lost)

#开始计算MTBF，MTTR，TBA，单位容量故障次数，单位容量经济损失
for i in station_list:
    if i.total_fault_count==0:
        i.MTBF = round(30 * 24 * i.station_generator_num , 2)
        i.MTTR = round(i.total_fault_time/3600, 2)
    else:
        i.MTBF=round(30*24*i.station_generator_num/i.total_fault_count,2)
        i.MTTR=round((i.total_fault_time/3600)/i.total_fault_count,2)
    i.TBA=round((30*24*i.station_generator_num-i.total_fault_time/3600)/(30*24*i.station_generator_num),4)
    i.fault_count_per_capacity=i.total_fault_count/i.station_capacity
    i.lost_per_capacity=i.total_lost/i.station_capacity

for i in station_list:
    print(i.station_name)
    print(i.MTBF)
    print(i.MTTR)
    print(i.TBA)
    print(i.fault_count_per_capacity)
    print(i.lost_per_capacity)

import matplotlib
import matplotlib.pyplot as plt
#横坐标显示中文
font = {'family': 'Microsoft YaHei', 'weight': 'bold', 'size': '14'}
matplotlib.rc("font", family="Microsoft YaHei", weight="bold", size="14")
x=list()
y=list()
for i in station_list:
    x.append(i.station_name.strip("风电场"))
    y.append(i.MTBF)
plt.figure(figsize=(20,8))
plt.bar(x,y,width=0.5,label="MTBF")
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a,b+0.01,"%.2f"%y[i],ha='center',fontsize=10) # plt.text 函数

plt.show()


