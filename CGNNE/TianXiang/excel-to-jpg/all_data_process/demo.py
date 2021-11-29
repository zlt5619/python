from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
import xlwt
import xlrd
from tkinter import *
from tkinter.filedialog import askopenfilename,askdirectory

class Data(object):
    def __init__(self,fengongsi_list=None,fengdianchang_list=None,fengongsi_fengdianchang_dict=None,
                 fengdianchang_jizutaishu_dict=None,
                 fengdianchang_xinxileixing_dict=None,
                 tingjishijian_dict=None,
                 fengdianchang_rongliang_dict=None,
                 jingjisunshi_dict=None):
        self.fengongsi_list=fengongsi_list
        self.fengdianchang_list=fengdianchang_list
        self.fengongsi_fengdianchang_dict=fengongsi_fengdianchang_dict
        self.fengdianchang_jizutaishu_dict=fengdianchang_jizutaishu_dict
        self.fengdianchang_xinxileixing_dict=fengdianchang_xinxileixing_dict
        self.tingjishijian_dict=tingjishijian_dict
        self.fengdianchang_rongliang_dict=fengdianchang_rongliang_dict
        self.jingjisunshi_dict=jingjisunshi_dict

class processOneList(object):
    def __init__(self, input_list=None):
        self.input_list = input_list
        self.only_list = None
        self.get_only_list()
        self.list_cishu = dict()

    def get_only_list(self):
        self.only_list = list(set(self.input_list))
        if '' in self.only_list:
            self.only_list.remove('')

    def get_list_cishu(self):
        for i in self.only_list:
            self.list_cishu[i] = 0
        for i in self.input_list:
            for j in self.only_list:
                if i == j:
                    self.list_cishu[j] += 1

class processTwoList(object):
    def __init__(self,list1=None,list2=None):
        self.list1=list1
        self.list2=list2
        self.list1_key=processOneList(input_list=list1).only_list
        self.list2_key=processOneList(input_list=list2).only_list
        self.yiduiduo_dict=dict()
        self.duoduiyi_dict=dict()
        self.duoduiyi_tongjicishu_dict=dict()


    def compareListLen(self):
        if len(self.list1_key)<=len(self.list2_key):
            self.short_list_key=self.list1_key
            self.long_list_key=self.list2_key
            self.short_list=self.list1
            self.long_list=self.list2
        else:
            self.short_list_key = self.list2_key
            self.long_list_key = self.list1_key
            self.short_list = self.list2
            self.long_list = self.list1

    #值少的一列，作为key，值多的一列，作为value
    def get_yiduiduo_dict(self):
        self.compareListLen()
        #首先创建字典，每个value为空列表
        for i in self.short_list_key:
            self.yiduiduo_dict[i]=[]

        for i in range(len(self.short_list)):
            for j in self.short_list_key:
                if j==self.short_list[i]:
                    self.yiduiduo_dict[j].append(self.long_list[i])
        for i in self.yiduiduo_dict.keys():
            self.yiduiduo_dict[i]=list(set(self.yiduiduo_dict[i]))

    #值多的一列，作为key，值少的一列，作为value
    def get_duoduiyi_dict(self):
        self.compareListLen()
        for i in self.long_list_key:
            self.duoduiyi_dict[i]=None
        for i in range(len(self.long_list)):
            for j in self.long_list_key:
                if j==self.long_list[i]:
                    self.duoduiyi_dict[j]=self.short_list[i]

    #若值多的一列，作为key，值少的一列，作为value，统计每个value出现的次数
    def get_duoduiyi_tongjicishu_dict(self):
        self.compareListLen()
        short_list_value_dict = dict()
        for l in self.short_list_key:
            short_list_value_dict[l] = 0
        for j in self.long_list_key:
            self.duoduiyi_tongjicishu_dict[j] = short_list_value_dict.copy()
        for i in range(len(self.long_list)):
            for j in self.long_list_key:
                if j==self.long_list[i]:
                    for k in self.short_list_key:
                        if k==self.short_list[i]:
                            self.duoduiyi_tongjicishu_dict[j][k]+=1

