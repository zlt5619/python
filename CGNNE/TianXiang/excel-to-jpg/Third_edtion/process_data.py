"""
查找一列数值的特点,
1、统计这一个列表中的唯一元素，形成列表
2、统计这一列表中一个元素出现的次数，字典 {某元素：出现次数}
"""
class process_one_list_item(object):
    def __init__(self,original_list=None):
        #获取要处理的列表
        self.original_list=original_list
        #设置最初的原始元组,列表
        self.set1=set()
        self.only_list=[]
        self.get_set()
        self.get_only_list()
        #设置最初的统计字典
        self.tongjicishu_dict=dict()
        self.get_tongjicishu_dict()
    #处理列表，形成唯一的元组
    def get_set(self):
        self.set1=set(self.original_list)
    #处理元组，形成列表
    def get_only_list(self):
        self.only_list=list(self.set1)
    #统计每个元素出现的次数
    def get_tongjicishu_dict(self):
        for i in self.only_list:
            self.tongjicishu_dict[i]=0
        for i in self.original_list:
            for j in self.tongjicishu_dict.keys():
                if i==j:
                    self.tongjicishu_dict[j]+=1

