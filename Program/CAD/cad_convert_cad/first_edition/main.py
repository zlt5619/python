from tkinter import Tk, Button

from pyautocad import Autocad, APoint


#端子排1
class duanzipai():
    def __init__(self,load_name=None):
        chang=20
        kuan=5
        wenzi_height=300
        AlignNum = 4
        self.point1=APoint(0,0)
        self.point2=APoint(chang,0)
        self.point3=APoint(chang,kuan)
        self.point4=APoint(0,kuan)
        self.wenzi_insert_point=APoint(chang/2,kuan/2)
        self.load_name=load_name
        self.wenzi_height=wenzi_height
        self.wenzi_alignNum=AlignNum

    @property
    def draw_info(self):
        line1=[self.point1,self.point2]
        line2=[self.point2,self.point3]
        line3=[self.point3,self.point4]
        line4=[self.point4,self.point1]
        line_info=[line1,line2,line3,line4]
        wenzi_info=[self.load_name,self.wenzi_insert_point,self.wenzi_height,self.wenzi_alignNum]
        arc_info=[]
        info=[line_info,wenzi_info,arc_info]
        return info
#画块的工具
def draw_line(blockObj,line_info):
    if line_info==[]:
        pass
    else:
        for l_info in line_info:
            point1=l_info[0]
            point2=l_info[1]
            blockObj.AddLine(point1,point2)
def draw_wenzi(blockObj,wenzi_info):
    if wenzi_info==[]:
        pass
    else:
        textObj=blockObj.AddText(wenzi_info[0], wenzi_info[1], wenzi_info[2])
        AlignNum = wenzi_info[3]
        textObj.Alignment = AlignNum
        insertPnt = wenzi_info[1]
        textObj.TextAlignmentPoint = insertPnt
def draw_arc(blockObj,arc_info):
    if arc_info==[]:
        pass
    else:
        pass
        #画弧
def draw_block(model=None):
    model_info=model.draw_info
    line_info=model_info[0]
    wenzi_info=model_info[1]
    arc_info=model_info[2]
    block_start_point = APoint(0, 0)
    blockObj = acad.ActiveDocument.Blocks.Add(block_start_point, wenzi_info[0])
    draw_line(blockObj,line_info)
    draw_wenzi(blockObj,wenzi_info)
    draw_arc(blockObj,arc_info)
    block_info.append(wenzi_info[0])
def function1():
    all_info=[]
    for obj in acad.iter_objects("Block"):
        # 以下获取块的属性信息
        # 如果想获取某一特定块的属性信息可以用ObjectID识别特定块
        print(obj.Name)
        obj.Explode

    for obj in acad.iter_objects("Text"):
        a=obj.TextString
        b=obj.InsertionPoint
        l=[a,b,obj]
        all_info.append(l)

    duanzipai_info=[]
    for i in all_info:
        if i[1][0]>25 and i[1][0]<40:
            duanzipai_info.append(i)
    # print(duanzipai_info)
    dianlan_info1=[]
    for i in all_info:
        if i[1][0]>40 and i[1][0]<62:
            dianlan_info1.append(i)
    # print(dianlan_info1)
    dianlan_info2=[]
    for i in all_info:
        if i[1][0]>62 and i[1][0]<70:
            dianlan_info2.append(i)
    # print(dianlan_info2)
    fuhe_info=[]
    for i in all_info:
        if i[1][0]>70 and i[1][1]>14:
            fuhe_info.append(i)
    # print(fuhe_info)
    for i in duanzipai_info:
        print(i[0],i[1])
    for i in dianlan_info1:
        print(i[0],i[1])
    for i in dianlan_info2:
        print(i[0],i[1])
    for i in fuhe_info:
        print(i[0],i[1])

    #画块
    for i in range(len(duanzipai_info)):
        p1=APoint(130,60-i*5)
        string1=duanzipai_info[i][0].split("\\l")[1]
        acad.model.AddText(string1, p1, 3)
    for i in range(len(dianlan_info1)):
        p1 = APoint(160, 60-i*5)
        acad.model.AddText(dianlan_info1[i][0], p1, 3)
    for i in range(len(dianlan_info2)):
        p1 = APoint(190, 60-i*5)
        acad.model.AddText(dianlan_info2[i][0], p1, 3)
    for i in range(len(fuhe_info)):
        p1 = APoint(240, 60-i*5)
        acad.model.AddText(fuhe_info[i][0], p1, 3)


    #布置块



if __name__=="__main__":
    root = Tk(className="cad转换")
    root.geometry("100x100")
    acad = Autocad(create_if_not_exists=True)
    b1=Button( text="转换", command=function1, height=1)
    b1.pack()
    block_info=[]
    root.mainloop()