from pyautocad import Autocad, APoint
from CAD.block.load_model.demo import load_model

acad=Autocad(create_if_not_exists=True)

l=load_model(load_name="风机1")

def draw_block(model=None,insertionPnt = APoint(0, 0)):
    model_info=model.draw_info
    line_info=model_info[0]
    wenzi_info=model_info[1]
    grip=APoint(0,0)
    blockObj = acad.ActiveDocument.Blocks.Add(grip, wenzi_info[0])
    for l_info in line_info:
        point1=l_info[0]
        point2=l_info[1]
        blockObj.AddLine(point1,point2)
    textObj=blockObj.AddText(wenzi_info[0], wenzi_info[1], wenzi_info[2])
    AlignNum = 4
    textObj.Alignment = AlignNum
    insertPnt = wenzi_info[1]
    textObj.TextAlignmentPoint = insertPnt
    acad.model.InsertBlock(insertionPnt, wenzi_info[0], 1, 1, 1, 0)

draw_block(model=l,insertionPnt=APoint(200,50))

