from pyautocad import Autocad,APoint

acad = Autocad(create_if_not_exists = True)
acad.prompt("Hello! AutoCAD from pyautocad.")

class Block():
    def __init__(self,name=None,insert_position=(),*args):
        self.grip_point=APoint(0,0)
        self.insert_point=APoint(insert_position[0],insert_position[1])
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
    def __init__(self,x=0,y=0,insert_position=()):
        self.insert_x=insert_position[0]
        self.insert_y=insert_position[1]
        self.p1=APoint(self.insert_x,self.insert_y)
        self.p2=APoint(self.insert_x,self.insert_y+y)
        self.p3=APoint(self.insert_x+x,self.insert_y+y)
        self.p4=APoint(self.insert_x+x,self.insert_y)
        self.name="矩形"
    def draw(self):
        acad.model.AddLine(self.p1, self.p2)
        acad.model.AddLine(self.p2, self.p3)
        acad.model.AddLine(self.p3, self.p4)
        acad.model.AddLine(self.p4, self.p1)

class Text():
    def __init__(self,text=None,height=0,insert_position=()):
        self.text=text
        self.height=height
        self.insert_x = insert_position[0]
        self.insert_y = insert_position[1]
        self.insert_point=APoint(self.insert_x,self.insert_y)
        self.name="文字"

    def draw(self):
        acad.model.AddText(self.text,self.insert_point,self.height)
# r1=Rectangle(x=400,y=200,insert_position=(300,300))
# t1=Text(text="hello world",height=100,insert_position=(0,0))
# b1=Block("abc",1000,500,r1,t1)
# r1.draw()
# t1.draw()