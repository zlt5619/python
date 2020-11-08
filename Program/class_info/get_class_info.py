class get_info():
    def __init__(self,target=None):
        self.target=target
        self.list=dir(self.target)
        self.guyoushuxing=[]
        self.fangfa=[]
        for i in self.list:
            if i.startswith("__"):
                self.guyoushuxing.append(i)
            else:
                self.fangfa.append(i)

        # print(self.guyoushuxing)
        # print(self.fangfa)

# get_info(target=[1,2,3])
# get_info(target=list)

class get_init_info():
    def __init__(self,list1=None,list2=None):
        self.length1=len(list1)
        self.length2=len(list2)
        self.list=[]
        if self.length1>self.length2:
            for a in list1:
                if a not in list2:
                    self.list.append(a)
        elif self.length1<self.length2:
            for a in list2:
                if a not in list1:
                    self.list.append(a)
        else:
            pass
        # print(self.list)

class to_txt():
    def __init__(self,*content):
        pass

class get_all_info():
    def __init__(self,klass=None,instance1=None,path="C:\\Users\\zlt56\\Desktop"):
        self.klass=klass
        self.instance1=instance1
        self.klass_info=get_info(target=self.klass)
        self.instance1_info=get_info(target=self.instance1)
        self.klass_init_info=get_init_info(list1=self.klass_info.fangfa,list2=self.instance1_info.fangfa)
        print(self.klass_info.fangfa)
        print(self.instance1_info.fangfa)
        print(self.klass_init_info.list)