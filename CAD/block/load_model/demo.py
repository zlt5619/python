from pyautocad import APoint

class load_model():
    def __init__(self,start_point=(0,0),chang=1000,kuan=500,load_name=None):
        self.point1=APoint(start_point[0],start_point[1])
        self.point2=APoint(start_point[0]+chang,start_point[1])
        self.point3=APoint(start_point[0]+chang,start_point[1]+kuan)
        self.point4=APoint(start_point[0],start_point[1]+kuan)
        self.wenzi_insert_point=APoint(start_point[0]+chang/2,start_point[1]+kuan/2)
        self.load_name=load_name
        self.wenzi_height=300

    @property
    def draw_info(self):
        line1=[self.point1,self.point2]
        line2=[self.point2,self.point3]
        line3=[self.point3,self.point4]
        line4=[self.point4,self.point1]
        line_info=[line1,line2,line3,line4]
        wenzi_info=[self.load_name,self.wenzi_insert_point,self.wenzi_height]
        info=[line_info,wenzi_info]
        return info


