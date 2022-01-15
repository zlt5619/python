import xlrd
import matplotlib.pyplot as plt
class generator_temperature_class(object):
    def __init__(self,id,time,before_bearing_tem,after_bearing_temp,huahua_temp,power):
        self.id=id
        self.time=time
        self.before_tem=before_bearing_tem
        self.after_tem=after_bearing_temp
        self.huahuan_tem=huahua_temp
        self.power=power


path="C:/Users/zlt/Desktop/刘梦/曲线图制作/附件1：大幕山风电场24号机组发电机温度数据.xls"
#读取excel表格
work_book = xlrd.open_workbook(path)
sheet=work_book.sheet_by_name("Sheet")
row_num=sheet.nrows
#创建generator温度对象的列表
generator_list=[]
for i in range(row_num):
    if i==0:
        pass
    else:
        id=i
        time,before_bearing_tem,after_bearing_temp,huahua_temp,power=sheet.row_values(i)
        time=xlrd.xldate.xldate_as_datetime(time,0)
        before_bearing_tem=round(before_bearing_tem,2)
        after_bearing_temp=round(after_bearing_temp,2)
        huahua_temp=round(huahua_temp,2)
        power=round(power,2)
        g=generator_temperature_class(id,time,before_bearing_tem,after_bearing_temp,huahua_temp,power)
        generator_list.append(g)


x=list()
y=list()

for i in range(1000,1010):
    x.append(generator_list[i].time)
    y.append(generator_list[i].before_tem)

plt.plot(x, y)
plt.show()
