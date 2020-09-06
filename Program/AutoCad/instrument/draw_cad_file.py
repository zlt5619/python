from pyautocad import Autocad,APoint
from Program.AutoCad.instrument.signal import signal,Signal_Frame

d={'PO010': {0: ['PO010', '=', 'MT001', '&&', 'MT005', '&&', '信号1'], 1: ['信号1', '=', 'PO001', '&&', '信号2'], 2: ['信号2', '=', 'MT003', '||', 'MT004']}, 'PO016': {0: ['PO016', '=', 'MT001', '&&', '信号1', '||', '信号2'], 1: ['信号1', '=', 'MT002', '&&', 'MT003', '||', 'MT004'], 2: ['信号2', '=', 'MT005', '||', 'MT004']}}

def draw_cad(data):
    #打印相关数据
    # print(data)
    output_signal=data.keys()
    output_data_set=set()
    draw_signal_data=dict()
    for i in output_signal:
        values=data[i]
        for j in range(len(values)):
            for k in range(len(values[j])):
                if values[j][k]=="=":
                    pass
                elif values[j][k]=="&&":
                    pass
                elif values[j][k]=="||":
                    pass
                elif values[j][k]==i:
                    pass
                else:
                    output_data_set.add(values[j][k])
        draw_signal_data[i]=output_data_set
        output_data_set=set()
    # print(draw_signal_data)
    draw_relevent_signal(data=draw_signal_data)
    draw_relvent_logic(raw_data=data,data=draw_signal_data)
#画出相关信号
def draw_relevent_signal(data=None):
    draw_list=[]
    for k,v in data.items():
        list1=list(v)
        list1.sort()
        list2=[]
        for i in range(len(list1)):
            if "信号" in list1[i]:
                pass
            else:
                list2.append(list1[i])
        list2.append(k)
        draw_list.append(list2)
    # print(draw_list)
    for i in range(len(draw_list)):

        s=Signal_Frame(insert_point=((len(draw_list[i])-1)*500,0),num=len(draw_list[i])-1,name=i)
        for k in range(len(draw_list[i])):
            if k==len(draw_list[i])-1:
                if i==0:
                    signal(draw_list[i][k],insert_point=(0,0))
                else:
                    signal(draw_list[i][k],insert_point=((len(draw_list[i-1])-1)*500,0))
            else:
                if i==0:
                    signal(draw_list[i][k],insert_point=(k*500,1400))
                else:
                    signal(draw_list[i][k],insert_point=(k*500+(len(draw_list[i-1])-1)*500,1400))
#画出相关逻辑
def draw_relvent_logic(raw_data=None,data=None):
    # print(raw_data)
    # print(data)
    draw_list = []
    for k, v in data.items():
        list1 = list(v)
        list1.sort()
        xinhao_list = []
        list2=[]
        for i in range(len(list1)):
            if "信号" in list1[i]:
                xinhao_list.append(list1[i])
            else:
                list2.append(list1[i])
        list2.append(k)
        draw_list.append([xinhao_list,list2])
    print(draw_list)


# draw_cad(d)