from pyautocad import Autocad,APoint

acad = Autocad(create_if_not_exists = True)
acad.prompt("Hello! AutoCAD from pyautocad.")

class signal():
    def __init__(self,text=None,insert_point=APoint(0,0)):
        self.text=text
        self.draw()
        self.block1_insertionPnt = APoint(0, 0)
    def draw(self):
        block1=acad.ActiveDocument.Blocks.Add(APoint(0,0), self.text)
        line1=block1.AddLine(APoint(0,0),APoint(500,0))
        line2=block1.AddLine(APoint(500,0),APoint(500,400))
        line3=block1.AddLine(APoint(500,400),APoint(0,400))
        line4=block1.AddLine(APoint(0,400),APoint(0,0))
        textString = self.text
        insertPnt = APoint(50, 150)
        height = 100
        textobj = block1.AddText(textString, insertPnt, height)

        RetVal = acad.model.InsertBlock(self.block1_insertionPnt, self.text, 1, 1, 1, 0)

s1=signal("MT004")




