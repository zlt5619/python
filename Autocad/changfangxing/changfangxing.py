from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)

#对长方形输入长，宽，默认起始点为（0，0）
class changfangxing():
    def __init__(self,chang=None,kuan=None,start_point=(0,0)):
        self.point1=APoint(start_point[0],start_point[1])
        self.point2=APoint(start_point[0]+chang,start_point[1])
        self.point3=APoint(start_point[0]+chang,start_point[1]+kuan)
        self.point4=APoint(start_point[0],start_point[1]+kuan)

    def draw(self):
        pass
