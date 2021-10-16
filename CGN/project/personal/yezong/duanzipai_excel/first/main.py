from tkinter import *
from pyautocad import Autocad
import winreg
import xlwt
#创建cad读取信息类
class cad_reader():
    def __init__(self,acad=None):
        self.cad_info=[]
        self.acad = acad
        #初步提取信息
        self.read_cad()

    def read_cad(self):
        #原始电缆信息
        self.raw_cable_info=[]
        #原始位置信息
        self.raw_loc_info=[]
        #剩余的信息
        self.raw_rest_info=[]
        for obj in self.acad.iter_objects("Text"):
            obj_x=round(obj.InsertionPoint[0],2)
            obj_y=round(obj.InsertionPoint[1],2)
            obj_name=obj.TextString
            obj_h=obj.Height
            list1=[obj_x,obj_y,obj_name,obj_h]
            if "CAC" in obj_name or "CAM" in obj_name:
                self.raw_cable_info.append(list1)
            elif "LOC" in obj_name and "BLOCK" not in obj_name:
                self.raw_loc_info.append(list1)
            elif "{" in obj_name:
                obj_name=obj_name.split(";")[1][:-1]
                list1=[obj_x,obj_y,obj_name,obj_h]
                self.raw_rest_info.append(list1)
            else:
                self.raw_rest_info.append(list1)
        self.cad_info.append(self.raw_cable_info)
        self.cad_info.append(self.raw_loc_info)
        self.cad_info.append(self.raw_rest_info)
#创建cad信息处理类
class cad_info_processor():
    def __init__(self,info=None):
        self.excel_info=[]
        self.raw_cable_info=info[0]
        self.raw_loc_info=info[1]
        self.raw_rest_info=info[2]
        #提取电缆名
        self.cable_info=self.process_cable()
        #进一步处理电缆信息
        self.process_detail_cable()
        #处理loc信号，将其分为左侧loc和右侧loc
        self.process_loc_info()
        #将loc信息和周围的信息结合起来
        self.loc_info=self.process_loc_rest()
        #处理电缆中间信息
        self.middle_cable_info=self.process_middle_cable_info()
        self.process_excel_info()
    #处理电缆信息
    def process_cable(self):
        raw_cable_info=self.raw_cable_info
        temp_cable_info=set()
        #生成电缆位置信息
        for i in raw_cable_info:
            temp_cable_info.add(i[2])
        #将电缆名称收集，方便后续信息填用
        cable_info=list(temp_cable_info)
        return cable_info
    #更进一步处理电缆信息，将电缆分为左右两侧电缆，然后排序
    def process_detail_cable(self):
        self.cable_location_info=dict()
        for i in self.cable_info:
            self.cable_location_info[i]=[]
            for j in self.raw_cable_info:
                if i==j[2]:
                    self.cable_location_info[i].append(j[0])
                    self.cable_location_info[i].append(j[1])
        self.zuo_cable_location_info = []
        self.you_cable_location_info = []
        for k in self.cable_location_info.keys():
            x1 = self.cable_location_info[k][0]
            x2 = self.cable_location_info[k][2]
            y = self.cable_location_info[k][1]
            list1 = [k, x1, y]
            list2 = [k, x2, y]
            if x1 < x2:
                self.zuo_cable_location_info.append(list1)
                self.you_cable_location_info.append(list2)
            else:
                self.zuo_cable_location_info.append(list2)
                self.you_cable_location_info.append(list1)
    #处理loc信号，将其分为左侧loc和右侧loc,并将电缆和loc信息联合
    def process_loc_info(self):
        self.zuo_cable_loc_info=dict()
        self.you_cable_loc_info=dict()
        for i in self.zuo_cable_location_info:
            i_x=i[1]
            i_y=i[2]
            i_name=i[0]
            self.zuo_cable_loc_info[i_name]=[i_y]
            for j in self.raw_loc_info:
                if i_x-80<j[0]<i_x:
                    list1=[j[1],j[2],j]
                    self.zuo_cable_loc_info[i_name].append(list1)
        for i in self.you_cable_location_info:
            i_x=i[1]
            i_y=i[2]
            i_name=i[0]
            self.you_cable_loc_info[i_name]=[i_y]
            for j in self.raw_loc_info:
                if i_x<j[0]<i_x+100:
                    list1 = [j[1], j[2],j]
                    self.you_cable_loc_info[i_name].append(list1)

        for i in self.zuo_cable_loc_info.keys():
            y=self.zuo_cable_loc_info[i][0]
            rest=self.zuo_cable_loc_info[i][1:]
            temp=[]
            compare_y=[]
            if len(rest)==1:
                pass
            else:
                for j in rest:
                    temp.append(j[0])
            temp.sort()
            for j in temp:
                if j>y:
                    compare_y.append(j)
            if compare_y==[]:
                pass
            else:
                for k in rest:
                    if compare_y[0]==k[0]:
                        list1=[y,k]
                        self.zuo_cable_loc_info[i]=list1
        for i in self.you_cable_loc_info.keys():
            y=self.you_cable_loc_info[i][0]
            rest=self.you_cable_loc_info[i][1:]
            temp=[]
            compare_y=[]
            if len(rest)==1:
                pass
            else:
                for j in rest:
                    temp.append(j[0])
            temp.sort()
            for j in temp:
                if j>y:
                    compare_y.append(j)
            if compare_y==[]:
                pass
            else:
                for k in rest:
                    if compare_y[0]==k[0]:
                        list1=[y,k]
                        self.you_cable_loc_info[i]=list1
        # for k,v in self.zuo_cable_loc_info.items():
        #     print(k,v)
        # print("-------------------------------------")
        # for k,v in self.you_cable_loc_info.items():
        #     print(k,v)
    #处理位置信息，将位置周围的信息填在一起
    def process_loc_rest(self):
        loc_info=[]
        for i in self.raw_loc_info:
            temp_loc_info1=[]
            temp_loc_info2=[]
            i_x=i[0]
            i_y=i[1]
            i_h=i[3]
            temp=[]
            temp.append(i)
            for j in self.raw_rest_info:
                if i_x-i_h<j[0]<i_x+i_h and i_y-5*i_h<j[1]<i_y+3*i_h:
                    temp_loc_info1.append(j[2])
                elif i_y+3.5*i_h<j[1]<i_y+8*i_h and i_x-10*i_h<j[0]<i_x+10*i_h:
                    temp_loc_info2.append(j[2])
                else:
                    pass
            temp=temp+temp_loc_info1+temp_loc_info2
            loc_info.append(temp)
        return loc_info
    #处理电缆中间信息
    def process_middle_cable_info(self):
        info=dict()

        for j in self.cable_location_info.keys():
            info[j]=[]
            x1=self.cable_location_info[j][0]
            x2=self.cable_location_info[j][2]
            y=self.cable_location_info[j][1]
            if x1>x2:
                x1,x2=x2,x1
            for i in self.raw_rest_info:
                if x1+5<i[0]<x2-5 and y-5<i[1]<y+7.5:
                    info[j].append(i[2])

        for k,v in info.items():
            for j in v:
                if "C" in v[0] or "M" in v[0]:
                    pass
                else:
                    v[0],v[1]=v[1],v[0]
        # for k,v in info.items():
        #     print(k,v)
        return info
    #已经将所有信息提取，生成相关excel数据
    def process_excel_info(self):
        self.cable_info.sort()
        cac=[]
        cam=[]
        for i in self.cable_info:
            if "CAC" in i:
                cac.append(i)
            else:
                cam.append(i)
        self.cable_info=cac+cam
        #将电缆名称输入excel——info里
        for i in self.cable_info:
            list1=[i]
            self.excel_info.append(list1)
        #根据loc信息，找相关rest信息
        for i in self.zuo_cable_loc_info.keys():
            for j in self.loc_info:
                if self.zuo_cable_loc_info[i][1][2]==j[0]:
                    self.zuo_cable_loc_info[i].append(j[1:])
        for i in self.you_cable_loc_info.keys():
            for j in self.loc_info:
                if self.you_cable_loc_info[i][1][2]==j[0]:
                    self.you_cable_loc_info[i].append(j[1:])
        #根据电缆信息，连接相关信息
        for i in self.excel_info:
            cable_name=i[0]
            for j in self.zuo_cable_loc_info.keys():
                if cable_name==j:
                    i.append(self.zuo_cable_loc_info[j][1][1][4:])
                    for k in self.zuo_cable_loc_info[j][2]:
                        if "TB" in k:
                            i.append(k)
                        elif "TR" in k and "TRA" not in k:
                            i.append(k)
                        else:
                            pass
            for j in self.you_cable_loc_info.keys():
                if cable_name==j:
                    i.append(self.you_cable_loc_info[j][1][1][4:])
                    for k in self.you_cable_loc_info[j][2]:
                        if "AR" in k:
                            i.append(k)
                        elif "TB" in k:
                            i.append(k)
                        elif "TR" in k and "TRA" not in k:
                            i.append(k)
            for j in self.middle_cable_info.keys():
                if cable_name==j:
                    i.append(self.middle_cable_info[j][0])
                    i.append(self.middle_cable_info[j][1][:2])
                    i.append(self.middle_cable_info[j][1][3])
                    i.append(self.middle_cable_info[j][1][5:7])

        # print(self.excel_info)

