from pyautocad import Autocad,APoint

# acad = Autocad(create_if_not_exists = True)
# acad.prompt("Hello! AutoCAD from pyautocad.")

class signal():
    def __init__(self,text=None,insert_point=None):
        self.text=text
        self.X=insert_point[0]
        self.Y=insert_point[1]
        self.insertionPnt =APoint(self.X,self.Y)
        self.input_point=APoint(self.X+250,self.Y+400)
        self.output_point=APoint(self.X+250,self.Y)
        self.acad=Autocad(create_if_not_exists=True)
        self.draw()

    def draw(self):
        block1=self.acad.ActiveDocument.Blocks.Add(APoint(0,0), self.text)
        line1=block1.AddLine(APoint(0,0),APoint(500,0))
        line2=block1.AddLine(APoint(500,0),APoint(500,400))
        line3=block1.AddLine(APoint(500,400),APoint(0,400))
        line4=block1.AddLine(APoint(0,400),APoint(0,0))
        textString = self.text
        insertPnt = APoint(50, 150)
        height = 100
        textobj = block1.AddText(textString, insertPnt, height)
        insertionPnt=self.insertionPnt
        RetVal = self.acad.model.InsertBlock(insertionPnt, self.text, 1, 1, 1, 0)

# s1=signal("MT004")

class Signal_Frame():
    def __init__(self,insert_point=None,num=0,name=0):
        self.name="frame"+str(name)
        self.num=num
        self.X=insert_point[0]
        self.Y=insert_point[1]
        self.insertionPnt = APoint(self.X,self.Y)
        self.acad=Autocad(create_if_not_exists=True)
        self.draw()

    def draw(self):
        block1=self.acad.ActiveDocument.Blocks.Add(APoint(0,0),self.name)
        line1=block1.AddLine(APoint(0,0),APoint(500*self.num,0))
        line2=block1.AddLine(APoint(500*self.num,0),APoint(500*self.num,1800))
        line3=block1.AddLine(APoint(500*self.num,1800),APoint(0,1800))
        line4=block1.AddLine(APoint(0,1800),APoint(0,0))

        insertionPnt=self.insertionPnt
        RetVal = self.acad.model.InsertBlock(insertionPnt, self.name, 1, 1, 1, 0)

s=Signal_Frame(insert_point=(0,0),num=5,name=1)



