import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime

path="C:/Users/zlt/Desktop/田祥资料/附件1：中广核新能源控股有限公司2021年08月故障记录汇总表.xlsx"

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

e=Excel_file(path=path)
e.get_target_sheet(target_sheet_name="故障填报主表")
e.get_first_row_list(first_row_num=3)
e.get_target_sheet_col_list(col_name="分公司名称")
e.get_target_sheet_row_list(row_num=100)
fengongsi_list=e.target_sheet_col_value_list
e.get_target_sheet_col_list(col_name="风场名称")
fengchangmingcheng_list=e.target_sheet_col_value_list
e.get_target_sheet_col_list(col_name="信息类型")
xixinleixing_list=e.target_sheet_col_value_list
e.get_target_sheet_col_list(col_name="机组总数")
jizutaishu_list=e.target_sheet_col_value_list
e.get_target_sheet_col_list(col_name='故障报出时间')
fault_start_time_list=e.target_sheet_col_value_list
e.get_target_sheet_col_list(col_name='复位运行时间')
fault_end_time_list=e.target_sheet_col_value_list
e.get_target_sheet_col_list(col_name='合计\n（元）')
jingjisunshi_list=e.target_sheet_col_value_list

class processOneList(object):
    def __init__(self, input_list=None):
        self.input_list = input_list
        self.only_list = None
        self.get_only_list()
        self.list_cishu = dict()

    def get_only_list(self):
        self.only_list = list(set(self.input_list))
        self.only_list.remove('')

    def get_list_cishu(self):
        for i in self.only_list:
            self.list_cishu[i] = 0
        for i in self.input_list:
            for j in self.only_list:
                if i == j:
                    self.list_cishu[j] += 1

# p=processOneList(e.target_sheet_col_value_list)
# p.get_list_cishu()
# print(p.only_list)
# print(p.list_cishu)

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

# p=processTwoList(list1=fengongsi_list,list2=fengchangmingcheng_list)
# p=processTwoList(list1=xixinleixing_list,list2=fengchangmingcheng_list)
# p=processTwoList(list1=jizutaishu_list,list2=fengchangmingcheng_list)
# p.get_duoduiyi_dict()
# print(p.duoduiyi_dict)
# p.get_duoduiyi_tongjicishu_dict()
# print(p.duoduiyi_tongjicishu_dict)

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

# p=processThreeList(list1=fengchangmingcheng_list,list2=xixinleixing_list,list3=jingjisunshi_list)
# print(p.jingjisunshi_dict)

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

# p=processFourList(list1=fengchangmingcheng_list,list2=xixinleixing_list,list3=fault_start_time_list,list4=fault_end_time_list)
# p.get_tingjishijian_dict()
# print(p.tingjishijian_dict)