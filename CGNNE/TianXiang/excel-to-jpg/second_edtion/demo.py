from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
import xlwt
import xlrd
from tkinter import *
from tkinter.filedialog import askopenfilename,askdirectory


class Excel_file(object):
    def __init__(self,path=None,target_sheetname=None):
        self.path=path
        self.target_sheetname=target_sheetname
        self.workbook=xlrd.open_workbook(self.path,encoding_override='utf-8')
        self.sheetnames=self.get_sheet_names()
        self.sheet_num=self.get_sheet_num()
        #需要分析的指定sheet
        self.target_sheet=self.get_target_sheet()
        #获得文件的第一行值
        self.first_row=self.get_target_sheet_first_row()
        #excel表中风电场的列表
        self.fengdianchang_list=self.get_fengdianchang_list()
        #excel 表中风电场的机组数
        self.jizushu_dict=self.get_jizushu_dict()
        #excel 表中故障停机次数
        self.guzhangcishu_dict=self.get_guzhangcishu_dict()
        #计算获得MTBF值
        self.MTBF_dict=self.get_MTBF_dict()
        #统计故障停机时间
        self.guzhangtingji_dict=self.get_guzhangtingji_dict()
        #计算获得MTTR值
        self.MTTR_dict=self.get_MTTR_dict()
        #计算获得TBA值
        self.TBA_dict=self.get_TBA_dict()
        #风机容量
        self.fengjirongliang_dict={'敖家山风电场':70,'柏杨坝风电场':50,'大幕山风电场': 58, '大坡顶风电场': 96, '富池风电场': 34, '寒池风电场': 70, '擂鼓台风电场': 84, '寿山风电场': 36, '五岳山风电场': 120, '仙舞山风电场': 60, '宣化风电场': 66, '余店风电场': 62, '元堡风电场':50, '朝阳山风电场': 24}
        #单位容量故障次数
        self.danwenrongliangguzhangcishu_dict=self.get_danweirongliangguzhangcishu_dict()
        #总的经济损失
        self.jingjisunsi_dict=self.get_jingjisunshi_dict()
        #单位经济损失
        self.danweijingjisunshi_dict=self.get_danweijingjisunshi_dict()

     #获取sheet的列表名称
    def get_sheet_names(self):
        return self.workbook.sheet_names()

    #获取sheet的总数
    def get_sheet_num(self):
        return self.workbook.nsheets

    #获取特定的sheet,如果不指定名称，就获得sheet名称含故障汇总的sheet，否则，获得指定名称的sheet
    def get_target_sheet(self):
        if self.target_sheetname==None:
            for i in self.sheetnames:
                if "故障汇总" in i:
                    return self.workbook.sheet_by_name(i)
        else:
            return self.workbook.sheet_by_name(self.target_sheetname)

    #获取sheet的第一行，确认各类指标
    def get_target_sheet_first_row(self):
        return list(self.target_sheet.row_values(0))

    #获取sheet的某一列数值，从第2行开始至最后一行
    def get_target_sheet_col(self,col_num):
        return self.target_sheet.col_values(col_num,start_rowx=1)
    #获取sheet的某一行数值
    def get_target_sheet_row(self,row_num):
        return self.target_sheet.row_values(row_num)

    #获取风电场列表，读取风电场一列，取set，得到相应列表
    def get_fengdianchang_list(self):
        fengdianchang_col_num=self.first_row.index('风电场')
        fengdianchang_col=self.get_target_sheet_col(fengdianchang_col_num)
        fengdianchang_set=set(fengdianchang_col)
        fengdianchang_set.remove('')
        fengdianchang_list=list(fengdianchang_set)
        return fengdianchang_list

    #获取风电场的机组数，读取风电场列和机组数量,将二者一一对应，形成字典
    def get_jizushu_dict(self):
        jizushu_dict=dict()
        fengdianchang_col_num = self.first_row.index('风电场')
        jizushu_col_num = self.first_row.index('机组总数')
        fengdianchang_col=self.get_target_sheet_col(fengdianchang_col_num)
        jizushu_col=self.get_target_sheet_col(jizushu_col_num)
        for i in range(len(fengdianchang_col)):
            if fengdianchang_col[i]=='':
                pass
            else:
                jizushu_dict[fengdianchang_col[i]]=jizushu_col[i]
        return jizushu_dict

    #统计故障停机次数，还是读取风电场和信息类型这两列
    def get_guzhangcishu_dict(self):
        guzhangcishu_dict=dict()
        #生成风电场故障次数字典，起始值为0
        for fengdianchang in self.fengdianchang_list:
            guzhangcishu_dict[fengdianchang]=0
        fengdianchang_col_num = self.first_row.index('风电场')
        xinxileixing_col_num = self.first_row.index('信息类型')
        fengdianchang_col = self.get_target_sheet_col(fengdianchang_col_num)
        xinxileixing_col = self.get_target_sheet_col(xinxileixing_col_num)
        #再进行遍历，如果信息类型为故障停机，则相应风电场故障次数加1
        for i in range(len(xinxileixing_col)):
            if xinxileixing_col[i]=="故障停机":
                guzhangcishu_dict[fengdianchang_col[i]]+=1
        return guzhangcishu_dict

    #计算MTBF值,根据相应公式计算
    def get_MTBF_dict(self):
        MTBF_dict=dict()
        for k,v in self.guzhangcishu_dict.items():
            if v==0:
                MTBF_dict[k]=30*24*self.jizushu_dict[k]
            else:
                MTBF_dict[k]=round(30*24*self.jizushu_dict[k]/self.guzhangcishu_dict[k],1)
        return MTBF_dict

    #统计故障停机总时间，读取风电场、信息类型、故障报出时间、复位运行时间四列，计算复位运行时间减去故障报出时间，相应加到对应风电场上
    def get_guzhangtingji_dict(self):
        guzhangtingji_dict = dict()
        # 生成风电场故障停机时间字典，起始值为0
        for fengdianchang in self.fengdianchang_list:
            guzhangtingji_dict[fengdianchang] = 0
        fengdianchang_col_num = self.first_row.index('风电场')
        xinxileixing_col_num = self.first_row.index('信息类型')
        guzhangbaochushijian_col_num=self.first_row.index('故障报出时间')
        fuweiyunxingshijian_col_num=self.first_row.index('复位运行时间')
        fengdianchang_col = self.get_target_sheet_col(fengdianchang_col_num)
        xinxileixing_col = self.get_target_sheet_col(xinxileixing_col_num)
        guzhangbaochushijian_col=self.get_target_sheet_col(guzhangbaochushijian_col_num)
        fuweiyunxingshijian_col=self.get_target_sheet_col(fuweiyunxingshijian_col_num)
        #首先判断，是否是故障停机，然后将数字量转化为日期量,若是''，则pass掉,生成两个变量用于计算
        start=None
        end=None
        each_time_list=[]
        for i in range(len(xinxileixing_col)):
            if xinxileixing_col[i]=="故障停机":
                if guzhangbaochushijian_col[i]=='':
                    start=0
                else:
                    time1 = xlrd.xldate_as_tuple(guzhangbaochushijian_col[i], 0)
                    time2 = datetime(*time1).strftime('%Y/%m/%d %H:%M:%S')
                    start=datetime.strptime(time2,'%Y/%m/%d %H:%M:%S')
                time3=xlrd.xldate_as_tuple(fuweiyunxingshijian_col[i], 0)
                time4=datetime(*time3).strftime('%Y/%m/%d %H:%M:%S')
                end=datetime.strptime(time4,'%Y/%m/%d %H:%M:%S')
                if start==0:
                    each_time=0
                else:
                    each_time = (end - start).total_seconds()
                guzhangtingji_dict[fengdianchang_col[i]]+=each_time
        for k,v in guzhangtingji_dict.items():
            guzhangtingji_dict[k]=round(v/3600,1)

        return guzhangtingji_dict

    #计算MTTR，故障总时间除以故障次数
    def get_MTTR_dict(self):
        MTTR_dict=dict()
        for k,v in self.guzhangtingji_dict.items():
            if self.guzhangcishu_dict[k]==0:
                MTTR_dict[k]=0
            else:
                MTTR_dict[k]=round(self.guzhangtingji_dict[k]/self.guzhangcishu_dict[k],1)
        return MTTR_dict

    #计算TBA，（30*24*机组数-故障总时间）/30*24*机组数
    def get_TBA_dict(self):
        TBA_dict=dict()
        for k,v in self.jizushu_dict.items():
            demo1= (30*24*self.jizushu_dict[k]-self.guzhangtingji_dict[k])/(30*24*self.jizushu_dict[k])*100
            demo2=round(demo1,2)
            TBA_dict[k]=demo2
        return TBA_dict

    #计算单位容量故障次数
    def get_danweirongliangguzhangcishu_dict(self):
        danweitongliangguzhangcishu_dict=dict()
        for k,v in self.guzhangcishu_dict.items():
            danweitongliangguzhangcishu_dict[k]=self.guzhangcishu_dict[k]/self.fengjirongliang_dict[k]
        return danweitongliangguzhangcishu_dict
    #计算总的容量经济损失,找到风电场和合计（元）两列，进行叠加
    def get_jingjisunshi_dict(self):
        jingjisunshi_dict=dict()
        # 生成风电场故障次数字典，起始值为0
        for fengdianchang in self.fengdianchang_list:
            jingjisunshi_dict[fengdianchang] = 0
        fengdianchang_col_num = self.first_row.index('风电场')
        xinxileixing_col_num = self.first_row.index('信息类型')
        heji_col_num = self.first_row.index('合计\n（元）')
        fengdianchang_col = self.get_target_sheet_col(fengdianchang_col_num)
        xinxileixing_col = self.get_target_sheet_col(xinxileixing_col_num)
        heji_col = self.get_target_sheet_col(heji_col_num)
        for i in range(len(xinxileixing_col)):
            if xinxileixing_col[i]=="故障停机":
                if heji_col[i]=='':
                    jingjisunshi_dict[fengdianchang_col[i]]+=0
                else:
                    jingjisunshi_dict[fengdianchang_col[i]]+=heji_col[i]
        return jingjisunshi_dict
    #计算单位经济损失
    def get_danweijingjisunshi_dict(self):
        danweijingjisunshi_dict=dict()
        for k,v in self.jingjisunsi_dict.items():
            danweijingjisunshi_dict[k]=self.jingjisunsi_dict[k]/self.fengjirongliang_dict[k]
        return danweijingjisunshi_dict

