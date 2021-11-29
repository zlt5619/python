"""
输入一个文件路径名
获取全部的子文件和子文件路径
"""
import os

class processDir(object):
    def __init__(self,path=None):
        self.path=path
        self.subfiles=[]
        self.subdirs=[]
        self.process()

    def process(self):
        raw_list=os.listdir(self.path)
        for i in raw_list:
            if os.path.isfile(self.path+"\\"+i):
                self.subfiles.append(self.path+"\\"+i)
            if os.path.isdir(self.path+"\\"+i):
                self.subdirs.append(self.path+"\\"+i)


path='C:\ProgramData'
p=processDir(path=path)
print(p.subdirs)
print("-----")
print(p.subfiles)