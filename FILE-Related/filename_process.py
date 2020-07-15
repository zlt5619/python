import re

import pandas as pd
from pandas.core.frame import DataFrame
filename=pd.read_excel('./test.xls')
file=filename.values.tolist()
# print(file)

first_file=[]
second_file=[]
dump_list=[]
def first_process_filename(item):
    element=item[0]
    if element.endswith('.torrent'):
        dump_list.append(element)
    elif element.endswith('.jpg'):
        dump_list.append(element)
    elif element.endswith('.nfo'):
        dump_list.append(element)
    elif element.endswith('.idx'):
        dump_list.append(element)
    elif element.endswith('.sub'):
        dump_list.append(element)
    elif element.endswith('.doc'):
        dump_list.append(element)
    elif element.endswith('.gif'):
        dump_list.append(element)
    else:
        first_file.append(element)
def second_process_filename(item):
    item_1 = re.sub(r'【.*】', "", item)
    item_2=re.sub(r'[.*]','',item_1)
    item_3=re.sub(r'BD*','',item_2)
    item_4=re.sub(r'Chi_Eng*','',item_3)
    item_5=re.sub(r'720p*','',item_4)
    item_6=re.sub(r'中英双字*','',item_5)
    item_7=re.sub(r'1280*','',item_6)
    item_8=re.sub(r'国英双语*','',item_7)
    item_9=re.sub(r'mkv','',item_8)
    item_10=re.sub(r'mp4','',item_9)
    item_11=re.sub(r'\[.*\]','',item_10)
    item_12=re.sub(r'1024','',item_11)
    item_13=re.sub(r'高清','',item_12)
    item_14=re.sub(r'rmvb','',item_13)
    item_15=re.sub(r'DVD','',item_14)
    item_16=re.sub(r'2015luRayx264-SPARKS','',item_15)
    item_17=re.sub(r'HD','',item_16)
    item_18=re.sub(r'超清','',item_17)
    item_19=re.sub(r'中英字幕x版(66影视www66yscc)','',item_18)
    item_20=re.sub(r'2015中英字幕luRayx264深影字幕组原创翻译','',item_19)
    item_20=re.sub(r'国英音轨','',item_19)

    second_file.append(item_18)

for item in file:
    first_process_filename(item)
# print(first_file)


for item in first_file:
    second_process_filename(item)
print(second_file)
dict1={'second_file':second_file}
data=DataFrame(dict1)
data.to_excel('result.xls',header=True)