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

# 按场站统计
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


# 风机厂信息
class Factory_Info(object):
    def __init__(self, id, name,num,capacity):
        self.id = id
        self.name = name
        self.num=num
        self.capcity=capacity
        self.total_fault_count=0
        self.total_falut_time=0.0
        self.total_maintanece_time=0.0
        self.power_lost=0.0
        self.total_cost=0.0


sheet02_02 = work_book02.sheet_by_name("Sheet2")
row_num02_02 = sheet02_02.nrows
factory_list = []
for i in range(1, row_num02_02):
    id, name ,num,capacity= sheet02_02.row_values(i)
    id = int(id)
    num=int(num)
    f = Factory_Info(id, name,num,capacity)
    factory_list.append(f)

# for i in factory_list:
#     print(i.id)
#     print(i.name)
#     print(i.num)
#     print(i.capcity)

#获取故障总次数，故障修复时间，经济损失

class Fault_info(object):
    def __init__(self,id,fault_first_location):
        self.id=id
        self.fault_first_location=fault_first_location
        self.total_fault_count=0
        self.total_fault_time=0.0
        self.maintanence_time=0.0
        self.total_lost=0.0

class Maintanence_info(object):
    def __init__(self,id,maintanence_level):
        self.id=id
        self.maintanence_level=maintanence_level
        self.total_fault_count = 0
        self.total_fault_time = 0.0
        self.maintanence_time = 0.0
        self.total_lost = 0.0


# 开始统计

fault_info_set=set()
maintantence_info_set=set()

for i in fault_list:
    fault_info_set.add(i.fault_first_location)
    maintantence_info_set.add(i.maintanence_level)
    if(i.info=="非计划停机"):
        for j in station_list:
            if i.station==j.station_name:
                j.total_fault_count+=1
                j.total_fault_time+=getTime(i.fault_start_time,i.recover_time).total_seconds()
                j.total_lost+=i.total
        for j in factory_list:
            if i.generator_factory==j.name:
                j.total_fault_count+=1
                j.total_falut_time+=getTime(i.fault_start_time,i.recover_time).total_seconds()
                j.total_maintanece_time+=getTime(i.maintanence_start_time,i.recover_time).total_seconds()
                j.total_cost+=i.total
                if i.lost_power=="":
                    pass
                else:
                    j.power_lost+=float(i.lost_power)

id=1
fault_info_list=[]
for i in fault_info_set:
    f=Fault_info(id,i)
    fault_info_list.append(f)
id=1
maintantence_info_list=[]
for i in maintantence_info_set:
    m=Maintanence_info(id,i)
    maintantence_info_list.append(m)

# for i in fault_info_list:
#     print(i.fault_first_location)
# for i in maintantence_info_list:
#     print(i.maintanence_level)


# for i in station_list:
#     print(i.station_name)
#     print(i.total_fault_count)
#     print(i.total_fault_time)
#     print(i.total_lost)
#
# for i in factory_list:
#     print(i.name)
#     print(i.total_fault_count)
#     print(i.total_falut_time)
#     print(i.total_maintanece_time)
#     print(i.total_cost)
#     print(i.power_lost)


#开始计算MTBF，MTTR，TBA，单位容量故障次数，单位容量经济损失
for i in station_list:
    if i.total_fault_count==0:
        i.MTBF = round(30 * 24 * i.station_generator_num , 1)
        i.MTTR = round(i.total_fault_time/3600, 1)
    else:
        i.MTBF=round(30*24*i.station_generator_num/i.total_fault_count,1)
        i.MTTR=round((i.total_fault_time/3600)/i.total_fault_count,1)
    i.TBA=round((30*24*i.station_generator_num-i.total_fault_time/3600)/(30*24*i.station_generator_num),4)
    i.fault_count_per_capacity=round(i.total_fault_count/i.station_capacity,1)
    i.lost_per_capacity=round(i.total_lost/i.station_capacity,2)
for i in factory_list:
    if i.total_fault_count==0:
        i.MTBF=round(30*24*i.num,1)
        i.MTTR=round(i.total_fault_count/3600,1)
    else:
        i.MTBF=round(30*24*i.num/i.total_fault_count,1)
        i.MTTR=round((i.total_falut_time/3600)/i.total_fault_count,1)
    i.TBA=round((30*24*i.num-i.total_falut_time/3600)/(30*24*i.num),4)
    i.fault_count_per_capacity=round(i.total_fault_count/i.capcity,1)
    i.lost_per_capacity=round(i.total_cost/i.capcity,2)