def Write_Excel_file(path=None, fengdianchang_list=None, MTBF=None, MTTR=None, TBA=None, guzhangcishu=None,
                         jingjisunshi=None):

        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('计算数据')
        worksheet.write(0, 0, '序号')
        worksheet.write(0, 1, '风电场')
        worksheet.write(0, 2, 'MTBF')
        worksheet.write(0, 3, 'MTTR')
        worksheet.write(0, 4, 'TBA')
        worksheet.write(0, 5, '单位容量故障次数')
        worksheet.write(0, 6, '单位容量经济损失')
        for i in range(1, len(fengdianchang_list) + 1):
            worksheet.write(i, 0, i)
            worksheet.write(i, 1, fengdianchang_list[i - 1])
            worksheet.write(i, 2, MTBF[fengdianchang_list[i - 1]])
            worksheet.write(i, 3, MTTR[fengdianchang_list[i - 1]])
            worksheet.write(i, 4, TBA[fengdianchang_list[i - 1]])
            worksheet.write(i, 5, guzhangcishu[fengdianchang_list[i - 1]])
            worksheet.write(i, 6, jingjisunshi[fengdianchang_list[i - 1]])

        workbook.save(path + "/demo.xls")

def huazhuxingtu(target_dict):
    target_dict=target_dict
    chanzhan_list=target_dict.keys()
    shuzhi_list=list(target_dict.values())
    y_shuzhi_list=[]
    process_changzhan_list = []

    #
    for i in chanzhan_list:
        i=i[:-3]
        process_changzhan_list.append(i)

    for i in shuzhi_list:
        y_shuzhi_list.append(i)

    matplotlib.rcParams["font.sans-serif"] = ["SimHei"]
    matplotlib.rcParams["axes.unicode_minus"] = False

    # 创建图表的基础
    plt.figure(figsize=(12, 4))

    # 限定y坐标的取值范围
    y_shuzhi_list.sort()

    plt.ylim((y_shuzhi_list[0], y_shuzhi_list[-1]))

    plt.xticks(range(len(chanzhan_list)), process_changzhan_list, rotation=0)

    # 画柱形图
    plt.bar(chanzhan_list, shuzhi_list, width=0.4, color='dodgerblue')

    # 展示图形
    plt.show()