class processThreeList(object):
    def __init__(self,list1=None,list2=None,list3=None):
        self.list1=list1
        self.list2=list2
        self.list3=list3
        self.list1_key = processOneList(self.list1).only_list
        self.list2_key = processOneList(self.list2).only_list
        self.tingjileixing_dict = dict()
        for i in self.list2_key:
            self.tingjileixing_dict[i]=0.0
        self.jingjisunshi_dict = dict()
        self.process()

    def process(self):
        for i in self.list1_key:
            self.jingjisunshi_dict[i]=self.tingjileixing_dict.copy()
        for i in range(len(self.list1)):
            for j in self.list1_key:
                if j==self.list1[i]:
                    for k in self.list2_key:
                        if k==self.list2[i]:
                            if self.list3[i]=='':
                                value=0
                            elif self.list3[i]=='无':
                                value=0
                            elif self.list3[i]=='/':
                                value=0
                            else:
                                value=self.list3[i]
                            self.jingjisunshi_dict[j][k]+=value

class processTime(object):
    def __init__(self,time1,time2):
        self.time1=time1
        self.time2=time2

    def process(self):
        if self.time1=="":
            time=0
            return time
        else:
            time1=xlrd.xldate_as_tuple(self.time1, 0)
            time2 = datetime(*time1).strftime('%Y/%m/%d %H:%M:%S')
            start = datetime.strptime(time2, '%Y/%m/%d %H:%M:%S')
            time3 = xlrd.xldate_as_tuple(self.time2, 0)
            time4 = datetime(*time3).strftime('%Y/%m/%d %H:%M:%S')
            end = datetime.strptime(time4, '%Y/%m/%d %H:%M:%S')
            time=(end-start).total_seconds()
            return time

class processFourList(object):
    def __init__(self,list1=None,list2=None,list3=None,list4=None):
        self.list1=list1
        self.list2=list2
        self.list3=list3
        self.list4=list4
        self.list1_key=processOneList(self.list1).only_list
        self.list2_key=processOneList(self.list2).only_list
        self.tingjileixing_dict=dict()
        self.tingjishijian_dict=dict()
        for i in self.list2_key:
            self.tingjileixing_dict[i]=0
        for i in self.list1_key:
            self.tingjishijian_dict[i]=self.tingjileixing_dict.copy()

    def get_tingjishijian_dict(self):
        for i in range(len(self.list1)):
            for j in self.list1_key:
                if self.list1[i]==j:
                    for k in self.list2_key:
                        if k==self.list2[i]:
                            time=processTime(self.list3[i],self.list4[i]).process()
                            self.tingjishijian_dict[j][k]+=time

class mplt(object):
    def __init__(self,y_list=None,x_list=None,leixing=None):
        self.y_list=y_list
        self.x_list=x_list
        self.leixing=leixing
        matplotlib.rcParams["font.sans-serif"] = ["SimHei"]
        matplotlib.rcParams["axes.unicode_minus"] = False
        plt.figure(figsize=(len(x_list)*0.8, 5))
        rect1=plt.bar(self.x_list,self.y_list,width=0.3)
        for rect in rect1:
            height = rect.get_height()  # 获取⾼度
            if height>1:
                text_height=int(height)
            else:
                text_height="%.2f%%" % (height * 100)
            plt.text(x=rect.get_x() + rect.get_width() / 2,  # ⽔平坐标
                     y=height,  # 竖直坐标
                     s=text_height,  # ⽂本
                     ha='center')  # ⽔平居中
        plt.xticks(range(len(x_list)), x_list,rotation=30,fontsize=8)
        plt.xlabel("风电场名称")
        plt.title(self.leixing+"图表")
        plt.show()

