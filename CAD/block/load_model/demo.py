from pyautocad import APoint

class load_model():
    #定义每一个负荷的标准
    def __init__(self,load_name=None):
        chang=1000
        kuan=500
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