#创建excel生成器
class excel_writer():
    def __init__(self,info=None):
        self.info=info
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('电缆信息')
        worksheet.write(0, 0, label='电缆名')
        worksheet.write(0, 1, label='起始房间号')
        worksheet.write(0, 2, label='起始设备')
        worksheet.write(0, 3, label='终止房间号')
        worksheet.write(0, 4, label='终止设备')
        worksheet.write(0, 5, label='电缆规格')
        worksheet.write(0, 6, label='鉴定等级')
        worksheet.write(0, 7, label='列别')
        worksheet.write(0, 8, label='颜色')
        worksheet.write(0, 9, label='安全等级')
        self.path=self.get_desktop()
        for i in range(len(info)):
            for j in range(len(info[i])):
                worksheet.write(i+1,j,info[i][j])
            worksheet.write(i+1,len(info[i]),"FC3")
        workbook.save(self.path+'\\cable_test.xls')

    def get_desktop(self):

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', )

        return winreg.QueryValueEx(key, "Desktop")[0]

"""
生成excel文件
1、读取cad文件，从中提取相关信息
形成文件格式
[cable_info,loc_info,rest_info]
cable_info 将两端电缆和中间的信息包含
loc_info 以loc为中心，上下的信息都要包含
rest_info就是剩下的信息
2、分析相关信息，将电缆的各类信息拼接成一个整体，1行
3、写入cad
"""

def create_excel():
    acad=Autocad(create_if_not_exists=True)
    #读取cad信息
    cad_info=cad_reader(acad=acad).cad_info
    #处理相关的cad信息
    excel_info=cad_info_processor(info=cad_info).excel_info
    #写入excel
    excel_writer(info=excel_info)

#主程序
if __name__=="__main__":
    acad = Autocad(create_if_not_exists=True)
    root=Tk(className="demo1")
    root.geometry("200x200")
    B1=Button(root,text="生成excel", command=lambda: create_excel(), height=1)
    B1.pack(pady=50)
    root.mainloop()