class Excel_file(object):
    def __init__(self,path):
        #输入参数
        self.path=path
        #开始读取excel表格
        self.workbook = xlrd.open_workbook(self.path, encoding_override='utf-8')

        #获取excel表格sheet的相关参数
        self.sheet_names = self.get_sheet_names()
        self.sheet_num = self.get_sheet_num()

        # 执行get_target_sheet方法后，获得target_sheet
        self.target_sheet=None
        self.target_sheet_rows=None
        self.target_sheet_cols=None

        #执行方法，获取分类第一排的列表
        self.first_row_num=0
        self.first_row_list = None

        #执行方法，获取相应的列的值
        self.target_sheet_col_names=None
        self.target_sheet_col_value_list=None

        #执行方法，获取相应的行的值
        self.target_row_value_list=None


    #获取excel表格全部sheets的列表
    def get_sheet_names(self):
        return self.workbook.sheet_names()

    #获取excel表格全部sheets的数量
    def get_sheet_num(self):
        return self.workbook.nsheets

    #获取excel表格中指定的sheet
    def get_target_sheet(self,target_sheet_name=None):
        sheet_name=target_sheet_name
        #如果输入sheet名称在excel文件sheet里面，则直接选择该sheet
        for i in self.sheet_names:
            if sheet_name == i:
                self.target_sheet=self.workbook.sheet_by_name(sheet_name)
            elif sheet_name in i:
                self.target_sheet=self.workbook.sheet_names(i)
            else:
                pass
        self.target_sheet_rows=self.target_sheet.nrows
        self.target_sheet_cols=self.target_sheet.ncols

    #获取sheet中真正意义上的第一排数据
    #默认读取第一行数据
    def get_first_row_list(self,first_row_num=1):
        self.first_row_num=first_row_num-1
        self.first_row_list=list(self.target_sheet.row_values(self.first_row_num))
        self.target_sheet_col_names=self.first_row_list

    #获取sheet中的指定列的值，从目标行往下，一直到最后一列
    def get_target_sheet_col_list(self,col_name=None):
        self.target_sheet_col_name=col_name
        for i in self.first_row_list:
            if col_name in i:
                self.target_sheet_col_num=self.first_row_list.index(i)
        self.target_sheet_col_value_list=list(self.target_sheet.col_values(self.target_sheet_col_num, start_rowx=self.first_row_num+1))

    #获取sheet中的指定行的值，每一行的所有值都获取
    def get_target_sheet_row_list(self,row_num):
        row_num=row_num-1
        self.target_row_value_list=list(self.target_sheet.row_values(row_num))

