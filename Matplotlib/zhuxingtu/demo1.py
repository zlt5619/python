import matplotlib.pyplot as plt
import matplotlib

#横坐标显示中文
font = {'family': 'Microsoft YaHei', 'weight': 'bold', 'size': '14'}
matplotlib.rc("font", family="Microsoft YaHei", weight="bold", size="14")

source_dict={'五岳山风电场': 15.2, '大幕山风电场': 3.9, '宣化风电场': 0.0, '寿山风电场': 0, '余店风电场': 9.2, '朝阳山风电场': 0, '仙舞山风电场': 7.9, '寒池风电场': 6.7, '元堡风电场': 4.8, '大坡顶风电场': 2.4, '富池风电场': 4.6, '柏杨坝风电场': 1.6, '敖家山风电场': 9.4, '擂鼓台风电场': 1.4}

changzhan_list=source_dict.keys()
MTTRL_list=source_dict.values()
process_changzhan_list=[]

for i in changzhan_list:
    i=i[:-3]
    process_changzhan_list.append(i)

# print(changzhan_list)
# print(MTTRL_list)

matplotlib.rcParams["font.sans-serif"] = ["SimHei"]
matplotlib.rcParams["axes.unicode_minus"] = False
#创建图表的基础
plt.figure(figsize=(12,4))

#限定y坐标的取值范围
plt.ylim((0,20))

#y坐标的划分
plt.yticks()

#x坐标的划分
plt.xticks(range(len(changzhan_list)),process_changzhan_list,rotation=0)

#画柱形图
plt.bar(changzhan_list,MTTRL_list,width=0.4,color='dodgerblue')

#展示图形
plt.show()




