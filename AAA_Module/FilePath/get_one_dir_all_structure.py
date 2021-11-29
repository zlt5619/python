"""
输入一个路径，获得全部的子目录

"""

import os

class processdir(object):
    def __init__(self,dir=None):
        self.dir=dir
        self.content=[dir]
        self.process()

    def process(self,dir=None):
        if dir==None:
            raw_list=os.listdir(self.dir)
            for i in raw_list:
                if os.path.isdir(self.dir+"/"+i):
                    self.content.append(self.dir+"/"+i)
                    self.process(dir=self.dir+"/"+i)
        else:
            raw_list = os.listdir(dir)
            for i in raw_list:
                if os.path.isdir(dir + "/" + i):
                    self.content.append(dir + "/" + i)
                    self.process(dir=dir + "/" + i)

dir='D:\programming'
p=processdir(dir=dir)
print(p.content)