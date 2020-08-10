from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
p1 = APoint(0, 0)
p2 = APoint(0, 2200)
p3=APoint(800,2200)
p4=APoint(800,0)

acad.model.AddLine(p1, p2)
acad.model.AddLine(p2, p3)
acad.model.AddLine(p3, p4)
acad.model.AddLine(p4, p1)

def draw_switch(position_X,positon_Y,load,switch):
    pp1=APoint(position_X,positon_Y)
    pp2=APoint(position_X,positon_Y+200)
    pp3=APoint(position_X+400,positon_Y+200)
    pp4=APoint(position_X+400,positon_Y)
    acad.model.AddLine(pp1, pp2)
    acad.model.AddLine(pp2, pp3)
    acad.model.AddLine(pp3, pp4)
    acad.model.AddLine(pp4, pp1)
    textString = load
    insertPnt = APoint(position_X+20, positon_Y+60)
    height =80
    acad.model.AddText(textString, insertPnt, height)
    textString = switch
    insertPnt = APoint(position_X+220, positon_Y+60)
    height = 70
    acad.model.AddText(textString, insertPnt, height)

draw_switch(0,1600,"电机1","5A")