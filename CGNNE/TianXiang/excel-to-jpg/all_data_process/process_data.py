"""
输入一个列表
1、统计这个列表的唯一元素存在
2、统计这个列表的每个元素的次数
"""
class processOneList(object):
    def __init__(self,input_list=None):
        self.input_list=input_list
        self.only_list=None
        self.get_only_list()
        self.list_cishu=dict()

    def get_only_list(self):
        self.only_list=list(set(self.input_list))

    def get_list_cishu(self):
        for i in self.only_list:
            self.list_cishu[i]=0
        for i in self.input_list:
            for j in self.only_list:
                if i==j:
                    self.list_cishu[j]+=1

"""
输入两个列表，一个值少，一个值多,长度相同，形成2个字典
1、{值少的一列：值多的一列}  一对多
2、{值多的一列：值少的一列}  多对一
3、{值多的一列：{值少的一列：统计次数，值少的一列：统计次数}}
"""
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

"""
输入四个列表
根据前面两列，确认字典的key
根据后面的时间序列获取相减的时间
"""
class processFourList(object):
    def __init__(self,list1=None,list2=None,list3=None,list4=None):
        self.list1=list1
        self.list2=list2
        self.list3=list3
        self.list4=list4
        self.list1_key=processOneList(self.list1).only_list
        self.list2_key=processOneList(self.list2).only_list
        self.tingjileixing_dict=dict()
        self.tingjijian_dict=dict()
        for i in self.list2_key:
            self.tingjileixing_dict[i]=0
        for i in self.list1_key:
            self.tingjijian_dict[i]=self.tingjileixing_dict.copy()

    def get_tingjishijian_dict(self):
        pass

