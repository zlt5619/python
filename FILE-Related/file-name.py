#给出输入路径
#将路径里的非目录文件，取其名字
#输出到excel表格中
import os
import xlwt
path=input("请输入相关路径\n")
list1=[]
list2=[]
def printFileName(path):
    if os.path.isfile(path):
        list1.append(path)
    else:
        print(path)
        subpaths=os.listdir(path)
        for subpath in subpaths:
            newpath=path+'\\'+subpath
            printFileName(newpath)
printFileName(path)
for item in list1:
    before,file=os.path.split(item)
    list2.append(file)

workbook=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=workbook.add_sheet('test',cell_overwrite_ok=True)
col=0
for row in range(int(len(list2))):
    sheet.write(row,col,list2[row])
workbook.save('test.xls')

