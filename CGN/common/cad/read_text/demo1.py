from pyautocad import Autocad
"""
读取cad文件，其中有两组字符串，挨得比较近，故将其合二为一
返回字典{1：“。。。”，2：“。。。”，。。。}
还要找到字符串正下方的文字
"""

def readcad():
    data=dict()
    acad = Autocad(create_if_not_exists=True)
    equipment_info=[]
    rest_info=[]
    for obj in acad.iter_objects("Text"):
        obj_x=obj.InsertionPoint[0]
        obj_y=obj.InsertionPoint[1]
        obj_text=obj.TextString
        list1=[obj_text,obj_x,obj_y]
        if len(obj_text)==4 and obj_text.startswith("2"):
            equipment_info.append(list1)
        else:
            #通过旋转角度判断是否入选
            if obj.Rotation==0:
                rest_info.append(list1)
    for i in range(len(equipment_info)):
        for j in rest_info:
            if equipment_info[i][2]-0.5 < j[2] < equipment_info[i][2]+0.5:
                if equipment_info[i][1]<j[1]<equipment_info[i][1]+15:
                    string1=equipment_info[i][0]+j[0]
                    data[i+1]=string1
    for i in range(len(equipment_info)):
        for j in rest_info:
            if equipment_info[i][2]-10 < j[2] < equipment_info[i][2]:
                if equipment_info[i][1]-3<j[1]<equipment_info[i][1]+2:
                    string2=j[0]
                    string1=data[i+1]
                    list1=[string1,string2]
                    data[i+1]=list1
    for k,v in data.items():
        print(str(k)+":"+str(v))

    return data
readcad()