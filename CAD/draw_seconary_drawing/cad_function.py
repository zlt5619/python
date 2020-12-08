from CAD.draw_seconary_drawing.excel import read_excel
from pyautocad import Autocad, APoint
from CAD.draw_seconary_drawing.cabinet_demo import cabinet
from CAD.draw_seconary_drawing.BN_demo import BN
acad=Autocad(create_if_not_exists=True)
block_info1=[]
block_info2=[]
block_info3=[]
block_info4=[]


def draw_line(blockObj, line_info):
    if line_info == []:
        pass
    else:
        for l_info in line_info:
            point1 = l_info[0]
            point2 = l_info[1]
            blockObj.AddLine(point1, point2)
def draw_wenzi(blockObj,wenzi_info):
    if wenzi_info == []:
        pass
    else:
        textObj = blockObj.AddText(wenzi_info[0], wenzi_info[1], wenzi_info[2])
        AlignNum = wenzi_info[3]
        textObj.Alignment = AlignNum
        insertPnt = wenzi_info[1]
        textObj.TextAlignmentPoint = insertPnt
#画输入柜
def draw_cabinet(source=None):
    source=source
    for item in source:
        c=cabinet(item)
        model_info=c.draw_info
        line_info = model_info[0]
        wenzi_info = model_info[1]
        arc_info = model_info[2]
        block_start_point = APoint(0, 0)
        blockObj = acad.ActiveDocument.Blocks.Add(block_start_point, wenzi_info[0])
        draw_line(blockObj, line_info)
        draw_wenzi(blockObj, wenzi_info)
        block_info1.append(wenzi_info[0])
def place_cabinet(place_info,block_info1):
    for insertionPnt, load_name in zip(place_info, block_info1):
        acad.model.InsertBlock(insertionPnt, load_name, 1, 1, 1, 0)
#画输入端子排
def draw_from_BN(place_from=None):
    from_BN=place_from
    for item in from_BN:
        c=BN(item)
        model_info=c.draw_info
        line_info = model_info[0]
        wenzi_info = model_info[1]
        arc_info = model_info[2]
        block_start_point = APoint(0, 0)
        blockObj = acad.ActiveDocument.Blocks.Add(block_start_point, wenzi_info[0])
        draw_line(blockObj, line_info)
        draw_wenzi(blockObj, wenzi_info)
        block_info2.append(wenzi_info[0])
def place_from_BN(place_info2,block_info2):
    for insertionPnt, load_name in zip(place_info2, block_info2):
        acad.model.InsertBlock(insertionPnt, load_name, 1, 1, 1, 0)
#画接受端子排
def draw_to_BN(place_to=None):
    to_BN = place_to
    for item in to_BN:
        c = BN(item)
        model_info = c.draw_info
        line_info = model_info[0]
        wenzi_info = model_info[1]
        arc_info = model_info[2]
        block_start_point = APoint(0, 0)
        blockObj = acad.ActiveDocument.Blocks.Add(block_start_point, wenzi_info[0])
        draw_line(blockObj, line_info)
        draw_wenzi(blockObj, wenzi_info)
        block_info3.append(wenzi_info[0])
def place_to_BN(place_info3,block_info3):
    for insertionPnt, load_name in zip(place_info3, block_info3):
        acad.model.InsertBlock(insertionPnt, load_name, 1, 1, 1, 0)
#画接受柜
def draw_to_cabinet(source=None):
    source=source
    for item in source:
        c=cabinet(item)
        model_info=c.draw_info
        line_info = model_info[0]
        wenzi_info = model_info[1]
        arc_info = model_info[2]
        block_start_point = APoint(0, 0)
        blockObj = acad.ActiveDocument.Blocks.Add(block_start_point, wenzi_info[0])
        draw_line(blockObj, line_info)
        draw_wenzi(blockObj, wenzi_info)
        block_info4.append(wenzi_info[0])
def place_to_cabinet(place_info4,block_info4):
    for insertionPnt, load_name in zip(place_info4, block_info4):
        acad.model.InsertBlock(insertionPnt, load_name, 1, 1, 1, 0)
#根据提取过后的数据，绘制CAD图
def draw_drawing(result=None):
    result=result
    #验证数据是否传递
    # print(result)
    place_info1 = []
    place_info2 = []
    place_info3 = []
    place_info4 = []
    draw_cabinet(result["source"])
    for i in range(35):
        place_info1.append(APoint(0,i*15))
    place_cabinet(place_info1,block_info1)

    draw_from_BN(result["place from"])
    for i in range(35):
        place_info2.append(APoint(75,i*15))
    place_from_BN(place_info2,block_info2)

    draw_to_BN(result["place to"])
    for i in range(35):
        place_info3.append(APoint(100, i * 15))
    place_from_BN(place_info3, block_info3)

    draw_to_cabinet(result["destination"])
    for i in range(35):
        place_info4.append(APoint(125, i * 15))
    place_to_cabinet(place_info4, block_info4)
"""
该方法拿到了相关的文件路径参数
1、处理excel信息，提取需要的数据
2、根据相应的数据，绘制相关的cad图
"""
def drawCAD(filelist=None):
    filelist=filelist
    # 在这里，就把读取到的路径处理好，单个元素，就是单个元素，多个元素，就用列表包含
    # 拿到的文件路径，是列表，列表里的元素是元组，元组则包含一个或多个路径,
    # 经过处理，若是单一元素，则filelist就是该路径，若是多元素，filelists就是列表包含多个路径
    filelists=[]
    filelist=filelist[0]
    if len(filelist)==1:
        filelist=filelist[0]
        # 读取相关的excel文件,返回有用的数据
        rd_excel=read_excel(filelist)
    else:
        for a in filelist:
            filelists.append(a)
        # 读取相关的excel文件,返回有用的数据
        rd_excel = read_excel(filelists)
    #验证是否传输了数据
    # print(filelist)
    # print(filelists)

    #将处理好的数据，传递给函数里的result，再传给下一个方法里
    result=rd_excel.result

    draw_drawing(result)