class HuatuFrame(Frame):
    def __init__(self,root=None,name=None,data=None):
        super().__init__(root)
        self.name=name
        self.data=data
        b1=Button(self,text="MTBF",command=lambda :self.huaMTBF())
        b1.grid(row=0,column=0,pady=20)
        b2 = Button(self, text="MTTR", command=lambda: self.huaMTTR())
        b2.grid(row=0,column=3,pady=20)
        b3 = Button(self, text="TBA", command=lambda: self.huaTBA())
        b3.grid(row=0,column=6,pady=20)
        b4 = Button(self, text="单位容量故障次数", command=lambda: self.huaGuzhang())
        b4.grid(row=1,column=0,columnspan=3,padx=5,pady=20)
        b5 = Button(self, text="单位容量经济损失", command=lambda: self.huaJingji())
        b5.grid(row=1,column=4,columnspan=3,padx=5,pady=20)

    def huaMTBF(self):
        fengongsi_fengchang_list=self.data.fengongsi_fengdianchang_dict[self.name]
        jizutaishu_list=[]
        guzhangcishu_list=[]
        MTBF_List=[]
        for i in fengongsi_fengchang_list:
            jizutaishu_list.append(self.data.fengdianchang_jizutaishu_dict[i])
            guzhangcishu_list.append(self.data.fengdianchang_xinxileixing_dict[i]['故障停机'])
        for i in range(len(jizutaishu_list)):
            if guzhangcishu_list[i]==0:
                MTBF_List.append(0.0)
            else:
                MTBF_List.append(30*24*jizutaishu_list[i]/guzhangcishu_list[i])
        M=mplt(y_list=MTBF_List,x_list=fengongsi_fengchang_list,leixing="MTBF")

    def huaMTTR(self):
        fengongsi_fengchang_list = self.data.fengongsi_fengdianchang_dict[self.name]
        xiufushijian_list=[]
        guzhangcishu_list = []
        MTTR_List=[]
        for i in fengongsi_fengchang_list:
            xiufushijian_list.append(self.data.tingjishijian_dict[i]['故障停机'])
            guzhangcishu_list.append(self.data.fengdianchang_xinxileixing_dict[i]['故障停机'])
        for i in range(len(xiufushijian_list)):
            if guzhangcishu_list[i]==0:
                MTTR_List.append(0.0)
            else:
                MTTR_List.append((xiufushijian_list[i]/3600)/guzhangcishu_list[i])
        M = mplt(y_list=MTTR_List, x_list=fengongsi_fengchang_list,leixing="MTTR")

    def huaTBA(self):
        fengongsi_fengchang_list = self.data.fengongsi_fengdianchang_dict[self.name]
        jizutaishu_list = []
        xiufushijian_list = []
        TBA_List=[]
        for i in fengongsi_fengchang_list:
            xiufushijian_list.append(self.data.tingjishijian_dict[i]['故障停机'])
            jizutaishu_list.append(self.data.fengdianchang_jizutaishu_dict[i])
        for i in range(len(xiufushijian_list)):
            TBA_List.append((30*24*jizutaishu_list[i]-xiufushijian_list[i]/3600)/(30*24*jizutaishu_list[i]))
        M = mplt(y_list=TBA_List, x_list=fengongsi_fengchang_list,leixing="TBA")

    def huaGuzhang(self):
        fengongsi_fengchang_list = self.data.fengongsi_fengdianchang_dict[self.name]
        guzhangcishu_list=[]
        zongrongliang_list=[]
        danweirongliang_guzhangcishu_list=[]
        for i in fengongsi_fengchang_list:
            guzhangcishu_list.append(self.data.fengdianchang_xinxileixing_dict[i]['故障停机'])
            zongrongliang_list.append(self.data.fengdianchang_rongliang_dict[i])
        for i in range(len(guzhangcishu_list)):
            danweirongliang_guzhangcishu_list.append(guzhangcishu_list[i]/zongrongliang_list[i])
        M = mplt(y_list=danweirongliang_guzhangcishu_list, x_list=fengongsi_fengchang_list,leixing="单位容量故障次数")

    def huaJingji(self):
        fengongsi_fengchang_list = self.data.fengongsi_fengdianchang_dict[self.name]
        zongrongliang_list = []
        jingjisunshi_list=[]
        danweirongliang_jingjisunshi_list=[]
        for i in fengongsi_fengchang_list:
            jingjisunshi_list.append(self.data.jingjisunshi_dict[i]['计划性停机']+self.data.jingjisunshi_dict[i]['故障停机'])
            zongrongliang_list.append(self.data.fengdianchang_rongliang_dict[i])
        for i in range(len(zongrongliang_list)):
            danweirongliang_jingjisunshi_list.append(jingjisunshi_list[i]/zongrongliang_list[i])
        M = mplt(y_list=danweirongliang_jingjisunshi_list, x_list=fengongsi_fengchang_list,leixing='单位容量经济损失')

