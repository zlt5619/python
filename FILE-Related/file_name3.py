"""
升级版，将文件名按照指定顺序打出来，生成excel
可以生成完整文件目录结构
新的一种布局格式
"""
import os
import pandas as pd
import collections
list1=[]
list2=[]
list3=[]
list4=[]
d=collections.OrderedDict()
def printFileName(path):
    if os.path.isdir(path):
        subpaths = os.listdir(path)
        for subpath in subpaths:
            newpath = path + '\\' + subpath
            printFileName(newpath)
    else:
        list1.append(path)
path=input("请输入相关路径\n")
if not os.path.exists(path):
    print("文件路径输入有误,请重新输入")
    path = input("请输入相关路径\n")
else:
    printFileName(path)
for item in list1:
    before,file=os.path.split(item)
    list2.append([before,file])
    list3.append(before)
file_prix=list(set(list3))
#取set后，顺序会改变，需要变回来
file_prix.sort(key=list3.index)
print(file_prix)
for element in file_prix:
    for i in range(len(list2)):
        if list2[i][0]==element:
            list4.append(list2[i][1])
    d[element]=list4
    list4=[]