class input_file_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.path1 = StringVar()
        self.filepath=None
        self.target_dict=None
        L1 = Label(self, text="输入文件:")
        L1.grid(row=0, column=0,pady=30,padx=20)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=0, column=1,pady=30)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath(self.path1), height=1)
        B1.grid(row=0, column=2, padx=10,pady=30)
        B2 = Button(self, text="生成Excel文件", command=lambda: self.read_excel(), height=1)
        B2.grid(row=1, column=0, padx=5,pady=0)
        B3 = Button(self, text="生成MTBF表", command=lambda: self.draw_MTBF_picture(), height=1)
        B3.grid(row=1, column=1, padx=5, pady=0)
        B4 = Button(self, text="生成MTTR表", command=lambda: self.draw_MTTR_picture(), height=1)
        B4.grid(row=1, column=2, padx=5, pady=0)
        B5 = Button(self, text="生成TBA表", command=lambda: self.draw_TBA_picture(), height=1)
        B5.grid(row=2, column=0, padx=5, pady=10)
        B6 = Button(self, text="生成单位容量故障次数表", command=lambda: self.draw_guzhangcishu_picture(), height=1)
        B6.grid(row=2, column=1, padx=5, pady=10)
        B7 = Button(self, text="生成单位容量经济损失表", command=lambda: self.draw_jingjisunshi_picture(), height=1)
        B7.grid(row=2, column=2, padx=5, pady=10)

    def selectPath(self,path1):
        path_ = askopenfilename()
        path1.set(path_)
        self.filepath=path_

    def read_excel(self):
        e=Excel_file(self.filepath)
        path1=askdirectory()
        print(path1)
        Write_Excel_file(path1, e.fengdianchang_list, e.MTBF_dict, e.MTTR_dict, e.TBA_dict,
                         e.danwenrongliangguzhangcishu_dict, e.danweijingjisunshi_dict)

    def draw_picture(self):

        huazhuxingtu(self.target_dict)

    def draw_MTBF_picture(self):
        e = Excel_file(self.filepath)
        self.target_dict=e.MTBF_dict
        self.draw_picture()

    def draw_MTTR_picture(self):
        e = Excel_file(self.filepath)
        self.target_dict = e.MTTR_dict
        self.draw_picture()

    def draw_TBA_picture(self):
        e = Excel_file(self.filepath)
        self.target_dict = e.TBA_dict
        self.draw_picture()

    def draw_guzhangcishu_picture(self):
        e = Excel_file(self.filepath)
        self.target_dict = e.danwenrongliangguzhangcishu_dict
        self.draw_picture()

    def draw_jingjisunshi_picture(self):
        e = Excel_file(self.filepath)
        self.target_dict = e.danweijingjisunshi_dict
        self.draw_picture()

root=Tk(className="Excel文件处理")
root.geometry("500x200")

if_frame=input_file_frame(root)
if_frame.pack()

root.mainloop()


