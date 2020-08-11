from pyautocad import Autocad,APoint

acad = Autocad(create_if_not_exists = True)
acad.prompt("Hello! AutoCAD from pyautocad.")

class Block():
    def __init__(self,name,insert_point_x,insert_point_y,*args):
        self.grip_point=APoint(0,0)
        self.insert_point=APoint(insert_point_x,insert_point_y)
        self.name=name
        self.blockobj=acad.ActiveDocument.Blocks.Add(self.grip_point,name)
        self.model_list=args
        for model in self.model_list:
            if model.name=="矩形":
                self.blockobj.AddLine(model.p1,model.p2)
                self.blockobj.AddLine(model.p2,model.p3)
                self.blockobj.AddLine(model.p3,model.p4)
                self.blockobj.AddLine(model.p4,model.p1)
            elif model.name=="文字":
                self.blockobj.AddText(model.text,model.insert_point,model.height)
            else:
                print("出错了")
        self.RetVal = acad.model.InsertBlock(self.insert_point, name, 1, 1, 1, 0)

class Rectangle():
    def __init__(self,x,y,insert_x,insert_y):
        self.p1=APoint(insert_x,insert_y)
        self.p2=APoint(insert_x,insert_y+y)
        self.p3=APoint(insert_x+x,insert_y+y)
        self.p4=APoint(insert_x+x,insert_y)
        self.name="矩形"

class Text():
    def __init__(self,text,height,insert_x,insert_y):
        self.text=text
        self.height=height
        self.insert_point=APoint(insert_x,insert_y)
        self.name="文字"

# r1=Rectangle(400,200,0,0)
# t1=Text("hello world",100,20,20)
# b1=Block("abc",1000,500,r1,t1)

