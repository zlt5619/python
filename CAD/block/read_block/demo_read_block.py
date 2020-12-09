from pyautocad import Autocad

acad = Autocad(create_if_not_exists=True)

# for obj in acad.iter_objects("Block"):
#     # 以下获取块的属性信息
#     # 如果想获取某一特定块的属性信息可以用ObjectID识别特定块
#     print(obj.ObjectName)
#     print(obj.InsertionPoint)
#     print(obj.Name)


# for obj in acad.iter_objects("Line"):
    # print(obj.StartPoint)
    # print(obj.EndPoint)
    # print(obj.Layer)
    # print(obj.Length)
    # print(obj.Linetype)
    # print(obj.Lineweight)
    # print(obj.ObjectName)
    # print(obj.Visible)
    # print("----------------------")

for obj in acad.iter_objects("Text"):
    print(obj.TextString)
    print(obj.Height)
    print(obj.InsertionPoint)

    print("----------------------")