class HuatuFrame2(Frame):
    def __init__(self,root=None,name=None,data=None):
        super().__init__(root)
        self.name=name
        self.data=data
        b1=Button(self,text="MTBF",command=lambda :self.huaMTBF())
        b1.grid(row=0,column=0,pady=20)
        b2 = Button(self, text="MTTR", command=lambda: self.huaMTTR())
        b2.grid(row=0,column=3,pady=20)
        b3 = Button(self, text="TBA", command=lambda: self.huaTBA())
        b3.grid(row=0,column=6,pady=20)
        b4 = Button(self, text="单位容量故障次数", command=lambda: self.huaGuzhang())
        b4.grid(row=1,column=0,columnspan=3,padx=5,pady=20)
        b5 = Button(self, text="单位容量经济损失", command=lambda: self.huaJingji())
        b5.grid(row=1,column=4,columnspan=3,padx=5,pady=20)

    def huaMTBF(self):
        fengongsi_list=self.data.fengongsi_list
        fengongsi_fengdianchang_dict=self.data.fengongsi_fengdianchang_dict
        jizutaishu_list = []
        guzhangcishu_list = []
        MTBF_List = []
        for i in fengongsi_list:
            jizutaishu=0
            guzhangcishu=0
            for j in fengongsi_fengdianchang_dict[i]:
                jizutaishu+=self.data.fengdianchang_jizutaishu_dict[j]
                guzhangcishu+=self.data.fengdianchang_xinxileixing_dict[j]['故障停机']
            jizutaishu_list.append(jizutaishu)
            guzhangcishu_list.append(guzhangcishu)
        for i in range(len(jizutaishu_list)):
            if guzhangcishu_list[i]==0:
                MTBF_List.append(0.0)
            else:
                MTBF_List.append(30*24*jizutaishu_list[i]/guzhangcishu_list[i])
        M = mplt(y_list=MTBF_List, x_list=fengongsi_list, leixing="MTBF")
    def huaMTTR(self):
        fengongsi_list = self.data.fengongsi_list
        fengongsi_fengdianchang_dict = self.data.fengongsi_fengdianchang_dict
        xiufushijian_list = []
        guzhangcishu_list = []
        MTTR_List = []
        for i in fengongsi_list:
            xiufushijian = 0
            guzhangcishu = 0
            for j in fengongsi_fengdianchang_dict[i]:
                xiufushijian+=self.data.tingjishijian_dict[j]['故障停机']
                guzhangcishu+=self.data.fengdianchang_xinxileixing_dict[j]['故障停机']
            xiufushijian_list.append(xiufushijian)
            guzhangcishu_list.append(guzhangcishu)
        for i in range(len(xiufushijian_list)):
            if guzhangcishu_list[i] == 0:
                MTTR_List.append(0.0)
            else:
                MTTR_List.append((xiufushijian_list[i]/3600)/guzhangcishu_list[i])
        M = mplt(y_list=MTTR_List, x_list=fengongsi_list, leixing="MTTR")
    def huaTBA(self):
        fengongsi_list = self.data.fengongsi_list
        fengongsi_fengdianchang_dict = self.data.fengongsi_fengdianchang_dict
        jizutaishu_list = []
        xiufushijian_list = []
        TBA_List = []
        for i in fengongsi_list:
            jizutaishu = 0
            xiufushijian = 0
            for j in fengongsi_fengdianchang_dict[i]:
                xiufushijian+=self.data.tingjishijian_dict[j]['故障停机']
                jizutaishu+=self.data.fengdianchang_jizutaishu_dict[j]
            xiufushijian_list.append(xiufushijian)
            jizutaishu_list.append(jizutaishu)
        for i in range(len(xiufushijian_list)):
            TBA_List.append(
                (30 * 24 * jizutaishu_list[i] - xiufushijian_list[i] / 3600) / (30 * 24 * jizutaishu_list[i]))
        M = mplt(y_list=TBA_List, x_list=fengongsi_list, leixing="TBA")
    def huaGuzhang(self):
        fengongsi_list = self.data.fengongsi_list
        fengongsi_fengdianchang_dict = self.data.fengongsi_fengdianchang_dict
        guzhangcishu_list = []
        zongrongliang_list = []
        danweirongliang_guzhangcishu_list = []
        for i in fengongsi_list:
            guzhangcishu = 0
            zongrongliang = 0
            for j in fengongsi_fengdianchang_dict[i]:
                guzhangcishu+=self.data.fengdianchang_xinxileixing_dict[j]['故障停机']
                zongrongliang+=self.data.fengdianchang_rongliang_dict[j]
            guzhangcishu_list.append(guzhangcishu)
            zongrongliang_list.append(zongrongliang)
        for i in range(len(guzhangcishu_list)):
            danweirongliang_guzhangcishu_list.append(guzhangcishu_list[i]/zongrongliang_list[i])
        M = mplt(y_list=danweirongliang_guzhangcishu_list, x_list=fengongsi_list, leixing="单位容量故障次数")
    def huaJingji(self):
        fengongsi_list = self.data.fengongsi_list
        fengongsi_fengdianchang_dict = self.data.fengongsi_fengdianchang_dict
        zongrongliang_list = []
        jingjisunshi_list = []
        danweirongliang_jingjisunshi_list = []
        for i in fengongsi_list:
            jingjisunshi = 0
            zongrongliang = 0
            for j in fengongsi_fengdianchang_dict[i]:
                jingjisunshi+=(
                    self.data.jingjisunshi_dict[j]['计划性停机'] + self.data.jingjisunshi_dict[j]['故障停机'])
                zongrongliang+=self.data.fengdianchang_rongliang_dict[j]
            jingjisunshi_list.append(jingjisunshi)
            zongrongliang_list.append(zongrongliang)
        for i in range(len(zongrongliang_list)):
            danweirongliang_jingjisunshi_list.append(jingjisunshi_list[i] / zongrongliang_list[i])
        M = mplt(y_list=danweirongliang_jingjisunshi_list, x_list=fengongsi_list, leixing='单位容量经济损失')

