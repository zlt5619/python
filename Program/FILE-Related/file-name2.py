"""
升级版，将文件名按照指定顺序打出来，生成excel
可以生成完整文件目录结构

"""
import os
import pandas as pd
list1=[]
list2=[]
def printFileName(path):
    list1.append(path)
    if os.path.isdir(path):
        subpaths = os.listdir(path)
        for subpath in subpaths:
            newpath = path + '\\' + subpath
            printFileName(newpath)

path=input("请输入相关路径\n")
if not os.path.exists(path):
    print("文件路径输入有误,请重新输入")
    path = input("请输入相关路径\n")
else:
    printFileName(path)

max_length=0
for items in list1:
    item=items.split('\\')
    length=len(item)
    if length>max_length:
        max_length=length
    list2.append(item)
col=[]
for i in range(max_length):
    i1=str(i+1)
    col.append("第"+i1+"级目录")
index=[]
for i in range(len(list1)):
    index.append(i+1)

dataframe1=pd.DataFrame(list2,columns=col, index=index)
dataframe1.to_excel('result.xls',header=True)
