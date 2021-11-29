from pyautocad import Autocad, APoint
from block.load_model.demo import load_model

acad=Autocad(create_if_not_exists=True)

l1=load_model(load_name="风机1")
l2=load_model(load_name="风机2")
l3=load_model(load_name="风机3")
block_info=[]
def draw_line(blockObj,line_info):
    if line_info==[]:
        pass
    else:
        for l_info in line_info:
            point1=l_info[0]
            point2=l_info[1]
            blockObj.AddLine(point1,point2)
def draw_wenzi(blockObj,wenzi_info):
    if wenzi_info==[]:
        pass
    else:
        textObj=blockObj.AddText(wenzi_info[0], wenzi_info[1], wenzi_info[2])
        AlignNum = wenzi_info[3]
        textObj.Alignment = AlignNum
        insertPnt = wenzi_info[1]
        textObj.TextAlignmentPoint = insertPnt
def draw_arc(blockObj,arc_info):
    if arc_info==[]:
        pass
    else:
        #画弧
        pass
def draw_block(model=None):
    model_info=model.draw_info
    line_info=model_info[0]
    wenzi_info=model_info[1]
    arc_info=model_info[2]
    block_start_point = APoint(0, 0)
    blockObj = acad.ActiveDocument.Blocks.Add(block_start_point, wenzi_info[0])
    draw_line(blockObj,line_info)
    draw_wenzi(blockObj,wenzi_info)
    draw_arc(blockObj,arc_info)
    block_info.append(wenzi_info[0])

def place_block(place_info,block_info):
    for insertionPnt,load_name in zip(place_info,block_info):
        acad.model.InsertBlock(insertionPnt, load_name, 1, 1, 1, 0)

draw_block(model=l1)
draw_block(model=l2)
draw_block(model=l3)
place_info=[APoint(0,0),APoint(1100,0),APoint(0,600)]
place_block(place_info,block_info)

for obj in acad.iter_objects("Block"):
    # 以下获取块的属性信息
    # 如果想获取某一特定块的属性信息可以用ObjectID识别特定块
    print(obj.ObjectName)
    # print(dir(obj))