class FengongsiFrame(Frame):
    def __init__(self,root=None,data=None,row_num=None):
        super().__init__(root)
        self.data=data
        self.row_num=row_num
        self.fengongsi_list=self.data.fengongsi_list
        b1=Button(self,text="分公司数据统计",command=lambda :self.showFengongsiFrame())
        b1.grid(row=0,column=1,columnspan=2,padx=2,pady=10)
        fengongsi_button_group={"bname":None,"bobj":None}
        self.fengongsi_group=dict()
        for i in range(len(self.fengongsi_list)):
            self.fengongsi_group[self.fengongsi_list[i]]=fengongsi_button_group.copy()
            self.fengongsi_group[self.fengongsi_list[i]]['bname']=self.fengongsi_list[i]
        for i, cb in enumerate(self.fengongsi_group):
            b=Button(self,text=self.fengongsi_group[cb]["bname"],command=lambda arg=cb: self.showNewFrame(arg))
            if int(i/4)==0:
                b.grid(row=int(i/4)+1,column=i%4,padx=2,pady=10)
            else:
                b.grid(row=int(i/4)+1,column=i%4,padx=2,pady=3)
            b['height']=2
            b['width']=10
            self.fengongsi_group[cb]["bobj"] = b

    def showNewFrame(self,bname):
        for i in self.fengongsi_group:
            if bname==i:
                b=self.fengongsi_group[i]['bobj']
                name=b.cget('text')
        data=self.data
        root3 = Tk(className=name+"数据图表显示")
        root3.geometry("400x200")
        huatu_frame = HuatuFrame(root3,name=name,data=data)
        huatu_frame.pack()
        root3.mainloop()

    def showFengongsiFrame(self):
        data=self.data
        root4=Tk(className="分公司数据图表显示")
        root4.geometry("400x200")
        huatu_frame = HuatuFrame2(root4, data=data)
        huatu_frame.pack()
        root4.mainloop()

