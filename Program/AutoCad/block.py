from pyautocad import Autocad,APoint

acad = Autocad(create_if_not_exists = True)
acad.prompt("Hello! AutoCAD from pyautocad.")

grip = APoint(20, 0)
blockObj = acad.ActiveDocument.Blocks.Add(grip, "HIT_Block")
center = APoint(0, 0)
radius = 1000
CircleObj = blockObj.AddCircle(center, radius)
rectangleobj1=blockObj.AddLine(APoint(0,0),APoint(1000,0))
rectangleobj2=blockObj.AddLine(APoint(0,0),APoint(0,1000))
textString ="123456789"
insertPnt = APoint(100, 100)
height =500
textobj=blockObj.AddText(textString, insertPnt, height)
insertionPnt = APoint(0, 0)
RetVal = acad.model.InsertBlock(insertionPnt, "HIT_Block", 1, 1, 1, 0 )

