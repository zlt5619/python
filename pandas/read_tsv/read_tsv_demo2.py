import pandas as pd
#输入文件所在路径
file_path=input("请输入要转换的文件路径\n")
#读取tsv文件
train=pd.read_csv(file_path, sep='\t')
#获取原文件所在文件夹位置
list=file_path.split('\\')
filename=list[-1].split('.')[0]

list=list[:-1]
path=''
for l in list:
    path=path+'\\'+l
path=path[1:]
format=input("请输入想转化的格式，xlsx或者csv")
if format=='csv':
    path=path+"\\"+filename+'.csv'
    #将DataFrame转为Excel
    train.to_csv(path,index=False,header=True)
else:
    path=path+"\\"+filename+'.xlsx'
    # 将DataFrame转为Excel
    train.to_excel(path, index=False, header=True)

print('转换完成')