class MainFrame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.path1 = StringVar()
        self.filepath = None
        L1 = Label(self, text="输入文件:")
        L1.grid(row=0, column=0, pady=30)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=0, column=1, pady=30)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath(self.path1), height=1)
        B1.grid(row=0, column=2, padx=10, pady=30)
        B2= Button(self, text="Excel文件处理", command=lambda: self.processExcelFile(), height=1)
        B2.grid(row=1, column=1, padx=10)

    def selectPath(self,path1):
        path_ = askopenfilename()
        path1.set(path_)
        self.filepath=path_

    def processExcelFile(self):
        e=Excel_file(path=self.filepath)
        e.get_target_sheet(target_sheet_name="故障填报主表")
        e.get_first_row_list(first_row_num=3)
        #获取分公司清单
        e.get_target_sheet_col_list(col_name="分公司名称")
        raw_fengongsi_list=e.target_sheet_col_value_list
        fengongsi_list=processOneList(raw_fengongsi_list).only_list
        #获取风电场清单
        e.get_target_sheet_col_list(col_name="风场名称")
        raw_fengdianchang_list=e.target_sheet_col_value_list
        fengdianchang_list=processOneList(raw_fengdianchang_list).only_list
        #获取风电场机组台数清单
        e.get_target_sheet_col_list(col_name="机组总数")
        raw_jizutaishu_list=e.target_sheet_col_value_list
        #获取故障次数清单
        e.get_target_sheet_col_list(col_name="信息类型")
        raw_xinxileixing_list=e.target_sheet_col_value_list
        #获取每个风电场每次故障的修复时间
        e.get_target_sheet_col_list(col_name='故障报出时间')
        raw_start_time_list=e.target_sheet_col_value_list
        e.get_target_sheet_col_list(col_name="复位运行时间")
        raw_end_time_list=e.target_sheet_col_value_list
        #获取每个风电场的经济损失
        e.get_target_sheet_col_list(col_name='合计\n（元）')
        raw_jingjisunshi_list=e.target_sheet_col_value_list


        #获取每个分公司有多少个风电场清单
        p=processTwoList(list1=raw_fengongsi_list,list2=raw_fengdianchang_list)
        p.get_yiduiduo_dict()
        fengongsi_fengdianchang_dict=p.yiduiduo_dict
        #获取每个风电场有多少台风机
        p=processTwoList(list1=raw_fengdianchang_list,list2=raw_jizutaishu_list)
        p.get_duoduiyi_dict()
        fengdianchang_jizutaishu_dict=p.duoduiyi_dict
        #获取每个风电场的故障次数
        p=processTwoList(list1=raw_fengdianchang_list,list2=raw_xinxileixing_list)
        p.get_duoduiyi_tongjicishu_dict()
        fengdianchang_xinxileixing_dict=p.duoduiyi_tongjicishu_dict
        #获取每个风电场每次故障的修复时间
        p=processFourList(list1=raw_fengdianchang_list,list2=raw_xinxileixing_list,list3=raw_start_time_list,list4=raw_end_time_list)
        p.get_tingjishijian_dict()
        tingjishijian_dict=p.tingjishijian_dict
        #每个风电场的容量
        fengdianchang_rongliang_dict=fengdianchang_jizutaishu_dict.copy()
        for k in fengdianchang_rongliang_dict:
            fengdianchang_rongliang_dict[k]=fengdianchang_rongliang_dict[k]*2.0
        #计算每个机组因不同类型停机产生的经济损失
        p=processThreeList(list1=raw_fengdianchang_list,list2=raw_xinxileixing_list,list3=raw_jingjisunshi_list)
        jingjisunshi_dict=p.jingjisunshi_dict

        d=Data(fengongsi_list=fengongsi_list,fengdianchang_list=fengdianchang_list,
               fengongsi_fengdianchang_dict=fengongsi_fengdianchang_dict,
               fengdianchang_jizutaishu_dict=fengdianchang_jizutaishu_dict,
               fengdianchang_xinxileixing_dict=fengdianchang_xinxileixing_dict,
               tingjishijian_dict=tingjishijian_dict,
               fengdianchang_rongliang_dict=fengdianchang_rongliang_dict,
               jingjisunshi_dict=jingjisunshi_dict)
        root2=Tk(className="分公司列表")
        row_num=int(len(fengongsi_list)/4)+2
        row_height=str(int(row_num*50))
        chicun="400x"+row_height
        root2.geometry(chicun)
        fengongsi_frame=FengongsiFrame(root2,data=d,row_num=row_num)
        fengongsi_frame.pack()
        root2.mainloop()

if __name__=="__main__":
    root = Tk(className="Excel文件处理")
    root.geometry("400x150")
    if_frame = MainFrame(root)
    if_frame.pack()
    root.mainloop()