from pyautocad import Autocad, APoint


acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

p1 = APoint(0, 0)
p2 = APoint(50, 25)
for i in range(5):
    text = acad.model.AddText('Hi %s!' % i, p1, 2.5)
    acad.model.AddLine(p1, p2)
    acad.model.AddCircle(p1, 10)
    p1.y += 10

dp = APoint(10, 0)
# ！！！！！！！遍历cad图形对象以及访问/修改对象属性
for text in acad.iter_objects('Text'):
    print('text: %s at: %s' % (text.TextString, text.InsertionPoint))
    text.InsertionPoint = APoint(text.InsertionPoint) + dp

for obj in acad.iter_objects(['Circle', 'Line']):
    print(obj.ObjectName)