#开始计算故障总次数和维修等级次数
for i in fault_list:
    for j in fault_info_list:
        if i.fault_first_location==j.fault_first_location:
            j.total_fault_count+=1
            if i.fault_start_time=="":
                pass
            else:
                j.total_fault_time += getTime(i.fault_start_time, i.recover_time).total_seconds()
            if i.fault_start_time == "":
                pass
            else:
                j.maintanence_time += getTime(i.maintanence_start_time, i.recover_time).total_seconds()
            j.total_lost+=i.total
for i in fault_list:
    for j in maintantence_info_list:
        if i.maintanence_level==j.maintanence_level:
            j.total_fault_count+=1
            if i.fault_start_time=="":
                pass
            else:
                j.total_fault_time += getTime(i.fault_start_time, i.recover_time).total_seconds()
            if i.fault_start_time == "":
                pass
            else:
                j.maintanence_time += getTime(i.maintanence_start_time, i.recover_time).total_seconds()
            j.total_lost+=i.total

#展示用
# for i in station_list:
#     print(i.station_name)
#     print(i.MTBF)
#     print(i.MTTR)
#     print(i.TBA)
#     print(i.fault_count_per_capacity)
#     print(i.lost_per_capacity)
# print("==============")

# for i in factory_list:
#     print(i.name)
#     print(i.MTBF)
#     print(i.MTTR)
#     print(i.TBA)
#     print(i.fault_count_per_capacity)
#     print(i.lost_per_capacity)
# print("==============")

for i in fault_info_list:
    print(i.fault_first_location)
    print(i.total_lost)
    print(i.total_fault_count)
    print(i.total_fault_time)
    print(i.maintanence_time)
for i in maintantence_info_list:
    print(i.maintanence_level)
    print(i.total_lost)
    print(i.total_fault_count)
    print(i.total_fault_time)
    print(i.maintanence_time)



#对对象进行排序处理
#sort(key=lambda 对象：对象.属性)
station_list.sort(key = lambda x:x.MTBF)
# for i in station_list:
#     print(i.station_name,end='\t')
#     print(i.MTBF,end='\t')





# 画图部分
import matplotlib
import matplotlib.pyplot as plt

x=list()
y=list()
for i in station_list:
    x.append(i.station_name.strip("风电场"))
    y.append(i.TBA)


def plot(title, x_label=None, y_value=None, y_label=None, hasaverage=None):
    """

    :param title: 图纸名称
    :param x_label: x的坐标值
    :param y_value: 与x对应的y的值
    :param y_label: y的坐标值
    :param hasaverage: 是否画平均线
    :return:
    """

    if y_label is None:
        y_label = []
    if y_value is None:
        y_value = []
    if x_label is None:
        x_label = []
    # 横坐标显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # font = {'family': 'Microsoft YaHei', 'size': '14'}
    # matplotlib.rc("font", family="Microsoft YaHei",  size="14")

    #指定画布大小
    plt.figure(figsize=(24, 4))


    #设置x轴坐标整体名称
    plt.xlabel("")
    # 添加Y轴标签
    plt.ylabel("")
    #设置柱形图的x坐标值，和对应的y值
    #设置柱子的宽度width
    #设置柱子的颜色color
    color=[]
    for i in range(len(x_label)):
        if i<3:
            color.append('r')
        elif i>(len(x_label)-4):
            color.append('g')
        else:
            color.append('b')
    plt.bar(x_label, y_value, width=0.4,color=color)
    if title=="TBA":
        # 设置图表名称
        plt.title(title, loc="center", pad=10)
        plt.ylim([0.96,1])
        for a, b, i in zip(x, y, range(len(x))):
            plt.text(a, b, "%.2f%%" % (y[i] * 100), ha='center', fontsize=10)
    else:
    # 通过zip 函数函数，遍历x，y列表
    #在柱形图上，设置文字
    # plt.text 函数
    # 设置图表名称
        plt.title(title, loc="center")
        for a, b, i in zip(x, y, range(len(x))):
            plt.text(a, b +300, "%.1f" % y[i], ha='center', fontsize=10)
    #画平均值线
    y_sum=0
    for i in y_value:
        y_sum+=i
    y_average=y_sum/len(y_value)
    # 添加水平直线
    plt.axhline(y=y_average, ls="-", c="orange",label="平均值")
    # 打开坐标网格
    plt.grid(axis="y",ls="-", c='grey', )
    #图例设置
    plt.legend(loc='lower center')
    plt.show()

plot("TBA",x,y)


