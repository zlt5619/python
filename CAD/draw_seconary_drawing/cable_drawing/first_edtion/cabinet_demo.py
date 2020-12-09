from pyautocad import Autocad, APoint

#创建cabinet模型
class cabinet():
    def __init__(self,name=None):
        chang = 75
        kuan = 15
        wenzi_height = 4
        AlignNum = 4
        self.point1 = APoint(0, 0)
        self.point2 = APoint(chang, 0)
        self.point3 = APoint(chang, kuan)
        self.point4 = APoint(0, kuan)
        self.wenzi_insert_point = APoint(chang / 2, kuan / 2)
        self.wenzi_height = wenzi_height
        self.wenzi_alignNum = AlignNum
        self.name=name

    @property
    def draw_info(self):
        line1 = [self.point1, self.point2]
        line2 = [self.point2, self.point3]
        line3 = [self.point3, self.point4]
        line4 = [self.point4, self.point1]
        line_info = [line1, line2, line3, line4]
        wenzi_info = [self.name, self.wenzi_insert_point, self.wenzi_height, self.wenzi_alignNum]
        arc_info = []
        info = [line_info, wenzi_info, arc_info]
        return info