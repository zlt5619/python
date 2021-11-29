"""
输入一个路径
获得所有的文件
"""

import os

class processdir2():
    def __init__(self,dir=None):
        self.dir=dir
        self.filelists=[]
        self.process()

    def process(self,dir=None):
        if dir==None:
            raw_list=os.listdir(self.dir)
            for i in raw_list:
                if os.path.isdir(self.dir+"/"+i):
                    str1=self.dir+"/"+i
                    self.process(dir=str1)
                else:
                    self.filelists.append(i)
        else:
            raw_list=os.listdir(dir)
            for i in raw_list:
                if os.path.isdir(dir+"/"+i):
                    str1=dir+"/"+i
                    self.process(dir=str1)
                else:
                    self.filelists.append(i)

dir='D:\programming'
p=processdir2(dir=dir)
print(p.filelists)