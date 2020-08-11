from pyautocad import Autocad,APoint

acad = Autocad(create_if_not_exists = True)
acad.prompt("Hello! AutoCAD from pyautocad.")

class Block():
    def __init__(self):
        pass

class Rectangle():
    def __init__(self,x,y):
        self.p1=APoint(0,0)
        self.p2=APoint(0,y)
        self.p3=APoint(x,y)
        self.p4=APoint(x,0)
        # acad.model.AddLine(self.p1, self.p2)
        # acad.model.AddLine(self.p2, self.p3)
        # acad.model.AddLine(self.p3, self.p4)
        # acad.model.AddLine(self.p4, self.p1)

          # 新建块的名称为"HIT_Block"；
          # grip为块定位夹点所在位置。

# center = APoint(40, 10)
# majAxis = APoint(10, 0, 0)
# EllObj = blockObj.AddEllipse(center, majAxis, 0.5)
#
# insertionPnt = APoint(0, 0)
# RetVal = acad.model.InsertBlock(insertionPnt, "HIT_Block", 1, 1, 1, 0 )



r=Rectangle(1000,500)

grip = APoint(20, 0)
blockObj = acad.ActiveDocument.Blocks.Add(grip, "HIT_Block")
center = APoint(0, 0)
radius = 1000
CircleObj = blockObj.AddCircle(center, radius)
rectangleobj1=blockObj.AddLine(APoint(0,0),APoint(1000,0))
rectangleobj2=blockObj.AddLine(APoint(0,0),APoint(0,1000))
insertionPnt = APoint(0, 0)
RetVal = acad.model.InsertBlock(insertionPnt, "HIT_Block", 1, 1, 1, 0 )